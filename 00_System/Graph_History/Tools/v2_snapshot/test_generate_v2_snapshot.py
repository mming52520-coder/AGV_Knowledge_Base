import json
import os
import tempfile
import unittest
from collections import Counter
from pathlib import Path

import generate_v2_snapshot as graph


class PathPolicyTests(unittest.TestCase):
    def test_generated_and_repository_metadata_are_excluded(self):
        self.assertEqual(graph.classify_path(".git/objects/aa/bb")[0], False)
        self.assertEqual(graph.classify_path("build/pkg/CMakeCache.txt")[0], False)
        self.assertEqual(graph.classify_path("devel/lib/node")[0], False)
        self.assertEqual(graph.classify_path("src/pkg/src/node.cpp.bak_20260506")[0], False)

    def test_ros_source_and_architecture_documents_are_included(self):
        self.assertEqual(graph.classify_path("src/pkg/package.xml")[0], True)
        self.assertEqual(graph.classify_path("src/pkg/src/node.cpp")[0], True)
        self.assertEqual(graph.classify_path("src/pkg/launch/run.launch")[0], True)
        self.assertEqual(graph.classify_path("docs/AGV_MIGRATION_MAP.md")[0], True)
        self.assertEqual(graph.classify_path("deploy/udev/99-agv-serial.rules.template")[0], True)
        self.assertEqual(graph.classify_path("src/_archived_battery_management/CATKIN_IGNORE")[0], True)

    def test_archived_and_tutorial_sources_are_context_not_primary(self):
        self.assertEqual(
            graph.source_disposition("src/_archived_battery_management/src/coulomb_meter.cpp")[0],
            "context",
        )
        self.assertEqual(
            graph.source_disposition("src/remote_ctrl/scripts/joy_turtlebot.py")[0],
            "context",
        )
        self.assertFalse(graph.is_primary_node_source("battery_management", "src/_archived_battery_management/src/coulomb_meter.cpp"))
        self.assertFalse(graph.is_primary_node_source("remote_ctrl", "src/remote_ctrl/scripts/joy_turtlesim.py"))


class IdentityTests(unittest.TestCase):
    def test_exact_v1_strong_keys_reuse_stable_ids(self):
        v1 = [
            {
                "entity_uid": "agv:ros:package:old_pkg",
                "type": "ros_package",
                "title": "old_pkg",
                "semantic": {"ros_name": "", "executable": ""},
            },
            {
                "entity_uid": "agv:ros:node:old_node",
                "type": "ros_node",
                "title": "old_node",
                "semantic": {"ros_name": "/runtime_name", "executable": "old_node"},
            },
            {
                "entity_uid": "agv:ros:interface:cmd-vel",
                "type": "ros_interface",
                "title": "/cmd_vel",
                "semantic": {
                    "ros_name": "/cmd_vel", "executable": "", "interface_kind": "topic"
                },
            },
        ]
        index = graph.V1IdentityIndex(v1)
        self.assertEqual(index.package_uid("old_pkg"), "agv:ros:package:old_pkg")
        self.assertEqual(
            index.node_uid("old_node", "/runtime_name"),
            "agv:ros:node:old_node",
        )
        self.assertEqual(
            index.interface_uid("/cmd_vel", "topic"),
            "agv:ros:interface:cmd-vel",
        )

    def test_new_interface_ids_are_stable_and_kind_sensitive(self):
        index = graph.V1IdentityIndex([])
        self.assertEqual(
            index.interface_uid("/mission/start", "service"),
            "agv:ros:service:mission-start",
        )
        self.assertEqual(
            index.interface_uid("/mission/start", "topic"),
            "agv:ros:interface:mission-start",
        )

    def test_new_atomic_interface_does_not_reuse_reserved_group_uid(self):
        index = graph.V1IdentityIndex([{
            "entity_uid": "agv:ros:interface:ultrasonic-distance",
            "type": "ros_interface",
            "title": "/ultrasonic/*_distance",
            "semantic": {
                "ros_name": "/ultrasonic/*_distance",
                "interface_kind": "topic_group",
                "executable": "",
            },
        }])
        self.assertEqual(
            index.interface_uid("/ultrasonic/distance", "topic"),
            "agv:ros:interface:ultrasonic-distance-atomic",
        )

    def test_interface_identity_is_keyed_by_ros_name_and_kind(self):
        index = graph.V1IdentityIndex([
            {
                "entity_uid": "agv:ros:interface:shared-topic",
                "type": "ros_interface",
                "title": "/shared",
                "semantic": {"ros_name": "/shared", "interface_kind": "topic"},
            },
            {
                "entity_uid": "agv:ros:service:shared-service",
                "type": "ros_interface",
                "title": "/shared",
                "semantic": {"ros_name": "/shared", "interface_kind": "service"},
            },
        ])
        self.assertEqual(index.interface_uid("/shared", "topic"), "agv:ros:interface:shared-topic")
        self.assertEqual(index.interface_uid("/shared", "service"), "agv:ros:service:shared-service")

    def test_similar_names_are_not_fuzzy_renamed(self):
        index = graph.V1IdentityIndex([{
            "entity_uid": "agv:ros:node:old_controller",
            "type": "ros_node",
            "title": "old_controller",
            "semantic": {"ros_name": "/old_controller", "executable": "old_controller"},
        }])
        self.assertEqual(
            index.node_uid("old_controller_v2", "/old_controller_v2"),
            "agv:ros:node:old_controller_v2",
        )


class ExtractionTests(unittest.TestCase):
    def test_endpoint_parser_supports_templated_cpp_and_static_python_wrapper(self):
        cpp_rows = list(graph._endpoint_matches(
            'sub_ = nh.subscribe<std_msgs::Bool>("/relay/enabled", 1, callback);',
            ".cpp",
        ))
        self.assertEqual(len(cpp_rows), 1)
        _, predicate, kind, packed = cpp_rows[0]
        self.assertEqual((predicate, kind), ("subscribes", "topic"))
        self.assertEqual(packed.split("\0"), ['"/relay/enabled"', "std_msgs::Bool"])

        py_rows = list(graph._endpoint_matches(
            'self._subscribe(\n  self._param_topic("odom", "/odom"),\n  Odometry, callback)',
            ".py",
        ))
        self.assertEqual(len(py_rows), 1)
        _, predicate, kind, packed = py_rows[0]
        self.assertEqual((predicate, kind), ("subscribes", "topic"))
        self.assertEqual(packed.split("\0"), ["/odom", "Odometry"])

    def test_static_python_wrapper_resolves_into_endpoint_use(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            root = Path(temp)
            pkg_dir = root / "src" / "bridge"
            script = pkg_dir / "scripts" / "bridge.py"
            script.parent.mkdir(parents=True)
            script.write_text(
                'from nav_msgs.msg import Odometry\n'
                'class Bridge:\n'
                '    def _subscribe(self, topic, msg_type, callback):\n'
                '        rospy.Subscriber(topic, msg_type, callback)\n'
                '    def configure(self):\n'
                '        self._subscribe(self._param_topic("odom", "/odom"), Odometry, callback)\n',
                encoding="utf-8",
            )
            package = graph.PackageInfo("bridge", "1.0", "src/bridge", pkg_dir, [], "active")
            node = graph.NodeInfo(
                package=package,
                executable="bridge",
                ros_name="/bridge",
                source_paths=["src/bridge/scripts/bridge.py"],
                launch_names=[],
                status="active",
                identity_name="bridge",
            )
            warnings = []
            uses = graph._extract_endpoint_uses(
                root,
                [node],
                graph.V1IdentityIndex([]),
                warnings,
            )
            self.assertEqual(len(uses), 1)
            self.assertEqual(uses[0].ros_name, "/odom")
            self.assertEqual(uses[0].predicate, "subscribes")
            self.assertEqual(uses[0].message_type, "nav_msgs/Odometry")
            self.assertFalse(warnings)

    def test_launch_group_namespace_is_applied_to_runtime_alias(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            launch = Path(temp) / "vehicle.launch"
            launch.write_text(
                '<launch><group ns="decision"><node pkg="agv_decision" '
                'type="teleop_node" name="teleop_node"/></group></launch>',
                encoding="utf-8",
            )
            rows = graph.scan_launch_nodes(launch)
            self.assertEqual(rows[0]["ros_name"], "/decision/teleop_node")

    def test_cmake_target_maps_different_source_stem(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            root = Path(temp)
            pkg_dir = root / "src" / "pkg"
            (pkg_dir / "src").mkdir(parents=True)
            (pkg_dir / "src" / "imu_probe_node.cpp").write_text("", encoding="utf-8")
            (pkg_dir / "CMakeLists.txt").write_text(
                "add_executable(imu_probe\n  src/imu_probe_node.cpp\n)\n",
                encoding="utf-8",
            )
            package = graph.PackageInfo("pkg", "1.0", "src/pkg", pkg_dir, [], "active")
            self.assertEqual(
                graph._cmake_targets(package, root)["imu_probe"],
                ["src/pkg/src/imu_probe_node.cpp"],
            )

    def test_cmake_foreach_only_expands_supported_node_pattern(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            root = Path(temp)
            pkg_dir = root / "src" / "pkg"
            (pkg_dir / "src").mkdir(parents=True)
            (pkg_dir / "src" / "ghost.cpp").write_text("", encoding="utf-8")
            package = graph.PackageInfo("pkg", "1.0", "src/pkg", pkg_dir, [], "active")

            (pkg_dir / "CMakeLists.txt").write_text(
                "foreach(node ghost)\n  add_library(${node} src/${node}.cpp)\nendforeach()\n",
                encoding="utf-8",
            )
            self.assertNotIn("ghost", graph._cmake_targets(package, root))

            (pkg_dir / "CMakeLists.txt").write_text(
                "foreach(node ghost)\n  add_executable(${node} src/${node}.cpp)\nendforeach()\n",
                encoding="utf-8",
            )
            self.assertEqual(
                graph._cmake_targets(package, root)["ghost"],
                ["src/pkg/src/ghost.cpp"],
            )

    def test_primary_node_path_prefers_ros_init_source_over_helper(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            root = Path(temp)
            pkg_dir = root / "src" / "wheeltec_base"
            (pkg_dir / "src").mkdir(parents=True)
            (pkg_dir / "src" / "Quaternion_Solution.cpp").write_text(
                "double helper() { return 0.0; }\n", encoding="utf-8"
            )
            (pkg_dir / "src" / "wheeltec_robot.cpp").write_text(
                'int main(int argc, char** argv) { ros::init(argc, argv, "wheeltec_robot"); }\n',
                encoding="utf-8",
            )
            (pkg_dir / "CMakeLists.txt").write_text(
                "add_executable(wheeltec_robot_node src/Quaternion_Solution.cpp src/wheeltec_robot.cpp)\n",
                encoding="utf-8",
            )
            package = graph.PackageInfo(
                "wheeltec_base", "1.0", "src/wheeltec_base", pkg_dir, [], "active"
            )
            nodes = graph._discover_nodes(root, [package], [])
            self.assertEqual(nodes[0].source_paths[0], "src/wheeltec_base/src/wheeltec_robot.cpp")
            self.assertEqual(set(nodes[0].source_paths), {
                "src/wheeltec_base/src/wheeltec_robot.cpp",
                "src/wheeltec_base/src/Quaternion_Solution.cpp",
            })

    def test_cross_package_motor_targets_are_disambiguated(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            root = Path(temp)
            definitions = [
                ("magnetic_controlled_motor", "motor_control"),
                ("ultrasonic_controlled_motor", "motor_control_node"),
            ]
            for package_name, target in definitions:
                pkg_dir = root / "src" / package_name
                (pkg_dir / "src").mkdir(parents=True)
                (pkg_dir / "package.xml").write_text(
                    f'<package format="2"><name>{package_name}</name><version>1.0.0</version>'
                    '<description>x</description><maintainer email="x@y">x</maintainer>'
                    '<license>MIT</license></package>',
                    encoding="utf-8",
                )
                (pkg_dir / "CMakeLists.txt").write_text(
                    f"add_executable({target} src/motor_control.cpp)\n",
                    encoding="utf-8",
                )
                (pkg_dir / "src" / "motor_control.cpp").write_text(
                    'int main(int argc, char** argv) { ros::init(argc, argv, "motor_controller"); }\n',
                    encoding="utf-8",
                )

            v1 = graph.V1IdentityIndex([{
                "entity_uid": "agv:ros:node:motor_control",
                "type": "ros_node",
                "title": "motor_control",
                "semantic": {"executable": "motor_control", "ros_name": "/motor_controller"},
            }])
            result = graph.extract_graph(root, v1, {})
            node_uids = {
                row["entity_uid"] for row in result.entities if row["type"] == "ros_node"
            }
            self.assertEqual(node_uids, {
                "agv:ros:node:magnetic_motor_control",
                "agv:ros:node:ultrasonic_motor_control",
            })
            package_relations = [
                row for row in result.relations if row["predicate"] == "package"
            ]
            self.assertEqual(Counter(row["from_entity_uid"] for row in package_relations), {
                "agv:ros:node:magnetic_motor_control": 1,
                "agv:ros:node:ultrasonic_motor_control": 1,
            })
            self.assertIn({
                "from_entity_uid": "agv:ros:node:magnetic_motor_control",
                "predicate": "package",
                "to_entity_uid": "agv:ros:package:magnetic_controlled_motor",
            }, [{k: row[k] for k in ("from_entity_uid", "predicate", "to_entity_uid")} for row in package_relations])
            self.assertIn({
                "from_entity_uid": "agv:ros:node:ultrasonic_motor_control",
                "predicate": "package",
                "to_entity_uid": "agv:ros:package:ultrasonic_controlled_motor",
            }, [{k: row[k] for k in ("from_entity_uid", "predicate", "to_entity_uid")} for row in package_relations])

    def test_python_launch_type_suffix_maps_to_source_node(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            root = Path(temp)
            pkg_dir = root / "src" / "bridge"
            (pkg_dir / "scripts").mkdir(parents=True)
            (pkg_dir / "launch").mkdir()
            (pkg_dir / "scripts" / "bridge.py").write_text(
                'import rospy\nrospy.init_node("bridge_runtime")\n', encoding="utf-8"
            )
            (pkg_dir / "launch" / "bridge.launch").write_text(
                '<launch><node pkg="bridge" type="bridge.py" name="bridge_launch"/></launch>',
                encoding="utf-8",
            )
            package = graph.PackageInfo("bridge", "1.0", "src/bridge", pkg_dir, [], "active")
            warnings = []
            nodes = graph._discover_nodes(root, [package], warnings)
            self.assertEqual(len(nodes), 1)
            self.assertEqual(nodes[0].executable, "bridge")
            self.assertEqual(nodes[0].ros_name, "/bridge_launch")
            self.assertEqual(nodes[0].launch_names, ["/bridge_launch"])
            self.assertFalse(any(
                warning["kind"] == "launch_node_without_source_evidence"
                for warning in warnings
            ))

    def test_fixture_extracts_packages_nodes_interfaces_and_relations(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            root = Path(temp)
            pkg = root / "src" / "demo_pkg"
            (pkg / "src").mkdir(parents=True)
            (pkg / "msg").mkdir()
            (pkg / "package.xml").write_text(
                """<package format=\"2\"><name>demo_pkg</name><version>1.2.3</version>\n"
                "<description>x</description><maintainer email=\"x@y\">x</maintainer>\n"
                "<license>MIT</license><exec_depend>std_msgs</exec_depend></package>""",
                encoding="utf-8",
            )
            (pkg / "CMakeLists.txt").write_text(
                "add_executable(demo_node src/demo_node.cpp)\n",
                encoding="utf-8",
            )
            (pkg / "msg" / "State.msg").write_text("bool ok\n", encoding="utf-8")
            (pkg / "src" / "demo_node.cpp").write_text(
                """#include <ros/ros.h>\n"
                "int main(int argc, char** argv) {\n"
                "  ros::init(argc, argv, \"demo_runtime\");\n"
                "  ros::NodeHandle nh;\n"
                "  auto p = nh.advertise<std_msgs::String>(\"/demo/out\", 1);\n"
                "  auto s = nh.subscribe(\"/demo/in\", 1, callback);\n"
                "  auto c = nh.serviceClient<std_srvs::Trigger>(\"/demo/check\");\n"
                "}\n""",
                encoding="utf-8",
            )

            result = graph.extract_graph(root, graph.V1IdentityIndex([]), {})
            by_uid = {row["entity_uid"]: row for row in result.entities}
            self.assertIn("agv:ros:package:demo_pkg", by_uid)
            self.assertIn("agv:ros:node:demo_node", by_uid)
            self.assertIn("agv:ros:interface:demo-out", by_uid)
            self.assertIn("agv:ros:interface:demo-in", by_uid)
            self.assertIn("agv:ros:service:demo-check", by_uid)
            self.assertIn("agv:ros:message:demo-pkg-state", by_uid)
            self.assertTrue(all(
                any(evidence["operation"] == "node_source" for evidence in entity["evidence"])
                for entity in result.entities
                if entity["type"] == "ros_node"
            ))
            relation_keys = {
                (row["from_entity_uid"], row["predicate"], row["to_entity_uid"])
                for row in result.relations
            }
            self.assertIn(
                ("agv:ros:node:demo_node", "package", "agv:ros:package:demo_pkg"),
                relation_keys,
            )
            self.assertIn(
                ("agv:ros:node:demo_node", "publishes", "agv:ros:interface:demo-out"),
                relation_keys,
            )
            self.assertIn(
                ("agv:ros:node:demo_node", "uses_services", "agv:ros:service:demo-check"),
                relation_keys,
            )


class DiffTests(unittest.TestCase):
    def test_diff_conserves_entity_counts_and_classifies_scope_expansion(self):
        v1 = [
            {"entity_uid": "a", "type": "ros_package", "semantic": {"version": "1"}, "semantic_fingerprint": "legacy-a"},
            {"entity_uid": "b", "type": "ros_package", "semantic": {"version": "1"}, "semantic_fingerprint": "legacy-b"},
            {"entity_uid": "c", "type": "ros_package", "semantic": {"version": "1"}, "semantic_fingerprint": "legacy-c"},
        ]
        v2 = [
            {"entity_uid": "a", "type": "ros_package", "semantic": {"version": "1"}, "semantic_fingerprint": "new-a"},
            {"entity_uid": "b", "type": "ros_package", "semantic": {"version": "2"}, "semantic_fingerprint": "new-b"},
            {"entity_uid": "d", "type": "ros_package", "semantic": {"version": "1"}, "semantic_fingerprint": "new-d"},
        ]
        diff = graph.diff_entities(v1, v2)
        self.assertEqual(diff["counts"], {
            "baseline": 3,
            "target": 3,
            "matched": 2,
            "unchanged": 1,
            "modified": 1,
            "added": 1,
            "removed": 1,
        })
        scope = graph.classify_scope_changes(v1, v2, baseline_has_file_manifest=False)
        self.assertEqual(scope[0]["change_kind"], "baseline_manifest_limitation")
        self.assertIn("d", scope[1]["entity_uids"])

    def test_group_interface_decomposition_is_explicit(self):
        v1 = [{
            "entity_uid": "agv:ros:interface:motor-services",
            "type": "ros_interface",
            "semantic": {"ros_name": "/motor_init + /motor_enable", "interface_kind": "service_group"},
        }]
        v2 = [
            {"entity_uid": "agv:ros:service:motor-init", "type": "ros_interface", "semantic": {"ros_name": "/motor_init", "interface_kind": "service"}},
            {"entity_uid": "agv:ros:service:motor-enable", "type": "ros_interface", "semantic": {"ros_name": "/motor_enable", "interface_kind": "service"}},
        ]
        rows = graph.build_group_decompositions(v1, v2, "v1", "v2")
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(row["predicate"] == "decomposed_into" for row in rows))

    def test_service_group_does_not_absorb_topics_with_matching_names(self):
        v1 = [{
            "entity_uid": "agv:ros:interface:trajectory-services",
            "type": "ros_interface",
            "semantic": {"ros_name": "/trajectory/*", "interface_kind": "service_group"},
        }]
        v2 = [
            {"entity_uid": "topic", "type": "ros_interface", "semantic": {"ros_name": "/trajectory/state", "interface_kind": "topic"}},
            {"entity_uid": "service", "type": "ros_interface", "semantic": {"ros_name": "/trajectory/start", "interface_kind": "service"}},
        ]
        rows = graph.build_group_decompositions(v1, v2, "v1", "v2")
        self.assertEqual([row["to_entity_uid"] for row in rows], ["service"])

    def test_constructor_initializer_supplies_topic_default(self):
        values = graph._variable_defaults('Reader(): distance_topic_("/ultrasonic/left_distance") {}')
        self.assertEqual(values["distance_topic_"], "/ultrasonic/left_distance")

    def test_relation_counts_conserve_and_removals_are_extraction_limited(self):
        common = {"from_entity_uid": "a", "predicate": "package", "to_entity_uid": "p", "qualifiers": {}}
        old_only = {"from_entity_uid": "a", "predicate": "subscribes", "to_entity_uid": "old", "qualifiers": {}}
        new_only = {"from_entity_uid": "a", "predicate": "subscribes", "to_entity_uid": "new", "qualifiers": {}}
        payload = graph.build_diff_payload(
            [], [], [common, old_only], [common, new_only], [], "v1", "v2", False,
            baseline_extractor_version="old", target_extractor_version="new",
        )
        self.assertEqual(payload["relation_counts"], {
            "baseline": 2, "target": 2, "matched": 1, "added": 1, "removed": 1,
            "removed_extraction_limited": 1,
        })
        self.assertEqual(
            payload["relation_removed"][0]["comparison_classification"],
            "extraction_limited",
        )
        self.assertFalse(payload["relation_removed"][0]["breaking"])
        self.assertFalse(payload["comparison_scope"]["source_code_unchanged_supported"])
        self.assertEqual(payload["comparison_scope"]["baseline_extractor_version"], "old")


class DeterminismTests(unittest.TestCase):
    def test_canonical_json_is_key_sorted_and_unicode_preserving(self):
        value = {"z": 1, "中文": [2, 1], "a": {"y": 2, "x": 1}}
        self.assertEqual(
            graph.canonical_json(value),
            '{"a":{"x":1,"y":2},"z":1,"中文":[2,1]}',
        )
        self.assertEqual(graph.sha256_json(value), graph.sha256_json(dict(reversed(list(value.items())))))

    def test_source_inventory_records_inclusions_and_exclusions_per_file(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            root = Path(temp)
            (root / "src" / "pkg").mkdir(parents=True)
            (root / "build" / "pkg").mkdir(parents=True)
            (root / "src" / "pkg" / "node.cpp").write_text("int main() {}\n", encoding="utf-8")
            (root / "build" / "pkg" / "node.o").write_bytes(b"object")
            records, hashes, fingerprint = graph.scan_source_files(root)
            self.assertEqual([row["path"] for row in records], sorted(row["path"] for row in records))
            included = next(row for row in records if row["path"] == "src/pkg/node.cpp")
            excluded = next(row for row in records if row["path"] == "build/pkg/node.o")
            self.assertEqual(included["disposition"], "included")
            self.assertEqual(included["sha256"], hashes["src/pkg/node.cpp"])
            self.assertEqual(excluded["disposition"], "excluded")
            self.assertIsNone(excluded["sha256"])
            self.assertEqual(len(fingerprint), 64)


class EvidenceValidationTests(unittest.TestCase):
    def test_baseline_source_evidence_resolves_and_is_strictly_validated(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            root = Path(temp)
            source = root / "source"
            v1 = root / "v1"
            baseline = root / "baseline"
            source.mkdir()
            v1.mkdir()
            path = baseline / "src" / "pkg" / "config.yaml"
            path.parent.mkdir(parents=True)
            path.write_text("mode: old\n", encoding="utf-8")
            evidence = graph._baseline_source_evidence(
                baseline,
                "src/pkg/config.yaml",
                "mode: old",
                "V1 fixture mode",
            )
            self.assertEqual(evidence["line"], 1)
            self.assertEqual(evidence["file_sha256"], graph.sha256_bytes(path.read_bytes()))
            risk = {
                "risk_id": "R00",
                "validation_state": "static_evidence_only",
                "independent_tests_run": False,
                "evidence": [evidence],
            }
            graph._validate_risk_evidence([risk], {"git_state": {}}, source, v1, [], baseline)
            path.write_text("mode: changed\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "baseline-source evidence hash mismatch"):
                graph._validate_risk_evidence([risk], {"git_state": {}}, source, v1, [], baseline)


class SnapshotIntegrationTests(unittest.TestCase):
    def test_overlap_guard_runs_before_output_creation(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            base = Path(temp)
            source = base / "source"
            v1 = base / "v1"
            source.mkdir()
            v1.mkdir()
            nested_output = source / "must_not_be_created"
            with self.assertRaisesRegex(ValueError, "output must not equal or nest"):
                graph.generate_snapshot(source, v1, nested_output, created="2026-07-14")
            self.assertFalse(nested_output.exists())

    def test_preexisting_hardlinked_output_artifact_is_rejected(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            base = Path(temp)
            source = base / "source"
            v1 = base / "v1"
            output = base / "output"
            source.mkdir()
            v1.mkdir()
            output.mkdir()
            seed = v1 / "seed.jsonl"
            seed.write_text("{}\n", encoding="utf-8")
            try:
                os.link(seed, output / "entities.jsonl")
            except OSError as error:
                self.skipTest(f"hard links unavailable: {error}")
            with self.assertRaisesRegex(ValueError, "unsafe linked artifacts"):
                graph.generate_snapshot(source, v1, output, created="2026-07-14")

    def test_required_outputs_validate_and_are_byte_deterministic(self):
        temp_base = Path(tempfile.gettempdir()) / "agv_v2_snapshot_tests"
        temp_base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temp_base) as temp:
            base = Path(temp)
            source = base / "source"
            pkg = source / "src" / "demo_pkg"
            (pkg / "src").mkdir(parents=True)
            (pkg / "package.xml").write_text(
                """<package format=\"2\"><name>demo_pkg</name><version>1.0.0</version>"
                "<description>x</description><maintainer email=\"x@y\">x</maintainer>"
                "<license>MIT</license></package>""",
                encoding="utf-8",
            )
            (pkg / "CMakeLists.txt").write_text(
                "add_executable(demo_node src/demo_node.cpp)\n", encoding="utf-8"
            )
            (pkg / "src" / "demo_node.cpp").write_text(
                """#include <ros/ros.h>\nint main(int argc,char** argv){\n"
                "ros::init(argc,argv,\"demo_node\"); ros::NodeHandle nh;\n"
                "auto p=nh.advertise<std_msgs::String>(\"/demo/out\",1);}\n""",
                encoding="utf-8",
            )
            v1 = base / "v1"
            v1.mkdir()
            baseline_entity = {
                "entity_uid": "agv:ros:package:demo_pkg",
                "type": "ros_package",
                "comparison_scope": "code",
                "title": "demo_pkg",
                "semantic": {
                    "type": "ros_package", "status": "active", "ros_name": "",
                    "executable": "", "interface_kind": "", "message_type": "",
                    "version": "0.9.0", "vehicles": ["三号车"],
                },
            }
            baseline_entity["semantic_fingerprint"] = graph.sha256_json(baseline_entity["semantic"])
            (v1 / "entities.jsonl").write_text(graph.canonical_json(baseline_entity) + "\n", encoding="utf-8")
            (v1 / "relations.jsonl").write_text("", encoding="utf-8")
            (v1 / "manifest.json").write_text(
                json.dumps({
                    "snapshot_id": "v1", "source_file_manifest_available": False,
                    "entity_count": 1, "semantic_relation_count": 0,
                }),
                encoding="utf-8",
            )
            output = base / "output"
            v1_tree_before = graph.tree_sha256(v1)
            manifest = graph.generate_snapshot(source, v1, output, created="2026-07-14")
            self.assertEqual(graph.OUTPUT_ARTIFACTS, {path.name for path in output.iterdir()})
            self.assertEqual(v1_tree_before, graph.tree_sha256(v1))
            self.assertEqual(manifest["baseline_tree_sha256"], v1_tree_before)
            graph.validate_output(output, source, v1)
            first = {path.name: path.read_bytes() for path in output.iterdir() if path.is_file()}
            summary_path = output / "V1-to-V2差异摘要.md"
            summary_path.write_text(
                summary_path.read_text(encoding="utf-8") + "\n\ufffd\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "Unicode replacement character U\\+FFFD"):
                graph.validate_output(output, source, v1)
            summary_path.write_bytes(first[summary_path.name])
            second_manifest = graph.generate_snapshot(source, v1, output, created="2026-07-14")
            second = {path.name: path.read_bytes() for path in output.iterdir() if path.is_file()}
            self.assertEqual(first, second)
            self.assertEqual(manifest["snapshot_fingerprint"], second_manifest["snapshot_fingerprint"])
            (output / "stale.txt").write_text("stale", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "stale/unexpected"):
                graph.generate_snapshot(source, v1, output, created="2026-07-14")


class AuditRecordTests(unittest.TestCase):
    def test_audit_migrations_include_terminal_and_parallel_relations(self):
        baseline_uids = [
            "agv:ros:node:remote_controller",
            "agv:ros:node:drive_feedback_odom",
            "agv:ros:node:gps_nmea_to_fix_json",
            "agv:ros:node:trajectory_tracker",
            "agv:ros:package:agv_mqtt_bridge",
        ]
        target_uids = [
            "agv:ros:node:teleop_node",
            "agv:ros:node:vehicle_state_estimator_node",
            "agv:ros:node:safety_supervisor_node",
            "agv:ros:node:chassis_gateway_node",
            "agv:ros:package:agv_telemetry",
            "agv:ros:package:agv_mission",
        ]
        baseline = [{"entity_uid": uid, "type": "ros_node", "semantic": {}} for uid in baseline_uids]
        target = [{"entity_uid": uid, "type": "ros_node", "semantic": {}} for uid in target_uids]
        rows = graph._documented_migrations(
            baseline, target, "v1", "v2", {"docs/AGV_MIGRATION_MAP.md": "hash"}
        )
        keys = {(row["from_entity_uid"], row["predicate"], row.get("to_entity_uid")) for row in rows}
        self.assertIn(("agv:ros:node:remote_controller", "parallel_replacement", "agv:ros:node:teleop_node"), keys)
        self.assertIn(("agv:ros:node:drive_feedback_odom", "superseded_by", "agv:ros:node:vehicle_state_estimator_node"), keys)
        self.assertIn(("agv:ros:node:gps_nmea_to_fix_json", "removed_without_replacement", None), keys)
        self.assertIn(("agv:ros:node:trajectory_tracker", "decomposed_into", "agv:ros:node:safety_supervisor_node"), keys)
        self.assertIn(("agv:ros:node:trajectory_tracker", "decomposed_into", "agv:ros:node:chassis_gateway_node"), keys)
        self.assertIn(("agv:ros:package:agv_mqtt_bridge", "capability_extracted_to", "agv:ros:package:agv_mission"), keys)
        gps = next(row for row in rows if row["from_entity_uid"] == "agv:ros:node:gps_nmea_to_fix_json")
        self.assertEqual(gps["match_method"], "explicit_snapshot_set_difference")
        self.assertLess(gps["confidence"], 1.0)
        self.assertEqual(gps["evidence"]["baseline_artifact"]["path"], "entities.jsonl")
        self.assertEqual(gps["evidence"]["target_artifact"]["path"], "entities.jsonl")
        self.assertEqual(gps["evidence"]["target_artifact"]["expected_count"], 0)

    def test_removed_without_replacement_remains_breaking_in_diff(self):
        baseline = [{
            "entity_uid": "agv:ros:node:gps_nmea_to_fix_json",
            "type": "ros_node",
            "semantic": {"executable": "gps_nmea_to_fix_json.py"},
            "semantic_fingerprint": "before",
        }]
        migration = [{
            "from_entity_uid": "agv:ros:node:gps_nmea_to_fix_json",
            "predicate": "removed_without_replacement",
            "to_entity_uid": None,
        }]
        payload = graph.build_diff_payload(
            baseline, [], [], [], migration, "v1", "v2", False
        )
        change = payload["entity_changes"][0]
        self.assertEqual(change["change_kind"], "removed_without_replacement")
        self.assertTrue(change["breaking"])
        self.assertEqual(change["review"], "needs-review")

    def test_removed_diagnostic_is_explicit_and_breaking(self):
        baseline = [{
            "entity_uid": "agv:ros:node:encoder_probe",
            "type": "ros_node",
            "semantic": {"executable": "encoder_probe"},
            "semantic_fingerprint": "before",
        }]
        migration = [{
            "from_entity_uid": "agv:ros:node:encoder_probe",
            "predicate": "removed_diagnostic",
            "to_entity_uid": None,
        }]
        payload = graph.build_diff_payload(
            baseline, [], [], [], migration, "v1", "v2", False
        )
        change = payload["entity_changes"][0]
        self.assertEqual(change["change_kind"], "removed_diagnostic")
        self.assertTrue(change["breaking"])
        self.assertEqual(change["review"], "needs-review")

    def test_risk_register_is_exactly_r01_through_r16(self):
        risks = graph.build_risk_register(Path("."), {"dirty": True, "status_counts": {" M": 31, "??": 126}})
        self.assertEqual([risk["risk_id"] for risk in risks], [f"R{i:02d}" for i in range(1, 17)])
        self.assertTrue(all(risk["validation_state"] == "static_evidence_only" for risk in risks))


if __name__ == "__main__":
    unittest.main()

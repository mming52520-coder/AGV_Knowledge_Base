import json
import tempfile
import unittest
from pathlib import Path

from generate_material_graph import (
    CLAIMS,
    LEARNING_SPECS,
    MATCH_SPECS,
    ROS_SOURCE_SPECS,
    build_graph,
    validate_graph,
)


class MaterialGraphGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_root = Path(__file__).parent / "tmp"
        cls.temp_root.mkdir(exist_ok=True)

    def test_generated_graph_has_unique_ids_and_resolved_match_links(self):
        with tempfile.TemporaryDirectory(dir=self.temp_root) as temp_dir:
            output = Path(temp_dir)
            result = build_graph(output)

            expected_source_count = len(LEARNING_SPECS) + len(ROS_SOURCE_SPECS)
            self.assertEqual(expected_source_count, result["source_count"])
            self.assertEqual(len(CLAIMS), result["claim_count"])
            self.assertEqual(len(MATCH_SPECS), result["match_count"])
            self.assertGreaterEqual(result["duplicate_alias_count"], 1)

            report = validate_graph(output)
            self.assertEqual([], report["errors"])
            self.assertEqual(expected_source_count, report["source_count"])

            catalog = [
                json.loads(line)
                for line in (output / "11_Engineering_Materials/_data/sources.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            self.assertEqual(len(catalog), len({item["source_id"] for item in catalog}))
            self.assertNotIn("README.md", "\n".join(item["source_path"] for item in catalog))
            self.assertNotIn("CODEX_MEMORY_exam_system_linux_deploy.md", "\n".join(item["source_path"] for item in catalog))

            coverage = json.loads(
                (output / "11_Engineering_Materials/_data/ros-source-coverage.json")
                .read_text(encoding="utf-8")
            )
            self.assertTrue(coverage["accounting"]["all_files_accounted_for"])
            self.assertEqual(
                coverage["inventory"]["file_count"],
                sum(row["file_count"] for row in coverage["category_summary"]),
            )
            self.assertEqual(
                coverage["inventory"]["total_bytes"],
                sum(row["total_bytes"] for row in coverage["category_summary"]),
            )
            self.assertEqual(
                len([spec for spec in ROS_SOURCE_SPECS if spec.get("scope") == "inventory-root"]),
                coverage["curated_outside_historical_subroot_count"],
            )
            categories = {row["category"]: row for row in coverage["category_summary"]}
            self.assertGreater(categories["excluded_installer_activation_binary"]["file_count"], 0)
            self.assertGreater(categories["excluded_mechanical_arm_or_unrelated_platform"]["file_count"], 0)
            self.assertGreater(categories["excluded_duplicate_or_superseded"]["file_count"], 0)

            requested_reference_slugs = {
                "c10b-l150-user-manual",
                "c10b-mcu-app-protocol",
                "electromagnetic-guidance-principles",
                "wheeltec-pid-guide",
                "wheeled-chassis-kinematics",
                "c10b-mainboard-schematic-2025",
                "c10b-resource-map",
                "r3mini-ackermann-installation",
                "legacy-ros-host-autostart",
            }
            source_slugs = {item["slug"] for item in catalog}
            self.assertTrue(requested_reference_slugs <= source_slugs)

            claims = [
                json.loads(line)
                for line in (output / "11_Engineering_Materials/_data/claims.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            claims_by_id = {item["claim_id"]: item for item in claims}
            generated_matches = [
                json.loads(line)
                for line in (output / "11_Engineering_Materials/_data/matches.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            for match in generated_matches:
                claim = claims_by_id[match["left_entity"]]
                if claim["snapshot"].startswith(("vendor-reference-", "legacy-reference-")):
                    self.assertIn(match["relation"], {"reference", "related_theory", "proposes"})
                    self.assertIn(
                        match["implementation_evidence"],
                        {"reference-model-mismatch", "theory-only", "legacy-reference-only"},
                    )

            index = output / "11_Engineering_Materials/_index.md"
            index.write_text(index.read_text(encoding="utf-8") + "\n[[11_Engineering_Materials/不存在的节点]]\n", encoding="utf-8")
            broken = validate_graph(output)
            self.assertTrue(any("unresolved wikilink" in error for error in broken["errors"]))

    def test_machine_files_and_markdown_are_deterministic(self):
        with tempfile.TemporaryDirectory(dir=self.temp_root) as first, tempfile.TemporaryDirectory(dir=self.temp_root) as second:
            build_graph(Path(first))
            build_graph(Path(second))

            first_files = {
                path.relative_to(first): path.read_bytes()
                for path in Path(first).rglob("*")
                if path.is_file()
            }
            second_files = {
                path.relative_to(second): path.read_bytes()
                for path in Path(second).rglob("*")
                if path.is_file()
            }
            self.assertEqual(first_files, second_files)


if __name__ == "__main__":
    unittest.main()

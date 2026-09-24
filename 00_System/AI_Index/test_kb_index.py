import argparse
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import kb_index as kb


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.vault = Path(self.temp.name)
        self.write("00_System/Graph_History/current.json", json.dumps({
            "current_snapshot": "v1", "candidate_snapshot": "v2",
        }) + "\n")
        subprocess.run(["git", "init", "-q", str(self.vault)], check=True)
        subprocess.run(
            ["git", "-C", str(self.vault), "add", "00_System/Graph_History/current.json"],
            check=True,
        )
        self.write("a.md", '---\nid: "doc:a"\ntype: ros_node\nproject: AGV\n---\n# 左侧循墙\n\n正文。\n')
        self.config_path = self.vault / "config.json"
        self.index_dir = self.vault / "index"
        self.config = {
            "schema_version": 1,
            "protected_tree_sha256": kb.protected_digest(self.vault),
            "critical_pages": [],
            "enrichments": {},
            "relations": [],
        }
        self.save_config()

    def tearDown(self):
        self.temp.cleanup()

    def write(self, path, text):
        target = self.vault / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def save_config(self):
        self.config_path.write_text(json.dumps(self.config, ensure_ascii=False), encoding="utf-8")

    def build(self):
        model = kb.build_model(self.vault, self.config_path)
        kb.write_index(self.index_dir, model)
        return model

    def query_args(self, **overrides):
        defaults = dict(project=None, vehicle=None, scope=None, snapshot=None,
                        include_candidate=False, include_history=False, limit=10)
        defaults.update(overrides)
        return argparse.Namespace(**defaults)

    def test_build_is_deterministic_and_move_keeps_identity(self):
        first = self.build()
        first_bytes = {name: (self.index_dir / name).read_bytes() for name in kb.INDEX_FILES}
        self.build()
        self.assertEqual(first_bytes, {name: (self.index_dir / name).read_bytes() for name in kb.INDEX_FILES})
        self.assertEqual(first, kb.check(self.vault, self.config_path, self.index_dir))
        self.write("folder/.keep", "")
        (self.vault / "a.md").rename(self.vault / "folder/a-renamed.md")
        moved = kb.build_model(self.vault, self.config_path)
        self.assertEqual(first["documents"][0]["id"], moved["documents"][0]["id"])
        self.assertEqual(moved["documents"][0]["path"], "folder/a-renamed.md")

    def test_duplicate_id_and_dangling_relation_fail(self):
        self.write("duplicate.md", '---\nid: "doc:a"\n---\n# 重复\n')
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "duplicate document id"):
            kb.build_model(self.vault, self.config_path)
        (self.vault / "duplicate.md").unlink()
        self.config["relations"] = [{"from": "doc:a", "relation": "related", "to": "missing"}]
        self.save_config()
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "dangling relation"):
            kb.build_model(self.vault, self.config_path)

    def test_instance_scope_and_candidate_filter(self):
        for snapshot in ("v1", "v2"):
            self.write(
                snapshot + ".md",
                f'---\nid: "{snapshot}::node:x"\ntype: graph_entity_instance\n'
                f'logical_entity_uid: "node:x"\nsnapshot_id: "{snapshot}"\n'
                f'snapshot_instance_id: "{snapshot}::node:x"\nproject: AGV\n---\n# 左侧循墙\n',
            )
        model = self.build()
        args = self.query_args()
        self.assertEqual(next(doc for doc in model["documents"] if doc["id"] == "v1::node:x")["class"], "current_snapshot")
        self.assertEqual(next(doc for doc in model["documents"] if doc["id"] == "v2::node:x")["class"], "candidate")
        self.assertEqual(
            [item["id"] for item in kb.query(model, self.vault, "左侧循墙", args)],
            ["doc:a", "v1::node:x"],
        )
        args.snapshot = "v2"
        self.assertEqual(
            [item["id"] for item in kb.query(model, self.vault, "左侧循墙", args)],
            ["v2::node:x"],
        )
        args.snapshot = None
        self.assertEqual(kb.query(model, self.vault, "v2::node:x", args), [])
        args.include_candidate = True
        self.assertEqual([item["id"] for item in kb.query(model, self.vault, "v2::node:x", args)], ["v2::node:x"])
        self.write(
            "v2.md",
            '---\nid: "v2::node:x"\ntype: graph_entity_instance\n'
            'logical_entity_uid: "node:x"\nsnapshot_id: "v2"\n'
            'snapshot_instance_id: "v1::node:x"\n---\n# 错误实例\n',
        )
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "invalid instance key"):
            kb.build_model(self.vault, self.config_path)

    def test_logical_page_never_becomes_current_implementation(self):
        logical = {"path": "03_ROS/Nodes/left_wall_node.md", "type": "ros_node", "snapshot": None}
        v1 = {"path": "00_System/Graph_History/Snapshots/v1/Entities/Nodes/left.md",
              "type": "graph_entity_instance", "snapshot": "v1"}
        v2 = {**v1, "path": "00_System/Graph_History/Snapshots/v2/Entities/Nodes/left.md", "snapshot": "v2"}
        change = {"path": "00_System/Graph_History/Changes/v1__v2/left.md",
                  "type": "graph_change", "snapshot": None}
        for current, candidate in (("v1", "v2"), ("v2", "v1")):
            pointer = {"current_snapshot": current, "candidate_snapshot": candidate}
            self.assertEqual(kb.classify(logical, pointer), "logical_reference")
            self.assertEqual(kb.classify(v1 if current == "v1" else v2, pointer), "current_snapshot")
            self.assertEqual(kb.classify(v2 if current == "v1" else v1, pointer), "candidate")
            self.assertEqual(kb.classify(change, pointer), "historical")
        self.assertEqual(kb.classify({"path": "04_Navigation/topic.md", "type": "algorithm", "snapshot": None},
                                     pointer), "document")

    def test_logical_reference_and_history_query_boundaries(self):
        self.write("03_ROS/Nodes/ultrasonic_follower.md",
                   '---\nid: "node:logical"\ntype: ros_node\n---\n# 左侧循墙\n')
        self.write("00_System/Graph_History/Changes/v1__v2/change.md",
                   '---\nid: "change:old"\ntype: graph_change\n---\n# 左侧循墙\n')
        model = self.build()
        args = self.query_args()
        result = kb.query(kb.check(self.vault, self.config_path, self.index_dir), self.vault, "左侧循墙", args)
        self.assertEqual([(item["id"], item["class"]) for item in result],
                         [("doc:a", "document"), ("node:logical", "logical_reference")])
        self.assertEqual(kb.query(model, self.vault, "change:old", args), [])
        args.include_candidate = True
        self.assertEqual(kb.query(model, self.vault, "change:old", args), [])
        args.include_history = True
        self.assertEqual([item["id"] for item in kb.query(model, self.vault, "change:old", args)], ["change:old"])

    def test_index_files_and_query_are_checked_on_disk(self):
        model = self.build()
        self.assertEqual(set(kb.INDEX_FILES), {path.name for path in self.index_dir.iterdir()})
        self.assertEqual(model, kb.check(self.vault, self.config_path, self.index_dir))
        (self.index_dir / "documents.jsonl").write_bytes(b"{}\n")
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "stale"):
            kb.check(self.vault, self.config_path, self.index_dir)
        self.build()
        (self.index_dir / "index.json").write_bytes(b"{}\n")
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "stale"):
            kb.check(self.vault, self.config_path, self.index_dir)

    def test_alias_keyword_ambiguity_and_missing_result(self):
        self.write("b.md", '---\nid: "doc:b"\nproject: Other\n---\n# 左侧循墙\n')
        self.config["enrichments"] = {"doc:a": {
            "aliases": ["双超声", "left-wall"],
            "summary": "超声循墙资料",
        }}
        self.save_config()
        model = self.build()
        args = self.query_args()
        self.assertEqual(
            [item["id"] for item in kb.query(model, self.vault, "双超声", args)],
            ["doc:a"],
        )
        self.assertEqual(len(kb.query(model, self.vault, "左侧循墙", args)), 2)
        self.assertEqual(kb.query(model, self.vault, "不存在的主题", args), [])
        args.project = "AGV"
        self.assertEqual(
            [item["id"] for item in kb.query(model, self.vault, "左侧循墙", args)],
            ["doc:a"],
        )

    def test_source_and_evidence_change_make_index_stale(self):
        self.write("evidence.md", "---\nid: doc:e\n---\n# 证据\n")
        self.config["enrichments"] = {"doc:a": {
            "aliases": ["左侧双超声"],
            "evidence": [{
                "path": "evidence.md", "locator": "证据", "kind": "note",
                "state": "static", "summary": "归档",
            }],
        }}
        self.save_config()
        self.build()
        kb.check(self.vault, self.config_path, self.index_dir)
        self.write("evidence.md", "---\nid: doc:e\n---\n# 证据\n发生变化。\n")
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "stale"):
            kb.check(self.vault, self.config_path, self.index_dir)
        self.build()
        kb.check(self.vault, self.config_path, self.index_dir)
        self.write("a.md", '---\nid: "doc:a"\n---\n# 改动后的标题\n')
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "stale"):
            kb.check(self.vault, self.config_path, self.index_dir)
        (self.vault / "evidence.md").unlink()
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "missing or unsafe evidence"):
            kb.build_model(self.vault, self.config_path)

    def test_protected_input_change_fails(self):
        self.build()
        self.write("00_System/Graph_History/current.json", '{"current_snapshot":"v2","candidate_snapshot":"v1"}\n')
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "immutable"):
            kb.check(self.vault, self.config_path, self.index_dir)

    def test_missing_protected_tag_fails(self):
        self.build()
        self.config["protected_tags"] = {"missing": "0" * 40}
        self.save_config()
        with self.assertRaisesRegex(kb.IndexErrorWithContext, "tag changed or missing"):
            kb.check(self.vault, self.config_path, self.index_dir)

    def test_snapshot_machine_data_supplies_scoped_reference(self):
        self.write(
            "v2.md",
            '---\nid: "v2::node:x"\ntype: graph_entity_instance\n'
            'logical_entity_uid: "node:x"\nsnapshot_id: "v2"\n'
            'snapshot_instance_id: "v2::node:x"\ntags: [AGV]\n---\n# 左侧节点\n',
        )
        self.write(
            "00_System/Graph_History/Snapshots/v2/Machine/entities.jsonl",
            json.dumps({
                "entity_uid": "node:x", "source_scope": "vehicle-3",
                "semantic": {"vehicles": ["三号车"]},
            }, ensure_ascii=False) + "\n",
        )
        doc = next(item for item in self.build()["documents"] if item["id"] == "v2::node:x")
        self.assertEqual(doc["project"], "AGV")
        self.assertEqual(doc["vehicles"], ["三号车"])
        self.assertEqual(doc["scope"], "vehicle-3")
        self.assertEqual(doc["evidence"][0]["state"], "static-candidate")

    def test_links_cover_alias_anchor_canvas_and_ignore_fence(self):
        self.write("b.md", "# 正文\n## 章节\n段落 ^block-id\n")
        self.write("map.canvas", "{}")
        self.write(
            "a.md",
            '---\nid: "doc:a"\n---\n# 导航\n'
            '[[b#章节|显示别名]] ![[map.canvas]] [[b#^block-id]]\n'
            '~~~text\n[[not-a-real-page]]\n~~~\n',
        )
        self.assertEqual(kb.link_failures(self.vault, ["a.md"]), [])
        self.write("b.md", "# 正文\n")
        self.assertIn("missing anchor", kb.link_failures(self.vault, ["a.md"])[0])


if __name__ == "__main__":
    unittest.main()

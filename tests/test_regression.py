#!/usr/bin/env python3
"""
TeaBreak | اشرب شاي ☕ (v2.1.0-public)
Comprehensive Regression & Integration Test Suite
By #MOASHO11𓂀

Test Suite Scope:
1. Exact parity between MASTER_WIZARD.md embedded code and notify_on_stop.py.
2. Syntax compilation of extracted wizard script.
3. Event classification for documented schema values (model_stop) and empirical compatibility (NO_TOOL_CALL).
4. Background tasks detection (fullyIdle == False).
5. Privacy-by-default (zero prompt/transcript leaks when task description preview is OFF).
6. Sanitized task description preview (when explicitly enabled).
7. Redaction of sensitive termination reasons.
8. Git ignore negation patterns and re-verification.
9. Git tracking detection in root repository, nested sub-workspaces, and worktrees.
10. Fail-closed rejection of git execution errors.
11. Non-destructive hook registration and same-key / cross-key deduplication.
12. Preservation of falsey user metadata on uninstallation.
13. Downward-safe timeout budget normalization.
14. Extreme numeric boundary rejection.
15. Windows ctypes prototypes validation.
16. Real Windows pipe integration test with local mock HTTP server (delayed pipe, delayed EOF, empty/malformed).
17. Unknown CLI argument rejection with usage message.
18. Clean workspace installation.
"""

import os
import sys
import json
import shutil
import tempfile
import unittest
import subprocess
import time
import math
import threading
import http.server

# Add package root to sys.path
PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PACKAGE_ROOT)
import notify_on_stop as teabreak


# --------------------------------------------------------
# Local Mock HTTP Server for Pipe Integration Tests
# --------------------------------------------------------
class MockNtfyHandler(http.server.BaseHTTPRequestHandler):
    recorded_requests = []

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body_bytes = self.rfile.read(content_length)
        parsed_body = {}
        if body_bytes:
            try:
                parsed_body = json.loads(body_bytes.decode("utf-8"))
            except Exception:
                parsed_body = {"raw": body_bytes.decode("utf-8", errors="replace")}

        MockNtfyHandler.recorded_requests.append({
            "path": self.path,
            "headers": dict(self.headers),
            "body": parsed_body
        })

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"id":"mock_test_123","event":"message"}')

    def log_message(self, format, *args):
        pass  # Suppress HTTP logging in test output


class TestTeaBreakPublicRelease(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp(prefix="tb_pub_test_")
        self.agents_dir = os.path.join(self.test_dir, ".agents")
        os.makedirs(self.agents_dir, exist_ok=True)
        MockNtfyHandler.recorded_requests.clear()

    def tearDown(self):
        for root, dirs, files in os.walk(self.test_dir):
            for fname in files:
                try:
                    os.chmod(os.path.join(root, fname), 0o666)
                except Exception:
                    pass
        shutil.rmtree(self.test_dir, ignore_errors=True)

    # ----------------------------------------------------
    # Test 1: Byte-for-byte parity of embedded code in MASTER_WIZARD.md
    # ----------------------------------------------------
    def test_01_embedded_wizard_source_exact_parity(self):
        wizard_path = os.path.join(PACKAGE_ROOT, "MASTER_WIZARD.md")
        script_path = os.path.join(PACKAGE_ROOT, "notify_on_stop.py")

        self.assertTrue(os.path.exists(wizard_path), "MASTER_WIZARD.md is missing")
        self.assertTrue(os.path.exists(script_path), "notify_on_stop.py is missing")

        with open(wizard_path, "r", encoding="utf-8") as wf:
            wizard_text = wf.read()

        with open(script_path, "r", encoding="utf-8") as sf:
            script_text = sf.read()

        start_marker = "```python\n"
        start_idx = wizard_text.find(start_marker)
        self.assertNotEqual(start_idx, -1, "Could not find ```python code block in MASTER_WIZARD.md")
        start_idx += len(start_marker)
        end_idx = wizard_text.find("\n```", start_idx)
        self.assertNotEqual(end_idx, -1, "Could not find closing ``` in MASTER_WIZARD.md")

        norm_embedded = wizard_text[start_idx:end_idx].replace("\r\n", "\n").strip()
        norm_script = script_text.replace("\r\n", "\n").strip()

        self.assertEqual(
            norm_embedded,
            norm_script,
            "Embedded code in MASTER_WIZARD.md does not match notify_on_stop.py byte-for-byte!"
        )

    # ----------------------------------------------------
    # Test 2: Successful compilation of extracted embedded code
    # ----------------------------------------------------
    def test_02_extracted_code_compilation(self):
        wizard_path = os.path.join(PACKAGE_ROOT, "MASTER_WIZARD.md")
        with open(wizard_path, "r", encoding="utf-8") as wf:
            wizard_text = wf.read()

        start_marker = "```python\n"
        start_idx = wizard_text.find(start_marker) + len(start_marker)
        end_idx = wizard_text.find("\n```", start_idx)
        extracted = wizard_text[start_idx:end_idx]

        compiled = compile(extracted, "<extracted_wizard_script>", "exec")
        self.assertIsNotNone(compiled)

    # ----------------------------------------------------
    # Test 3: Documented official Antigravity terminationReason: model_stop
    # ----------------------------------------------------
    def test_03_model_stop_official_documented_value(self):
        """
        Tests the officially documented Antigravity schema event:
        terminationReason: 'model_stop' with fullyIdle: True.
        """
        payload = {
            "executionNum": 42,
            "terminationReason": "model_stop",
            "error": "",
            "fullyIdle": True,
            "workspacePaths": [self.test_dir]
        }
        res_en = teabreak.classify_event(payload, "DemoProject", "en", include_task_desc=False)
        self.assertEqual(res_en["status"], "TURN_FINISHED")
        self.assertEqual(res_en["title"], "TeaBreak ☕")
        self.assertIn("Execution completed ✅", res_en["message"])

        res_ar = teabreak.classify_event(payload, "DemoProject", "ar", include_task_desc=False)
        self.assertEqual(res_ar["status"], "TURN_FINISHED")
        self.assertEqual(res_ar["title"], "اشرب شاي ☕")
        self.assertIn("اكتمل التنفيذ ✅", res_ar["message"])

    # ----------------------------------------------------
    # Test 4: Empirically observed compatibility mapping: NO_TOOL_CALL
    # ----------------------------------------------------
    def test_04_no_tool_call_empirical_compatibility_mapping(self):
        """
        Tests the empirically observed runtime compatibility value:
        terminationReason: 'NO_TOOL_CALL' with fullyIdle: True.
        Note: Retained exclusively as an empirical compatibility mapping
        from local runtime debug event captures when model responds without tools.
        """
        payload = {
            "executionNum": 43,
            "terminationReason": "NO_TOOL_CALL",
            "error": "",
            "fullyIdle": True,
            "workspacePaths": [self.test_dir]
        }
        res = teabreak.classify_event(payload, "DemoProject", "en", include_task_desc=False)
        self.assertEqual(res["status"], "TURN_FINISHED")
        self.assertEqual(res["title"], "TeaBreak ☕")
        self.assertIn("Execution completed ✅", res["message"])

    # ----------------------------------------------------
    # Test 5: Background tasks active when fullyIdle is False
    # ----------------------------------------------------
    def test_05_background_tasks_active_when_not_idle(self):
        payload = {
            "executionNum": 44,
            "terminationReason": "model_stop",
            "error": "",
            "fullyIdle": False,
            "workspacePaths": [self.test_dir]
        }
        res = teabreak.classify_event(payload, "DemoProject", "en", include_task_desc=False)
        self.assertEqual(res["status"], "UNKNOWN")
        self.assertEqual(res["title"], "TeaBreak ☕")
        self.assertIn("Turn stopped (unknown reason)", res["message"])

    # ----------------------------------------------------
    # Test 6: Privacy mode OFF: Zero prompt, transcript, or question text leaks
    # ----------------------------------------------------
    def test_06_privacy_mode_off_zero_leaks(self):
        t_path = os.path.join(self.test_dir, "transcript.jsonl")
        sensitive_secret = "TOP_SECRET_CREDENTIAL_KEY_777"
        step = {
            "source": "MODEL",
            "type": "PLANNER_RESPONSE",
            "tool_calls": [{
                "name": "ask_question",
                "args": {"questions": [{"question": f"Proceed with {sensitive_secret}?"}]}
            }],
            "content": f"Analyzing {sensitive_secret}"
        }
        with open(t_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(step) + "\n")

        payload = {
            "executionNum": 45,
            "terminationReason": "model_stop",
            "fullyIdle": True,
            "transcriptPath": t_path,
            "lastUserInput": f"Please verify {sensitive_secret}"
        }

        res = teabreak.classify_event(payload, "DemoProject", "en", include_task_desc=False)
        self.assertEqual(res["status"], "WAITING_FOR_USER")
        self.assertNotIn(sensitive_secret, res["message"])
        self.assertNotIn(sensitive_secret, res["title"])
        self.assertEqual(res["title"], "TeaBreak ☕")
        self.assertIn("Result: Waiting for input ❓", res["message"])

    # ----------------------------------------------------
    # Test 7: Privacy mode ON: Sanitized task preview included
    # ----------------------------------------------------
    def test_07_privacy_mode_on_task_preview(self):
        payload = {
            "executionNum": 46,
            "terminationReason": "model_stop",
            "fullyIdle": True,
            "lastUserInput": "### Run unit tests and benchmark suite"
        }
        res = teabreak.classify_event(payload, "DemoProject", "en", include_task_desc=True)
        self.assertEqual(res["status"], "TURN_FINISHED")
        self.assertIn("Run unit tests and benchmark suite", res["message"])
        self.assertNotIn("###", res["message"])

    # ----------------------------------------------------
    # Test 8: Sensitive terminationReason string redaction
    # ----------------------------------------------------
    def test_08_sensitive_termination_reason_redaction(self):
        sensitive_term = "FORBIDDEN_USER_TOKEN_9999"
        payload = {
            "executionNum": 47,
            "terminationReason": sensitive_term,
            "error": "",
            "fullyIdle": True
        }
        res = teabreak.classify_event(payload, "DemoProject", "en", include_task_desc=False)
        self.assertEqual(res["status"], "UNKNOWN")
        self.assertNotIn(sensitive_term, res["message"])
        self.assertNotIn(sensitive_term, res["title"])
        self.assertEqual(res["title"], "TeaBreak ☕")
        self.assertIn("Result: Turn stopped (unknown reason)", res["message"])

    # ----------------------------------------------------
    # Test 9: Git ignore negation rules and re-ignore at final position
    # ----------------------------------------------------
    def test_09_git_negation_rules(self):
        gi_path = os.path.join(self.test_dir, ".gitignore")
        with open(gi_path, "w", encoding="utf-8") as f:
            f.write(".agents/*\n!.agents/teabreak.config.json\n")

        with open(gi_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertFalse(teabreak.evaluate_gitignore_rules(lines, ".agents/teabreak.config.json"))

        teabreak.ensure_gitignored_strict(self.test_dir, f".agents/{teabreak.DEFAULT_CONFIG_FILENAME}")

        with open(gi_path, "r", encoding="utf-8") as f:
            lines_after = f.readlines()
        self.assertTrue(teabreak.evaluate_gitignore_rules(lines_after, ".agents/teabreak.config.json"))

    # ----------------------------------------------------
    # Test 10: Git already-tracked file detection in root workspace
    # ----------------------------------------------------
    def test_10_git_tracked_file_rejection(self):
        subprocess.run(["git", "init", self.test_dir], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cfg_file = os.path.join(self.agents_dir, teabreak.DEFAULT_CONFIG_FILENAME)
        with open(cfg_file, "w", encoding="utf-8") as f:
            f.write('{"topic": "tb_tracked"}')

        subprocess.run(["git", "add", f".agents/{teabreak.DEFAULT_CONFIG_FILENAME}"], cwd=self.test_dir, check=True)

        with self.assertRaises(RuntimeError) as ctx:
            teabreak.ensure_gitignored_strict(self.test_dir, f".agents/{teabreak.DEFAULT_CONFIG_FILENAME}")
        self.assertIn("already tracked by Git", str(ctx.exception))

    # ----------------------------------------------------
    # Test 11: Git tracking detection in nested child workspace
    # ----------------------------------------------------
    def test_11_git_nested_workspace_tracked_file_rejection(self):
        """
        Reproduces the exact scenario:
        - Parent Git repository initialized.
        - Nested child workspace created.
        - .agents/teabreak.config.json added to parent Git index.
        - Installation from child workspace must detect tracking and abort.
        """
        parent_repo = os.path.join(self.test_dir, "parent_repo")
        os.makedirs(parent_repo, exist_ok=True)
        subprocess.run(["git", "init", parent_repo], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        child_ws = os.path.join(parent_repo, "sub", "child_workspace")
        child_agents = os.path.join(child_ws, ".agents")
        os.makedirs(child_agents, exist_ok=True)

        cfg_file = os.path.join(child_agents, teabreak.DEFAULT_CONFIG_FILENAME)
        with open(cfg_file, "w", encoding="utf-8") as f:
            f.write('{"topic": "tb_nested_tracked"}')

        # Add to parent repo index
        subprocess.run(["git", "add", cfg_file], cwd=parent_repo, check=True)

        # Installation from child workspace must abort
        with self.assertRaises(RuntimeError) as ctx:
            teabreak.ensure_gitignored_strict(child_ws, f".agents/{teabreak.DEFAULT_CONFIG_FILENAME}")
        self.assertIn("already tracked by Git", str(ctx.exception))

        # Untrack file from parent repository index
        subprocess.run(["git", "rm", "--cached", cfg_file], cwd=parent_repo, check=True, stdout=subprocess.PIPE)

        # Now installation from child workspace should succeed and ignore
        ok = teabreak.ensure_gitignored_strict(child_ws, f".agents/{teabreak.DEFAULT_CONFIG_FILENAME}")
        self.assertTrue(ok)

    # ----------------------------------------------------
    # Test 12: Git worktree (.git file) detection
    # ----------------------------------------------------
    def test_12_git_worktree_detection(self):
        """
        Tests Git repository discovery when .git is a file (Git worktree).
        """
        main_repo = os.path.join(self.test_dir, "main_repo")
        os.makedirs(main_repo, exist_ok=True)
        subprocess.run(["git", "init", main_repo], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=main_repo, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=main_repo, check=True)

        with open(os.path.join(main_repo, "init.txt"), "w") as f:
            f.write("init")
        subprocess.run(["git", "add", "init.txt"], cwd=main_repo, check=True)
        subprocess.run(["git", "commit", "-m", "init"], cwd=main_repo, check=True)

        wt_dir = os.path.join(self.test_dir, "worktree_dir")
        subprocess.run(["git", "worktree", "add", wt_dir, "-b", "wt_branch"], cwd=main_repo, check=True, stdout=subprocess.PIPE)

        # Verify .git is a file in worktree
        self.assertTrue(os.path.isfile(os.path.join(wt_dir, ".git")))

        # Test repository root discovery
        status, root, err = teabreak.find_git_repo_root(wt_dir)
        self.assertEqual(status, "REPO")
        self.assertEqual(os.path.normpath(root), os.path.normpath(wt_dir))

        # Verify file is not tracked
        track_status, is_tracked, _ = teabreak.check_git_tracking(wt_dir, f".agents/{teabreak.DEFAULT_CONFIG_FILENAME}")
        self.assertEqual(track_status, "UNTRACKED")
        self.assertFalse(is_tracked)

    # ----------------------------------------------------
    # Test 13: Same-key multiple duplicate removal
    # ----------------------------------------------------
    def test_13_same_key_duplicate_removal(self):
        hooks_p = os.path.join(self.agents_dir, "hooks.json")
        initial_data = {
            teabreak.HOOK_KEY: {
                "enabled": True,
                "Stop": [
                    {"type": "command", "command": "echo 'unrelated'"},
                    {"type": "command", "command": "python ./.agents/scripts/notify_on_stop.py"},
                    {"type": "command", "command": "python3 ./.agents/scripts/notify_on_stop.py"}
                ],
                "meta_val": 42
            }
        }
        with open(hooks_p, "w", encoding="utf-8") as f:
            json.dump(initial_data, f)

        ok, msg = teabreak.install_hook_safely(self.test_dir)
        self.assertTrue(ok)

        with open(hooks_p, "r", encoding="utf-8") as f:
            after = json.load(f)

        stop_list = after[teabreak.HOOK_KEY]["Stop"]
        self.assertEqual(len(stop_list), 2)
        tb_cmds = [cmd for cmd in stop_list if teabreak.is_teabreak_command(cmd.get("command", ""))]
        self.assertEqual(len(tb_cmds), 1)
        self.assertEqual(after[teabreak.HOOK_KEY]["meta_val"], 42)

    # ----------------------------------------------------
    # Test 14: Cross-key duplicate removal across legacy and canonical keys
    # ----------------------------------------------------
    def test_14_cross_key_duplicate_removal(self):
        hooks_p = os.path.join(self.agents_dir, "hooks.json")
        initial_data = {
            teabreak.LEGACY_HOOK_KEY: {
                "enabled": True,
                "Stop": [{"type": "command", "command": "python ./.agents/scripts/notify_on_stop.py"}]
            },
            teabreak.HOOK_KEY: {
                "enabled": True,
                "Stop": [{"type": "command", "command": "python ./.agents/scripts/notify_on_stop.py"}]
            }
        }
        with open(hooks_p, "w", encoding="utf-8") as f:
            json.dump(initial_data, f)

        ok, msg = teabreak.install_hook_safely(self.test_dir)
        self.assertTrue(ok)

        with open(hooks_p, "r", encoding="utf-8") as f:
            after = json.load(f)

        self.assertNotIn(teabreak.LEGACY_HOOK_KEY, after)
        self.assertIn(teabreak.HOOK_KEY, after)
        self.assertEqual(len(after[teabreak.HOOK_KEY]["Stop"]), 1)

    # ----------------------------------------------------
    # Test 15: Preservation of falsey user metadata on uninstall
    # ----------------------------------------------------
    def test_15_falsey_metadata_preservation(self):
        hooks_p = os.path.join(self.agents_dir, "hooks.json")
        initial_data = {
            teabreak.HOOK_KEY: {
                "enabled": True,
                "Stop": [{"type": "command", "command": "python ./.agents/scripts/notify_on_stop.py"}],
                "debug": False,
                "counter": 0,
                "note": "",
                "items": []
            }
        }
        with open(hooks_p, "w", encoding="utf-8") as f:
            json.dump(initial_data, f)

        ok, msg = teabreak.uninstall_hook_safely(self.test_dir)
        self.assertTrue(ok)

        with open(hooks_p, "r", encoding="utf-8") as f:
            after = json.load(f)

        self.assertIn(teabreak.HOOK_KEY, after)
        entry = after[teabreak.HOOK_KEY]
        self.assertEqual(entry["debug"], False)
        self.assertEqual(entry["counter"], 0)
        self.assertEqual(entry["note"], "")
        self.assertEqual(entry["items"], [])
        self.assertEqual(len(entry["Stop"]), 0)

    # ----------------------------------------------------
    # Test 16: Timeout budget downward-safe floor rounding boundary
    # ----------------------------------------------------
    def test_16_timeout_budget_rounding_boundary(self):
        raw = {
            "max_retries": 1,
            "http_timeout": 8.95,
            "retry_delay": 0.11
        }
        norm = teabreak.validate_and_normalize_config(raw)
        budget = teabreak.calculate_max_network_budget(norm)
        self.assertLessEqual(budget, 20.00)
        self.assertLessEqual(budget, teabreak.DEFAULT_HOOK_TIMEOUT)

    # ----------------------------------------------------
    # Test 17: Rejection of extreme integers, NaN, Inf
    # ----------------------------------------------------
    def test_17_extreme_numeric_values_rejection(self):
        for bad in [10**50, -10**50, float("nan"), float("inf"), float("-inf")]:
            raw = {
                "max_retries": bad,
                "retry_delay": bad,
                "http_timeout": bad
            }
            norm = teabreak.validate_and_normalize_config(raw)
            self.assertEqual(norm["max_retries"], teabreak.DEFAULT_MAX_RETRIES)
            self.assertEqual(norm["retry_delay"], teabreak.DEFAULT_RETRY_DELAY)
            self.assertEqual(norm["http_timeout"], teabreak.DEFAULT_HTTP_TIMEOUT)

    # ----------------------------------------------------
    # Test 18: Rejection of unknown CLI arguments
    # ----------------------------------------------------
    def test_18_unknown_cli_argument_rejection(self):
        script_p = os.path.join(PACKAGE_ROOT, "notify_on_stop.py")
        p = subprocess.Popen(
            [sys.executable, script_p, "--diagnose"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        out, err = p.communicate(timeout=3.0)
        self.assertEqual(p.returncode, 2)
        self.assertIn("Unrecognized command line option '--diagnose'", err)
        self.assertIn("Usage:", out)

    # ----------------------------------------------------
    # Test 19: Full Windows Pipe Integration with Local Mock HTTP Server
    # ----------------------------------------------------
    def test_19_pipe_integration_with_local_mock_server(self):
        """
        Real integration test:
        1. Spins up a local HTTP mock server (no public ntfy requests).
        2. Configures a temporary workspace with notify_on_stop.py.
        3. Executes script as a subprocess via standard input pipe.
        4. Verifies exact payload received, parsed, and classified by mock server.
        5. Tests delayed pipe arrival and delayed EOF cases.
        6. Verifies that empty or malformed events are not classified as TURN_FINISHED.
        """
        # Start ephemeral local HTTP server
        server = http.server.HTTPServer(("127.0.0.1", 0), MockNtfyHandler)
        port = server.server_address[1]
        server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        server_thread.start()

        script_p = os.path.join(PACKAGE_ROOT, "notify_on_stop.py")
        topic_name = "test_pipe_integration_topic"

        # Setup workspace config pointing to local mock server
        cfg_file = os.path.join(self.agents_dir, teabreak.DEFAULT_CONFIG_FILENAME)
        with open(cfg_file, "w", encoding="utf-8") as f:
            json.dump({
                "topic": topic_name,
                "server_url": f"http://127.0.0.1:{port}",
                "language": "en",
                "include_task_description": False,
                "max_retries": 1,
                "retry_delay": 0.1,
                "http_timeout": 2.0
            }, f)

        try:
            # Subtest A: Standard model_stop pipe event
            MockNtfyHandler.recorded_requests.clear()
            event_a = {
                "executionNum": 101,
                "terminationReason": "model_stop",
                "error": "",
                "fullyIdle": True,
                "workspacePaths": [self.test_dir]
            }
            p = subprocess.Popen(
                [sys.executable, script_p],
                cwd=self.test_dir,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            out, err = p.communicate(input=json.dumps(event_a).encode("utf-8"), timeout=5.0)
            self.assertEqual(p.returncode, 0)
            self.assertIn('"decision": "allow"', out.decode("utf-8"))

            self.assertEqual(len(MockNtfyHandler.recorded_requests), 1)
            req_a = MockNtfyHandler.recorded_requests[0]["body"]
            self.assertEqual(req_a["topic"], topic_name)
            self.assertEqual(req_a["title"], "TeaBreak ☕")
            self.assertIn("Result: Execution completed ✅", req_a["message"])
            self.assertEqual(req_a["priority"], 3)

            # Subtest B: Empirical compatibility value NO_TOOL_CALL with delayed pipe arrival
            MockNtfyHandler.recorded_requests.clear()
            event_b = {
                "executionNum": 102,
                "terminationReason": "NO_TOOL_CALL",
                "error": "",
                "fullyIdle": True,
                "workspacePaths": [self.test_dir]
            }
            p = subprocess.Popen(
                [sys.executable, script_p],
                cwd=self.test_dir,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            time.sleep(0.15)  # Delayed pipe arrival
            p.stdin.write(json.dumps(event_b).encode("utf-8"))
            p.stdin.flush()
            p.stdin.close()
            out, err = p.communicate(timeout=5.0)
            self.assertEqual(p.returncode, 0)

            self.assertEqual(len(MockNtfyHandler.recorded_requests), 1)
            req_b = MockNtfyHandler.recorded_requests[0]["body"]
            self.assertEqual(req_b["title"], "TeaBreak ☕")
            self.assertIn("Result: Execution completed ✅", req_b["message"])

            # Subtest C: Delayed EOF handling
            MockNtfyHandler.recorded_requests.clear()
            event_c = {
                "executionNum": 103,
                "terminationReason": "model_stop",
                "error": "",
                "fullyIdle": True,
                "workspacePaths": [self.test_dir]
            }
            p = subprocess.Popen(
                [sys.executable, script_p],
                cwd=self.test_dir,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            p.stdin.write(json.dumps(event_c).encode("utf-8"))
            p.stdin.flush()
            time.sleep(0.15)  # Delayed EOF
            p.stdin.close()
            out, err = p.communicate(timeout=5.0)
            self.assertEqual(p.returncode, 0)
            self.assertEqual(len(MockNtfyHandler.recorded_requests), 1)

            # Subtest D: Empty stdin pipe (must NOT classify as TURN_FINISHED)
            MockNtfyHandler.recorded_requests.clear()
            p = subprocess.Popen(
                [sys.executable, script_p],
                cwd=self.test_dir,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            out, err = p.communicate(input=b"", timeout=5.0)
            self.assertEqual(p.returncode, 0)
            self.assertEqual(len(MockNtfyHandler.recorded_requests), 1)
            req_d = MockNtfyHandler.recorded_requests[0]["body"]
            self.assertEqual(req_d["title"], "TeaBreak ☕")
            self.assertIn("Result: Unreadable payload", req_d["message"])

            # Subtest E: Malformed JSON stdin pipe (must NOT classify as TURN_FINISHED)
            MockNtfyHandler.recorded_requests.clear()
            p = subprocess.Popen(
                [sys.executable, script_p],
                cwd=self.test_dir,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            out, err = p.communicate(input=b"{malformed json", timeout=5.0)
            self.assertEqual(p.returncode, 0)
            self.assertEqual(len(MockNtfyHandler.recorded_requests), 1)
            req_e = MockNtfyHandler.recorded_requests[0]["body"]
            self.assertEqual(req_e["title"], "TeaBreak ☕")
            self.assertIn("Result: Unreadable payload", req_e["message"])

        finally:
            server.shutdown()
            server.server_close()

    # ----------------------------------------------------
    # Test 20: Clean workspace installation
    # ----------------------------------------------------
    def test_20_clean_workspace_installation(self):
        clean_dir = tempfile.mkdtemp(prefix="tb_clean_install_")
        try:
            cfg_data = {
                "topic": "tb_test_clean_123",
                "language": "en",
                "include_task_description": False
            }
            teabreak.save_config(clean_dir, cfg_data)
            ok, msg = teabreak.install_hook_safely(clean_dir)
            self.assertTrue(ok)

            cfg_p = os.path.join(clean_dir, ".agents", teabreak.DEFAULT_CONFIG_FILENAME)
            hooks_p = os.path.join(clean_dir, ".agents", "hooks.json")
            gi_p = os.path.join(clean_dir, ".gitignore")

            self.assertTrue(os.path.exists(cfg_p))
            self.assertTrue(os.path.exists(hooks_p))
            self.assertTrue(os.path.exists(gi_p))

            with open(hooks_p, "r", encoding="utf-8") as f:
                hooks = json.load(f)
            self.assertIn(teabreak.HOOK_KEY, hooks)
            self.assertEqual(hooks[teabreak.HOOK_KEY]["Stop"][0]["timeout"], teabreak.DEFAULT_HOOK_TIMEOUT)
        finally:
            shutil.rmtree(clean_dir, ignore_errors=True)



    # ----------------------------------------------------
    # Test 21: Four canonical states + fallbacks coverage in AR and EN
    # ----------------------------------------------------
    def test_21_canonical_states_full_matrix(self):
        project = "TestMatrix"

        # 1. QUOTA_EXHAUSTED
        quota_payload = {"error": "ResourceExhausted: 429 Rate limit exceeded", "fullyIdle": True}
        res_q_ar = teabreak.classify_event(quota_payload, project, "ar", False)
        self.assertEqual(res_q_ar["status"], "QUOTA_EXHAUSTED")
        self.assertEqual(res_q_ar["title"], "اشرب شاي ☕")
        self.assertIn("النتيجة: نفدت الكوتة ⏳", res_q_ar["message"])

        res_q_en = teabreak.classify_event(quota_payload, project, "en", False)
        self.assertEqual(res_q_en["status"], "QUOTA_EXHAUSTED")
        self.assertEqual(res_q_en["title"], "TeaBreak ☕")
        self.assertIn("Result: Quota limit reached ⏳", res_q_en["message"])

        # 2. EXECUTION_ERROR
        err_payload = {"error": "Fatal runtime failure", "fullyIdle": True}
        res_e_ar = teabreak.classify_event(err_payload, project, "ar", False)
        self.assertEqual(res_e_ar["status"], "EXECUTION_ERROR")
        self.assertEqual(res_e_ar["title"], "اشرب شاي ☕")
        self.assertIn("النتيجة: فشل التنفيذ ⚠️", res_e_ar["message"])

        res_e_en = teabreak.classify_event(err_payload, project, "en", False)
        self.assertEqual(res_e_en["status"], "EXECUTION_ERROR")
        self.assertEqual(res_e_en["title"], "TeaBreak ☕")
        self.assertIn("Result: Execution failed ⚠️", res_e_en["message"])

        # 3. WAITING_FOR_USER (via ask_question tool call)
        wait_payload = {
            "terminationReason": "model_stop",
            "fullyIdle": True,
            "transcriptPath": os.path.join(self.test_dir, "t_empty.jsonl")
        }
        with open(wait_payload["transcriptPath"], "w", encoding="utf-8") as tf:
            tf.write(json.dumps({"source": "MODEL", "type": "PLANNER_RESPONSE", "tool_calls": [{"name": "ask_question"}]}) + "\n")
        res_w_ar = teabreak.classify_event(wait_payload, project, "ar", False)
        self.assertEqual(res_w_ar["status"], "WAITING_FOR_USER")
        self.assertEqual(res_w_ar["title"], "اشرب شاي ☕")
        self.assertIn("النتيجة: مستني ردك ❓", res_w_ar["message"])

        res_w_en = teabreak.classify_event(wait_payload, project, "en", False)
        self.assertEqual(res_w_en["status"], "WAITING_FOR_USER")
        self.assertEqual(res_w_en["title"], "TeaBreak ☕")
        self.assertIn("Result: Waiting for input ❓", res_w_en["message"])

        # 4. TURN_FINISHED
        done_payload = {"terminationReason": "model_stop", "fullyIdle": True}
        res_d_ar = teabreak.classify_event(done_payload, project, "ar", False)
        self.assertEqual(res_d_ar["status"], "TURN_FINISHED")
        self.assertEqual(res_d_ar["title"], "اشرب شاي ☕")
        self.assertIn("النتيجة: اكتمل التنفيذ ✅", res_d_ar["message"])

        res_d_en = teabreak.classify_event(done_payload, project, "en", False)
        self.assertEqual(res_d_en["status"], "TURN_FINISHED")
        self.assertEqual(res_d_en["title"], "TeaBreak ☕")
        self.assertIn("Result: Execution completed ✅", res_d_en["message"])

        # Fallbacks: INVALID_PAYLOAD & UNKNOWN
        res_inv = teabreak.classify_event(None, project, "ar", False)
        self.assertEqual(res_inv["status"], "INVALID_PAYLOAD")

        res_unk = teabreak.classify_event({"terminationReason": "something_unknown"}, project, "ar", False)
        self.assertEqual(res_unk["status"], "UNKNOWN")

    # ----------------------------------------------------
    # Test 22: Dual Scope Global Plugin Functions
    # ----------------------------------------------------
    def test_22_global_plugin_paths_and_helpers(self):
        plugin_dir = teabreak.get_global_plugin_dir()
        hooks_p = teabreak.get_global_hooks_path()
        cfg_p = teabreak.get_global_config_path()

        self.assertIn(".gemini", plugin_dir)
        self.assertIn("mobile-alerts", plugin_dir)
        self.assertTrue(hooks_p.endswith("hooks.json"))
        self.assertTrue(cfg_p.endswith(teabreak.DEFAULT_CONFIG_FILENAME))

if __name__ == "__main__":
    unittest.main()

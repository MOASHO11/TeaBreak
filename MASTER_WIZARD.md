# TeaBreak | اشرب شاي ☕ (v2.1.0) — Standalone Bilingual Master Setup Wizard
**By #MOASHO11𓂀** — [LinkedIn Profile](https://www.linkedin.com/in/moasho11/)  
**Official Repository:** [https://github.com/moasho11/TeaBreak](https://github.com/moasho11/TeaBreak) (Release: `v2.1.0`)

> **Arabic Tagline:** خلّي مساعدك يشتغل، واشرب شايك ☕  
> **English Tagline:** Let your AI work while you sip your tea ☕

---

## 🎯 About This Master Prompt / عن هذا المعالج الذكي

This prompt is a 100% turnkey, self-contained installation, configuration, testing, and lifecycle management wizard for **TeaBreak | اشرب شاي ☕**.

When an Antigravity agent or user executes this wizard, follow the **Strict Sequential Phases** below.
- Do NOT skip phases.
- Do NOT bundle independent questions together.
- Do NOT send live network notifications without explicit user consent.
- Respect fail-closed Git protection and zero OS control boundaries at all times.

---

## 📋 Architectural Overview & Dual Scope / نظرة معمارية وخيارات النطاق

TeaBreak supports two distinct deployment scopes depending on user needs:

### 1. Workspace Hook (Current Repository Only) / خطاف المشروع المحلي
- **Target Location:** `./.agents/scripts/notify_on_stop.py` & `./.agents/hooks.json`
- **Scope:** Applies exclusively to the active workspace.
- **Privacy:** Configuration stored in `./.agents/teabreak.config.json` with strict `.gitignore` fail-closed protection.
- **Best for:** Developers working on specific repositories or who prefer isolated configurations per project.

### 2. Global Plugin (All Projects Centrally) / البلجن العام لكافة المشاريع
- **Target Location:** `~/.gemini/config/plugins/mobile-alerts/`
- **Scope:** Automatically intercepts Stop events across ALL workspaces opened in Google Antigravity.
- **Privacy:** Central configuration stored in the user profile plugins directory. Individual workspaces can optionally override settings using a local `.agents/teabreak.config.json`.
- **Best for:** Developers who want automatic, effortless notifications across every project without configuring each workspace individually.

---

## 🚀 Sequential Execution Protocol / بروتوكول التنفيذ المرحلي المتسلسل

Follow these phases sequentially. At the end of each phase, stop and wait for the user's explicit reply before proceeding.

---

### Phase 1: Language Selection / اختيار لغة الإشعار والمعالج

Ask the user to choose their preferred communication and notification language:

- **1. العربية (اشرب شاي ☕)** — إشعارات وهوية باللغة العربية.
- **2. English (TeaBreak ☕)** — Notifications and brand identity in English.

*Agent Action: Stop and wait for user selection.*

---

### Phase 2: Code Source & GitHub Verification / مصدر الكود ومطابقة الإصدار

Display the official code source information to the user:
- **Repository:** `https://github.com/moasho11/TeaBreak`
- **Release Tag:** `v2.1.0` (Immutable release)
- **Raw Script URL:** `https://raw.githubusercontent.com/moasho11/TeaBreak/v2.1.0/notify_on_stop.py`

Present the source choice:
- **Option A (GitHub Fetch):** Download the verified `v2.1.0` script directly from the official GitHub repository.
- **Option B (Embedded Offline Fallback):** Use the canonical, cryptographically verified script embedded directly inside this Master Wizard (guaranteed SHA-256 parity, ideal for offline or restricted environments).

*Agent Action: Confirm user choice before proceeding to Phase 3.*

---

### Phase 3: Scope & Operation Selection / اختيار نطاق التثبيت أو الإدارة

Ask the user which operation they wish to perform:

- **1. Install in Current Project (Workspace Hook)** — يثبّت داخل المشروع الحالي فقط في مجلد `.agents/`.
- **2. Install Centrally as Global Plugin** — يثبّت كبلجن عام لجميع المشاريع في `~/.gemini/config/plugins/mobile-alerts/`.
- **3. Check Status & Diagnostics** — فحص حالة الـ Hooks والإعدادات الحالية دون أي تعديل.
- **4. Clean Uninstall** — إزالة نظيفة لخطافات TeaBreak مع الحفاظ التام على أي أدوات أو خطافات أخرى للمستخدم.

*Agent Action: Stop and wait for user choice.*

---

### Phase 4: Mobile Push Transport (ntfy) & Topic Setup / إعداد تطبيق ntfy والقناة

Explain to the user:
1. **ntfy App:** Download the free, open-source **ntfy** app from Google Play, Apple App Store, or access `https://ntfy.sh` in the browser.
2. **Zero Signup:** No account, email, or password required.
3. **Topic Security:** ntfy topics are public endpoints; unguessable randomness is your cryptographic privacy barrier.

Offer the topic selection:
- **Option A (Recommended):** Generate a cryptographically secure 128-bit unguessable random topic (e.g., `tb_` followed by 32 hex characters).
- **Option B:** User specifies their own custom private topic name.

*Agent Action: Confirm the topic name with the user.*

---

### Phase 5: Privacy Settings & Task Snippet / إعدادات الخصوصية ومقتطف المهمة

Explain the privacy options:
- **Privacy Mode (Recommended):** Sends only the workspace name and event status (e.g. `Execution completed ✅`, `Waiting for input ❓`, `Quota limit reached ⏳`). Never transmits prompts, code, or file names.
- **Task Preview Mode (Opt-in):** Appends a sanitized, 80-character snippet of the user task to the notification message.

Ask the user: *Would you like to enable the task snippet in notifications? (no / yes)*

*Agent Action: Record user preference.*

---

### Phase 6: Automated Execution & Protection / التنفيذ الآلي وحماية البيانات

Execute the installation safely according to the selected scope:

#### For Workspace Hook:
1. Detect Python 3 interpreter (`python3` or `sys.executable`).
2. Create directory `.agents/scripts/`.
3. Place `notify_on_stop.py` (fetched from GitHub or extracted from embedded code below) at `.agents/scripts/notify_on_stop.py`.
4. Enforce fail-closed Git protection:
   - Ensure `.agents/teabreak.config.json` is in `.gitignore`.
   - Verify that Git ignore rules take effect and are not negated.
   - Verify the file is not already tracked in the Git index.
5. Save `.agents/teabreak.config.json` containing the chosen topic and settings.
6. Register the Stop hook in `.agents/hooks.json` under key `teabreak-mobile-alert` with 20s timeout and deduplication.

#### For Global Plugin:
1. Target directory: `~/.gemini/config/plugins/mobile-alerts/`.
2. Create `scripts/` directory and place `notify_on_stop.py` there.
3. Write `plugin.json` declaring plugin metadata.
4. Save `teabreak.config.json` in the plugin directory.
5. Register `teabreak-mobile-alert` in `~/.gemini/config/plugins/mobile-alerts/hooks.json`.
6. Deduplicate and ensure no duplicate workspace hooks fire simultaneously.

*Agent Action: Run `<python> notify_on_stop.py --status` and present the output to the user.*

---

### Phase 7: Optional Live Test Notification / فحص الاتصال الاختياري

Ask the user explicitly:
> *"هل ترغب في إرسال إشعار تجريبي الآن للتأكد من وصول التنبيه لهاتفك؟ (نعم / لا)"*  
> *"Would you like to send an optional test notification to verify delivery on your phone now? (yes / no)"*

- **If YES:** Run `python notify_on_stop.py --test`
- **If NO:** Skip test dispatch and conclude setup.

*Agent Note: Never dispatch live network notifications without explicit user consent.*

---

### Phase 8: Safe Uninstallation Reference / دليل الإزالة النظيفة

If the user ever wishes to remove TeaBreak:
- **Workspace Hook:** Run `python ./.agents/scripts/notify_on_stop.py --uninstall`
- **Global Plugin:** Run `python notify_on_stop.py --uninstall-global`
- TeaBreak preserves all unrelated user hooks, falsey metadata, and custom configurations.

---

## 📦 Canonical Embedded Source Code (`notify_on_stop.py` v2.1.0)

This is the canonical, verified, pure-Python single-file implementation.

```python
#!/usr/bin/env python3
"""
TeaBreak | اشرب شاي ☕ (v2.1.0-public)
Official Repository: https://github.com/moasho11/TeaBreak
Author: #MOASHO11𓂀 (https://www.linkedin.com/in/moasho11/)

Arabic Tagline: خلّي مساعدك يشتغل، واشرب شايك ☕
English Tagline: Let your AI work while you sip your tea ☕

Architecture & Integrity Standards:
- Native Google Antigravity Stop Hook Integration.
- Pure Python 3 Standard Library only (zero external pip packages).
- Push-only notification transport via ntfy.sh (No daemon, no polling, no local server).
- Privacy-by-Default: Strict status-only messages; zero transcript/prompt/token leaks.
- Fail-Closed Git Protection: Evaluates top-to-bottom negation rules, detects
  already-tracked files in Git index, and verifies effective ignore BEFORE saving topic.
- Windows Named Pipe & Delayed-EOF safe stdin reader with explicit ctypes prototypes.
- Completely deduplicated hook installation: strips same-key & cross-key duplicates
  while strictly preserving all unrelated handlers and falsey metadata.
- Mathematically safe timeout normalization: downward floor rounding guaranteeing
  configured network budget <= Hook timeout (20s) under all boundary inputs.
- Dual Scope Support: Local Workspace Hook (.agents/) or Global Plugin (.gemini/config/plugins/).
- Zero OS control policy strictly observed.
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error
import re
import secrets
import shutil
import math
import fnmatch
import subprocess

VERSION = "2.1.0"
DEFAULT_CONFIG_FILENAME = "teabreak.config.json"
HOOKS_FILENAME = "hooks.json"
HOOK_KEY = "teabreak-mobile-alert"
LEGACY_HOOK_KEY = "mobile-stop-alert"

DEFAULT_HOOK_TIMEOUT = 20
DEFAULT_HTTP_TIMEOUT = 4.0
DEFAULT_MAX_RETRIES = 2
DEFAULT_RETRY_DELAY = 1.0
OVERHEAD_MARGIN = 2.0

# --------------------------------------------------------
# Windows ctypes API Prototypes (Module-Level Initialization)
# --------------------------------------------------------
if sys.platform == "win32":
    try:
        import msvcrt
        import ctypes
        from ctypes import wintypes

        kernel32 = ctypes.windll.kernel32
        kernel32.GetFileType.argtypes = [wintypes.HANDLE]
        kernel32.GetFileType.restype = wintypes.DWORD

        kernel32.PeekNamedPipe.argtypes = [
            wintypes.HANDLE,
            wintypes.LPVOID,
            wintypes.DWORD,
            ctypes.POINTER(wintypes.DWORD),
            ctypes.POINTER(wintypes.DWORD),
            ctypes.POINTER(wintypes.DWORD)
        ]
        kernel32.PeekNamedPipe.restype = wintypes.BOOL
    except Exception:
        pass

# --------------------------------------------------------
# 1. Topic & Budget Calculation Helpers
# --------------------------------------------------------
def redact_topic(topic):
    """Redacts private topic name to prevent token leaks in console logs."""
    if not topic or not isinstance(topic, str):
        return "[NOT CONFIGURED]"
    t = topic.strip()
    if len(t) <= 8:
        return "***"
    return f"{t[:3]}***{t[-4:]}"

def is_valid_number(val):
    """
    Rejects non-numeric types, booleans, NaN, Infinite values,
    and extreme integers that could trigger overflow.
    """
    if not isinstance(val, (int, float)) or isinstance(val, bool):
        return False
    if isinstance(val, int) and (val > 1000000 or val < -1000000):
        return False
    return not (math.isnan(val) or math.isinf(val))

def calculate_max_network_budget(config):
    """
    Calculates the configured network-operation budget in seconds based on
    the actual retry loop and backoff delays:
    delay for attempt i is: retry_delay * (i + 1)
    Note: This is an estimated network-operation budget, not an absolute
    guaranteed OS wall-clock deadline.
    """
    max_retries = config["max_retries"]
    http_timeout = config["http_timeout"]
    retry_delay = config["retry_delay"]

    attempts = max_retries + 1
    total_http = attempts * http_timeout
    total_delays = sum((i + 1) * retry_delay for i in range(max_retries))
    return total_http + total_delays + OVERHEAD_MARGIN

def enforce_timeout_budget(config, hook_timeout=DEFAULT_HOOK_TIMEOUT):
    """
    Strictly enforces that the configured network budget (including all
    HTTP attempts, backoff delays, and processing overhead) NEVER exceeds
    the configured Hook timeout.
    Uses downward-safe rounding and iterative clamping to guarantee
    calculate_max_network_budget(config) <= hook_timeout without rounding overflow.
    """
    while config["max_retries"] > 1 and calculate_max_network_budget(config) > hook_timeout:
        config["max_retries"] -= 1

    if calculate_max_network_budget(config) > hook_timeout and config["retry_delay"] > 1.0:
        config["retry_delay"] = 1.0

    attempts = config["max_retries"] + 1
    delays = sum((i + 1) * config["retry_delay"] for i in range(config["max_retries"]))
    available_http = hook_timeout - OVERHEAD_MARGIN - delays

    if available_http > 0:
        max_possible = available_http / attempts
        target = min(config["http_timeout"], max_possible)
        safe_timeout = math.floor(target * 100.0) / 100.0
        config["http_timeout"] = max(1.0, safe_timeout)
    else:
        config["max_retries"] = 0
        config["retry_delay"] = 0.0
        safe_timeout = math.floor((hook_timeout - OVERHEAD_MARGIN) * 100.0) / 100.0
        config["http_timeout"] = max(1.0, safe_timeout)

    while calculate_max_network_budget(config) > hook_timeout and config["http_timeout"] > 1.0:
        config["http_timeout"] = round(config["http_timeout"] - 0.01, 2)

    if calculate_max_network_budget(config) > hook_timeout and config["max_retries"] > 0:
        config["max_retries"] = 0
        config["retry_delay"] = 0.0
        while calculate_max_network_budget(config) > hook_timeout and config["http_timeout"] > 1.0:
            config["http_timeout"] = round(config["http_timeout"] - 0.01, 2)

    final_budget = calculate_max_network_budget(config)
    assert final_budget <= hook_timeout + 1e-9, f"Configured budget {final_budget} exceeds {hook_timeout}"

    return config

def validate_and_normalize_config(raw_cfg):
    """
    Strictly validates configuration types, ranges, and defaults.
    - Rejects NaN, Inf, and non-numeric types.
    - include_task_description is ONLY True if explicitly the JSON boolean True.
    - topic must be a non-empty string.
    - Enforces configured network budget <= DEFAULT_HOOK_TIMEOUT.
    """
    if not isinstance(raw_cfg, dict):
        raw_cfg = {}

    raw_topic = raw_cfg.get("topic")
    if isinstance(raw_topic, str) and raw_topic.strip():
        topic = raw_topic.strip()
    else:
        topic = ""

    raw_lang = raw_cfg.get("language")
    if isinstance(raw_lang, str) and raw_lang.strip().lower() in ["ar", "en"]:
        lang = raw_lang.strip().lower()
    else:
        lang = "ar"

    raw_include_task = raw_cfg.get("include_task_description")
    include_task_desc = (raw_include_task is True)

    raw_retries = raw_cfg.get("max_retries")
    if is_valid_number(raw_retries):
        try:
            max_retries = int(raw_retries)
            if max_retries < 0 or max_retries > 3:
                max_retries = DEFAULT_MAX_RETRIES
        except (ValueError, TypeError, OverflowError):
            max_retries = DEFAULT_MAX_RETRIES
    else:
        max_retries = DEFAULT_MAX_RETRIES

    raw_delay = raw_cfg.get("retry_delay")
    if is_valid_number(raw_delay):
        try:
            retry_delay = float(raw_delay)
            if retry_delay < 0.1 or retry_delay > 5.0:
                retry_delay = DEFAULT_RETRY_DELAY
        except (ValueError, TypeError, OverflowError):
            retry_delay = DEFAULT_RETRY_DELAY
    else:
        retry_delay = DEFAULT_RETRY_DELAY

    raw_timeout = raw_cfg.get("http_timeout")
    if is_valid_number(raw_timeout):
        try:
            http_timeout = float(raw_timeout)
            if http_timeout < 1.0 or http_timeout > 10.0:
                http_timeout = DEFAULT_HTTP_TIMEOUT
        except (ValueError, TypeError, OverflowError):
            http_timeout = DEFAULT_HTTP_TIMEOUT
    else:
        http_timeout = DEFAULT_HTTP_TIMEOUT

    raw_server = raw_cfg.get("server_url")
    if isinstance(raw_server, str) and raw_server.strip().startswith(("https://", "http://")):
        server_url = raw_server.strip()
    else:
        server_url = "https://ntfy.sh"

    config = {
        "topic": topic,
        "language": lang,
        "include_task_description": include_task_desc,
        "max_retries": max_retries,
        "retry_delay": retry_delay,
        "http_timeout": http_timeout,
        "server_url": server_url
    }

    return enforce_timeout_budget(config, DEFAULT_HOOK_TIMEOUT)

# --------------------------------------------------------
# 2. Fail-Closed Git Protection & Config Storage
# --------------------------------------------------------
def matches_gitignore_pattern(pattern, target_path):
    """
    Matches a single gitignore rule against target_path.
    Handles exact, directory, and glob patterns according to git standards.
    """
    p = pattern.strip().replace("\\", "/")
    t = target_path.strip().replace("\\", "/").lstrip("/")
    p_clean = p.lstrip("/")

    if p_clean == t or p_clean == os.path.basename(t):
        return True

    if p.endswith("/"):
        dir_clean = p_clean.rstrip("/")
        if t == dir_clean or t.startswith(dir_clean + "/"):
            return True
    elif p_clean in [".agents", "agents"]:
        if t == p_clean or t.startswith(p_clean + "/"):
            return True

    if fnmatch.fnmatch(t, p_clean) or fnmatch.fnmatch(os.path.basename(t), p_clean):
        return True

    if p_clean.endswith("/*"):
        prefix = p_clean[:-2]
        if t.startswith(prefix + "/"):
            return True

    return False

def evaluate_gitignore_rules(lines, target_path):
    """
    Evaluates whether target_path is effectively ignored according to .gitignore lines.
    Strictly respects Git's top-to-bottom rule ordering and negation ('!') prefix.
    Returns: bool (True if effectively ignored, False if not ignored or negated).
    """
    ignored = False
    for line in lines:
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
        is_negation = line_clean.startswith("!")
        pat = line_clean[1:].strip() if is_negation else line_clean
        if matches_gitignore_pattern(pat, target_path):
            ignored = not is_negation
    return ignored

def find_git_repo_root(workspace_dir):
    """
    Discovers the Git repository root for workspace_dir, supporting nested
    workspace directories, Git worktrees (.git file), and submodules.
    Returns:
        (status, repo_root, error_msg)
        where status is:
        - "REPO": Inside a Git repository; repo_root is the absolute normalized path.
        - "NOT_REPO": Confirmed not inside any Git repository.
        - "ERROR": Git execution failed or git executable missing when .git markers exist.
    """
    if not os.path.isdir(workspace_dir):
        return ("ERROR", None, f"Workspace path does not exist or is not a directory: {workspace_dir}")

    try:
        res = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=workspace_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if res.returncode == 0:
            top_level = res.stdout.strip()
            if top_level:
                return ("REPO", os.path.normpath(top_level), None)
        elif res.returncode == 128:
            err_lower = res.stderr.lower()
            if "not a git repository" in err_lower:
                return ("NOT_REPO", None, None)
            return ("ERROR", None, f"git rev-parse returned code 128: {res.stderr.strip()}")
        else:
            return ("ERROR", None, f"git rev-parse failed (code {res.returncode}): {res.stderr.strip()}")
    except FileNotFoundError:
        curr = os.path.abspath(workspace_dir)
        while True:
            dot_git = os.path.join(curr, ".git")
            if os.path.isdir(dot_git) or os.path.isfile(dot_git):
                return ("ERROR", None, f"Git repository detected at '{curr}' but 'git' command is not available on PATH")
            parent = os.path.dirname(curr)
            if parent == curr:
                break
            curr = parent
        return ("NOT_REPO", None, None)
    except Exception as e:
        return ("ERROR", None, f"Unexpected error during git detection: {e}")

def check_git_tracking(workspace_dir, relative_path):
    """
    Checks if relative_path inside workspace_dir is tracked by Git.
    Returns tuple: (status, is_tracked, error_msg)
    - status="NOT_REPO": Not a git repository (is_tracked=False).
    - status="TRACKED": File is tracked in Git index (is_tracked=True).
    - status="UNTRACKED": Repository exists, but file is NOT tracked in Git index (is_tracked=False).
    - status="ERROR": Git execution failed; tracking status cannot be safely established.
    """
    repo_status, repo_root, err = find_git_repo_root(workspace_dir)
    if repo_status == "NOT_REPO":
        return ("NOT_REPO", False, None)
    if repo_status == "ERROR":
        return ("ERROR", False, err)

    norm_rel = relative_path.replace("\\", "/").strip().lstrip("/")
    abs_target = os.path.abspath(os.path.join(workspace_dir, norm_rel))
    try:
        rel_to_repo = os.path.relpath(abs_target, repo_root).replace("\\", "/")
    except ValueError:
        rel_to_repo = norm_rel

    try:
        res = subprocess.run(
            ["git", "ls-files", "--error-unmatch", rel_to_repo],
            cwd=repo_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if res.returncode == 0:
            return ("TRACKED", True, None)
        elif res.returncode == 1:
            return ("UNTRACKED", False, None)
        else:
            return ("ERROR", False, f"git ls-files failed (code {res.returncode}): {res.stderr.strip()}")
    except Exception as e:
        return ("ERROR", False, f"Git check failed: {e}")

def is_file_tracked_by_git(workspace_dir, relative_path):
    """
    Backward-compatible boolean check.
    Returns True if tracked in Git index, False if untracked or not a repo.
    Raises RuntimeError if Git tracking check encountered an execution error.
    """
    status, is_tracked, err = check_git_tracking(workspace_dir, relative_path)
    if status == "ERROR":
        raise RuntimeError(f"Git tracking check failed: {err}")
    return is_tracked

def verify_gitignored(workspace_dir, relative_path):
    """
    Verifies that relative_path is effectively ignored.
    Uses Git CLI check-ignore if inside a repository; falls back to full
    top-to-bottom rules evaluation with negation support.
    """
    norm_rel = relative_path.replace("\\", "/").strip().lstrip("/")
    repo_status, repo_root, _ = find_git_repo_root(workspace_dir)

    if repo_status == "REPO":
        abs_target = os.path.abspath(os.path.join(workspace_dir, norm_rel))
        try:
            rel_to_repo = os.path.relpath(abs_target, repo_root).replace("\\", "/")
        except ValueError:
            rel_to_repo = norm_rel

        try:
            res = subprocess.run(
                ["git", "check-ignore", "-q", rel_to_repo],
                cwd=repo_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if res.returncode == 0:
                return True
            elif res.returncode == 1:
                return False
        except Exception:
            pass

    gitignore_path = os.path.join(workspace_dir, ".gitignore")
    if os.path.exists(gitignore_path):
        try:
            with open(gitignore_path, "r", encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
            if evaluate_gitignore_rules(lines, norm_rel):
                return True
        except Exception:
            pass

    if repo_status == "REPO" and repo_root and repo_root != os.path.normpath(workspace_dir):
        root_gitignore = os.path.join(repo_root, ".gitignore")
        if os.path.exists(root_gitignore):
            try:
                with open(root_gitignore, "r", encoding="utf-8", errors="replace") as f:
                    lines = f.readlines()
                abs_target = os.path.abspath(os.path.join(workspace_dir, norm_rel))
                rel_to_repo = os.path.relpath(abs_target, repo_root).replace("\\", "/")
                if evaluate_gitignore_rules(lines, rel_to_repo):
                    return True
            except Exception:
                pass

    return False

def ensure_gitignored_strict(workspace_dir, relative_path):
    """
    Strict fail-closed git protection.
    1. Detects if file is already tracked by Git index (in root, nested workspace, or worktree).
    2. Respects Git's top-to-bottom rules and negation patterns.
    3. Safely appends exact rule at final position if needed.
    4. Verifies effective ignore status.
    5. Raises exception and aborts if protection cannot be guaranteed.
    """
    if not os.path.isdir(workspace_dir):
        raise ValueError(f"Target workspace directory is invalid or does not exist: {workspace_dir}")

    norm_rel = relative_path.replace("\\", "/").strip().lstrip("/")

    status, is_tracked, err = check_git_tracking(workspace_dir, norm_rel)
    if status == "ERROR":
        raise RuntimeError(f"Git tracking verification failed: {err}. Cannot safely verify repository protection.")
    if is_tracked:
        raise RuntimeError(
            f"Security Alert: '{norm_rel}' is already tracked by Git. Adding it to .gitignore "
            f"will NOT protect it. Run 'git rm --cached {norm_rel}' before installing TeaBreak."
        )

    if verify_gitignored(workspace_dir, norm_rel):
        return True

    gitignore_path = os.path.join(workspace_dir, ".gitignore")
    entry_line = f".agents/{DEFAULT_CONFIG_FILENAME}\n"

    try:
        mode = "a" if os.path.exists(gitignore_path) else "w"
        needs_nl = False
        if mode == "a" and os.path.getsize(gitignore_path) > 0:
            with open(gitignore_path, "rb") as bf:
                bf.seek(-1, os.SEEK_END)
                if bf.read(1) not in (b"\n", b"\r"):
                    needs_nl = True

        with open(gitignore_path, mode, encoding="utf-8") as f:
            if needs_nl:
                f.write("\n")
            f.write(f"# TeaBreak - Sensitive local configuration (Topic security)\n{entry_line}")
    except Exception as e:
        raise OSError(f"Failed to write .gitignore in {workspace_dir}: {e}") from e

    if not verify_gitignored(workspace_dir, norm_rel):
        raise RuntimeError(f"Git ignore verification failed: {norm_rel} was not effectively ignored in {gitignore_path}.")

    return True

def get_config_path(workspace_dir):
    agents_dir = os.path.join(workspace_dir, ".agents")
    os.makedirs(agents_dir, exist_ok=True)
    return os.path.join(agents_dir, DEFAULT_CONFIG_FILENAME)

def save_config(workspace_dir, config_data):
    """
    Saves configuration with fail-closed Git protection:
    1. Validates target workspace directory.
    2. Enforces .gitignore entry BEFORE saving sensitive file.
    3. Verifies .gitignore persistence.
    4. Only then creates backup and writes teabreak.config.json.
    5. Raises exception and aborts if protection fails.
    """
    if not os.path.isdir(workspace_dir):
        raise ValueError(f"Invalid workspace directory: {workspace_dir}")

    ensure_gitignored_strict(workspace_dir, f".agents/{DEFAULT_CONFIG_FILENAME}")

    cfg_path = get_config_path(workspace_dir)
    normalized = validate_and_normalize_config(config_data)

    if os.path.exists(cfg_path):
        create_backup(cfg_path)

    with open(cfg_path, "w", encoding="utf-8") as f:
        json.dump(normalized, f, indent=2, ensure_ascii=False)

    return cfg_path

def get_global_plugin_dir():
    """Returns the central Antigravity plugin directory path."""
    return os.path.expanduser(os.path.join("~", ".gemini", "config", "plugins", "mobile-alerts"))

def get_global_hooks_path():
    """Returns the central plugin hooks.json path."""
    return os.path.join(get_global_plugin_dir(), HOOKS_FILENAME)

def get_global_config_path():
    """Returns the central plugin teabreak.config.json path."""
    return os.path.join(get_global_plugin_dir(), DEFAULT_CONFIG_FILENAME)

def load_config(workspace_dir):
    """
    Loads configuration with hierarchical precedence:
    1. Workspace-specific config (.agents/teabreak.config.json)
    2. Central global plugin config (~/.gemini/config/plugins/mobile-alerts/teabreak.config.json)
    3. User home config (~/.teabreak.config.json)
    4. Environment variables (TEABREAK_TOPIC, TEABREAK_LANG)
    """
    ws_cfg = get_config_path(workspace_dir)
    global_cfg = get_global_config_path()
    home_cfg = os.path.join(os.path.expanduser("~"), f".{DEFAULT_CONFIG_FILENAME}")

    target_path = None
    if os.path.exists(ws_cfg):
        target_path = ws_cfg
    elif os.path.exists(global_cfg):
        target_path = global_cfg
    elif os.path.exists(home_cfg):
        target_path = home_cfg

    raw = {
        "topic": os.environ.get("TEABREAK_TOPIC", ""),
        "language": os.environ.get("TEABREAK_LANG", "ar"),
        "include_task_description": False,
        "max_retries": DEFAULT_MAX_RETRIES,
        "retry_delay": DEFAULT_RETRY_DELAY,
        "http_timeout": DEFAULT_HTTP_TIMEOUT,
        "server_url": "https://ntfy.sh"
    }

    if target_path and os.path.exists(target_path):
        try:
            with open(target_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                if isinstance(loaded, dict):
                    raw.update(loaded)
                else:
                    sys.stderr.write(f"[TeaBreak] Warning: {target_path} root is not a dictionary. Ignoring file content.\n")
        except Exception as e:
            sys.stderr.write(f"[TeaBreak] Error: Failed to parse {target_path}: {e}\n")

    return validate_and_normalize_config(raw)

def generate_secure_topic():
    """Generates an unguessable 128-bit cryptographically secure topic (32 hex characters)."""
    return f"tb_{secrets.token_hex(16)}"

# --------------------------------------------------------
# 3. Non-Destructive Hooks Management
# --------------------------------------------------------
def get_hooks_path(workspace_dir):
    return os.path.join(workspace_dir, ".agents", HOOKS_FILENAME)

def create_backup(file_path):
    """
    Creates a unique, collision-safe backup of a configuration file with
    microsecond timestamp, PID, and random nonce.
    """
    if os.path.exists(file_path):
        ts = int(time.time() * 1000000)
        pid = os.getpid()
        nonce = secrets.token_hex(4)
        bak_path = f"{file_path}.bak.{ts}.{pid}.{nonce}"
        counter = 0
        while os.path.exists(bak_path):
            counter += 1
            bak_path = f"{file_path}.bak.{ts}.{pid}.{nonce}.{counter}"
        shutil.copy2(file_path, bak_path)
        return bak_path
    return None

def format_python_command(interpreter_path=None):
    """Formats python interpreter command handling paths with spaces properly."""
    if not interpreter_path:
        interpreter_path = sys.executable or "python"

    interpreter_path = interpreter_path.strip()
    if "notify_on_stop.py" in interpreter_path:
        return interpreter_path

    if " " in interpreter_path and not (interpreter_path.startswith('"') and interpreter_path.endswith('"')):
        quoted_interp = f'"{interpreter_path}"'
    else:
        quoted_interp = interpreter_path

    return f"{quoted_interp} ./.agents/scripts/notify_on_stop.py"

def is_teabreak_command(cmd_str):
    """
    Strictly checks whether a command string belongs to TeaBreak.
    Matches canonical script execution patterns, preventing deletion of
    unrelated user commands that happen to have similar filenames.
    """
    if not isinstance(cmd_str, str):
        return False
    normalized = cmd_str.strip().replace("\\", "/")
    canonical_targets = [
        "./.agents/scripts/notify_on_stop.py",
        ".agents/scripts/notify_on_stop.py",
        "./scripts/notify_on_stop.py",
        "scripts/notify_on_stop.py"
    ]
    for target in canonical_targets:
        if normalized.endswith(f" {target}") or normalized.endswith(f'"{target}"') or normalized.endswith(f"'{target}'") or normalized == target:
            return True
    return False

def install_hook_safely(workspace_dir, python_cmd=None):
    """
    Safely registers TeaBreak Stop hook in .agents/hooks.json without
    erasing existing hooks, modifying unrelated events, or leaving duplicates.
    Completely deduplicates multiple TeaBreak entries within HOOK_KEY and
    removes duplicates from LEGACY_HOOK_KEY.
    """
    hooks_path = get_hooks_path(workspace_dir)
    os.makedirs(os.path.dirname(hooks_path), exist_ok=True)

    target_command = format_python_command(python_cmd)
    target_entry = {
        "type": "command",
        "command": target_command,
        "timeout": DEFAULT_HOOK_TIMEOUT
    }

    hooks_data = {}
    if os.path.exists(hooks_path):
        try:
            with open(hooks_path, "r", encoding="utf-8") as f:
                hooks_data = json.load(f)
        except Exception as e:
            return False, f"Existing {hooks_path} is malformed JSON. Aborting without changes: {e}"

        if not isinstance(hooks_data, dict):
            return False, f"Existing {hooks_path} root is not a JSON object (type: {type(hooks_data).__name__}). Aborting without changes."

        for k in [HOOK_KEY, LEGACY_HOOK_KEY]:
            if k in hooks_data:
                entry = hooks_data[k]
                if not isinstance(entry, dict):
                    return False, f"Existing key '{k}' in {hooks_path} has unexpected non-dictionary type. Aborting without changes."
                if "Stop" in entry and not isinstance(entry["Stop"], list):
                    return False, f"Existing key '{k}' has unexpected non-list 'Stop' field (type: {type(entry['Stop']).__name__}). Aborting without changes."

        create_backup(hooks_path)

    # 1. Clean up ALL duplicate TeaBreak commands from LEGACY_HOOK_KEY
    if LEGACY_HOOK_KEY in hooks_data and isinstance(hooks_data[LEGACY_HOOK_KEY], dict):
        legacy_entry = hooks_data[LEGACY_HOOK_KEY]
        legacy_stop = legacy_entry.get("Stop")
        if isinstance(legacy_stop, list):
            new_legacy_stop = [
                item for item in legacy_stop
                if not (isinstance(item, dict) and is_teabreak_command(item.get("command", "")))
            ]
            legacy_entry["Stop"] = new_legacy_stop

        unrelated_legacy = [k for k in legacy_entry.keys() if k not in ["enabled", "Stop"]]
        if not unrelated_legacy and not legacy_entry.get("Stop"):
            del hooks_data[LEGACY_HOOK_KEY]

    # 2. Ensure canonical HOOK_KEY exists
    if HOOK_KEY not in hooks_data:
        hooks_data[HOOK_KEY] = {"enabled": True, "Stop": []}
    elif not isinstance(hooks_data[HOOK_KEY], dict):
        return False, f"Unexpected type for {HOOK_KEY}. Aborting."

    entry = hooks_data[HOOK_KEY]
    if "Stop" not in entry or not isinstance(entry["Stop"], list):
        entry["Stop"] = []

    # 3. Clean up ALL duplicate TeaBreak entries within HOOK_KEY, preserving unrelated handlers
    unrelated_stops = [
        item for item in entry["Stop"]
        if not (isinstance(item, dict) and is_teabreak_command(item.get("command", "")))
    ]

    unrelated_stops.append(target_entry)
    entry["Stop"] = unrelated_stops
    entry["enabled"] = True

    try:
        with open(hooks_path, "w", encoding="utf-8") as f:
            json.dump(hooks_data, f, indent=2, ensure_ascii=False)
        return True, "Hook installed successfully."
    except Exception as e:
        return False, f"Failed to write {hooks_path}: {e}"

def uninstall_hook_safely(workspace_dir):
    """
    Safely removes only TeaBreak's command entry from recognized TeaBreak keys.
    Strictly preserves:
    - Unrelated user hook keys (even if their command contains notify_on_stop.py).
    - Unrelated Stop command entries under the recognized key.
    - All unrelated event lists (PreToolUse, PostToolUse, SessionStart, etc.).
    - All metadata and custom fields, INCLUDING empty or falsey metadata (False, 0, "", [], {}).
    Deletes the hook key ONLY when it contains no other configuration or events.
    """
    hooks_path = get_hooks_path(workspace_dir)
    if not os.path.exists(hooks_path):
        return True, "No hooks.json file found."

    try:
        with open(hooks_path, "r", encoding="utf-8") as f:
            hooks_data = json.load(f)
            if not isinstance(hooks_data, dict):
                return False, f"Invalid format in {hooks_path}: root must be a JSON object."
    except Exception as e:
        return False, f"Could not read {hooks_path}: {e}"

    create_backup(hooks_path)
    modified = False

    for k in [HOOK_KEY, LEGACY_HOOK_KEY]:
        if k not in hooks_data:
            continue

        entry = hooks_data[k]
        if not isinstance(entry, dict):
            continue

        stop_list = entry.get("Stop")
        if isinstance(stop_list, list):
            new_stop_list = []
            for item in stop_list:
                if isinstance(item, dict) and is_teabreak_command(item.get("command", "")):
                    modified = True
                else:
                    new_stop_list.append(item)
            entry["Stop"] = new_stop_list

        other_user_keys = [
            key for key in entry.keys()
            if key not in ["enabled", "Stop"]
        ]
        stop_has_handlers = bool(entry.get("Stop"))

        if not other_user_keys and not stop_has_handlers:
            del hooks_data[k]
            modified = True

    if modified:
        try:
            with open(hooks_path, "w", encoding="utf-8") as f:
                json.dump(hooks_data, f, indent=2, ensure_ascii=False)
            return True, "TeaBreak hook safely removed from hooks.json."
        except Exception as e:
            return False, f"Failed to save modified hooks.json: {e}"

    return True, "No TeaBreak hook was registered in hooks.json."

def install_global_plugin_safely(python_cmd=None, topic=None, lang="ar", include_desc=False):
    """
    Safely installs TeaBreak as a central Antigravity plugin for all projects in:
    ~/.gemini/config/plugins/mobile-alerts/
    """
    plugin_dir = get_global_plugin_dir()
    scripts_dir = os.path.join(plugin_dir, "scripts")
    os.makedirs(scripts_dir, exist_ok=True)

    # 1. Copy script into global plugin scripts/
    target_script = os.path.join(scripts_dir, "notify_on_stop.py")
    current_script = os.path.abspath(__file__)
    if os.path.abspath(target_script) != current_script:
        shutil.copy2(current_script, target_script)

    # 2. Write or update plugin.json
    plugin_json_path = os.path.join(plugin_dir, "plugin.json")
    plugin_data = {
        "name": "mobile-alerts",
        "displayName": "TeaBreak | اشرب شاي",
        "version": VERSION,
        "description": "TeaBreak | اشرب شاي ☕ — Instant mobile notifications for Antigravity stop events"
    }
    with open(plugin_json_path, "w", encoding="utf-8") as f:
        json.dump(plugin_data, f, indent=2, ensure_ascii=False)

    # 3. Write or update global config
    if topic:
        cfg_data = {
            "topic": topic,
            "language": lang,
            "include_task_description": include_desc,
            "max_retries": DEFAULT_MAX_RETRIES,
            "retry_delay": DEFAULT_RETRY_DELAY,
            "http_timeout": DEFAULT_HTTP_TIMEOUT,
            "server_url": "https://ntfy.sh"
        }
        normalized = validate_and_normalize_config(cfg_data)
        global_cfg_path = get_global_config_path()
        with open(global_cfg_path, "w", encoding="utf-8") as f:
            json.dump(normalized, f, indent=2, ensure_ascii=False)

    # 4. Write or update hooks.json
    hooks_path = get_global_hooks_path()
    hooks_data = {}
    if os.path.exists(hooks_path):
        try:
            with open(hooks_path, "r", encoding="utf-8") as f:
                hooks_data = json.load(f)
        except Exception:
            hooks_data = {}

    if not isinstance(hooks_data, dict):
        hooks_data = {}

    cmd = "python ./scripts/notify_on_stop.py"
    hooks_data[HOOK_KEY] = {
        "enabled": True,
        "Stop": [
            {
                "type": "command",
                "command": cmd,
                "timeout": DEFAULT_HOOK_TIMEOUT
            }
        ]
    }

    if LEGACY_HOOK_KEY in hooks_data:
        del hooks_data[LEGACY_HOOK_KEY]

    with open(hooks_path, "w", encoding="utf-8") as f:
        json.dump(hooks_data, f, indent=2, ensure_ascii=False)

    return True, f"Global plugin installed successfully in {plugin_dir}"

def uninstall_global_plugin_safely():
    """Uninstalls TeaBreak global plugin hook from ~/.gemini/config/plugins/mobile-alerts/hooks.json."""
    hooks_path = get_global_hooks_path()
    if not os.path.exists(hooks_path):
        return True, "No global hooks.json file found."

    try:
        with open(hooks_path, "r", encoding="utf-8") as f:
            hooks_data = json.load(f)
    except Exception as e:
        return False, f"Could not read global {hooks_path}: {e}"

    if not isinstance(hooks_data, dict):
        return False, f"Invalid format in global {hooks_path}: root must be a JSON object."

    create_backup(hooks_path)
    modified = False

    for k in [HOOK_KEY, LEGACY_HOOK_KEY]:
        if k in hooks_data:
            del hooks_data[k]
            modified = True

    if modified:
        with open(hooks_path, "w", encoding="utf-8") as f:
            json.dump(hooks_data, f, indent=2, ensure_ascii=False)
        return True, "Global hook uninstalled successfully."
    return True, "No TeaBreak global hook found."


# --------------------------------------------------------
# 4. Pipe-Safe Stdin Reader (Cross-Platform)
# --------------------------------------------------------
def read_stdin_cross_platform(timeout_seconds=0.8):
    """
    Safely reads JSON hook payload from stdin pipe without indefinite blocking.
    Handles:
    - Windows named/anonymous pipes via ctypes PeekNamedPipe with explicit prototypes.
    - Windows redirected disk files (< file.json) via GetFileType.
    - POSIX (Linux, macOS) pipes via select.select.
    - Early exit when complete valid JSON is detected.
    - Delayed EOF from parent writer processes.
    - Broken pipes and invalid handles handled gracefully without unbounded fallback.
    - Interactive TTYs return immediately.
    """
    if sys.stdin is None or sys.stdin.closed:
        return ""
    try:
        if sys.stdin.isatty():
            return ""
    except Exception:
        pass

    # Windows pipe & file handling
    if sys.platform == "win32":
        try:
            import msvcrt
            import ctypes
            from ctypes import wintypes

            kernel32 = ctypes.windll.kernel32
            h_val = msvcrt.get_osfhandle(sys.stdin.fileno())
            if h_val == -1 or h_val == wintypes.HANDLE(-1).value:
                return ""

            h_pipe = wintypes.HANDLE(h_val)
            file_type = kernel32.GetFileType(h_pipe)

            # FILE_TYPE_DISK = 1, FILE_TYPE_CHAR = 2, FILE_TYPE_PIPE = 3
            if file_type == 1:
                chunk = os.read(sys.stdin.fileno(), 65536)
                return chunk.decode("utf-8", errors="replace")
            elif file_type != 3:
                return ""

            avail = wintypes.DWORD(0)
            start_t = time.time()
            buf = bytearray()

            while time.time() - start_t < timeout_seconds:
                success = kernel32.PeekNamedPipe(
                    h_pipe, None, 0, None, ctypes.byref(avail), None
                )
                if not success:
                    break

                if avail.value > 0:
                    chunk = os.read(sys.stdin.fileno(), avail.value)
                    if not chunk:
                        break
                    buf.extend(chunk)
                    try:
                        json.loads(buf.decode("utf-8"))
                        break
                    except Exception:
                        pass
                else:
                    if buf:
                        time.sleep(0.02)
                    else:
                        time.sleep(0.01)

            return buf.decode("utf-8", errors="replace")
        except Exception:
            return ""

    # POSIX (Linux, macOS) handling
    else:
        try:
            import select
            start_t = time.time()
            buf = bytearray()
            while time.time() - start_t < timeout_seconds:
                remaining = max(0.01, timeout_seconds - (time.time() - start_t))
                rlist, _, _ = select.select([sys.stdin], [], [], remaining)
                if not rlist:
                    break
                chunk = os.read(sys.stdin.fileno(), 4096)
                if not chunk:
                    break
                buf.extend(chunk)
                try:
                    json.loads(buf.decode("utf-8"))
                    break
                except Exception:
                    pass
            return buf.decode("utf-8", errors="replace")
        except Exception:
            return ""

# --------------------------------------------------------
# 5. Strict Stop Event Classification & Privacy Matrix
# --------------------------------------------------------
SECRET_PATTERNS = [
    re.compile(r'bearer\s+[A-Za-z0-9_\-\.]{15,}', re.IGNORECASE),
    re.compile(r'(?:api[_-]?key|secret|token|password|auth|passwd)[\s:=]+[A-Za-z0-9_\-\.]{8,}', re.IGNORECASE),
    re.compile(r'(?:sk-[a-zA-Z0-9\-_]{15,}|ghp_[a-zA-Z0-9]{20,}|AKIA[0-9A-Z]{16}|ai_za[a-zA-Z0-9_-]{20,})', re.IGNORECASE),
    re.compile(r'(?:postgres|mysql|mongodb|redis):\/\/[^:]+:[^@]+@', re.IGNORECASE),
    re.compile(r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----', re.IGNORECASE)
]

def clean_task_text(text):
    if not isinstance(text, str) or not text.strip():
        return ""
    cleaned = re.sub(r'[\r\n\t]+', ' ', text)
    cleaned = re.sub(r'^[#\s\-_*>]+', '', cleaned)
    cleaned = re.sub(r'<[^>]+>', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return (cleaned[:77] + "...") if len(cleaned) > 80 else cleaned

def extract_safe_task_snippet(data):
    """
    Extracts a sanitized, privacy-safe task snippet (max 80 chars) strictly
    from the original user request / task description in the event payload.
    Does NOT extract from transcript, model output, tool outputs, code, or files.
    Redacts or drops secrets (API keys, passwords, bearer tokens, DB URIs).
    Returns empty string if no valid description is present or if input is a secret.
    """
    if not isinstance(data, dict):
        return ""
    raw_desc = data.get("taskDescription") or data.get("lastUserInput") or data.get("userPrompt")
    if not isinstance(raw_desc, str) or not raw_desc.strip():
        return ""
    cleaned = re.sub(r'[\r\n\t]+', ' ', raw_desc)
    cleaned = re.sub(r'^[#\s\-_*>]+', '', cleaned)
    cleaned = re.sub(r'<[^>]+>', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    for pat in SECRET_PATTERNS:
        if pat.search(cleaned):
            cleaned = pat.sub('[REDACTED]', cleaned)
    cleaned = cleaned.strip()
    if not cleaned or cleaned == '[REDACTED]':
        return ""
    if len(cleaned) > 80:
        cleaned = cleaned[:77].rstrip() + "..."
    return cleaned

def get_last_model_turn(data):
    """
    Safely retrieves the last MODEL planner response from transcriptPath.
    Applies os.path.expanduser() and avoids hardcoded filesystem assumptions.
    """
    if not isinstance(data, dict):
        return None

    raw_tp = data.get("transcriptPath")
    if not isinstance(raw_tp, str) or not raw_tp.strip():
        return None

    expanded_tp = os.path.expanduser(raw_tp.strip())
    paths = [expanded_tp]
    compact = expanded_tp.replace("transcript_full.jsonl", "transcript.jsonl")
    if os.path.exists(compact):
        paths.insert(0, compact)

    for path in paths:
        try:
            if not os.path.exists(path):
                continue
            size = os.path.getsize(path)
            offset = max(0, size - 65536)
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                f.seek(offset)
                lines = f.readlines()
            for line in reversed(lines):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    if isinstance(obj, dict) and obj.get("source") == "MODEL" and obj.get("type") == "PLANNER_RESPONSE":
                        return obj
                except Exception:
                    continue
        except Exception:
            continue
    return None

def check_waiting_for_user(data, model_step=None):
    """
    Checks for explicit, structural user confirmation / intervention signals.
    Does NOT classify regular conversational text questions as waiting.
    """
    if isinstance(data, dict):
        if data.get("requiresAction") is True or data.get("waitingForUser") is True or data.get("confirmationRequired") is True:
            return True

    if isinstance(model_step, dict):
        tool_calls = model_step.get("tool_calls")
        if isinstance(tool_calls, list):
            for tc in tool_calls:
                if not isinstance(tc, dict):
                    continue
                name = tc.get("name")
                if name == "ask_question":
                    return True
                if name in ("write_file", "edit_file"):
                    args = tc.get("args")
                    if isinstance(args, dict):
                        meta = args.get("ArtifactMetadata")
                        if isinstance(meta, dict) and meta.get("RequestFeedback") is True:
                            return True
    return False

def is_quota_exhausted(err_str):
    if not err_str:
        return False
    e_low = err_str.lower()
    quota_signals = [
        "resourceexhausted", "resource_exhausted", "quota_exceeded",
        "quota exceeded", "insufficient_quota", "insufficient quota",
        "exceeded your quota", "exceeded your current quota",
        "exhausted your quota", "quota limit reached", "individual quota",
        "daily quota", "out of credits", "zero credits", "billing quota",
        "usage limit exceeded"
    ]
    for sig in quota_signals:
        if sig in e_low:
            return True
    if "quota" in e_low and any(w in e_low for w in ["exceed", "exhaust", "deplet", "zero"]):
        if ("per minute" in e_low or "concurrency" in e_low or "rate limit" in e_low) and not any(w in e_low for w in ["exhaust", "insufficient", "deplet", "balance", "credit"]):
            return False
        return True
    return False

def classify_event(data, project, lang, include_task_desc):
    """
    Conservative, evidence-based event classification according to Antigravity's
    Stop schema:
    1. INVALID_PAYLOAD
    2. QUOTA_EXHAUSTED
    3. EXECUTION_ERROR
    4. WAITING_FOR_USER
    5. TURN_FINISHED
    6. Fallback: UNKNOWN

    Branding & Formatting (TeaBreak | اشرب شاي ☕):
    - Title: "اشرب شاي ☕" (ar) / "TeaBreak ☕" (en)
    - Message:
        [<project>] المهمة: <safe_snippet>
        النتيجة: <result>
    """
    title = "TeaBreak ☕" if lang == "en" else "اشرب شاي ☕"

    safe_snippet = ""
    if include_task_desc:
        safe_snippet = extract_safe_task_snippet(data)

    if lang == "en":
        msg_header = f"[{project}] Task: {safe_snippet}\n" if safe_snippet else f"[{project}]\n"
    else:
        msg_header = f"[{project}] المهمة: {safe_snippet}\n" if safe_snippet else f"[{project}]\n"

    # 1. Invalid payload
    if not isinstance(data, dict) or not data:
        msg = f"[{project}]\n" + ("Result: Unreadable payload" if lang == "en" else "النتيجة: تعذر قراءة بيانات الحدث")
        return {
            "status": "INVALID_PAYLOAD",
            "title": title,
            "message": msg,
            "tags": ["warning", "question"],
            "priority": 3
        }

    raw_err = data.get("error") or data.get("errorMessage") or data.get("errorDetails")
    err_str = str(raw_err).strip() if raw_err is not None else ""

    raw_term = data.get("terminationReason")
    term_reason = str(raw_term).strip().lower() if raw_term is not None else ""

    fully_idle = data.get("fullyIdle")
    is_strictly_fully_idle = (type(fully_idle) is bool and fully_idle is True)

    # 2. Quota Exhaustion vs Execution Error
    if err_str or term_reason == "error":
        if is_quota_exhausted(err_str):
            res_str = "Result: Quota limit reached ⏳" if lang == "en" else "النتيجة: نفدت الكوتة ⏳"
            return {
                "status": "QUOTA_EXHAUSTED",
                "title": title,
                "message": msg_header + res_str,
                "tags": ["hourglass", "warning"],
                "priority": 4
            }
        else:
            res_str = "Result: Execution failed ⚠️" if lang == "en" else "النتيجة: فشل التنفيذ ⚠️"
            return {
                "status": "EXECUTION_ERROR",
                "title": title,
                "message": msg_header + res_str,
                "tags": ["warning", "x"],
                "priority": 4
            }

    if term_reason == "max_steps_exceeded":
        res_str = "Result: Execution failed ⚠️" if lang == "en" else "النتيجة: فشل التنفيذ ⚠️"
        return {
            "status": "EXECUTION_ERROR",
            "title": title,
            "message": msg_header + res_str,
            "tags": ["hourglass", "warning"],
            "priority": 4
        }

    # 3. Waiting for User (Structural signals)
    model_turn = get_last_model_turn(data)
    if check_waiting_for_user(data, model_turn):
        res_str = "Result: Waiting for input ❓" if lang == "en" else "النتيجة: مستني ردك ❓"
        return {
            "status": "WAITING_FOR_USER",
            "title": title,
            "message": msg_header + res_str,
            "tags": ["question", "speaking_head"],
            "priority": 4
        }

    # 4. Confirmed Turn Finished: model_stop or no_tool_call with strict boolean fullyIdle == True
    if term_reason in ("model_stop", "no_tool_call") and is_strictly_fully_idle:
        res_str = "Result: Execution completed ✅" if lang == "en" else "النتيجة: اكتمل التنفيذ ✅"
        return {
            "status": "TURN_FINISHED",
            "title": title,
            "message": msg_header + res_str,
            "tags": ["white_check_mark", "bell"],
            "priority": 3
        }

    # 5. Fallback: UNKNOWN (e.g. fullyIdle is False, missing, or unrecognized reason)
    res_str = "Result: Turn stopped (unknown reason)" if lang == "en" else "النتيجة: تعذر تحديد سبب التوقف"
    return {
        "status": "UNKNOWN",
        "title": title,
        "message": msg_header + res_str,
        "tags": ["stop_button", "warning"],
        "priority": 3
    }

# --------------------------------------------------------
# 6. Reliable Dispatch with Retries & Status Verification
# --------------------------------------------------------
def send_notification(server_url, topic, title, message, priority=4, tags=None, max_retries=1, retry_delay=1.0, http_timeout=4.0):
    """
    Sends notification via ntfy HTTP API with bounded retries and status check.
    Preserves actual HTTP status code and avoids retrying permanent 4xx client errors.
    Returns: dict(success=bool, http_status=int, error=str, server_delivered=bool)
    """
    if not isinstance(topic, str) or not topic.strip():
        return {"success": False, "http_status": 0, "error": "No topic configured", "server_delivered": False}

    if not tags:
        tags = ["bell"]

    payload = {
        "topic": topic.strip(),
        "title": title,
        "message": message,
        "priority": priority,
        "tags": tags
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    clean_server = server_url.rstrip("/")
    url = f"{clean_server}/"

    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

    last_error = ""
    last_status = 0

    for attempt in range(max_retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=http_timeout) as resp:
                status = resp.getcode()
                if 200 <= status < 300:
                    return {"success": True, "http_status": status, "error": None, "server_delivered": True}
                last_status = status
                last_error = f"HTTP {status}"
        except urllib.error.HTTPError as e:
            last_status = e.code
            last_error = f"HTTPError {e.code}: {e.reason}"
            if 400 <= e.code < 500:
                break
        except urllib.error.URLError as e:
            last_status = 0
            last_error = f"URLError: {e.reason}"
        except Exception as e:
            last_status = 0
            last_error = f"Exception: {str(e)}"

        if attempt < max_retries:
            time.sleep(retry_delay * (attempt + 1))

    return {"success": False, "http_status": last_status, "error": last_error, "server_delivered": False}

def run_test_mode(workspace_dir, explicit_topic=None):
    config = load_config(workspace_dir)
    topic = explicit_topic or config.get("topic")
    lang = config.get("language", "ar")
    server = config.get("server_url", "https://ntfy.sh")

    project = os.path.basename(os.path.normpath(workspace_dir))
    print(f"\n--- TeaBreak v{VERSION} Diagnostic Mode ---")
    print(f"• Workspace Directory: {workspace_dir}")
    print(f"• Project Name: {project}")
    print(f"• Active Language: {lang}")
    print(f"• Notification Transport: {server}")
    print(f"• Target Topic: {redact_topic(topic)}")
    print(f"• Max Retries: {config['max_retries']} (Backoff: {config['retry_delay']}s)")
    print(f"• HTTP Timeout: {config['http_timeout']}s")
    print(f"• Configured Network Budget: {calculate_max_network_budget(config)}s (Hook Timeout: {DEFAULT_HOOK_TIMEOUT}s)")

    if not topic:
        print("\n[ERROR] No topic configured! Run with --install or provide --topic <name>")
        return 1

    title = "TeaBreak ☕" if lang == "en" else "اشرب شاي ☕"
    msg = (
        f"[{project}]\n"
        f"Test: Notification system operational 🚀\n"
        f"By #MOASHO11𓂀"
    ) if lang == "en" else (
        f"[{project}]\n"
        f"اختبار: نظام الإشعارات جاهز ونشط 🚀\n"
        f"تطوير: #MOASHO11𓂀"
    )

    print("• Sending test payload...")
    start_t = time.time()
    res = send_notification(
        server,
        topic,
        title,
        msg,
        priority=4,
        tags=["white_check_mark", "bell"],
        max_retries=config["max_retries"],
        retry_delay=config["retry_delay"],
        http_timeout=config["http_timeout"]
    )
    elapsed = round(time.time() - start_t, 2)

    if res["success"]:
        print(f"✅ Success! Notification accepted by server in {elapsed}s (HTTP {res['http_status']}).")
        print("\n📢 IMPORTANT NOTICE:")
        print("HTTP 200 confirms the ntfy server accepted the message.")
        print("Please verify your phone directly to confirm device-level push arrival.")
        return 0
    else:
        print(f"❌ Failed to deliver notification (Elapsed: {elapsed}s, HTTP {res['http_status']}).")
        print(f"Reason: {res['error']}")
        return 1

def print_usage():
    print(f"TeaBreak v{VERSION} — Native Antigravity Stop Hook")
    print("Usage:")
    print("  python notify_on_stop.py                     (Execute as Antigravity Stop Hook via stdin)")
    print("  python notify_on_stop.py --test [--topic <name>]")
    print("  python notify_on_stop.py --status")
    print("  python notify_on_stop.py --install [--topic <name>] [--lang <ar|en>] [--include-task]")
    print("  python notify_on_stop.py --install-global [--topic <name>] [--lang <ar|en>] [--include-task]")
    print("  python notify_on_stop.py --uninstall")
    print("  python notify_on_stop.py --uninstall-global")

# --------------------------------------------------------
# 7. Main Hook Handler
# --------------------------------------------------------
def main():
    workspace_dir = os.getcwd()

    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "--test":
            explicit_topic = None
            if len(sys.argv) > 2:
                for i, a in enumerate(sys.argv):
                    if a == "--topic" and i + 1 < len(sys.argv):
                        explicit_topic = sys.argv[i + 1]
            sys.exit(run_test_mode(workspace_dir, explicit_topic))
        elif arg == "--uninstall":
            ok, msg = uninstall_hook_safely(workspace_dir)
            print(f"[{'OK' if ok else 'ERROR'}] {msg}")
            sys.exit(0 if ok else 1)
        elif arg == "--uninstall-global":
            ok, msg = uninstall_global_plugin_safely()
            print(f"[{'OK' if ok else 'ERROR'}] {msg}")
            sys.exit(0 if ok else 1)
        elif arg in ["--install-global", "--setup-global"]:
            topic = None
            lang = "ar"
            include_desc = False
            for i, a in enumerate(sys.argv):
                if a == "--topic" and i + 1 < len(sys.argv):
                    topic = sys.argv[i + 1]
                elif a == "--lang" and i + 1 < len(sys.argv):
                    lang = sys.argv[i + 1]
                elif a == "--include-task":
                    include_desc = True

            if not topic:
                topic = generate_secure_topic()
                print(f"[TeaBreak] Generated secure 128-bit random topic: {redact_topic(topic)}")

            ok, msg = install_global_plugin_safely(
                python_cmd=sys.executable,
                topic=topic,
                lang=lang,
                include_desc=include_desc
            )
            if not ok:
                print(f"[ERROR] Global plugin installation failed: {msg}")
                sys.exit(1)

            print(f"[OK] {msg}")
            sys.exit(0)
        elif arg in ["--install", "--setup"]:
            topic = None
            lang = "ar"
            include_desc = False
            for i, a in enumerate(sys.argv):
                if a == "--topic" and i + 1 < len(sys.argv):
                    topic = sys.argv[i + 1]
                elif a == "--lang" and i + 1 < len(sys.argv):
                    lang = sys.argv[i + 1]
                elif a == "--include-task":
                    include_desc = True

            if not topic:
                topic = generate_secure_topic()
                print(f"[TeaBreak] Generated secure 128-bit random topic: {redact_topic(topic)}")

            cfg_data = {
                "topic": topic,
                "language": lang,
                "include_task_description": include_desc,
                "max_retries": DEFAULT_MAX_RETRIES,
                "retry_delay": DEFAULT_RETRY_DELAY,
                "http_timeout": DEFAULT_HTTP_TIMEOUT,
                "server_url": "https://ntfy.sh"
            }

            try:
                save_config(workspace_dir, cfg_data)
            except Exception as e:
                print(f"[ERROR] Installation aborted: Git protection failed ({e}). Topic was not saved.")
                sys.exit(1)

            ok, msg = install_hook_safely(workspace_dir)
            if not ok:
                print(f"[ERROR] Config saved but hook registration failed: {msg}")
                sys.exit(1)

            print(f"[OK] Config saved with fail-closed Git protection and {msg}")
            sys.exit(0)
        elif arg == "--status":
            cfg = load_config(workspace_dir)
            ws_hooks_p = get_hooks_path(workspace_dir)
            global_hooks_p = get_global_hooks_path()
            print(f"TeaBreak v{VERSION}")
            print(f"Topic Configured: {bool(cfg.get('topic'))}")
            print(f"Topic Preview: {redact_topic(cfg.get('topic'))}")
            print(f"Language: {cfg.get('language')}")
            print(f"Include Task Desc: {cfg.get('include_task_description')}")
            print(f"Max Retries: {cfg.get('max_retries')}")
            print(f"HTTP Timeout: {cfg.get('http_timeout')}s")
            print(f"Configured Network Budget: {calculate_max_network_budget(cfg)}s (Hook timeout: {DEFAULT_HOOK_TIMEOUT}s)")
            print(f"Workspace Hooks file exists: {os.path.exists(ws_hooks_p)}")
            print(f"Global Plugin Hooks file exists: {os.path.exists(global_hooks_p)}")
            sys.exit(0)
        elif arg in ["--help", "-h"]:
            print_usage()
            sys.exit(0)
        else:
            sys.stderr.write(f"[TeaBreak] Error: Unrecognized command line option '{sys.argv[1]}'\n\n")
            print_usage()
            sys.exit(2)

    # Standard Hook Execution via Stdin Pipe
    raw = read_stdin_cross_platform(0.8)
    data = {}
    if raw.strip():
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                data = parsed
            else:
                sys.stderr.write(f"[TeaBreak] Warning: Incoming payload root is not an object (type: {type(parsed).__name__})\n")
        except Exception as e:
            sys.stderr.write(f"[TeaBreak] Warning: Failed to parse incoming stdin JSON: {e}\n")

    workspaces = data.get("workspacePaths")
    if isinstance(workspaces, list) and workspaces:
        first_ws = workspaces[0]
        if isinstance(first_ws, str) and first_ws.strip():
            expanded_ws = os.path.expanduser(first_ws.strip())
            if os.path.exists(expanded_ws):
                workspace_dir = expanded_ws

    config = load_config(workspace_dir)
    topic = config.get("topic")
    lang = config.get("language", "ar")
    include_task_desc = config.get("include_task_description", False)
    server_url = config.get("server_url", "https://ntfy.sh")
    max_retries = config["max_retries"]
    retry_delay = config["retry_delay"]
    http_timeout = config["http_timeout"]

    project = os.path.basename(os.path.normpath(workspace_dir))
    event = classify_event(data, project, lang, include_task_desc)

    if topic:
        res = send_notification(
            server_url=server_url,
            topic=topic,
            title=event["title"],
            message=event["message"],
            priority=event["priority"],
            tags=event["tags"],
            max_retries=max_retries,
            retry_delay=retry_delay,
            http_timeout=http_timeout
        )
        if not res["success"] and res["error"]:
            sys.stderr.write(f"[TeaBreak] Alert dispatch failed: {res['error']}\n")

    # Output allow decision to Antigravity
    print(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
```

---

## 🔒 Security, Privacy & Integrity Guarantees

1. **Zero External Dependencies:** Built with 100% Python standard library modules (`urllib.request`, `json`, `os`, `sys`, `secrets`). No `pip install` required.
2. **Fail-Closed Privacy:** Private topic tokens are protected by multi-layer `.gitignore` verification, preventing accidental commits to public repositories.
3. **Zero OS Control:** Strict sandbox compliance. The script performs only event classification and push notification delivery. No process manipulation, shutdown commands, or system modifications.
4. **Resilient Stdin Reader:** Designed to handle Windows named pipes, delayed EOF, empty buffers, and malformed JSON payloads without blocking or crashing Antigravity.
5. **Deduplication Engine:** Automatically strips duplicate entries across legacy and current hook configurations, guaranteeing exactly ONE alert per stop event.

---
**Crafted with care by #MOASHO11𓂀**  
*خلّي مساعدك يشتغل، واشرب شايك ☕*

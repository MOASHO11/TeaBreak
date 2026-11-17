# TeaBreak ☕ (v2.1.0) | اشرب شاي
> **Let your AI work while you sip your tea ☕**  
> *[خلّي مساعدك يشتغل، واشرب شايك ☕](README.ar.md)*

[![Language: English](https://img.shields.io/badge/Language-English-blue.svg)](#)
[![Language: Arabic](https://img.shields.io/badge/Language-العربية-green.svg)](README.ar.md)
[![License: Open Source](https://img.shields.io/badge/License-Open%20Source-orange.svg)](#)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](#)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-0%20(Pure%20Stdlib)-blueviolet.svg)](#)

**Author:** [#MOASHO11𓂀](https://www.linkedin.com/in/moasho11/)  
**Official Repository:** [https://github.com/moasho11/TeaBreak](https://github.com/moasho11/TeaBreak)  
**Release Tag:** `v2.1.0`  
**Push Transport:** [ntfy.sh](https://ntfy.sh) (Free, open-source HTTP pub-sub push notification service)

---

## 🌐 Language Navigation / لغة الدليل
- **English (Default)** — You are here.
- **[العربية (Arabic Edition)](README.ar.md)** — انقر هنا للانتقال إلى النسخة العربية الكاملة.

---

## 📖 Table of Contents
1. [Overview & Philosophy](#overview--philosophy)
2. [Why TeaBreak?](#why-teabreak)
3. [Core Architectural Features](#core-architectural-features)
4. [Dual Installation Scopes](#dual-installation-scopes)
5. [Installation Methods](#installation-methods)
   - [Method 1: Interactive Master Wizard (Recommended)](#method-1-interactive-master-wizard-recommended)
   - [Method 2: Command-Line Interface (Manual CLI)](#method-2-command-line-interface-manual-cli)
6. [Event Classification Matrix (The 4 Canonical States)](#event-classification-matrix-the-4-canonical-states)
7. [Security, Privacy & Git Protection](#security-privacy--git-protection)
8. [Status & Testing](#status--testing)
9. [Clean Uninstallation](#clean-uninstallation)
10. [Author & Contact](#author--contact)

---

## Overview & Philosophy

**TeaBreak | اشرب شاي ☕** is a privacy-first, zero-dependency push notification bridge engineered specifically for **Google Antigravity**.

When working with long-running agent workflows—such as large refactorings, test suites, multi-step builds, or complex debugging—developers face two frustrating scenarios:
1. **Screen Babysitting:** Staying pinned to the workstation just to see when the agent completes its turn or halts.
2. **Context Switching Lag:** Stepping away from the desk, only to return minutes later to discover the agent stopped early asking for a clarification question or exhausted its quota.

**TeaBreak solves this elegantly:**  
It hooks natively into Antigravity's Stop events, rigorously classifies the outcome across 4 canonical operational states, and delivers an instant, lightweight push alert directly to your phone via [ntfy.sh](https://ntfy.sh).

---

## Why TeaBreak?

- **100% Pure Python Standard Library:** No `pip install`, no wheels, no external dependencies (`urllib.request`, `json`, `ctypes`, `subprocess`, `os`, `sys`, `secrets`).
- **No Background Daemons or Polling:** Zero CPU overhead. Runs strictly on-demand as a native Antigravity Stop Hook.
- **No Heavy Messaging Bots or Accounts:** No Telegram bots, Discord webhooks, Firebase credentials, or cloud subscriptions required.
- **Strict Privacy-by-Default:** Does NOT transmit prompt content, code snippets, or file paths. Sends only workspace name and execution status.
- **Fail-Closed Git Protection:** Verifies that your private topic configuration is ignored by `.gitignore` before saving, preventing accidental credential leaks.
- **Deduplication Engine:** Cleans up duplicate hook registrations across projects, ensuring exactly ONE notification per event.
- **Windows Named Pipe Resiliency:** Handles delayed EOF, empty buffers, and malformed payloads gracefully without blocking or hanging.
- **Zero OS Control Boundary:** Does not interact with OS processes, system shutdown, registry, or credentials.

---

## Dual Installation Scopes

TeaBreak v2.1.0 gives you complete architectural flexibility:

| Feature | Workspace Hook (Local) | Global Plugin (Central) |
|---|---|---|
| **Location** | `./.agents/scripts/notify_on_stop.py` | `~/.gemini/config/plugins/mobile-alerts/` |
| **Scope** | Active workspace / repository only | All Antigravity workspaces automatically |
| **Configuration** | Local `./.agents/teabreak.config.json` | Central plugin config (with local override support) |
| **Best For** | Specific repositories needing isolation | Effortless notifications across all projects |

---

## Installation Methods

### Method 1: Interactive Master Wizard (Recommended)

The easiest way to install and configure TeaBreak:
1. Open your workspace in Google Antigravity.
2. Copy the entire contents of [`MASTER_WIZARD.md`](MASTER_WIZARD.md) and paste it into the agent chat.
3. The wizard will interactively guide you through:
   - Language selection (Arabic `اشرب شاي ☕` / English `TeaBreak ☕`).
   - Official GitHub code verification (`v2.1.0`).
   - Scope selection (Workspace Hook vs. Global Plugin).
   - Instant 128-bit unguessable random topic generation.
   - Privacy configuration (with or without task snippet).
   - Safe status verification and optional test notification.

---

### Method 2: Command-Line Interface (Manual CLI)

#### Prerequisites:
1. Python 3.8+ installed.
2. Install the free **ntfy** mobile app ([Android](https://play.google.com/store/apps/details?id=io.heckel.ntfy) / [iOS](https://apps.apple.com/app/ntfy/id1625396347)) or open [https://ntfy.sh](https://ntfy.sh) in your browser.

#### Install in Current Workspace:
```bash
python notify_on_stop.py --install --lang en
```
Or specify a custom topic and enable task snippets:
```bash
python notify_on_stop.py --install --topic my_secret_topic_123 --lang en --include-task
```

#### Install Centrally as Global Plugin:
```bash
python notify_on_stop.py --install-global --lang en
```

---

## Event Classification Matrix (The 4 Canonical States)

TeaBreak classifies Antigravity Stop events with mathematical and technical rigor into 4 primary canonical states and 2 fallbacks:

| Status Code | English Title | English Message | Arabic Title | Arabic Message | Priority |
|---|---|---|---|---|:---:|
| `QUOTA_EXHAUSTED` | `TeaBreak ☕` | `[Project]
Result: Quota limit reached ⏳` | `اشرب شاي ☕` | `[المشروع]
النتيجة: نفدت الكوتة ⏳` | 4 (High) |
| `EXECUTION_ERROR` | `TeaBreak ☕` | `[Project]
Result: Execution failed ⚠️` | `اشرب شاي ☕` | `[المشروع]
النتيجة: فشل التنفيذ ⚠️` | 4 (High) |
| `WAITING_FOR_USER` | `TeaBreak ☕` | `[Project]
Result: Waiting for input ❓` | `اشرب شاي ☕` | `[المشروع]
النتيجة: مستني ردك ❓` | 4 (High) |
| `TURN_FINISHED` | `TeaBreak ☕` | `[Project]
Result: Execution completed ✅` | `اشرب شاي ☕` | `[المشروع]
النتيجة: اكتمل التنفيذ ✅` | 3 (Default) |
| `UNKNOWN` *(Fallback)* | `TeaBreak ☕` | `[Project]
Result: Turn stopped (unknown reason)` | `اشرب شاي ☕` | `[المشروع]
النتيجة: تعذر تحديد سبب التوقف` | 3 |
| `INVALID_PAYLOAD` *(Fallback)* | `TeaBreak ☕` | `[Project]
Result: Unreadable payload` | `اشرب شاي ☕` | `[المشروع]
النتيجة: تعذر قراءة بيانات الحدث` | 3 |

*Note: When task preview is enabled (`--include-task`), a sanitized 80-character snippet of the task prompt is prepended:*  
`[Project] Task: <sanitized task snippet>
Result: <result>`

---

## Security, Privacy & Git Protection

1. **Fail-Closed Git Verification:**  
   Before storing any topic name in `teabreak.config.json`, the installer checks `.gitignore` rules (including negation patterns) and ensures the file is not tracked in the Git index. If Git ignore verification fails, setup halts immediately to prevent credential leaks.
2. **Privacy-by-Default:**  
   Prompt text, conversational transcripts, and private filenames are never transmitted unless task snippets are explicitly enabled.
3. **Zero Telemetry:**  
   TeaBreak contains zero analytics, tracking beacons, or third-party servers. Push dispatches travel via direct TLS HTTPS to `ntfy.sh` (or your self-hosted ntfy instance).

---

## Status & Testing

### View Active Configuration:
```bash
python notify_on_stop.py --status
```
Outputs active language, partially redacted topic, network budget, and hook registration status without dispatching any network requests.

### Dispatch Live Test Notification:
```bash
python notify_on_stop.py --test
```
Dispatches a single test notification to confirm end-to-end delivery to your mobile phone.

---

## Clean Uninstallation

### Remove Workspace Hook:
```bash
python notify_on_stop.py --uninstall
```

### Remove Global Plugin:
```bash
python notify_on_stop.py --uninstall-global
```

*TeaBreak cleanly removes only its own hook entries and preserves all unrelated user hooks, falsey metadata, and custom configurations.*

---

<div align="center">

### TeaBreak ☕
**Let your AI work while you sip your tea ☕**  
*خلّي مساعدك يشتغل، واشرب شايك ☕*

<br/>

**Crafted with care by #MOASHO11𓂀**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-moasho11-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/moasho11/)
[![GitHub](https://img.shields.io/badge/GitHub-TeaBreak-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/moasho11/TeaBreak)

</div>

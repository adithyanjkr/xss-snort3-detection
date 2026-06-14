# 🎯 XSS Detection via Snort 3 IDS

A minimal proof-of-concept lab demonstrating real-time detection of Cross-Site Scripting (XSS) web-layer attacks using custom signatures inside the **Snort 3** Intrusion Detection System.

---

## 📌 Architecture Setup

**Offensive Component:**  A local Python Flask application (`app.py`) running over port `8080`. It mimics a community feedback board and is intentionally left vulnerable to Reflected XSS by processing user payloads using Jinja2's unsanitized `| safe` evaluation filter.

**Defensive Component:**  A **Snort 3** IDS instance actively sniffing the local loopback adapter interface (`lo`), matching raw HTTP string packet sequences against custom-tailored signature templates.

---

## 💥 Quick Simulation

1. Fire up the target server (`python3 app.py`) and initialize the Snort monitoring engine:

   sudo snort -c /etc/snort/snort.lua -i lo -k none -A alert_fast

2. Navigate to http://127.0.0.1:8080 via browser and submit the injection vector:

   <script>alert('JKR')</script>

3. The malicious script reflects directly onto the application viewport, triggering a browser client-side execution popup window.

## 🚨 Captured IDS Alerts

Snort instantaneously matches the request payload buffers on the loopback stream and logs the following live security flags straight to stdout:

06/04-15:04:09.255324 [**] [1:999999:1] "XSS-RAW: Generic Script Keyword Detected" [**] [Priority: 0] [TCP] 192.168.1.4:48564 -> 192.168.1.4:8080
06/04-15:04:09.255324 [**] [1:1000006:1] "XSS-HTTP: Script Tag Injected into POST Body" [**] [Priority: 0] [TCP] 192.168.1.4:48564 -> 192.168.1.4:8080

## 🛠️ How to Fix It

1. Secure Coding: Remove the explicit | safe engine modifiers to fallback on Flask's automatic context-aware HTML entity-escaping rules (&lt; and &gt;).

2. Network inline Blocking: Migrate your local Snort tracking orchestration parameters from standard passive alert flags to active drop rule configurations to mitigate incoming exploits at the network adapter block.

## 👤 Author - Adithyan.V

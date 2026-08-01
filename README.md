# DorkRecon

DorkRecon is a lightweight domain reconnaissance tool that automates the generation of targeted Google Dork queries. It identifies indexed, exposed assets—such as configuration files, database backups, and administrative portals—to evaluate an organization's external attack surface.

## ⚖️ Legal & Authorized Use Disclaimer
This tool is strictly intended for authorized penetration testing, red team engagements, and defensive auditing. Users are entirely responsible for ensuring explicit, written authorization before analyzing target domains. Unauthorized scanning or utilization of data may violate computer fraud laws (e.g., CFAA). The developers assume no liability for misuse.

## 🚀 Features
* **Zero Dependencies:** Built entirely on the Python 3 standard library for clean, sandboxed execution.
* **10 Reconnaissance Classifications:** Targets config files, SQL backups, log directories, API leaks, and subdomains.
* **Automated Triage:** Optional browser integration (`--open`) with configurable transaction pacing to prevent rate limits.

## 📦 Installation & Deployment

### System Requirements
* Python 3.8 or higher
* Standard terminal environment

### Linux / macOS
```bash
git clone https://github.com/v4l-obscuraproject/DorkRecon
cd DorkRecon
python3 dork_gen.py example.com
```

### Windows (Command Prompt / PowerShell)
```cmd
git clone https://github.com/v4l-obscuraproject/DorkRecon
cd DorkRecon
python dork_gen.py example.com
```

---

## 🛠️ Detailed Usage & Syntax

### Basic Domain Query Generation
```bash
python3 dork_gen.py example.com
```

### Automated Browser Triage
To launch generated queries dynamically inside default browser tabs:
```bash
python3 dork_gen.py example.com --open
```

### Congestion Control / Pacing
To modify target delays (seconds) and mitigate search engine rate-limiting thresholds:
```bash
python3 dork_gen.py example.com --open --delay 3
```

---

## 🛡️ Execution & Security Policies
Because this script interacts directly with native web browsers to surface open-source intelligence, local operating system endpoint controls may require administrative confirmation during initial setup:
* **macOS Gatekeeper:** If blocked as an unidentified developer script, authorize execution via `System Settings → Privacy & Security → Open Anyway`.
* **Windows SmartScreen:** If flagged due to an unestablished file reputation, proceed via `More info → Run anyway`.

## 🗺️ Future Roadmap (Engineering Backlog)
* Implement modular backend search engine parsers (e.g., DuckDuckGo HTML, Bing API).
* Integrate dynamic proxy rotation modules (`HTTP/SOCKS5`) for scalable execution.
* Add automated JSON/CSV serialization for seamless pipeline integration with tools like Nmap.

## 📄 License & Credits
* **License:** MIT License
* **Development:** 5h9q_
* **Publishing:** rosp_1


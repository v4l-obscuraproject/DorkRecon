DorkRecon

DorkRecon is a domain reconnaissance tool that generates Google dork queries — advanced search operators (site:, filetype:, inurl:, intitle:) that find content Google has indexed but that probably shouldn't be publicly exposed. It's written in Python 3 and MIT-licensed.

Scroll down for installation commands and usage.

Installation and Running

DorkRecon requires Python 3.8+ and has no external dependencies — it only uses Python's standard library.

macOS / Linux

Open Terminal, then run:

bash
git clone https://github.com/v4l-obscuraproject/DorkRecon (only use this if you didnt download the zip file through github.)
cd DorkRecon
python3 dork_gen.py example.com
Windows
Open Command Prompt or PowerShell, then run:

git clone https://github.com/v4l-obscuraproject/DorkRecon (only use this if you didnt download the zip file through github.)
cd DorkRecon
python dork_gen.py example.com

(On Windows, the command is usually just python instead of python3 — if python doesn't work, try python3 or py instead, depending on how Python was installed.)

macOS security warning

macOS may show an "unsafe" / "can't be opened because it is from an unidentified developer" warning when running downloaded scripts for the first time. This is standard Gatekeeper behavior for any file downloaded from the internet, not a sign of an actual problem with this specific file — it's a short, fully readable Python script with no obfuscation and no external calls beyond opening your browser. If you've reviewed the code and trust it, allow it via:

System Settings → Privacy & Security → scroll down → "Open Anyway"

Windows security warning

Windows Defender SmartScreen may show a "Windows protected your PC" / "unrecognized app" warning when running make.bat or downloaded scripts for the first time. This is standard SmartScreen behavior for files downloaded from the internet without an established reputation, not a sign of an actual problem with this specific file. If you've reviewed the code and trust it, proceed via:

Click "More info" → "Run anyway"

General usage
bash
# Print dork queries for a domain
python3 dork_gen.py example.com

# Also open each query automatically in your browser
python3 dork_gen.py example.com --open

# Control delay (seconds) between opening browser tabs (default: 2.0)
python3 dork_gen.py example.com --open --delay 3
Features
Simple command-line interface, no setup required
Written in pure Python 3 — no external dependencies
Generates 10 categories of recon dork queries per domain
Optional --open flag to launch each query directly in your browser
Adjustable delay between browser tabs
What DorkRecon is used for

Given a target domain, DorkRecon produces 10 categories of recon queries:

Exposed config files (.env, .ini, .cfg)
Exposed SQL/database files
Indexed login/admin pages
Open directory listings
Exposed backup files (.bak, .old)
Exposed log files
Publicly indexed documents (PDFs, Word docs, spreadsheets)
Error messages/stack traces that leak internals
Exposed API keys/secrets mentioned in text
Subdomains Google has indexed

Intended use case: the reconnaissance phase of an authorized penetration test or red team engagement — checking what an organization's own domain has accidentally exposed to Google's index, so it can be fixed before an actual attacker finds it. Same category of tool as recon-focused parts of Recon-ng or theHarvester.

Not intended for: looking up people (no email/username/personal lookup functionality). Only meant to run against domains you own or have written authorization to test.

Disclaimer

The technique this tool uses (searching Google with advanced operators) is not itself illegal — it's the same as typing a search into Google manually. However, running reconnaissance against a domain you don't own or don't have explicit written authorization to test can violate computer fraud laws depending on jurisdiction and what's done with the results.

The developers of DorkRecon are not responsible for misuse of this tool. Users are solely responsible for ensuring they have proper authorization before running this tool against any domain, and for how they use any information it surfaces. See OBSCURA_Terms_of_Service.md for full terms.

License

MIT License — see LICENSE for details.

Credits

Made by 5h9q_ (developer) and rosp_1 (publishing).

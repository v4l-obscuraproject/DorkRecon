# DorkRecon

**DorkRecon** is a domain reconnaissance tool that generates Google dork
queries — advanced search operators (`site:`, `filetype:`, `inurl:`,
`intitle:`) that find content Google has indexed but that probably
shouldn't be publicly exposed. It's written in **Python 3** and
**MIT-licensed**.

## Features

- Simple command-line interface, no setup required
- Written in pure Python 3 — no external dependencies
- Generates 10 categories of recon dork queries per domain
- Optional `--open` flag to launch each query directly in your browser
- Adjustable delay between browser tabs

## Uses

DorkRecon generates Google dork queries to find content that's been
indexed by Google but probably shouldn't be publicly exposed. Given a
target domain, it produces 10 categories of recon queries:

- Exposed config files (`.env`, `.ini`, `.cfg`)
- Exposed SQL/database files
- Indexed login/admin pages
- Open directory listings
- Exposed backup files (`.bak`, `.old`)
- Exposed log files
- Publicly indexed documents (PDFs, Word docs, spreadsheets)
- Error messages/stack traces that leak internals
- Exposed API keys/secrets mentioned in text
- Subdomains Google has indexed

**Intended use case:** the reconnaissance phase of an authorized
penetration test or red team engagement — checking what an organization's
own domain has accidentally exposed to Google's index, so it can be fixed
before an actual attacker finds it. Same category of tool as recon-focused
parts of Recon-ng or theHarvester.

**Not intended for:** looking up people (no email/username/personal
lookup functionality). Only meant to run against domains you own or have
written authorization to test.

## Installation and Running

DorkRecon requires Python 3.8+ and has no external dependencies — it only
uses Python's standard library.

```bash
git clone <repo-url>
cd DorkRecon
python3 dork_gen.py example.com
```

## License

MIT License — see [LICENSE](LICENSE) for details.

## Credits

Made by **5h9q_** (developer) and **rosp_1** (publishing).
See [CREDITS.md](CREDITS.md).

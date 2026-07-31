"""
DorkRecon
Domain Recon Dork Generator

Created by: 5h9q_ (developer) and rosp_1 (publishing) on discord.
Licensed under the MIT License (see LICENSE file)

Generates Google dork queries to find exposed files, misconfigurations,
and indexed content for a specific domain -- a standard part of the
reconnaissance phase in authorized penetration testing / red team engagements.

IMPORTANT: Only run this against domains you own or have explicit written
authorization to test. Running recon against domains you don't own without
permission can violate computer fraud laws even though the technique itself
(searching Google) is not inherently illegal.

Usage:
    python dork_gen.py example.com
    python dork_gen.py example.com --open   (opens each query in your browser)

Note: Google does not provide a free public API for search results as of 2026
(the Custom Search JSON API free tier is being phased out and closed to new
signups). This tool generates correct dork syntax and opens it in your
default browser for manual review, rather than attempting to scrape Google
directly -- which violates Google's Terms of Service and gets IPs blocked
quickly regardless of intent.
"""

import argparse
import urllib.parse
import webbrowser
import time

BANNER = r"""
  ____  ____   _____  _____ _    _ _____
 / __ \|  _ \ / ____|/ ____| |  | |  __ \     /\
| |  | | |_) | (___ | |    | |  | | |__) |   /  \
| |  | |  _ < \___ \| |    | |  | |  _  /   / /\ \
| |__| | |_) |____) | |____| |__| | | \ \  / ____ \
 \____/|____/|_____/ \_____|\____/|_|  \_\/_/    \_\

 ___          _   ___
|   \ ___ _ _| |_| _ \___ __ ___ _ _
| |) / _ \ '_| / /   / -_) _/ _ \ ' \
|___/\___/_| |_\_\_|_\___\__\___/_||_|

    5h9q_  (developer)        rosp_1  (publishing) |--| these our are socials on discord if you want to contact for support.
"""

DORK_TEMPLATES = [
    ("Exposed config files", 'site:{domain} filetype:env OR filetype:ini OR filetype:cfg'),
    ("Exposed SQL/database files", 'site:{domain} filetype:sql OR filetype:db'),
    ("Login / admin pages indexed", 'site:{domain} inurl:admin OR inurl:login'),
    ("Directory listings", 'site:{domain} intitle:"index of"'),
    ("Exposed backup files", 'site:{domain} filetype:bak OR filetype:old OR filetype:backup'),
    ("Exposed log files", 'site:{domain} filetype:log'),
    ("Publicly indexed documents", 'site:{domain} filetype:pdf OR filetype:docx OR filetype:xlsx'),
    ("Error messages / stack traces", 'site:{domain} "warning" OR "error" OR "exception" intext:sql'),
    ("Exposed API keys / tokens in text", 'site:{domain} "api_key" OR "apikey" OR "secret"'),
    ("Subdomains indexed by Google", 'site:{domain} -www'),
]


def generate_dorks(domain: str):
    return [(label, template.format(domain=domain)) for label, template in DORK_TEMPLATES]


def main():
    parser = argparse.ArgumentParser(
        description="Generate Google dork queries for authorized domain recon"
    )
    parser.add_argument("domain", help="Target domain (must be one you own or are authorized to test)")
    parser.add_argument("--open", action="store_true", help="Open each dork query in your default browser")
    parser.add_argument("--delay", type=float, default=2.0, help="Seconds between opening each browser tab")
    args = parser.parse_args()

    print(BANNER)
    print(f"[*] Generating recon dorks for: {args.domain}")
    print("[!] Only use against domains you own or are authorized to test.\n")

    dorks = generate_dorks(args.domain)

    for label, query in dorks:
        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        print(f"[{label}]")
        print(f"    Query: {query}")
        print(f"    URL:   {url}\n")

        if args.open:
            webbrowser.open(url)
            time.sleep(args.delay)

    print(f"[*] Generated {len(dorks)} dork queries.")
    if not args.open:
        print("[*] Run with --open to automatically open each query in your browser.")


if __name__ == "__main__":
    main()

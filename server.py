#!/usr/bin/env python3
"""
Professional Portfolio Server for Mirza Muhammad Wali Baig
Run: python server.py
Then open: http://localhost:8080
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import json
from datetime import datetime
from urllib.parse import urlparse, parse_qs

# ─── Configuration ────────────────────────────────────────────────
PORT = 8080
HOST = "localhost"
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# ─── Visitor log (in-memory) ─────────────────────────────────────
visitor_log = []

# ─── ANSI colours for terminal ───────────────────────────────────
class C:
    TEAL   = "\033[96m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    RESET  = "\033[0m"


def banner():
    print(f"""
{C.TEAL}{C.BOLD}
╔══════════════════════════════════════════════════════════╗
║       Mirza Wali Baig · Professional Portfolio           ║
║       Compliance & Regulatory Affairs Professional       ║
╚══════════════════════════════════════════════════════════╝{C.RESET}
{C.GREEN}  ✔  Server started  →  http://{HOST}:{PORT}{C.RESET}
{C.DIM}  Press Ctrl+C to stop{C.RESET}
""")


class PortfolioHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler with logging and API endpoints."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, fmt, *args):
        """Override default log to add colour and timestamps."""
        now = datetime.now().strftime("%H:%M:%S")
        status = str(args[1]) if len(args) > 1 else "?"
        colour = C.GREEN if status.startswith("2") else (C.YELLOW if status.startswith("3") else C.RED)
        path = str(args[0]).split(" ")[1] if " " in str(args[0]) else args[0]
        print(f"  {C.DIM}[{now}]{C.RESET}  {colour}{status}{C.RESET}  {path}")

        # Track visitors
        visitor_log.append({
            "time": now,
            "path": path,
            "status": status,
            "ip": self.client_address[0],
        })

    def do_GET(self):
        parsed = urlparse(self.path)

        # ─── API: visitor stats ──────────────────────────────────
        if parsed.path == "/api/stats":
            data = {
                "total_requests": len(visitor_log),
                "unique_ips": len({v["ip"] for v in visitor_log}),
                "server_uptime": "active",
                "profile": {
                    "name": "Mirza Muhammad Wali Baig",
                    "title": "Compliance & Regulatory Affairs Professional",
                    "location": "Berlin, Germany",
                    "email": "mm.wali.baig@gmail.com",
                    "linkedin": "https://www.linkedin.com/in/mwalibaig01/",
                    "languages": ["Urdu (Native)", "English (C1)", "German (B2)"],
                    "certifications": [
                        "Lean Six Sigma Green Belt – IMC Institute (2023)",
                        "Biosafety & Safety in Health Institutions – DUHS (2020)",
                    ],
                },
            }
            body = json.dumps(data, indent=2).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)
            return

        # ─── API: health check ───────────────────────────────────
        if parsed.path == "/api/health":
            body = json.dumps({"status": "ok", "server": "Wali Portfolio Server"}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        # ─── Default: serve static files ────────────────────────
        super().do_GET()

    def end_headers(self):
        """Add security and caching headers."""
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Cache-Control", "no-cache, must-revalidate")
        super().end_headers()

    def guess_type(self, path):
        """Ensure correct MIME types."""
        mime, _ = super().guess_type(path)
        if path.endswith(".html"):
            return "text/html; charset=utf-8"
        return mime or "application/octet-stream"


def main():
    os.chdir(DIRECTORY)
    banner()

    with socketserver.TCPServer((HOST, PORT), PortfolioHandler) as httpd:
        httpd.allow_reuse_address = True
        url = f"http://{HOST}:{PORT}"

        # Auto-open browser after short delay
        try:
            print(f"  {C.YELLOW}→  Opening browser…{C.RESET}\n")
            webbrowser.open(url)
        except Exception:
            pass

        print(f"  {C.DIM}API endpoints:{C.RESET}")
        print(f"  {C.DIM}  GET /api/stats   →  profile & visitor stats (JSON){C.RESET}")
        print(f"  {C.DIM}  GET /api/health  →  server health check (JSON){C.RESET}\n")
        print(f"  {C.DIM}{'─' * 54}{C.RESET}")
        print(f"  {C.DIM}  Incoming requests:{C.RESET}\n")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            total = len(visitor_log)
            print(f"\n\n  {C.YELLOW}Server stopped.{C.RESET}")
            print(f"  {C.DIM}Total requests served: {total}{C.RESET}\n")
            sys.exit(0)


if __name__ == "__main__":
    main()

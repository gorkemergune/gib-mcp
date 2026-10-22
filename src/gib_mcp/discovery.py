"""Read-only browser discovery; no invented search selectors or API routes."""
import argparse
import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from playwright.async_api import async_playwright

TARGET = "https://gib.gov.tr/mevzuat/arama?tur=vergi-mevzuati&ktype=99&kanun-turu=ozelge"

async def discover(output: Path, headed: bool = False):
    output.mkdir(parents=True, exist_ok=True)
    responses = []
    failures = []
    script_errors = []
    print("GİB keşfi: tarayıcı başlatılıyor", file=sys.stderr, flush=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not headed)
        try:
            page = await browser.new_page(locale="tr-TR")
            page.set_default_timeout(30000)
            def record(response):
                if response.request.resource_type in {"xhr", "fetch"}:
                    # Deliberately omit headers, cookies and response bodies.
                    responses.append({"url": response.url, "status": response.status,
                                      "method": response.request.method})
            page.on("response", record)
            page.on("requestfailed", lambda req: failures.append({"url": req.url, "error": req.failure}))
            page.on("pageerror", lambda error: script_errors.append(str(error)))
            print("GİB keşfi: sayfa yükleniyor", file=sys.stderr, flush=True)
            response = await page.goto(TARGET, wait_until="domcontentloaded", timeout=45000)
            # Bounded observation window; absence of results is not proof of no records.
            try:
                await page.wait_for_function("document.body && document.body.innerText.trim().length > 50", timeout=20000)
            except Exception as error:
                script_errors.append(f"Content readiness: {type(error).__name__}")
            print("GİB keşfi: çıktılar kaydediliyor", file=sys.stderr, flush=True)
            await page.screenshot(path=str(output / "page.png"), full_page=True)
            (output / "page.html").write_text(await page.content(), encoding="utf-8")
            (output / "page.txt").write_text(await page.locator("body").inner_text(), encoding="utf-8")
            controls = await page.locator("input, select, button").evaluate_all("els => els.map(e => ({tag:e.tagName,type:e.type,name:e.name,id:e.id,placeholder:e.getAttribute('placeholder'),text:e.innerText,ariaLabel:e.getAttribute('aria-label')}))")
            report = {"source_url": TARGET, "final_url": page.url,
                      "fetched_at": datetime.now(timezone.utc).isoformat(),
                      "http_status": response.status if response else None,
                      "responses": responses, "controls": controls,
                      "request_failures": failures, "script_errors": script_errors,
                      "status": "observed" if controls else "incomplete",
                      "note": "Initial page only; search/pagination must be inspected separately."}
            (output / "discovery.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
            return report
        finally:
            await browser.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("artifacts"))
    parser.add_argument("--headed", action="store_true")
    args = parser.parse_args()
    report = asyncio.run(discover(args.output, args.headed))
    print(f"Keşif: {report['status']}; rapor: {args.output / 'discovery.json'}", file=sys.stderr)
    if report["status"] == "incomplete":
        raise SystemExit(2)

if __name__ == "__main__":
    main()

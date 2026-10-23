#!/usr/bin/env python3
"""Build script that triggers the TypeScript PDF generation engine or falls back to typst if needed."""
import os
import sys
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TS_BUILD_SCRIPT = os.path.join(ROOT, "scripts", "build_pdf.ts")
OUTPUT_PDF = os.path.join(ROOT, "DE_CUONG_ON_TAP_KTGK_I_VAT_LI_10_2026.pdf")

def main():
    print("Executing TypeScript build engine via npx tsx scripts/build_pdf.ts...")
    result = subprocess.run(["npx", "tsx", TS_BUILD_SCRIPT], cwd=ROOT)
    if result.returncode == 0:
        size_kb = os.path.getsize(OUTPUT_PDF) / 1024
        print(f"Successfully generated PDF via TypeScript -> {OUTPUT_PDF} ({size_kb:,.1f} KB)")
    else:
        print("TypeScript build engine failed! Falling back to typst...")
        import typst
        INPUT_TYP = os.path.join(ROOT, "src", "main.typ")
        REPO_FONTS = os.path.join(ROOT, "src", "fonts")
        FONT_DIRS = [d for d in (REPO_FONTS, "/tmp/fonts") if os.path.isdir(d)]
        typst.compile(INPUT_TYP, output=OUTPUT_PDF, font_paths=FONT_DIRS)
        size_kb = os.path.getsize(OUTPUT_PDF) / 1024
        print(f"Compiled PDF via Typst -> {OUTPUT_PDF} ({size_kb:,.1f} KB)")

if __name__ == "__main__":
    sys.exit(main())

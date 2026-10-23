#!/usr/bin/env python3
"""Execute TypeScript build pipeline scripts/build_pdf.ts."""
import subprocess
import sys

def main():
    print("Executing TypeScript build pipeline (npx tsx scripts/build_pdf.ts)...")
    res = subprocess.run(["npx", "tsx", "scripts/build_pdf.ts"], check=True)
    return res.returncode

if __name__ == "__main__":
    sys.exit(main())

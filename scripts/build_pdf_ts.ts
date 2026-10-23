import React from "react";
import ReactDOMServer from "react-dom/server";
import puppeteer from "puppeteer";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { AstryxDocument } from "../src/ts/components/AstryxDocument.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, "..");
const OUTPUT_PDF = path.join(ROOT_DIR, "DE_CUONG_ON_TAP_KTGK_I_VAT_LI_10_2026.pdf");

async function generatePDF() {
  console.log("🚀 Rendering React Astryx Document to HTML...");
  const htmlContent = `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Đề Cương Ôn Tập KTGK I Vật Lí 10 (2026-2027)</title>
</head>
<body>
  ${ReactDOMServer.renderToString(React.createElement(AstryxDocument))}
</body>
</html>`;

  console.log("🌐 Launching Puppeteer / Chrome Headless...");
  const browser = await puppeteer.launch({
    executablePath: "/usr/bin/google-chrome",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu"]
  });

  const page = await browser.newPage();
  await page.setContent(htmlContent, { waitUntil: "domcontentloaded" });

  console.log("📄 Exporting PDF to", OUTPUT_PDF);
  await page.pdf({
    path: OUTPUT_PDF,
    format: "A4",
    printBackground: true,
    margin: {
      top: "15mm",
      bottom: "15mm",
      left: "12mm",
      right: "12mm"
    }
  });

  await browser.close();
  const stats = fs.statSync(OUTPUT_PDF);
  console.log(`✅ Successfully compiled PDF -> ${OUTPUT_PDF} (${(stats.size / 1024).toFixed(1)} KB)`);
}

generatePDF().catch((err) => {
  console.error("❌ Error generating PDF:", err);
  process.exit(1);
});

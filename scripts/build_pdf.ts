import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import React from 'react';
import { renderToString } from 'react-dom/server';
import puppeteer from 'puppeteer-core';
import { App } from '../src/ts/App.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');
const OUTPUT_PDF = path.join(ROOT, 'DE_CUONG_ON_TAP_KTGK_I_VAT_LI_10_2026.pdf');

async function main() {
  console.log('Rendering Astryx React App to HTML...');
  const appHtml = renderToString(React.createElement(App));

  const fullHtml = `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Đề Cương Ôn Tập KTGK I Vật Lí 10 (2026-2027)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Fira+Code:wght@500;700&display=swap" rel="stylesheet">
  <style>
    @page {
      size: A4;
      margin: 15mm 12mm 15mm 12mm;
      @bottom-right {
        content: "Trang " counter(page);
        font-family: 'Be Vietnam Pro', sans-serif;
        font-size: 8pt;
        color: #64748B;
      }
      @bottom-left {
        content: "Vật lí 10 — KTGK I (2026-2027) | Astryx Design System";
        font-family: 'Be Vietnam Pro', sans-serif;
        font-size: 8pt;
        color: #64748B;
      }
    }
    body {
      margin: 0;
      padding: 0;
      font-family: 'Be Vietnam Pro', sans-serif;
      color: #0F172A;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    * {
      box-sizing: border-box;
    }
    h1, h2, h3, h4 {
      page-break-after: avoid;
    }
    .astryx-card, .astryx-table-container {
      page-break-inside: avoid;
    }
  </style>
</head>
<body>
  ${appHtml}
</body>
</html>`;

  const htmlPath = path.join(ROOT, 'dist', 'index.html');
  fs.mkdirSync(path.join(ROOT, 'dist'), { recursive: true });
  fs.writeFileSync(htmlPath, fullHtml, 'utf-8');
  console.log(`Saved HTML preview to ${htmlPath}`);

  console.log('Launching headless Chrome to generate PDF...');
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/google-chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--font-render-hinting=none'],
    headless: true,
  });

  const page = await browser.newPage();
  await page.setContent(fullHtml, { waitUntil: 'networkidle0' });

  await page.pdf({
    path: OUTPUT_PDF,
    format: 'A4',
    margin: {
      top: '15mm',
      bottom: '15mm',
      left: '12mm',
      right: '12mm',
    },
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: `<div style="font-size:8px; font-family:'Be Vietnam Pro', sans-serif; color:#64748B; width:100%; padding:0 12mm; display:flex; justify-content:space-between; border-bottom:1px solid #CBD5E1; margin-bottom:4px;">
      <span><strong>ĐỀ CƯƠNG ÔN TẬP KTGK I — VẬT LÍ 10 (2026–2027)</strong></span>
      <span>Bộ GDPT 2018 — Kết nối tri thức</span>
    </div>`,
    footerTemplate: `<div style="font-size:8px; font-family:'Be Vietnam Pro', sans-serif; color:#64748B; width:100%; padding:0 12mm; display:flex; justify-content:space-between; border-top:1px solid #CBD5E1; paddingTop:4px;">
      <span>Biên soạn theo Astryx Design System & TypeScript Engine</span>
      <span>Trang <span class="pageNumber"></span> / <span class="totalPages"></span></span>
    </div>`,
  });

  await browser.close();

  const stats = fs.statSync(OUTPUT_PDF);
  console.log(`✅ Successfully compiled PDF -> ${OUTPUT_PDF} (${(stats.size / 1024).toFixed(1)} KB)`);
}

main().catch((err) => {
  console.error('Build PDF failed:', err);
  process.exit(1);
});

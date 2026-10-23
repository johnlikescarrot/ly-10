import { renderToString } from 'react-dom/server';
import React from 'react';
import { App } from '../dist/App.js';
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

async function main() {
  console.log('Rendering React + Astryx component tree to HTML...');
  const appHtml = renderToString(React.createElement(App));

  const fullHtml = `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Đề Cương Ôn Tập KTGK I - Vật Lí 10 (2026-2027)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    @page {
      size: A4;
      margin: 15mm 15mm 15mm 15mm;
      @bottom-right {
        content: counter(page) " / " counter(pages);
      }
    }
    body {
      font-family: 'Be Vietnam Pro', sans-serif;
      margin: 0;
      padding: 0;
      color: #0F172A;
      background: #FFFFFF;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    .part-container {
      page-break-after: always;
    }
    .part-container:last-child {
      page-break-after: auto;
    }
  </style>
</head>
<body>
  <div id="root">${appHtml}</div>
</body>
</html>`;

  const htmlPath = path.resolve('./dist/rendered_astryx.html');
  fs.writeFileSync(htmlPath, fullHtml, 'utf-8');
  console.log(`Saved rendered HTML to ${htmlPath}`);

  console.log('Launching Playwright Chromium to render PDF...');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });

  const pdfPath = path.resolve('./DE_CUONG_ON_TAP_KTGK_I_VAT_LI_10_2026.pdf');
  await page.pdf({
    path: pdfPath,
    format: 'A4',
    printBackground: true,
    margin: { top: '15mm', bottom: '15mm', left: '15mm', right: '15mm' }
  });

  await browser.close();
  console.log(`Successfully compiled PDF using Playwright + Astryx -> ${pdfPath}`);
}

main().catch(err => {
  console.error('Error generating PDF:', err);
  process.exit(1);
});

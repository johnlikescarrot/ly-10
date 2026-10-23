import fs from 'fs';
import path from 'path';
import puppeteer from 'puppeteer';
import { buildFullHtml } from '../src/ts/generate_html';

async function generatePdf() {
  console.log('Generating HTML content...');
  const htmlContent = buildFullHtml();
  const htmlPath = path.join(__dirname, '../dist_ts_output.html');
  fs.writeFileSync(htmlPath, htmlContent, 'utf8');

  console.log('Launching Headless Chrome via Puppeteer...');
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setContent(htmlContent, { waitUntil: 'networkidle0' });

  const pdfPath = path.join(__dirname, '../DE_CUONG_ON_TAP_KTGK_I_VAT_LI_10_2026.pdf');
  console.log(`Rendering PDF to ${pdfPath}...`);
  await page.pdf({
    path: pdfPath,
    format: 'A4',
    printBackground: true,
    margin: {
      top: '15mm',
      bottom: '15mm',
      left: '12mm',
      right: '12mm'
    }
  });

  await browser.close();
  const stats = fs.statSync(pdfPath);
  console.log(`PDF compiled successfully! Size: ${(stats.size / 1024).toFixed(1)} KB`);
}

generatePdf().catch((err) => {
  console.error('Error compiling PDF:', err);
  process.exit(1);
});

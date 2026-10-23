import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { bankMCQs, bankTFs, bankSAs, bankEssays } from '../src/ts/data/questionBankData.js';
import { theoryLessons } from '../src/ts/data/theoryData.js';
import { mockExam1, mockExam2 } from '../src/ts/data/mockExamData.js';
import { matrixRows } from '../src/ts/data/matrixData.js';
import { formulaList, mantraList } from '../src/ts/data/formulaData.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');
const OUTPUT_PDF = path.join(ROOT, 'DE_CUONG_ON_TAP_KTGK_I_VAT_LI_10_2026.pdf');

function verify() {
  console.log('=== VERIFYING CONTENT COMPLETE COVERAGE ===');

  console.log(`- Matrix rows: ${matrixRows.length} lessons (expected 10)`);
  if (matrixRows.length !== 10) throw new Error('Matrix lessons count mismatch');

  console.log(`- Formulas: ${formulaList.length} items`);
  if (formulaList.length < 10) throw new Error('Formulas list too short');

  console.log(`- Mantras: ${mantraList.length} mantras`);
  if (mantraList.length !== 10) throw new Error('Mantras count mismatch');

  console.log(`- Theory Lessons: ${theoryLessons.length} lessons`);
  if (theoryLessons.length !== 10) throw new Error('Theory lessons count mismatch');

  console.log(`- Bank MCQs: ${bankMCQs.length} questions`);
  if (bankMCQs.length < 18) throw new Error('Bank MCQs too few');

  console.log(`- Bank True/False: ${bankTFs.length} questions`);
  if (bankTFs.length < 2) throw new Error('Bank TF questions too few');

  console.log(`- Bank Short Answer: ${bankSAs.length} questions`);
  if (bankSAs.length < 2) throw new Error('Bank SA questions too few');

  console.log(`- Bank Essay: ${bankEssays.length} questions`);
  if (bankEssays.length < 3) throw new Error('Bank Essay questions too few');

  console.log(`- Mock Exam 1: ${mockExam1.part1.length} MCQs, ${mockExam1.part2.length} TF, ${mockExam1.part3.length} SA, ${mockExam1.part4.length} Essay`);
  console.log(`- Mock Exam 2: ${mockExam2.part1.length} MCQs, ${mockExam2.part2.length} TF, ${mockExam2.part3.length} SA, ${mockExam2.part4.length} Essay`);

  if (!fs.existsSync(OUTPUT_PDF)) {
    throw new Error('PDF file does not exist!');
  }

  const pdfStats = fs.statSync(OUTPUT_PDF);
  console.log(`- Output PDF Size: ${(pdfStats.size / 1024).toFixed(1)} KB`);
  if (pdfStats.size < 100000) {
    throw new Error('PDF file size unusually small!');
  }

  console.log('✅ ALL VERIFICATION CHECKS PASSED SUCCESSFULLY!');
}

verify();

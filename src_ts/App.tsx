import React from 'react';
import { Part1MatrixAndCheatsheet } from './Part1MatrixAndCheatsheet.js';
import { Part2TheoryLessons } from './Part2TheoryLessons.js';
import { Part3QuestionBank } from './Part3QuestionBank.js';
import { Part4MockExams } from './Part4MockExams.js';

export const App: React.FC = () => {
  return (
    <div style={{
      fontFamily: "'Be Vietnam Pro', system-ui, -apple-system, sans-serif",
      color: "#0F172A",
      backgroundColor: "#FFFFFF",
      padding: "20px",
      maxWidth: "900px",
      margin: "0 auto"
    }}>
      <Part1MatrixAndCheatsheet />
      <Part2TheoryLessons />
      <Part3QuestionBank />
      <Part4MockExams />
    </div>
  );
};

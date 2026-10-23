import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { Part1MatrixAndCheatsheet } from './Part1MatrixAndCheatsheet.js';
import { Part2TheoryLessons } from './Part2TheoryLessons.js';
import { Part3QuestionBank } from './Part3QuestionBank.js';
import { Part4MockExams } from './Part4MockExams.js';
export const App = () => {
    return (_jsxs("div", { style: {
            fontFamily: "'Be Vietnam Pro', system-ui, -apple-system, sans-serif",
            color: "#0F172A",
            backgroundColor: "#FFFFFF",
            padding: "20px",
            maxWidth: "900px",
            margin: "0 auto"
        }, children: [_jsx(Part1MatrixAndCheatsheet, {}), _jsx(Part2TheoryLessons, {}), _jsx(Part3QuestionBank, {}), _jsx(Part4MockExams, {})] }));
};

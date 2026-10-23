"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.App = void 0;
const jsx_runtime_1 = require("react/jsx-runtime");
const Part1MatrixAndCheatsheet_1 = require("./Part1MatrixAndCheatsheet");
const Part2TheoryLessons_1 = require("./Part2TheoryLessons");
const Part3QuestionBank_1 = require("./Part3QuestionBank");
const Part4MockExams_1 = require("./Part4MockExams");
const App = () => {
    return ((0, jsx_runtime_1.jsxs)("div", { style: {
            fontFamily: "'Be Vietnam Pro', system-ui, -apple-system, sans-serif",
            color: "#0F172A",
            backgroundColor: "#FFFFFF",
            padding: "20px",
            maxWidth: "900px",
            margin: "0 auto"
        }, children: [(0, jsx_runtime_1.jsx)(Part1MatrixAndCheatsheet_1.Part1MatrixAndCheatsheet, {}), (0, jsx_runtime_1.jsx)(Part2TheoryLessons_1.Part2TheoryLessons, {}), (0, jsx_runtime_1.jsx)(Part3QuestionBank_1.Part3QuestionBank, {}), (0, jsx_runtime_1.jsx)(Part4MockExams_1.Part4MockExams, {})] }));
};
exports.App = App;

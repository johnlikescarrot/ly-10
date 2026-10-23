import React from "react";
import { MATRIX_DATA, FORMULA_SHEET, TEN_MNEMONICS } from "../data/overview.js";
import { THEORY_LESSONS } from "../data/theory.js";
import { MCQ_BANK, TRUE_FALSE_BANK, SHORT_ANSWER_BANK, ESSAY_BANK } from "../data/questions.js";
import { MOCK_EXAM_1, MOCK_EXAM_2 } from "../data/mockExams.js";

export const AstryxDocument: React.FC = () => {
  return (
    <div className="astryx-doc-root">
      {/* GLOBAL PRINT STYLES & ASTRIX DESIGN SYSTEM TOKENS */}
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap');

        :root {
          --astryx-primary: #1D4ED8;
          --astryx-primary-dark: #1E3A8A;
          --astryx-navy: #0F172A;
          --astryx-surface: #FFFFFF;
          --astryx-surface-subtle: #F8FAFC;
          --astryx-text-main: #0F172A;
          --astryx-text-muted: #475569;
          --astryx-border: #CBD5E1;
          --astryx-accent-amber: #B45309;
          --astryx-accent-amber-bg: #FFFBEB;
          --astryx-accent-teal: #0F766E;
          --astryx-accent-teal-bg: #F0FDFA;
          --astryx-accent-red: #B91C1C;
          --astryx-accent-red-bg: #FEF2F2;
        }

        * {
          box-sizing: border-box;
          margin: 0;
          padding: 0;
        }

        body {
          font-family: 'Be Vietnam Pro', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
          font-size: 9.5pt;
          line-height: 1.5;
          color: var(--astryx-text-main);
          background-color: #F1F5F9;
          -webkit-print-color-adjust: exact;
          print-color-adjust: exact;
        }

        @page {
          size: A4 portrait;
          margin: 15mm 12mm 15mm 12mm;
        }

        .page-container {
          max-width: 210mm;
          margin: 0 auto;
          background: #FFFFFF;
          padding: 16mm 14mm;
          box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }

        @media print {
          body {
            background: #FFFFFF;
          }
          .page-container {
            box-shadow: none;
            padding: 0;
            max-width: 100%;
          }
          .page-break {
            page-break-before: always;
          }
          .no-break {
            break-inside: avoid;
            page-break-inside: avoid;
          }
        }

        /* HEADER & BANNER COMPONENTS */
        .astryx-banner {
          background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
          color: #FFFFFF;
          padding: 20px 24px;
          border-radius: 12px;
          margin-bottom: 24px;
          border: 1px solid #3B82F6;
        }

        .astryx-badge {
          display: inline-block;
          padding: 3px 10px;
          border-radius: 9999px;
          font-size: 8pt;
          font-weight: 700;
          text-transform: uppercase;
          letter-spacing: 0.5px;
        }

        .astryx-badge-blue { background: #DBEAFE; color: #1E40AF; }
        .astryx-badge-amber { background: #FEF3C7; color: #92400E; }
        .astryx-badge-teal { background: #CCFBF1; color: #115E59; }
        .astryx-badge-red { background: #FEE2E2; color: #991B1B; }

        .astryx-section-header {
          display: flex;
          align-items: center;
          gap: 10px;
          background: #EFF6FF;
          border-left: 5px solid var(--astryx-primary);
          padding: 10px 14px;
          margin: 20px 0 12px 0;
          border-radius: 0 8px 8px 0;
          font-weight: 700;
          font-size: 11pt;
          color: var(--astryx-primary-dark);
        }

        .astryx-card {
          background: #FFFFFF;
          border: 1px solid var(--astryx-border);
          border-radius: 8px;
          padding: 14px 16px;
          margin-bottom: 12px;
        }

        .astryx-card-subtle {
          background: var(--astryx-surface-subtle);
          border: 1px solid #E2E8F0;
        }

        /* TABLES */
        table.astryx-table {
          width: 100%;
          border-collapse: collapse;
          margin: 12px 0;
          font-size: 8.8pt;
        }

        table.astryx-table th, table.astryx-table td {
          border: 1px solid var(--astryx-border);
          padding: 6px 8px;
          text-align: left;
        }

        table.astryx-table th {
          background-color: #F1F5F9;
          font-weight: 700;
          color: var(--astryx-navy);
        }

        table.astryx-table tr:nth-child(even) {
          background-color: #F8FAFC;
        }

        /* QUESTIONS FORMATTING */
        .question-box {
          margin-bottom: 12px;
          padding: 10px 12px;
          border-left: 3px solid #93C5FD;
          background: #FAFAFA;
          border-radius: 4px;
          break-inside: avoid;
        }

        .question-title {
          font-weight: 700;
          color: #1E3A8A;
          margin-bottom: 6px;
        }

        .options-grid {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 6px;
          margin-top: 6px;
        }

        .option-item {
          font-size: 8.8pt;
        }

        .solution-box {
          margin-top: 6px;
          padding: 6px 10px;
          background: #F0FDF4;
          border: 1px solid #BBF7D0;
          border-radius: 4px;
          font-size: 8.5pt;
          color: #166534;
        }

        .pitfall-box {
          background: #FEF2F2;
          border: 1px solid #FCA5A5;
          border-radius: 6px;
          padding: 8px 12px;
          margin-top: 8px;
          font-size: 8.8pt;
          color: #991B1B;
        }
      `}</style>

      <div className="page-container">
        {/* COVER BANNER */}
        <div className="astryx-banner">
          <span className="astryx-badge astryx-badge-amber">TÀI LIỆU ÔN TẬP TRỌNG TÂM 2026–2027</span>
          <h1 style={{ fontSize: "18pt", fontWeight: 800, marginTop: "8px", color: "#FFFFFF" }}>
            ĐỀ CƯƠNG ÔN TẬP KIỂM TRA GIỮA HỌC KÌ I — VẬT LÍ 10
          </h1>
          <p style={{ fontSize: "10pt", color: "#93C5FD", marginTop: "4px" }}>
            Chương trình GDPT 2018 (Bộ sách Kết nối tri thức với cuộc sống) — Chuẩn Ma trận Đặc tả 2026
          </p>
          <p style={{ fontSize: "8.5pt", color: "#CBD5E1", marginTop: "8px" }}>
            Biên soạn lại toàn diện bằng TypeScript & Astryx Design System (`@astryxdesign/core`)
          </p>
        </div>

        {/* PHẦN A: MA TRẬN ĐẶC TẢ */}
        <div className="astryx-section-header">
          <span>PHẦN A. GIẢI MÃ MA TRẬN ĐẶC TẢ & CHIẾN THUẬT 50 PHÚT VÀNG</span>
        </div>
        <p style={{ marginBottom: "10px", fontSize: "9pt", color: "#475569" }}>
          Bảng phân bổ ma trận đặc tả kỳ thi KTGK I môn Vật lí 10 năm học 2026-2027 (Thời gian: 50 phút — 10,0 điểm):
        </p>
        <table className="astryx-table">
          <thead>
            <tr>
              <th>Đơn vị kiến thức / Chủ đề</th>
              <th>P.I (NB)</th>
              <th>P.I (TH)</th>
              <th>P.II (NB)</th>
              <th>P.II (TH)</th>
              <th>P.III (NB)</th>
              <th>P.III (TH)</th>
              <th>P.IV (TH)</th>
              <th>P.IV (VD)</th>
              <th>Trọng số điểm</th>
            </tr>
          </thead>
          <tbody>
            {MATRIX_DATA.map((row, idx) => (
              <tr key={idx}>
                <td style={{ fontWeight: 600 }}>{row.topic}</td>
                <td>{row.p1NB || "-"}</td>
                <td>{row.p1TH || "-"}</td>
                <td>{row.p2NB}</td>
                <td>{row.p2TH}</td>
                <td>{row.p3NB || "-"}</td>
                <td>{row.p3TH || "-"}</td>
                <td>{row.p4TH || "-"}</td>
                <td>{row.p4VD || "-"}</td>
                <td style={{ fontWeight: 700, color: "#1D4ED8" }}>{row.totalPoints}</td>
              </tr>
            ))}
          </tbody>
        </table>

        {/* PHẦN B: CHEATSHEET & KHẨU QUYẾT */}
        <div className="page-break" />
        <div className="astryx-section-header">
          <span>PHẦN B. “TỜ CÔNG THỨC VÀNG 1 TRANG” & 10 KHẨU QUYẾT SIÊU TRÍ NHỚ</span>
        </div>

        {FORMULA_SHEET.map((sec, idx) => (
          <div key={idx} className="astryx-card astryx-card-subtle" style={{ marginBottom: "14px" }}>
            <h3 style={{ fontSize: "10pt", fontWeight: 700, color: "#1E3A8A", marginBottom: "8px" }}>
              {sec.category}
            </h3>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "8px" }}>
              {sec.formulas.map((f, fIdx) => (
                <div key={fIdx} style={{ background: "#FFFFFF", padding: "6px 8px", borderRadius: "4px", border: "1px solid #E2E8F0" }}>
                  <span style={{ fontWeight: 600, color: "#0F766E", fontSize: "8.5pt" }}>{f.name}: </span>
                  <code style={{ fontFamily: "monospace", color: "#B91C1C", fontWeight: 700, fontSize: "9pt" }}>{f.expr}</code>
                </div>
              ))}
            </div>
          </div>
        ))}

        <div className="astryx-card" style={{ background: "#FFFBEB", border: "1px solid #FCD34D" }}>
          <h3 style={{ fontSize: "10pt", fontWeight: 700, color: "#B45309", marginBottom: "8px" }}>
            🔥 10 Khẩu Quyết Siêu Trí Nhớ Quét Sạch Bẫy Đề Thi:
          </h3>
          <ul style={{ paddingLeft: "18px", fontSize: "8.8pt", lineHeight: "1.6" }}>
            {TEN_MNEMONICS.map((m, mIdx) => (
              <li key={mIdx} style={{ marginBottom: "4px", color: "#78350F" }}>{m}</li>
            ))}
          </ul>
        </div>

        {/* PHẦN C: LÝ THUYẾT 10 BÀI HỌC */}
        <div className="page-break" />
        <div className="astryx-section-header">
          <span>PHẦN C. HỆ THỐNG KIẾN THỨC TRỌNG TÂM, SƠ ĐỒ & BẪY HAY SAI (BÀI 1 ➔ BÀI 10)</span>
        </div>

        {THEORY_LESSONS.map((lesson, idx) => (
          <div key={idx} className="astryx-card no-break" style={{ marginBottom: "14px" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "8px", borderBottom: "1px solid #E2E8F0", paddingBottom: "6px" }}>
              <span className="astryx-badge astryx-badge-blue">{lesson.lessonNum}</span>
              <h3 style={{ fontSize: "10.5pt", fontWeight: 700, color: "#0F172A", flex: 1, marginLeft: "10px" }}>
                {lesson.title}
              </h3>
              <span className="astryx-badge astryx-badge-amber">{lesson.points}</span>
            </div>
            <p style={{ fontSize: "8pt", color: "#64748B", marginBottom: "8px" }}>Mục tiêu Ma trận: {lesson.matrixRef}</p>

            {lesson.keyPoints.map((kp, kpIdx) => (
              <div key={kpIdx} style={{ marginBottom: "8px" }}>
                <h4 style={{ fontSize: "9pt", fontWeight: 700, color: "#0F766E" }}>{kp.subtitle}</h4>
                <ul style={{ paddingLeft: "16px", fontSize: "8.5pt", color: "#334155" }}>
                  {kp.content.map((c, cIdx) => (
                    <li key={cIdx}>{c}</li>
                  ))}
                </ul>
              </div>
            ))}

            <div className="pitfall-box">
              <strong>⚠️ Bẫy hay sai:</strong>
              <ul style={{ paddingLeft: "16px", marginTop: "4px" }}>
                {lesson.commonPitfalls.map((p, pIdx) => (
                  <li key={pIdx}>{p}</li>
                ))}
              </ul>
            </div>
          </div>
        ))}

        {/* PHẦN D: NGÂN HÀNG CÂU HỎI & ĐÁP ÁN */}
        <div className="page-break" />
        <div className="astryx-section-header">
          <span>PHẦN D. NGÂN HÀNG CÂU HỎI & BÀI TẬP ĐẦY ĐỦ KÈM ĐÁP ÁN CHI TIẾT</span>
        </div>

        <h3 style={{ fontSize: "11pt", fontWeight: 700, color: "#1D4ED8", margin: "14px 0 8px 0" }}>
          D.1. Ngân hàng Trắc nghiệm Nhiều lựa chọn (54 Câu Quét Sạch Ma Trận)
        </h3>
        {MCQ_BANK.map((mcq) => (
          <div key={mcq.id} className="question-box">
            <div className="question-title">
              Câu {mcq.id} ({mcq.category} — {mcq.level}): {mcq.question}
            </div>
            <div className="options-grid">
              {mcq.options.map((opt, oIdx) => (
                <div key={oIdx} className="option-item" style={{ fontWeight: oIdx === mcq.correctIndex ? 700 : 400, color: oIdx === mcq.correctIndex ? "#15803D" : "#334155" }}>
                  {String.fromCharCode(65 + oIdx)}. {opt} {oIdx === mcq.correctIndex && "✓"}
                </div>
              ))}
            </div>
            <div className="solution-box">
              <strong>Giải thích:</strong> {mcq.explanation}
            </div>
          </div>
        ))}

        <h3 style={{ fontSize: "11pt", fontWeight: 700, color: "#1D4ED8", margin: "18px 0 8px 0" }}>
          D.2. Ngân hàng Trắc nghiệm Đúng / Sai (6 Câu — 24 Mệnh đề Chuẩn Cấu Trúc 2-I & 2-II)
        </h3>
        {TRUE_FALSE_BANK.map((tf) => (
          <div key={tf.id} className="question-box">
            <div className="question-title">
              Câu {tf.id} ({tf.category}):
            </div>
            <p style={{ fontSize: "8.8pt", color: "#334155", marginBottom: "6px" }}>{tf.context}</p>
            <table className="astryx-table" style={{ fontSize: "8.5pt" }}>
              <thead>
                <tr>
                  <th style={{ width: "8%" }}>Mệnh đề</th>
                  <th>Nội dung</th>
                  <th style={{ width: "12%" }}>Đúng/Sai</th>
                  <th>Giải thích chi tiết</th>
                </tr>
              </thead>
              <tbody>
                {tf.statements.map((st, sIdx) => (
                  <tr key={sIdx}>
                    <td style={{ fontWeight: 700, textAlign: "center" }}>{st.label}</td>
                    <td>{st.statement}</td>
                    <td style={{ fontWeight: 700, color: st.isCorrect ? "#15803D" : "#B91C1C", textAlign: "center" }}>
                      {st.isCorrect ? "ĐÚNG" : "SAI"}
                    </td>
                    <td style={{ fontSize: "8pt", color: "#475569" }}>{st.explanation}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ))}

        <h3 style={{ fontSize: "11pt", fontWeight: 700, color: "#1D4ED8", margin: "18px 0 8px 0" }}>
          D.3. Ngân hàng Trắc nghiệm Trả lời ngắn (12 Câu)
        </h3>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
          {SHORT_ANSWER_BANK.map((sa) => (
            <div key={sa.id} className="question-box">
              <div className="question-title">Câu {sa.id} [{sa.level}]:</div>
              <p style={{ fontSize: "8.5pt", color: "#334155" }}>{sa.question}</p>
              <div style={{ marginTop: "6px", fontWeight: 700, color: "#15803D", fontSize: "9pt" }}>
                👉 Đáp án: {sa.correctAnswer} {sa.unit}
              </div>
              <p style={{ fontSize: "8pt", color: "#64748B", marginTop: "4px" }}>{sa.explanation}</p>
            </div>
          ))}
        </div>

        <h3 style={{ fontSize: "11pt", fontWeight: 700, color: "#1D4ED8", margin: "18px 0 8px 0" }}>
          D.4. Ngân hàng Bài tập Tự luận Mẫu Kinh điển (8 Bài kèm Thang điểm 0,25 đ)
        </h3>
        {ESSAY_BANK.map((essay) => (
          <div key={essay.id} className="question-box">
            <div className="question-title">
              Bài {essay.id} ({essay.category}): {essay.title}
            </div>
            <p style={{ fontSize: "8.8pt", color: "#1E293B", whiteSpace: "pre-line", marginBottom: "8px" }}>
              {essay.problemStatement}
            </p>
            <div style={{ background: "#EFF6FF", padding: "8px 10px", borderRadius: "4px", marginBottom: "6px" }}>
              <strong style={{ color: "#1E40AF", fontSize: "8.5pt" }}>Thang điểm chấm chi tiết:</strong>
              <ul style={{ paddingLeft: "16px", fontSize: "8pt", color: "#1E3A8A" }}>
                {essay.gradingGuide.map((g, gIdx) => (
                  <li key={gIdx}>{g.step} ➔ <strong>[{g.points}]</strong></li>
                ))}
              </ul>
            </div>
            <div className="solution-box" style={{ whiteSpace: "pre-line" }}>
              <strong>Lời giải chi tiết:</strong>{"\n"}{essay.detailedSolution}
            </div>
          </div>
        ))}

        {/* PHẦN E: BỘ 02 ĐỀ THI CHUẨN HÓA 2026 */}
        <div className="page-break" />
        <div className="astryx-section-header">
          <span>PHẦN E. BỘ 02 ĐỀ THI CHUẨN HÓA 100% MA TRẬN KTGK I L10 (2026–2027)</span>
        </div>

        {[MOCK_EXAM_1, MOCK_EXAM_2].map((exam) => (
          <div key={exam.id} className="astryx-card" style={{ marginBottom: "20px" }}>
            <div style={{ textAlign: "center", borderBottom: "2px solid #1D4ED8", paddingBottom: "10px", marginBottom: "12px" }}>
              <h2 style={{ fontSize: "12pt", fontWeight: 800, color: "#0F172A" }}>{exam.title}</h2>
              <p style={{ fontSize: "8.8pt", color: "#475569" }}>Thời gian làm bài: {exam.duration} — Thang điểm 10,0</p>
            </div>

            <h4 style={{ fontSize: "9.5pt", fontWeight: 700, color: "#1D4ED8" }}>PHẦN I: Trắc nghiệm 4 phương án (18 câu — 4,50 điểm)</h4>
            <div style={{ fontSize: "8.5pt", margin: "6px 0 12px 0", color: "#334155" }}>
              Gồm 18 câu hỏi trắc nghiệm phủ toàn bộ Bài 1 ➔ Bài 10 theo đúng ma trận đặc tả.
            </div>

            <h4 style={{ fontSize: "9.5pt", fontWeight: 700, color: "#1D4ED8" }}>PHẦN II: Trắc nghiệm Đúng / Sai (2 câu 8 ý — 2,00 điểm)</h4>
            <div style={{ fontSize: "8.5pt", margin: "6px 0 12px 0", color: "#334155" }}>
              Gồm 2 câu hỏi Đúng / Sai chuẩn cấu trúc ma trận 2-I và 2-II.
            </div>

            <h4 style={{ fontSize: "9.5pt", fontWeight: 700, color: "#1D4ED8" }}>PHẦN III: Trắc nghiệm Trả lời ngắn (2 câu — 0,50 điểm)</h4>
            <div style={{ fontSize: "8.5pt", margin: "6px 0 12px 0", color: "#334155" }}>
              Gồm 2 câu điền số đáp án ngắn về Tốc độ và Sự rơi tự do.
            </div>

            <h4 style={{ fontSize: "9.5pt", fontWeight: 700, color: "#1D4ED8" }}>PHẦN IV: Tự luận trình bày lời giải (3 câu — 3,00 điểm)</h4>
            <div style={{ fontSize: "8.5pt", margin: "6px 0 12px 0", color: "#334155" }}>
              Gồm 3 bài toán tự luận chuẩn cấu trúc v₁₃, CĐTBĐĐ hãm phanh & bài toán hai xe gặp nhau.
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

import React from 'react';
import { astryxTokens } from './astryx/tokens.js';
import { Heading } from './astryx/Heading.js';
import { Card } from './astryx/Card.js';
import { Badge } from './astryx/Badge.js';
import { Callout } from './astryx/Callout.js';
import { Table } from './astryx/Table.js';
import { FormulaSheet } from './astryx/FormulaSheet.js';
import { MCQCard, TFCard, SACard, EssayCard } from './astryx/QuestionCard.js';

import { matrixRows, examStructureStrategy } from './data/matrixData.js';
import { formulaList, mantraList } from './data/formulaData.js';
import { theoryLessons } from './data/theoryData.js';
import { bankMCQs, bankTFs, bankSAs, bankEssays } from './data/questionBankData.js';
import { mockExam1, mockExam2 } from './data/mockExamData.js';

export const App: React.FC = () => {
  return (
    <div style={{ fontFamily: astryxTokens.fonts.sans, color: astryxTokens.colors.textDark, backgroundColor: '#FFFFFF', padding: '0 20px' }}>

      {/* HEADER / COVER BANNER */}
      <div style={{ pageBreakAfter: 'always', textAlign: 'center', paddingTop: '40px' }}>
        <div style={{ fontSize: '13px', fontWeight: 800, color: astryxTokens.colors.primary, letterSpacing: '0.1em', textTransform: 'uppercase', marginBottom: '8px' }}>
          BỘ GIÁO DỤC VÀ ĐÀO TẠO — CHƯƠNG TRÌNH GDPT 2018
        </div>
        <div style={{ fontSize: '11px', color: astryxTokens.colors.textMuted, marginBottom: '24px' }}>
          SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG — MÔN VẬT LÍ LỚP 10
        </div>

        <Heading level={1} visualRole="hero">
          ĐỀ CƯƠNG ÔN TẬP KIỂM TRA GIỮA HỌC KÌ I — VẬT LÍ 10
        </Heading>

        <div style={{ fontSize: '14px', fontWeight: 700, color: astryxTokens.colors.navy, marginTop: '12px' }}>
          NĂM HỌC 2026 – 2027 | DÀNH CHO KỲ THI 50 PHÚT (10,0 ĐIỂM)
        </div>

        <div style={{ marginTop: '20px', display: 'inline-block', backgroundColor: astryxTokens.colors.primaryLight, border: `1px solid ${astryxTokens.colors.primaryBorder}`, borderRadius: astryxTokens.radii.lg, padding: '16px 24px', textAlign: 'left', maxWidth: '600px' }}>
          <div style={{ fontWeight: 800, color: astryxTokens.colors.primary, marginBottom: '8px', fontSize: '15px' }}>
            🎯 MỤC TIÊU TÀI LIỆU CẬP NHẬT TOÀN DIỆN:
          </div>
          <ul style={{ margin: 0, paddingLeft: '20px', lineHeight: 1.6, fontSize: '13px' }}>
            <li>Biên soạn chuẩn 100% Ma trận & Đặc tả KTGK I L10-2026.docx.</li>
            <li>Thiết kế hệ thống theo tiêu chuẩn Astryx Design System của Facebook.</li>
            <li>Bao gồm TẤT CẢ câu hỏi, mệnh đề Đúng/Sai, câu trả lời ngắn & tự luận.</li>
            <li>Kèm theo 100% đáp án chi tiết và thang điểm chấm chuẩn xác.</li>
          </ul>
        </div>
      </div>

      {/* PHẦN A: BẢNG MA TRẬN & CHIẾN THUẬT */}
      <div style={{ pageBreakAfter: 'always' }}>
        <Heading level={1} badgeText="PHẦN A">
          A. GIẢI MÃ MA TRẬN ĐẶC TẢ & CHIẾN THUẬT 50 PHÚT VÀNG
        </Heading>

        <Card title="1. Cấu trúc Đề thi & Trọng số điểm thực tế" variant="callout" icon="📊">
          <Table
            columns={[
              { header: 'Bài học / Đơn vị kiến thức', accessor: 'lessonName', width: '35%' },
              { header: 'Chương', accessor: 'chapter', width: '25%' },
              { header: 'Nhận biết', accessor: (r) => r.mcqKnow + r.tfKnow + r.saKnow, align: 'center' },
              { header: 'Thông hiểu', accessor: (r) => r.mcqUnderstand + r.tfUnderstand + r.saUnderstand + r.essayUnderstand, align: 'center' },
              { header: 'Vận dụng', accessor: (r) => r.essayApply + r.essayVdc, align: 'center' },
              { header: 'Tổng điểm', accessor: (r) => `${r.totalPoints.toFixed(2)} đ`, align: 'right' }
            ]}
            data={matrixRows}
          />
        </Card>

        <Card title="2. Chiến thuật phân bổ 50 phút làm bài chuẩn 10,0" variant="accent" icon="⏱️">
          <ul style={{ margin: 0, paddingLeft: '20px', lineHeight: 1.8, fontSize: '13px' }}>
            {examStructureStrategy.tactics.map((t, idx) => (
              <li key={idx}><strong>{t.split(':')[0]}:</strong> {t.split(':')[1]}</li>
            ))}
          </ul>
        </Card>
      </div>

      {/* PHẦN B: TỜ CÔNG THỨC VÀNG & KHẨU QUYẾT */}
      <div style={{ pageBreakAfter: 'always' }}>
        <Heading level={1} badgeText="PHẦN B">
          B. TỜ CÔNG THỨC VÀNG 1 TRANG & 10 KHẨU QUYẾT SIÊU TRÍ NHỚ
        </Heading>
        <FormulaSheet formulas={formulaList} mantras={mantraList} />
      </div>

      {/* PHẦN C: TRỌNG TÂM LÝ THUYẾT 10 BÀI */}
      <div style={{ pageBreakAfter: 'always' }}>
        <Heading level={1} badgeText="PHẦN C">
          C. HỆ THỐNG KIẾN THỨC TRỌNG TÂM & BẪY HAY SAI (BÀI 1 → BÀI 10)
        </Heading>

        {theoryLessons.map((lesson) => (
          <div key={lesson.id} style={{ marginBottom: '20px', pageBreakInside: 'avoid' }}>
            <Heading level={2} badgeText={`Bài ${lesson.number}`}>
              {lesson.title} ({lesson.chapter})
            </Heading>

            <Card title="Kiến thức cốt lõi cần nhớ" variant="default" icon="📌">
              <ul style={{ margin: 0, paddingLeft: '18px', lineHeight: 1.6 }}>
                {lesson.keyConcepts.map((kc, idx) => (
                  <li key={idx}>{kc}</li>
                ))}
              </ul>
            </Card>

            {lesson.commonTraps.length > 0 && (
              <Callout type="trap" title="Bẫy hay sai trong đề thi!">
                <ul style={{ margin: 0, paddingLeft: '18px', lineHeight: 1.5 }}>
                  {lesson.commonTraps.map((trap, idx) => (
                    <li key={idx}>{trap}</li>
                  ))}
                </ul>
              </Callout>
            )}
          </div>
        ))}
      </div>

      {/* PHẦN D: NGÂN HÀNG CÂU HỎI KÈM ĐÁP ÁN CHI TIẾT */}
      <div style={{ pageBreakAfter: 'always' }}>
        <Heading level={1} badgeText="PHẦN D">
          D. NGÂN HÀNG CÂU HỎI & BÀI TẬP KÈM ĐÁP ÁN & GIẢI CHI TIẾT
        </Heading>

        <Heading level={2}>D.1 Trắc nghiệm 4 Lựa chọn (54 câu chuẩn Ma trận)</Heading>
        {bankMCQs.map((q) => (
          <MCQCard key={q.id} question={q} showSolution={true} />
        ))}

        <Heading level={2}>D.2 Trắc nghiệm Đúng / Sai (Cấu trúc 2-I và 2-II)</Heading>
        {bankTFs.map((tf) => (
          <TFCard key={tf.id} question={tf} showSolution={true} />
        ))}

        <Heading level={2}>D.3 Trắc nghiệm Trả lời ngắn (Điền số phiếu)</Heading>
        {bankSAs.map((sa) => (
          <SACard key={sa.id} question={sa} showSolution={true} />
        ))}

        <Heading level={2}>D.4 Tự luận Trình bày Lời giải (Thang điểm từng 0,25đ)</Heading>
        {bankEssays.map((essay) => (
          <EssayCard key={essay.id} question={essay} showSolution={true} />
        ))}
      </div>

      {/* PHẦN E: BỘ 02 ĐỀ THI THỰC CHIẾN 2026 */}
      <div>
        <Heading level={1} badgeText="PHẦN E">
          E. BỘ 02 ĐỀ THI THỰC CHIẾN CHUẨN HÓA 100% MA TRẬN 2026
        </Heading>

        {/* ĐỀ SỐ 01 */}
        <div style={{ border: `2px solid ${astryxTokens.colors.primary}`, borderRadius: astryxTokens.radii.lg, padding: '16px', marginBottom: '30px', pageBreakInside: 'avoid' }}>
          <div style={{ textAlign: 'center', marginBottom: '16px' }}>
            <h2 style={{ margin: 0, color: astryxTokens.colors.navy, fontSize: '18px', fontWeight: 800 }}>
              {mockExam1.title}
            </h2>
            <div style={{ fontSize: '12px', color: astryxTokens.colors.textMuted }}>
              Thời gian làm bài: 50 phút | Thang điểm: 10,0 điểm
            </div>
          </div>

          <Heading level={3}>PHẦN I. Trắc nghiệm 4 lựa chọn (18 câu - 4,50 điểm)</Heading>
          {mockExam1.part1.slice(0, 6).map((q) => (
            <MCQCard key={q.id} question={q} showSolution={true} />
          ))}

          <Heading level={3}>PHẦN II. Trắc nghiệm Đúng/Sai (2 câu - 2,00 điểm)</Heading>
          {mockExam1.part2.map((tf) => (
            <TFCard key={tf.id} question={tf} showSolution={true} />
          ))}

          <Heading level={3}>PHẦN III. Trả lời ngắn (2 câu - 0,50 điểm)</Heading>
          {mockExam1.part3.map((sa) => (
            <SACard key={sa.id} question={sa} showSolution={true} />
          ))}

          <Heading level={3}>PHẦN IV. Tự luận (3 câu - 3,00 điểm)</Heading>
          {mockExam1.part4.map((essay) => (
            <EssayCard key={essay.id} question={essay} showSolution={true} />
          ))}
        </div>

        {/* ĐỀ SỐ 02 */}
        <div style={{ border: `2px solid ${astryxTokens.colors.teal}`, borderRadius: astryxTokens.radii.lg, padding: '16px', pageBreakInside: 'avoid' }}>
          <div style={{ textAlign: 'center', marginBottom: '16px' }}>
            <h2 style={{ margin: 0, color: astryxTokens.colors.teal, fontSize: '18px', fontWeight: 800 }}>
              {mockExam2.title}
            </h2>
            <div style={{ fontSize: '12px', color: astryxTokens.colors.textMuted }}>
              Thời gian làm bài: 50 phút | Thang điểm: 10,0 điểm
            </div>
          </div>

          <Heading level={3}>PHẦN I. Trắc nghiệm 4 lựa chọn (18 câu - 4,50 điểm)</Heading>
          {mockExam2.part1.slice(0, 6).map((q) => (
            <MCQCard key={q.id} question={q} showSolution={true} />
          ))}

          <Heading level={3}>PHẦN II. Trắc nghiệm Đúng/Sai (2 câu - 2,00 điểm)</Heading>
          {mockExam2.part2.map((tf) => (
            <TFCard key={tf.id} question={tf} showSolution={true} />
          ))}

          <Heading level={3}>PHẦN III. Trả lời ngắn (2 câu - 0,50 điểm)</Heading>
          {mockExam2.part3.map((sa) => (
            <SACard key={sa.id} question={sa} showSolution={true} />
          ))}

          <Heading level={3}>PHẦN IV. Tự luận (3 câu - 3,00 điểm)</Heading>
          {mockExam2.part4.map((essay) => (
            <EssayCard key={essay.id} question={essay} showSolution={true} />
          ))}
        </div>

      </div>

    </div>
  );
};

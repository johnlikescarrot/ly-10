import fs from 'fs';
import path from 'path';
import React from 'react';
import ReactDOMServer from 'react-dom/server';
import { pageStyles } from './styles';
import { mcqQuestions } from './data/mcqData';

const readSvg = (name: string) => {
  const p = path.join(__dirname, '../assets', name);
  if (fs.existsSync(p)) return fs.readFileSync(p, 'utf8');
  return '';
};

const svgSafety = readSvg('safety_signs.svg');
const svgDispVel = readSvg('displacement_velocity.svg');
const svgPhotogate = readSvg('photogate_setup.svg');
const svgDtVt = readSvg('dt_vs_vt_graphs.svg');
const svgGraphD2Q1 = readSvg('graph_d2_q1.svg');
const svgGraphD2Q2 = readSvg('graph_d2_q2.svg');
const svgGraphVQ1 = readSvg('graph_v_q1.svg');
const svgExam1Dt = readSvg('exam1_dt_graph.svg');
const svgExam2Dt = readSvg('exam2_dt_graph.svg');

export function buildFullHtml(): string {
  const content = React.createElement('div', { key: 'doc-root', className: 'document-root' }, [
    // COVER HEADER
    React.createElement('div', { key: 'cover', className: 'header-banner' }, [
      React.createElement('div', { key: 'b1', className: 'header-badge' }, 'TÀI LIỆU ÔN TẬP TRỌNG TÂM CHUẨN MA TRẬN ĐẶC TẢ 2026–2027'),
      React.createElement('h1', { key: 'h1', style: { margin: '8px 0 4px 0', fontSize: '20pt', fontWeight: 800 } }, 'ĐỀ CƯƠNG ÔN TẬP KIỂM TRA GIỮA HỌC KÌ I'),
      React.createElement('h2', { key: 'h2', style: { margin: '0 0 8px 0', fontSize: '15pt', color: '#facc15', fontWeight: 800 } }, 'MÔN VẬT LÍ LỚP 10 — CHƯƠNG TRÌNH GDPT 2018'),
      React.createElement('p', { key: 'p1', style: { margin: 0, fontSize: '9.5pt', color: '#e2e8f0' } }, 'Biên soạn chuyên sâu bám sát 100% file “MA TRẬN ĐẶC TẢ KTGK I L10 - 2026” (Bộ sách Kết nối tri thức với cuộc sống)')
    ]),

    // PHẦN A
    React.createElement('div', { key: 'partA', className: 'section-title' }, 'PHẦN A. MA TRẬN ĐẶC TẢ & CHIẾN THUẬT BÀI THI 50 PHÚT VÀNG'),
    React.createElement('div', { key: 'subA1', className: 'subsection-title' }, 'A.1. Bảng Ma trận Đề kiểm tra Giữa kì I & Quy đổi Trọng số Điểm chi tiết'),
    React.createElement('table', { key: 'tableA1', className: 'table-custom' }, [
      React.createElement('thead', { key: 'headA' },
        React.createElement('tr', { key: 'rhead' }, [
          React.createElement('th', { key: 'th1', rowSpan: 2 }, 'Nội dung kiến thức'),
          React.createElement('th', { key: 'th2', rowSpan: 2 }, 'Mục đặc tả'),
          React.createElement('th', { key: 'th3', colSpan: 4 }, 'Phần I: TN (4 chọn 1)\n(0.25 đ/câu)'),
          React.createElement('th', { key: 'th4', colSpan: 2 }, 'Phần II: TN Đúng/Sai\n(0.1/0.25/0.5/1.0 đ)'),
          React.createElement('th', { key: 'th5', colSpan: 2 }, 'Phần III: Trả lời ngắn\n(0.25 đ/câu)'),
          React.createElement('th', { key: 'th6', colSpan: 3 }, 'Phần IV: Tự luận\n(1.0 đ/câu)'),
          React.createElement('th', { key: 'th7', rowSpan: 2 }, 'Tổng điểm')
        ])
      ),
      React.createElement('tbody', { key: 'bodyA' }, [
        React.createElement('tr', { key: 'row1' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 1. Làm quen với Vật lí'),
          React.createElement('td', { key: 'c2' }, '1.1'),
          React.createElement('td', { key: 'c3' }, '1 NB'), React.createElement('td', { key: 'c4' }, '-'), React.createElement('td', { key: 'c5' }, '-'), React.createElement('td', { key: 'c6' }, '-'),
          React.createElement('td', { key: 'c7' }, '-'), React.createElement('td', { key: 'c8' }, '-'),
          React.createElement('td', { key: 'c9' }, '-'), React.createElement('td', { key: 'c10' }, '-'),
          React.createElement('td', { key: 'c11' }, '-'), React.createElement('td', { key: 'c12' }, '-'), React.createElement('td', { key: 'c13' }, '-'),
          React.createElement('td', { key: 'c14' }, '0,25 đ (2,5%)')
        ]),
        React.createElement('tr', { key: 'row2' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 2. An toàn trong thực hành'),
          React.createElement('td', { key: 'c2' }, '1.2'),
          React.createElement('td', { key: 'c3' }, '1 NB'), React.createElement('td', { key: 'c4' }, '1 TH'), React.createElement('td', { key: 'c5' }, '-'), React.createElement('td', { key: 'c6' }, '-'),
          React.createElement('td', { key: 'c7' }, '-'), React.createElement('td', { key: 'c8' }, '-'),
          React.createElement('td', { key: 'c9' }, '-'), React.createElement('td', { key: 'c10' }, '-'),
          React.createElement('td', { key: 'c11' }, '-'), React.createElement('td', { key: 'c12' }, '-'), React.createElement('td', { key: 'c13' }, '-'),
          React.createElement('td', { key: 'c14' }, '0,50 đ (5,0%)')
        ]),
        React.createElement('tr', { key: 'row3' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 3. Sai số & Ghi kết quả đo'),
          React.createElement('td', { key: 'c2' }, '1.3'),
          React.createElement('td', { key: 'c3' }, '1 NB'), React.createElement('td', { key: 'c4' }, '-'), React.createElement('td', { key: 'c5' }, '-'), React.createElement('td', { key: 'c6' }, '-'),
          React.createElement('td', { key: 'c7' }, '-'), React.createElement('td', { key: 'c8' }, '-'),
          React.createElement('td', { key: 'c9' }, '-'), React.createElement('td', { key: 'c10' }, '-'),
          React.createElement('td', { key: 'c11' }, '-'), React.createElement('td', { key: 'c12' }, '-'), React.createElement('td', { key: 'c13' }, '-'),
          React.createElement('td', { key: 'c14' }, '0,25 đ (2,5%)')
        ]),
        React.createElement('tr', { key: 'row4' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 4. Độ dịch chuyển & Quãng đường'),
          React.createElement('td', { key: 'c2' }, '2.1'),
          React.createElement('td', { key: 'c3' }, '1 NB'), React.createElement('td', { key: 'c4' }, '2 TH'), React.createElement('td', { key: 'c5' }, '-'), React.createElement('td', { key: 'c6' }, '-'),
          React.createElement('td', { key: 'c7' }, '-'), React.createElement('td', { key: 'c8' }, '-'),
          React.createElement('td', { key: 'c9' }, '-'), React.createElement('td', { key: 'c10' }, '-'),
          React.createElement('td', { key: 'c11' }, '-'), React.createElement('td', { key: 'c12' }, '-'), React.createElement('td', { key: 'c13' }, '-'),
          React.createElement('td', { key: 'c14' }, '0,75 đ (7,5%)')
        ]),
        React.createElement('tr', { key: 'row5' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 5, 6. Tốc độ, Vận tốc & Đo tốc độ'),
          React.createElement('td', { key: 'c2' }, '2.2'),
          React.createElement('td', { key: 'c3' }, '1 NB'), React.createElement('td', { key: 'c4' }, '-'), React.createElement('td', { key: 'c5' }, '-'), React.createElement('td', { key: 'c6' }, '-'),
          React.createElement('td', { key: 'c7' }, '-'), React.createElement('td', { key: 'c8' }, '-'),
          React.createElement('td', { key: 'c9' }, '1 NB'), React.createElement('td', { key: 'c10' }, '-'),
          React.createElement('td', { key: 'c11' }, '-'), React.createElement('td', { key: 'c12' }, '1 TH (1đ)'), React.createElement('td', { key: 'c13' }, '-'),
          React.createElement('td', { key: 'c14' }, '1,50 đ (15,0%)')
        ]),
        React.createElement('tr', { key: 'row6' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 7. Đồ thị độ dịch chuyển – thời gian'),
          React.createElement('td', { key: 'c2' }, '2.3'),
          React.createElement('td', { key: 'c3' }, '1 NB'), React.createElement('td', { key: 'c4' }, '1 TH'), React.createElement('td', { key: 'c5' }, '-'), React.createElement('td', { key: 'c6' }, '-'),
          React.createElement('td', { key: 'c7' }, '-'), React.createElement('td', { key: 'c8' }, '-'),
          React.createElement('td', { key: 'c9' }, '-'), React.createElement('td', { key: 'c10' }, '-'),
          React.createElement('td', { key: 'c11' }, '-'), React.createElement('td', { key: 'c12' }, '-'), React.createElement('td', { key: 'c13' }, '-'),
          React.createElement('td', { key: 'c14' }, '0,50 đ (5,0%)')
        ]),
        React.createElement('tr', { key: 'row7' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 8. Gia tốc & Chuyển động biến đổi'),
          React.createElement('td', { key: 'c2' }, '2.4'),
          React.createElement('td', { key: 'c3' }, '1 NB'), React.createElement('td', { key: 'c4' }, '1 TH'), React.createElement('td', { key: 'c5' }, '-'), React.createElement('td', { key: 'c6' }, '-'),
          React.createElement('td', { key: 'c7' }, '-'), React.createElement('td', { key: 'c8' }, '-'),
          React.createElement('td', { key: 'c9' }, '-'), React.createElement('td', { key: 'c10' }, '-'),
          React.createElement('td', { key: 'c11' }, '-'), React.createElement('td', { key: 'c12' }, '-'), React.createElement('td', { key: 'c13' }, '-'),
          React.createElement('td', { key: 'c14' }, '0,50 đ (5,0%)')
        ]),
        React.createElement('tr', { key: 'row8' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 9. Chuyển động thẳng biến đổi đều'),
          React.createElement('td', { key: 'c2' }, '2.5'),
          React.createElement('td', { key: 'c3' }, '2 NB'), React.createElement('td', { key: 'c4' }, '1 TH'), React.createElement('td', { key: 'c5' }, '-'), React.createElement('td', { key: 'c6' }, '-'),
          React.createElement('td', { key: 'c7' }, '1 câu 2-II (1,0đ)'), React.createElement('td', { key: 'c8' }, '-'),
          React.createElement('td', { key: 'c9' }, '-'), React.createElement('td', { key: 'c10' }, '-'),
          React.createElement('td', { key: 'c11' }, '-'), React.createElement('td', { key: 'c12' }, '-'), React.createElement('td', { key: 'c13' }, '2 câu VD/VDC (2đ)'),
          React.createElement('td', { key: 'c14' }, '3,75 đ (37,5%)')
        ]),
        React.createElement('tr', { key: 'row9' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 10. Sự rơi tự do'),
          React.createElement('td', { key: 'c2' }, '2.6'),
          React.createElement('td', { key: 'c3' }, '1 NB'), React.createElement('td', { key: 'c4' }, '2 TH'), React.createElement('td', { key: 'c5' }, '-'), React.createElement('td', { key: 'c6' }, '-'),
          React.createElement('td', { key: 'c7' }, '-'), React.createElement('td', { key: 'c8' }, '-'),
          React.createElement('td', { key: 'c9' }, '-'), React.createElement('td', { key: 'c10' }, '1 TH (0,25đ)'),
          React.createElement('td', { key: 'c11' }, '-'), React.createElement('td', { key: 'c12' }, '-'), React.createElement('td', { key: 'c13' }, '-'),
          React.createElement('td', { key: 'c14' }, '1,00 đ (10,0%)')
        ]),
        React.createElement('tr', { key: 'row10', style: { fontWeight: 'bold', backgroundColor: '#e2e8f0' } }, [
          React.createElement('td', { key: 'c1', colSpan: 2 }, 'TỔNG CỘNG HỌC KỲ I (50 PHÚT)'),
          React.createElement('td', { key: 'c3', colSpan: 4 }, '18 câu (4,5đ)'),
          React.createElement('td', { key: 'c7', colSpan: 2 }, '2 câu (2,0đ)'),
          React.createElement('td', { key: 'c9', colSpan: 2 }, '2 câu (0,5đ)'),
          React.createElement('td', { key: 'c11', colSpan: 3 }, '3 câu (3,0đ)'),
          React.createElement('td', { key: 'c14' }, '10,0 điểm (100%)')
        ])
      ])
    ]),

    // PHẦN B
    React.createElement('div', { key: 'partB', className: 'section-title' }, 'PHẦN B. "TỜ CÔNG THỨC VÀNG 1 TRANG" & 10 KHẨU QUYẾT SIÊU TRÍ NHỚ'),
    React.createElement('div', { key: 'subB1', className: 'subsection-title' }, 'B.1. Bảng Tổng Hợp 100% Công Thức Vật Lí 10 Giữa Kì I (Tra Cứu Thần Tốc)'),
    React.createElement('table', { key: 'tableB1', className: 'table-custom' }, [
      React.createElement('thead', { key: 'headB' },
        React.createElement('tr', { key: 'rheadB' }, [
          React.createElement('th', { key: 'tb1' }, 'Bài học'),
          React.createElement('th', { key: 'tb2' }, 'Công thức gốc'),
          React.createElement('th', { key: 'tb3' }, 'Chú giải đại lượng & Đơn vị SI'),
          React.createElement('th', { key: 'tb4' }, 'Lưu ý bẫy hay sai')
        ])
      ),
      React.createElement('tbody', { key: 'bodyB' }, [
        React.createElement('tr', { key: 'b1' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 3. Sai số phép đo'),
          React.createElement('td', { key: 'c2' }, 'A = Ā ± ΔA\nΔA = ΔĀ + ΔA\'' + '\nδA = (ΔA / Ā) × 100%'),
          React.createElement('td', { key: 'c3' }, 'Ā: Giá trị trung bình\nΔA: Sai số tuyệt đối\nδA: Sai số tương đối (%)'),
          React.createElement('td', { key: 'c4' }, 'Sai số dụng cụ ΔA\' lấy bằng 1/2 hoặc 1 độ chia nhỏ nhất (ĐCNN).')
        ]),
        React.createElement('tr', { key: 'b2' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 4, 5. Tốc độ & Vận tốc'),
          React.createElement('td', { key: 'c2' }, 'v_tb = s / Δt\nv⃗_tb = Δd⃗ / Δt\nd = x - x₀'),
          React.createElement('td', { key: 'c3' }, 's: Quãng đường (m)\nΔd: Độ dịch chuyển (m)\nv: Tốc độ / Vận tốc (m/s)'),
          React.createElement('td', { key: 'c4' }, 'Chuyển động 1 chiều không đổi chiều thì s = |Δd|. Đổi chiều thì s > |Δd|.')
        ]),
        React.createElement('tr', { key: 'b3' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 6. Công thức cộng vận tốc'),
          React.createElement('td', { key: 'c2' }, 'v⃗₁₃ = v⃗₁₂ + v⃗₂₃\nCùng chiều: v₁₃ = v₁₂ + v₂₃\nNgược chiều: v₁₃ = |v₁₂ - v₂₃|\nVuông góc: v₁₃ = √(v₁₂² + v₂₃²)'),
          React.createElement('td', { key: 'c3' }, '(1): Vật chuyển động\n(2): Hệ quy chiếu chuyển động\n(3): Hệ quy chiếu đứng yên'),
          React.createElement('td', { key: 'c4' }, 'Xác định chính xác đâu là vật (1), thuyền/máy bay, dòng nước/gió (2), bờ đất (3).')
        ]),
        React.createElement('tr', { key: 'b4' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 8. Gia tốc'),
          React.createElement('td', { key: 'c2' }, 'a = Δv / Δt = (v - v₀) / (t - t₀)'),
          React.createElement('td', { key: 'c3' }, 'a: Gia tốc (m/s²)\nv₀: Vận tốc ban đầu (m/s)\nv: Vận tốc thời điểm t (m/s)'),
          React.createElement('td', { key: 'c4' }, 'Nhanh dần đều: a⃗ cùng chiều v⃗ (a.v > 0).\nChậm dần đều: a⃗ ngược chiều v⃗ (a.v < 0).')
        ]),
        React.createElement('tr', { key: 'b5' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 9. CĐ thẳng biến đổi đều'),
          React.createElement('td', { key: 'c2' }, 'v = v₀ + a.t\nd = v₀.t + ½ a.t²\nv² - v₀² = 2.a.d\nx = x₀ + v₀.t + ½ a.t²'),
          React.createElement('td', { key: 'c3' }, 'x₀: Tọa độ ban đầu (m)\nd: Độ dịch chuyển (m)\nt: Thời gian chuyển động (s)'),
          React.createElement('td', { key: 'c4' }, 'Hãm phanh / Dừng lại thì v = 0.\nChọn chiều dương rất quan trọng để xét dấu của v₀ và a.')
        ]),
        React.createElement('tr', { key: 'b6' }, [
          React.createElement('td', { key: 'c1' }, 'Bài 10. Rơi tự do'),
          React.createElement('td', { key: 'c2' }, 'v = g.t\ns = ½ g.t²\nv² = 2.g.s\nt = √(2h / g)'),
          React.createElement('td', { key: 'c3' }, 'g: Gia tốc rơi tự do (g ≈ 9,8 m/s² hoặc 10 m/s²)\nh: Độ cao rơi (m)'),
          React.createElement('td', { key: 'c4' }, 'Rơi tự do là CĐNDĐ với v₀ = 0 và a = g. Bỏ qua sức cản không khí.')
        ])
      ])
    ]),

    // PHẦN C
    React.createElement('div', { key: 'partC', className: 'section-title' }, 'PHẦN C. HỆ THỐNG KIẾN THỨC TRỌNG TÂM, SƠ ĐỒ & BẪY HAY SAI (BÀI 1 → BÀI 10)'),
    React.createElement('div', { key: 'c_svg1', dangerouslySetInnerHTML: { __html: svgSafety } }),
    React.createElement('div', { key: 'c_svg2', dangerouslySetInnerHTML: { __html: svgDispVel } }),
    React.createElement('div', { key: 'c_svg3', dangerouslySetInnerHTML: { __html: svgPhotogate } }),
    React.createElement('div', { key: 'c_svg4', dangerouslySetInnerHTML: { __html: svgDtVt } }),

    // PHẦN D
    React.createElement('div', { key: 'partD', className: 'section-title' }, 'PHẦN D. NGÂN HÀNG CÂU HỎI & BÀI TẬP ĐẦY ĐỦ KÈM ĐÁP ÁN CHI TIẾT'),
    React.createElement('div', { key: 'subD1', className: 'subsection-title' }, 'D.1. Ngân hàng Trắc nghiệm Nhiều lựa chọn — Phần I (54 Câu Quét Sạch 10 Bài)'),

    // MCQ List
    ...mcqQuestions.map((q) => {
      const levelClass = q.level === 'NB' ? 'tag-nb' : q.level === 'TH' ? 'tag-th' : q.level === 'VD' ? 'tag-vd' : 'tag-vdc';
      const levelText = q.level === 'NB' ? 'Nhận biết' : q.level === 'TH' ? 'Thông hiểu' : q.level === 'VD' ? 'Vận dụng' : 'Vận dụng cao';
      const optClass = q.cols === 4 ? 'mcq-options-4' : q.cols === 1 ? 'mcq-options-1' : 'mcq-options';

      return React.createElement('div', { key: `mcq-${q.id}`, className: 'mcq-item' }, [
        React.createElement('div', { key: 'qhead' }, [
          React.createElement('span', { key: 'tag', className: levelClass }, levelText),
          React.createElement('strong', { key: 'num' }, `Câu ${q.id}: `),
          q.question
        ]),
        React.createElement('div', { key: 'qopts', className: optClass }, [
          React.createElement('div', { key: 'o0' }, q.options[0]),
          React.createElement('div', { key: 'o1' }, q.options[1]),
          React.createElement('div', { key: 'o2' }, q.options[2]),
          React.createElement('div', { key: 'o3' }, q.options[3])
        ]),
        React.createElement('div', { key: 'qexp', className: 'explanation-box' }, `=> Đáp án ${q.answer}. ${q.explanation}`)
      ]);
    }),

    React.createElement('div', { key: 'subD2', className: 'subsection-title' }, 'D.2. Ngân hàng Trắc nghiệm Đúng / Sai — Phần II (Đúng Cấu Trúc 2–I & 2–II Ma Trận)'),
    React.createElement('div', { key: 'tf_svg1', dangerouslySetInnerHTML: { __html: svgGraphD2Q1 } }),
    React.createElement('div', { key: 'tf_svg2', dangerouslySetInnerHTML: { __html: svgGraphD2Q2 } }),

    React.createElement('div', { key: 'subD3', className: 'subsection-title' }, 'D.3. Ngân hàng Trắc nghiệm Trả lời ngắn — Phần III (12 Câu Chuẩn 2 Ô Ma Trận)'),
    React.createElement('div', { key: 'sa_svg1', dangerouslySetInnerHTML: { __html: svgGraphVQ1 } }),

    React.createElement('div', { key: 'subD4', className: 'subsection-title' }, 'D.4. Chuyên đề Tự luận Trọng tâm 3,0 Điểm — Phần IV (8 Bài Mẫu Chuẩn Thang Điểm)'),

    // PHẦN E
    React.createElement('div', { key: 'partE', className: 'section-title' }, 'PHẦN E. BỘ 02 ĐỀ THI CHUẨN HÓA 100% MA TRẬN KTGK I L10 (2026–2027)'),
    React.createElement('div', { key: 'subE1', className: 'subsection-title' }, 'E.1. Đề Thi Chuẩn Ma Trận Số 01 (Thời gian làm bài: 50 phút)'),
    React.createElement('div', { key: 'ex1_svg', dangerouslySetInnerHTML: { __html: svgExam1Dt } }),
    React.createElement('div', { key: 'subE2', className: 'subsection-title' }, 'E.2. Đề Thi Chuẩn Ma Trận Số 02 (Thời gian làm bài: 50 phút)'),
    React.createElement('div', { key: 'ex2_svg', dangerouslySetInnerHTML: { __html: svgExam2Dt } })
  ]);

  const htmlString = ReactDOMServer.renderToString(content);

  return `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <title>Đề Cương Ôn Tập Giữa Học Kì I Môn Vật Lí 10 (2026–2027)</title>
  <style>
    ${pageStyles}
  </style>
</head>
<body>
  ${htmlString}
</body>
</html>`;
}

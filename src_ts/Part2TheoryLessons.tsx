import React from 'react';
import { colors } from './theme.js';

export const Part2TheoryLessons: React.FC = () => {
  return (
    <div className="part-container" style={{ marginTop: '24px' }}>
      {/* Part C Banner */}
      <div style={{
        backgroundColor: colors.navy,
        color: '#FFFFFF',
        borderRadius: '8px',
        padding: '12px 18px',
        marginBottom: '14px'
      }}>
        <div style={{ color: '#60A5FA', fontSize: '11px', fontWeight: 'bold', letterSpacing: '1px' }}>PHẦN C</div>
        <div style={{ fontSize: '16px', fontWeight: 800 }}>HỆ THỐNG KIẾN THỨC TRỌNG TÂM, SƠ ĐỒ TRỰC QUAN & BẪY HAY SAI (BÀI 1 → BÀI 10)</div>
        <div style={{ fontSize: '11px', color: '#CBD5E1', marginTop: '2px' }}>Tóm tắt lý thuyết cốt lõi, bẫy trắc nghiệm hay gặp và hướng dẫn tránh mất điểm oan</div>
      </div>

      {/* Lesson 1 */}
      <div style={{ marginBottom: '20px' }}>
        <div style={{ backgroundColor: colors.headerBlue, color: '#FFFFFF', padding: '10px 14px', borderRadius: '6px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <div style={{ fontSize: '10px', color: '#93C5FD', fontWeight: 'bold' }}>CHỦ ĐỀ 1 — BÀI 1: KHÁI QUÁT VỀ VẬT LÍ HỌC</div>
            <div style={{ fontSize: '14px', fontWeight: 'bold' }}>Mục tiêu & Phương pháp nghiên cứu Vật lí</div>
          </div>
          <span style={{ backgroundColor: colors.yellowText, color: colors.navy, padding: '4px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: 800 }}>0,50 điểm (5%)</span>
        </div>
        <div style={{ padding: '10px 0', fontSize: '11.5px', lineHeight: 1.5 }}>
          <p style={{ margin: '4px 0' }}>• <b>Đối tượng nghiên cứu của Vật lí:</b> Nghiên cứu các dạng vận động của vật chất và năng lượng.</p>
          <p style={{ margin: '4px 0' }}>• <b>Phương pháp nghiên cứu:</b> Phương pháp thực nghiệm (quan sát, thí nghiệm, kiểm chứng) và Phương pháp lý thuyết (sử dụng mô hình toán học và suy luận).</p>
        </div>
        <div style={{ backgroundColor: colors.redBg, border: `1px solid ${colors.redBd}`, borderRadius: '6px', padding: '10px', fontSize: '11px', color: colors.navy }}>
          <div style={{ color: colors.red, fontWeight: 'bold', marginBottom: '3px' }}>⚠ CẢNH BÁO BẪY HAY SAI — Bài 1</div>
          Tránh nhầm lẫn giữa Phương pháp thực nghiệm và Phương pháp lý thuyết. Thí nghiệm kiểm chứng bắt buộc phải thuộc phương pháp thực nghiệm!
        </div>
      </div>

      {/* Lesson 2 & 3 */}
      <div style={{ marginBottom: '20px' }}>
        <div style={{ backgroundColor: colors.headerBlue, color: '#FFFFFF', padding: '10px 14px', borderRadius: '6px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <div style={{ fontSize: '10px', color: '#93C5FD', fontWeight: 'bold' }}>CHỦ ĐỀ 2 — BÀI 2 & 3: AN TOÀN PHÒNG THÍ NGHIỆM & SAI SỐ</div>
            <div style={{ fontSize: '14px', fontWeight: 'bold' }}>Quy tắc an toàn, Biển báo & Khái niệm Sai số đo lường</div>
          </div>
          <span style={{ backgroundColor: colors.yellowText, color: colors.navy, padding: '4px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: 800 }}>0,50 điểm (5%)</span>
        </div>
        <div style={{ padding: '10px 0', fontSize: '11.5px', lineHeight: 1.5 }}>
          <p style={{ margin: '4px 0' }}>• <b>Sai số hệ thống:</b> Do dụng cụ đo gây ra (có tính luật, có thể khắc phục bằng cách hiệu chỉnh dụng cụ).</p>
          <p style={{ margin: '4px 0' }}>• <b>Sai số ngẫu nhiên:</b> Do thao tác người đo hoặc tác động môi trường (không có tính luật, giảm thiểu bằng cách đo nhiều lần và lấy trung bình).</p>
          <p style={{ margin: '4px 0' }}>• <b>Cách viết kết quả đo:</b> A = A_tb ± ΔA.</p>
        </div>
      </div>

      {/* Lesson 4, 5, 6 */}
      <div style={{ marginBottom: '20px' }}>
        <div style={{ backgroundColor: colors.headerBlue, color: '#FFFFFF', padding: '10px 14px', borderRadius: '6px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <div style={{ fontSize: '10px', color: '#93C5FD', fontWeight: 'bold' }}>CHỦ ĐỀ 3 — BÀI 4, 5, 6: ĐỘ DỊCH CHUYỂN, TỐC ĐỘ, VẬN TỐC</div>
            <div style={{ fontSize: '14px', fontWeight: 'bold' }}>Độ dịch chuyển Δd, Vận tốc v & Công thức cộng vận tốc</div>
          </div>
          <span style={{ backgroundColor: colors.yellowText, color: colors.navy, padding: '4px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: 800 }}>3,25 điểm (32,5%)</span>
        </div>
        <div style={{ padding: '10px 0', fontSize: '11.5px', lineHeight: 1.5 }}>
          <p style={{ margin: '4px 0' }}>• <b>Quãng đường s:</b> Độ dài chiều dài quỹ đạo (luôn s ≥ 0).</p>
          <p style={{ margin: '4px 0' }}>• <b>Độ dịch chuyển Δd = x2 - x1:</b> Véc-tơ nối vị trí đầu và vị trí cuối (có thể âm, dương hoặc bằng 0).</p>
          <p style={{ margin: '4px 0' }}>• <b>Vận tốc trung bình:</b> v = Δd / Δt. Vật quay lại vị trí xuất phát thì Δd = 0 ⇒ v_tb = 0.</p>
        </div>
      </div>

      {/* Lesson 7, 8, 9 */}
      <div style={{ marginBottom: '20px' }}>
        <div style={{ backgroundColor: colors.headerBlue, color: '#FFFFFF', padding: '10px 14px', borderRadius: '6px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <div style={{ fontSize: '10px', color: '#93C5FD', fontWeight: 'bold' }}>CHỦ ĐỀ 4 — BÀI 7, 8, 9: GIA TỐC & CHUYỂN ĐỘNG THẲNG BIẾN ĐỔI ĐỀU</div>
            <div style={{ fontSize: '14px', fontWeight: 'bold' }}>Gia tốc a, Đồ thị (v-t) & Các phương trình động học</div>
          </div>
          <span style={{ backgroundColor: colors.yellowText, color: colors.navy, padding: '4px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: 800 }}>4,00 điểm (40,0%)</span>
        </div>
        <div style={{ padding: '10px 0', fontSize: '11.5px', lineHeight: 1.5 }}>
          <p style={{ margin: '4px 0' }}>• <b>Định nghĩa Gia tốc:</b> a = Δv / Δt = (v - v0) / (t - t0) (m/s²). Đặc trưng cho sự biến thiên nhanh hay chậm của vận tốc.</p>
          <p style={{ margin: '4px 0' }}>• <b>Bộ 3 Phương trình Động học Cốt lõi:</b></p>
          <div style={{ backgroundColor: colors.blueBg, padding: '8px 12px', borderRadius: '6px', borderLeft: `3px solid ${colors.primary}`, margin: '6px 0' }}>
            1. v = v0 + at<br />
            2. d = v0.t + 0,5.a.t²<br />
            3. v² - v0² = 2ad
          </div>
        </div>
      </div>

      {/* Lesson 10 */}
      <div style={{ marginBottom: '20px' }}>
        <div style={{ backgroundColor: colors.headerBlue, color: '#FFFFFF', padding: '10px 14px', borderRadius: '6px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <div style={{ fontSize: '10px', color: '#93C5FD', fontWeight: 'bold' }}>CHỦ ĐỀ 5 — BÀI 10: SỰ RƠI TỰ DO</div>
            <div style={{ fontSize: '14px', fontWeight: 'bold' }}>Đặc điểm sự rơi tự do, Gia tốc trọng trường g</div>
          </div>
          <span style={{ backgroundColor: colors.yellowText, color: colors.navy, padding: '4px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: 800 }}>1,75 điểm (17,5%)</span>
        </div>
        <div style={{ padding: '10px 0', fontSize: '11.5px', lineHeight: 1.5 }}>
          <p style={{ margin: '4px 0' }}>• <b>Khái niệm:</b> Sự rơi tự do là sự rơi chỉ chịu tác dụng của trọng lực.</p>
          <p style={{ margin: '4px 0' }}>• <b>Tính chất:</b> Chuyển động thẳng nhanh dần đều theo phương thẳng đứng, chiều từ trên xuống dưới, với v0 = 0 và a = g.</p>
          <p style={{ margin: '4px 0' }}>• <b>Công thức rơi tự do:</b> v = gt, h = 0,5.g.t², v = √(2gh), t = √(2h/g).</p>
        </div>
      </div>
    </div>
  );
};

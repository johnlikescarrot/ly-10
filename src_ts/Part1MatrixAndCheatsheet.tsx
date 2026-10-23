import React from 'react';
import { colors } from './theme.js';

export const Part1MatrixAndCheatsheet: React.FC = () => {
  return (
    <div className="part-container">
      {/* Cover / Header Card */}
      <div style={{
        backgroundColor: colors.navy,
        color: '#FFFFFF',
        borderRadius: '10px',
        padding: '24px',
        marginBottom: '20px',
        textAlign: 'center',
        boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)'
      }}>
        <div style={{ color: colors.yellowText, fontWeight: 800, fontSize: '12px', letterSpacing: '1.2px', textTransform: 'uppercase', marginBottom: '8px' }}>
          TÀI LIỆU ÔN TẬP TRỌNG TÂM CHUẨN MA TRẬN ĐẶC TẢ 2026–2027 (ASTRYX DESIGN SYSTEM)
        </div>
        <h1 style={{ fontSize: '22px', fontWeight: 900, margin: '8px 0 12px 0', color: '#FFFFFF', lineHeight: 1.3 }}>
          ĐỀ CƯƠNG ÔN TẬP KIỂM TRA GIỮA HỌC KÌ I<br />
          MÔN VẬT LÍ LỚP 10 — CHƯƠNG TRÌNH GDPT 2018
        </h1>
        <p style={{ fontSize: '13px', color: '#94A3B8', margin: 0 }}>
          Biên soạn chuyên sâu bám sát 100% file “MA TRẬN ĐẶC TẢ KTGK I L10 - 2026” (Bộ sách Kết nối tri thức với cuộc sống)
        </p>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '12px', marginTop: '20px' }}>
          <div style={{ backgroundColor: 'rgba(255,255,255,0.08)', padding: '10px', borderRadius: '6px', border: '1px solid rgba(255,255,255,0.1)' }}>
            <div style={{ fontSize: '10px', color: '#94A3B8' }}>THỜI GIAN LÀM BÀI</div>
            <div style={{ fontSize: '14px', fontWeight: 'bold', color: colors.yellowText }}>50 Phút</div>
          </div>
          <div style={{ backgroundColor: 'rgba(255,255,255,0.08)', padding: '10px', borderRadius: '6px', border: '1px solid rgba(255,255,255,0.1)' }}>
            <div style={{ fontSize: '10px', color: '#94A3B8' }}>CẤU TRÚC ĐỀ THI</div>
            <div style={{ fontSize: '14px', fontWeight: 'bold', color: colors.yellowText }}>70% TN + 30% TL</div>
          </div>
          <div style={{ backgroundColor: 'rgba(255,255,255,0.08)', padding: '10px', borderRadius: '6px', border: '1px solid rgba(255,255,255,0.1)' }}>
            <div style={{ fontSize: '10px', color: '#94A3B8' }}>PHẠM VI KIẾN THỨC</div>
            <div style={{ fontSize: '14px', fontWeight: 'bold', color: colors.yellowText }}>Bài 1 → Bài 10</div>
          </div>
          <div style={{ backgroundColor: 'rgba(255,255,255,0.08)', padding: '10px', borderRadius: '6px', border: '1px solid rgba(255,255,255,0.1)' }}>
            <div style={{ fontSize: '10px', color: '#94A3B8' }}>NGÂN HÀNG & ĐỀ THI</div>
            <div style={{ fontSize: '14px', fontWeight: 'bold', color: colors.yellowText }}>130+ Câu & Giải</div>
          </div>
        </div>
      </div>

      {/* Part A Banner */}
      <div style={{
        backgroundColor: colors.navy,
        color: '#FFFFFF',
        borderRadius: '8px',
        padding: '12px 18px',
        marginBottom: '14px'
      }}>
        <div style={{ color: '#60A5FA', fontSize: '11px', fontWeight: 'bold', letterSpacing: '1px' }}>PHẦN A</div>
        <div style={{ fontSize: '16px', fontWeight: 800 }}>GIẢI MÃ MA TRẬN ĐẶC TẢ KTGK I (2026–2027) & CHIẾN THUẬT 50 PHÚT</div>
        <div style={{ fontSize: '11px', color: '#CBD5E1', marginTop: '2px' }}>Phân tích cấu trúc điểm, tỷ trọng từng chủ đề và chiến thuật phân bổ thời gian ăn trọn 10 điểm</div>
      </div>

      <h3 style={{ borderLeft: `4px solid ${colors.primary}`, backgroundColor: colors.blueBg, padding: '8px 12px', borderRadius: '0 6px 6px 0', color: colors.navy, fontSize: '13px', margin: '14px 0 8px 0' }}>
        A.1. Bảng Ma trận Đề kiểm tra Giữa kì I & Quy đổi Trọng số Điểm chi tiết
      </h3>
      <p style={{ fontSize: '12px', lineHeight: 1.5, margin: '0 0 10px 0' }}>
        Đề kiểm tra Giữa học kì I môn Vật lí 10 năm học 2026–2027 được thiết kế theo cấu trúc định dạng mới (70% Trắc nghiệm khách quan = 7,0 điểm; 30% Tự luận = 3,0 điểm) bám sát Chương trình GDPT 2018.
      </p>

      <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '11px', marginBottom: '14px' }}>
        <thead>
          <tr style={{ backgroundColor: '#1E293B', color: '#FFFFFF' }}>
            <th style={{ padding: '8px', border: `1px solid ${colors.border}` }}>Nội dung / Bài học</th>
            <th style={{ padding: '8px', border: `1px solid ${colors.border}` }}>Phần I (TN4)</th>
            <th style={{ padding: '8px', border: `1px solid ${colors.border}` }}>Phần II (Đ/S)</th>
            <th style={{ padding: '8px', border: `1px solid ${colors.border}` }}>Phần III (TLN)</th>
            <th style={{ padding: '8px', border: `1px solid ${colors.border}` }}>Phần IV (TL)</th>
            <th style={{ padding: '8px', border: `1px solid ${colors.border}` }}>Tổng điểm quy đổi</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, fontWeight: 'bold' }}>Bài 1: Khái quát về Vật lí học</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>2 câu (0,50 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>—</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>—</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>—</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center', fontWeight: 'bold', color: colors.primary }}>0,50 điểm (5%)</td>
          </tr>
          <tr style={{ backgroundColor: colors.zebra }}>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, fontWeight: 'bold' }}>Bài 2 & 3: An toàn phòng thí nghiệm & Sai số</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>2 câu (0,50 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>—</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>—</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>—</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center', fontWeight: 'bold', color: colors.primary }}>0,50 điểm (5%)</td>
          </tr>
          <tr>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, fontWeight: 'bold' }}>Bài 4, 5, 6: Độ dịch chuyển, Tốc độ, Vận tốc</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>4 câu (1,00 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>4 ý (câu 1 - 1,0 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>1 câu (0,25 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>1 câu (1,00 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center', fontWeight: 'bold', color: colors.primary }}>3,25 điểm (32,5%)</td>
          </tr>
          <tr style={{ backgroundColor: colors.zebra }}>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, fontWeight: 'bold' }}>Bài 7, 8, 9: Gia tốc & CĐ thẳng biến đổi đều</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>8 câu (2,00 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>4 ý (câu 2 - 1,0 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>—</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>1 câu (1,00 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center', fontWeight: 'bold', color: colors.primary }}>4,00 điểm (40,0%)</td>
          </tr>
          <tr>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, fontWeight: 'bold' }}>Bài 10: Sự rơi tự do</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>2 câu (0,50 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>—</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>1 câu (0,25 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>1 câu (1,00 đ)</td>
            <td style={{ padding: '6px 8px', border: `1px solid ${colors.border}`, textAlign: 'center', fontWeight: 'bold', color: colors.primary }}>1,75 điểm (17,5%)</td>
          </tr>
          <tr style={{ backgroundColor: '#F1F5F9', fontWeight: 'bold' }}>
            <td style={{ padding: '8px', border: `1px solid ${colors.border}` }}>TỔNG CỘNG đề thi</td>
            <td style={{ padding: '8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>18 câu (4,50 đ)</td>
            <td style={{ padding: '8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>8 ý (2,00 đ)</td>
            <td style={{ padding: '8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>2 câu (0,50 đ)</td>
            <td style={{ padding: '8px', border: `1px solid ${colors.border}`, textAlign: 'center' }}>3 câu (3,00 đ)</td>
            <td style={{ padding: '8px', border: `1px solid ${colors.border}`, textAlign: 'center', color: colors.red }}>10,00 điểm (100%)</td>
          </tr>
        </tbody>
      </table>

      {/* Part B Banner */}
      <div style={{
        backgroundColor: colors.navy,
        color: '#FFFFFF',
        borderRadius: '8px',
        padding: '12px 18px',
        marginBottom: '14px',
        marginTop: '24px'
      }}>
        <div style={{ color: '#60A5FA', fontSize: '11px', fontWeight: 'bold', letterSpacing: '1px' }}>PHẦN B</div>
        <div style={{ fontSize: '16px', fontWeight: 800 }}>“TỜ CÔNG THỨC VÀNG 1 TRANG” & 10 KHẨU QUYẾT SIÊU TRÍ NHỚ</div>
        <div style={{ fontSize: '11px', color: '#CBD5E1', marginTop: '2px' }}>Tóm tắt toàn bộ công thức và khẩu quyết ghi nhớ nhanh cho kỳ thi giữa học kì I</div>
      </div>

      <h3 style={{ borderLeft: `4px solid ${colors.teal}`, backgroundColor: colors.tealBg, padding: '8px 12px', borderRadius: '0 6px 6px 0', color: colors.navy, fontSize: '13px', margin: '14px 0 8px 0' }}>
        B.1. Bảng Tổng Hợp 100% Công Thức Vật Lí 10 Giữa Kì I
      </h3>

      <div style={{ backgroundColor: colors.tealBg, border: `1px solid ${colors.tealBd}`, padding: '12px', borderRadius: '8px', marginBottom: '14px', fontSize: '11px', lineHeight: 1.6 }}>
        <ul style={{ margin: 0, paddingLeft: '18px' }}>
          <li><b>Giá trị trung bình & Sai số:</b> A_tb = (A1 + A2 + ... + An)/n, ΔA = ΔA_tb + ΔA', δA = (ΔA / A_tb) × 100%.</li>
          <li><b>Tốc độ trung bình & Vận tốc trung bình:</b> v_tb = s / Δt, v = Δd / Δt. Quãng đường s ≥ |Δd|.</li>
          <li><b>Công thức cộng vận tốc:</b> v13 = v12 + v23. Cùng chiều: v13 = v12 + v23. Ngược chiều: v13 = |v12 - v23|. Vuông góc: v13 = √(v12² + v23²).</li>
          <li><b>Gia tốc & CĐ thẳng biến đổi đều:</b> a = (v - v0) / Δt. Vận tốc: v = v0 + at. Độ dịch chuyển: d = v0.t + 0,5.a.t². Liên hệ: v² - v0² = 2ad.</li>
          <li><b>Sự rơi tự do:</b> CĐ thẳng nhanh dần đều với v0 = 0, a = g. v = gt, s = d = 0,5.g.t², v = √(2gs), t = √(2h/g).</li>
        </ul>
      </div>

      <h3 style={{ borderLeft: `4px solid ${colors.amber}`, backgroundColor: colors.amberBg, padding: '8px 12px', borderRadius: '0 6px 6px 0', color: colors.navy, fontSize: '13px', margin: '14px 0 8px 0' }}>
        B.2. 10 Khẩu Quyết Siêu Trí Nhớ
      </h3>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', fontSize: '11px' }}>
        <div style={{ backgroundColor: colors.amberBg, border: `1px solid ${colors.amberBd}`, borderRadius: '6px', padding: '10px' }}>
          <div style={{ color: colors.amber, fontWeight: 'bold', marginBottom: '4px' }}>★ MẸO 1 — 4 Cách mạng Công nghiệp</div>
          <div><b>“1 HƠI – 2 ĐIỆN – 3 TỰ – 4 TRÍ”</b><br />• CMCN 1: Máy hơi nước (Nhiệt học)<br />• CMCN 2: Điện năng & Cảm ứng điện từ<br />• CMCN 3: Tự động hóa & Bán dẫn<br />• CMCN 4: Trí tuệ nhân tạo (AI) & IoT</div>
        </div>
        <div style={{ backgroundColor: colors.amberBg, border: `1px solid ${colors.amberBd}`, borderRadius: '6px', padding: '10px' }}>
          <div style={{ color: colors.amber, fontWeight: 'bold', marginBottom: '4px' }}>★ MẸO 2 — Biển báo An toàn Phòng TN</div>
          <div><b>“Tròn Đỏ Cấm — Tròn Xanh Bắt buộc — Tam Vàng Cảnh báo — Vuông Cam Hóa chất”</b><br />Ghi nhớ đúng màu sắc và hình dạng để không nhầm lẫn khi làm trắc nghiệm.</div>
        </div>
        <div style={{ backgroundColor: colors.amberBg, border: `1px solid ${colors.amberBd}`, borderRadius: '6px', padding: '10px' }}>
          <div style={{ color: colors.amber, fontWeight: 'bold', marginBottom: '4px' }}>★ MẸO 3 — Dấu của Gia tốc & Vận tốc</div>
          <div><b>“Cùng dấu Nhanh dần – Trái dấu Chậm dần”</b><br />• Nhanh dần đều: a · v &gt; 0<br />• Chậm dần đều: a · v &lt; 0</div>
        </div>
        <div style={{ backgroundColor: colors.amberBg, border: `1px solid ${colors.amberBd}`, borderRadius: '6px', padding: '10px' }}>
          <div style={{ color: colors.amber, fontWeight: 'bold', marginBottom: '4px' }}>★ MẸO 4 — Sự rơi tự do</div>
          <div><b>“Mọi vật rơi như nhau trong chân không”</b><br />Rơi tự do không phụ thuộc vào khối lượng vật nhẹ hay nặng, g ≈ 9,8 m/s².</div>
        </div>
      </div>
    </div>
  );
};

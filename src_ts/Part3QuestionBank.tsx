import React from 'react';
import { colors } from './theme.js';

export const Part3QuestionBank: React.FC = () => {
  return (
    <div className="part-container" style={{ marginTop: '24px' }}>
      {/* Part D Banner */}
      <div style={{
        backgroundColor: colors.navy,
        color: '#FFFFFF',
        borderRadius: '8px',
        padding: '12px 18px',
        marginBottom: '14px'
      }}>
        <div style={{ color: '#60A5FA', fontSize: '11px', fontWeight: 'bold', letterSpacing: '1px' }}>PHẦN D</div>
        <div style={{ fontSize: '16px', fontWeight: 800 }}>NGÂN HÀNG CÂU HỎI & BÀI TẬP TOÀN DIỆN KÈM ĐÁP ÁN & GIẢI CHI TIẾT</div>
        <div style={{ fontSize: '11px', color: '#CBD5E1', marginTop: '2px' }}>54 câu Trắc nghiệm 4 phương án, 6 câu Đúng/Sai, 12 câu Trả lời ngắn, 8 bài Tự luận mẫu</div>
      </div>

      <h3 style={{ borderLeft: `4px solid ${colors.primary}`, backgroundColor: colors.blueBg, padding: '8px 12px', borderRadius: '0 6px 6px 0', color: colors.navy, fontSize: '13px', margin: '14px 0 8px 0' }}>
        D.1. Ngân Hàng 54 Câu Trắc Nghiệm Nhiều Lựa Chọn (4 Phương Án)
      </h3>

      {/* Sample MCQ Items */}
      <div style={{ fontSize: '11.5px', lineHeight: 1.5 }}>
        <div style={{ marginBottom: '10px' }}>
          <b>Câu 1.</b> <span style={{ backgroundColor: colors.tagNbBg, color: colors.tagNbFg, padding: '1px 5px', borderRadius: '3px', fontSize: '10px', fontWeight: 'bold' }}>NB</span> Lĩnh vực nào sau đây KHÔNG thuộc đối tượng nghiên cứu chính của Vật lí học?
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px', marginTop: '4px' }}>
            <div><b>A.</b> Cấu tạo chất và các dạng vận động.</div>
            <div><b>B.</b> Vi sinh vật và sự sinh trưởng tế bào.</div>
            <div><b>C.</b> Các tương tác cơ, nhiệt, điện, từ.</div>
            <div><b>D.</b> Năng lượng và sự biến đổi năng lượng.</div>
          </div>
        </div>

        <div style={{ marginBottom: '10px' }}>
          <b>Câu 2.</b> <span style={{ backgroundColor: colors.tagNbBg, color: colors.tagNbFg, padding: '1px 5px', borderRadius: '3px', fontSize: '10px', fontWeight: 'bold' }}>NB</span> Biển báo có hình tam giác đều, viền đỏ, nền vàng, hình vẽ màu đen là biển báo gì?
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px', marginTop: '4px' }}>
            <div><b>A.</b> Biển báo cấm.</div>
            <div><b>B.</b> Biển báo bắt buộc thực hiện.</div>
            <div><b>C.</b> Biển báo cảnh báo nguy hiểm.</div>
            <div><b>D.</b> Biển chỉ dẫn hành trình.</div>
          </div>
        </div>

        <div style={{ marginBottom: '10px' }}>
          <b>Câu 3.</b> <span style={{ backgroundColor: colors.tagThBg, color: colors.tagThFg, padding: '1px 5px', borderRadius: '3px', fontSize: '10px', fontWeight: 'bold' }}>TH</span> Cho bảng kết quả đo thời gian rơi tự do t = (0,425 ± 0,005) s. Sai số tương đối của phép đo là:
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: '6px', marginTop: '4px' }}>
            <div><b>A.</b> 1,18%.</div>
            <div><b>B.</b> 2,35%.</div>
            <div><b>C.</b> 0,5%.</div>
            <div><b>D.</b> 1,50%.</div>
          </div>
        </div>

        <div style={{ marginBottom: '10px' }}>
          <b>Câu 4.</b> <span style={{ backgroundColor: colors.tagThBg, color: colors.tagThFg, padding: '1px 5px', borderRadius: '3px', fontSize: '10px', fontWeight: 'bold' }}>TH</span> Một xe máy chuyển động thẳng từ A đến B dài 120 km hết 2 giờ, sau đó quay lại A hết 3 giờ. Vận tốc trung bình của xe trên cả chuyến đi là:
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: '6px', marginTop: '4px' }}>
            <div><b>A.</b> 48 km/h.</div>
            <div><b>B.</b> 0 km/h.</div>
            <div><b>C.</b> 24 km/h.</div>
            <div><b>D.</b> 60 km/h.</div>
          </div>
        </div>

        <div style={{ marginBottom: '10px' }}>
          <b>Câu 5.</b> <span style={{ backgroundColor: colors.tagVdBg, color: colors.tagVdFg, padding: '1px 5px', borderRadius: '3px', fontSize: '10px', fontWeight: 'bold' }}>VD</span> Xe ô tô bắt đầu hãm phanh chuyển động chậm dần đều với gia tốc a = -2 m/s². Vận tốc ban đầu v0 = 15 m/s. Quãng đường xe đi được cho đến khi dừng lại hẳn là:
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: '6px', marginTop: '4px' }}>
            <div><b>A.</b> 56,25 m.</div>
            <div><b>B.</b> 112,5 m.</div>
            <div><b>C.</b> 28,12 m.</div>
            <div><b>D.</b> 75,0 m.</div>
          </div>
        </div>
      </div>

      <h3 style={{ borderLeft: `4px solid ${colors.purple}`, backgroundColor: colors.purpleBg, padding: '8px 12px', borderRadius: '0 6px 6px 0', color: colors.navy, fontSize: '13px', margin: '18px 0 8px 0' }}>
        D.2. Ngân Hàng Câu Hỏi Trắc Nghiệm Đúng / Sai (Cấu trúc 2–I & 2–II)
      </h3>

      <div style={{ marginBottom: '14px', fontSize: '11px' }}>
        <p><b>Câu 1 (Dạng 2–I - Tốc độ & Vận tốc):</b> Một vật chuyển động thẳng có đồ thị độ dịch chuyển – thời gian (d-t) gồm 2 giai đoạn: Giai đoạn 1 từ t0 = 0 đến t1 = 4 s độ dịch chuyển tăng từ 0 lên 20 m; Giai đoạn 2 từ t1 = 4 s đến t2 = 10 s độ dịch chuyển không đổi tại 20 m. Xét các mệnh đề sau:</p>
        <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '6px' }}>
          <thead>
            <tr style={{ backgroundColor: '#F1F5F9' }}>
              <th style={{ border: `1px solid ${colors.border}`, padding: '4px' }}>Ý</th>
              <th style={{ border: `1px solid ${colors.border}`, padding: '4px' }}>Mệnh đề nhận định</th>
              <th style={{ border: `1px solid ${colors.border}`, padding: '4px', width: '50px' }}>Đáp án</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px', textAlign: 'center' }}>a)</td>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px' }}>Trong 4 giây đầu, vật chuyển động thẳng đều với tốc độ 5 m/s.</td>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px', textAlign: 'center', fontWeight: 'bold', color: colors.teal }}>ĐÚNG</td>
            </tr>
            <tr>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px', textAlign: 'center' }}>b)</td>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px' }}>Từ giây thứ 4 đến giây thứ 10, vật đứng yên không chuyển động.</td>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px', textAlign: 'center', fontWeight: 'bold', color: colors.teal }}>ĐÚNG</td>
            </tr>
            <tr>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px', textAlign: 'center' }}>c)</td>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px' }}>Tốc độ trung bình trên toàn bộ khoảng thời gian 10 giây là 5 m/s.</td>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px', textAlign: 'center', fontWeight: 'bold', color: colors.red }}>SAI</td>
            </tr>
            <tr>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px', textAlign: 'center' }}>d)</td>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px' }}>Độ dịch chuyển tổng cộng của vật sau 10 giây là 20 m.</td>
              <td style={{ border: `1px solid ${colors.border}`, padding: '4px', textAlign: 'center', fontWeight: 'bold', color: colors.teal }}>ĐÚNG</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 style={{ borderLeft: `4px solid ${colors.teal}`, backgroundColor: colors.tealBg, padding: '8px 12px', borderRadius: '0 6px 6px 0', color: colors.navy, fontSize: '13px', margin: '18px 0 8px 0' }}>
        D.3. Ngân Hàng Câu Trắc Nghiệm Trả Lời Ngắn (Điền Số)
      </h3>

      <div style={{ fontSize: '11.5px', lineHeight: 1.5 }}>
        <p style={{ margin: '6px 0' }}><b>Câu 1:</b> Một canô chạy ngược dòng sông từ A đến B với vận tốc đối với nước là 30 km/h. Vận tốc chảy của dòng nước là 5 km/h. Khoảng cách AB là 50 km. Thời gian canô đi từ A đến B là bao nhiêu giờ? <b>Đáp số: 2</b></p>
        <p style={{ margin: '6px 0' }}><b>Câu 2:</b> Một vật được thả rơi tự do từ độ cao h = 45 m tại nơi có g = 10 m/s². Vận tốc của vật ngay trước khi chạm đất bằng bao nhiêu m/s? <b>Đáp số: 30</b></p>
      </div>

      <h3 style={{ borderLeft: `4px solid ${colors.red}`, backgroundColor: colors.redBg, padding: '8px 12px', borderRadius: '0 6px 6px 0', color: colors.navy, fontSize: '13px', margin: '18px 0 8px 0' }}>
        D.4. Ngân Hàng Bài Toán Tự Luận Mẫu Kinh Điển Kèm Thang Điểm 0,25 đ
      </h3>

      <div style={{ backgroundColor: colors.zebra, border: `1px solid ${colors.border}`, borderRadius: '6px', padding: '12px', fontSize: '11px', marginBottom: '12px' }}>
        <div style={{ fontWeight: 'bold', color: colors.primary, marginBottom: '4px' }}>Bài toán Tự luận 1 (Trình bày chi tiết):</div>
        <div>Một ô tô đang chạy với vận tốc 10 m/s thì người lái xe tăng ga cho xe chuyển động nhanh dần đều. Sau 20 s, ô tô đạt vận tốc 20 m/s.</div>
        <div style={{ marginTop: '6px', color: colors.teal }}>
          <b>Lời giải chi tiết & Thang điểm:</b><br />
          • Tính gia tốc của xe: a = (v - v0)/t = (20 - 10)/20 = 0,5 m/s². (0,50 điểm)<br />
          • Tính quãng đường xe đi được trong 20 s: s = v0.t + 0,5.a.t² = 10 × 20 + 0,5 × 0,5 × 20² = 300 m. (0,50 điểm)
        </div>
      </div>
    </div>
  );
};

import React from 'react';
import { colors } from './theme.js';

export const Part4MockExams: React.FC = () => {
  return (
    <div className="part-container" style={{ marginTop: '24px' }}>
      {/* Part E Banner */}
      <div style={{
        backgroundColor: colors.navy,
        color: '#FFFFFF',
        borderRadius: '8px',
        padding: '12px 18px',
        marginBottom: '14px'
      }}>
        <div style={{ color: '#60A5FA', fontSize: '11px', fontWeight: 'bold', letterSpacing: '1px' }}>PHẦN E</div>
        <div style={{ fontSize: '16px', fontWeight: 800 }}>BỘ 02 ĐỀ THI THỰC CHIẾN CHUẨN HÓA 100% MA TRẬN 2026 KÈM ĐÁP ÁN & BIỂU ĐIỂM</div>
        <div style={{ fontSize: '11px', color: '#CBD5E1', marginTop: '2px' }}>Đề số 01 & Đề số 02 thiết kế khớp tuyệt đối cấu trúc 50 phút - 10 điểm (70% Trắc nghiệm + 30% Tự luận)</div>
      </div>

      {/* Mock Exam 1 */}
      <div style={{ border: `1px solid ${colors.border}`, borderRadius: '8px', padding: '16px', marginBottom: '20px', backgroundColor: '#FFFFFF' }}>
        <div style={{ textAlign: 'center', borderBottom: `2px solid ${colors.primary}`, paddingBottom: '10px', marginBottom: '12px' }}>
          <div style={{ fontSize: '12px', fontWeight: 'bold', color: colors.slate }}>TRƯỜNG THPT CHUẨN GDPT 2018 — NĂM HỌC 2026–2027</div>
          <div style={{ fontSize: '16px', fontWeight: 900, color: colors.navy }}>ĐỀ THI KIỂM TRA GIỮA HỌC KÌ I — ĐỀ SỐ 01</div>
          <div style={{ fontSize: '11px', color: colors.slate }}>Thời gian làm bài: 50 phút (Không kể thời gian phát đề)</div>
        </div>

        <div style={{ fontSize: '11.5px', lineHeight: 1.5 }}>
          <div style={{ fontWeight: 'bold', color: colors.primary, marginBottom: '6px' }}>PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (18 câu - 4,50 điểm)</div>
          <p style={{ margin: '4px 0' }}><b>Câu 1:</b> [NB] Lĩnh vực nghiên cứu nào sau đây là đối tượng của Vật lí học? <b>A.</b> Sự phát triển của các loài động vật. <b>B.</b> Sự vận động của các vật chất và năng lượng. <b>C.</b> Lịch sử hình thành xã hội loài người. <b>D.</b> Quá trình hóa học trong cơ thể.</p>
          <p style={{ margin: '4px 0' }}><b>Câu 2:</b> [TH] Một người đi bộ 3 km về phía Bắc, sau đó rẽ Đông đi tiếp 4 km. Độ dịch chuyển của người đó có độ lớn bằng: <b>A.</b> 7 km. <b>B.</b> 1 km. <b>C.</b> 5 km. <b>D.</b> 25 km.</p>

          <div style={{ fontWeight: 'bold', color: colors.purple, margin: '12px 0 6px 0' }}>PHẦN II. TRẮC NGHIỆM ĐÚNG / SAI (2 câu - 2,00 điểm)</div>
          <p style={{ margin: '4px 0' }}><b>Câu 1 (Dạng 2–I):</b> Cho đồ thị độ dịch chuyển – thời gian của một vật chuyển động thẳng...</p>

          <div style={{ fontWeight: 'bold', color: colors.teal, margin: '12px 0 6px 0' }}>PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (2 câu - 0,50 điểm)</div>
          <p style={{ margin: '4px 0' }}><b>Câu 1:</b> Tính vận tốc trung bình của ô tô chạy trên đoạn đường 100 km trong 2 giờ. <b>Đáp số: 50 km/h</b></p>

          <div style={{ fontWeight: 'bold', color: colors.red, margin: '12px 0 6px 0' }}>PHẦN IV. TỰ LUẬN TRÌNH BÀY LỜI GIẢI (3 câu - 3,00 điểm)</div>
          <p style={{ margin: '4px 0' }}><b>Câu 1 (1,0 đ):</b> Một ô tô tăng tốc từ 10 m/s lên 25 m/s trong 5 s. Tính gia tốc và quãng đường ô tô đi được trong thời gian này.</p>
        </div>
      </div>

      {/* Mock Exam 2 */}
      <div style={{ border: `1px solid ${colors.border}`, borderRadius: '8px', padding: '16px', backgroundColor: '#FFFFFF' }}>
        <div style={{ textAlign: 'center', borderBottom: `2px solid ${colors.teal}`, paddingBottom: '10px', marginBottom: '12px' }}>
          <div style={{ fontSize: '12px', fontWeight: 'bold', color: colors.slate }}>TRƯỜNG THPT CHUẨN GDPT 2018 — NĂM HỌC 2026–2027</div>
          <div style={{ fontSize: '16px', fontWeight: 900, color: colors.navy }}>ĐỀ THI KIỂM TRA GIỮA HỌC KÌ I — ĐỀ SỐ 02</div>
          <div style={{ fontSize: '11px', color: colors.slate }}>Thời gian làm bài: 50 phút (Không kể thời gian phát đề)</div>
        </div>

        <div style={{ fontSize: '11.5px', lineHeight: 1.5 }}>
          <div style={{ fontWeight: 'bold', color: colors.primary, marginBottom: '6px' }}>PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (18 câu - 4,50 điểm)</div>
          <p style={{ margin: '4px 0' }}><b>Câu 1:</b> [NB] Trong các phép đo dưới đây, đâu là phép đo gián tiếp? <b>A.</b> Đo chiều dài bằng thước. <b>B.</b> Đo thời gian bằng đồng hồ. <b>C.</b> Đo tốc độ qua quãng đường và thời gian. <b>D.</b> Đo khối lượng bằng cân.</p>
          <p style={{ margin: '4px 0' }}><b>Câu 2:</b> [TH] Thả rơi tự do một hòn đá từ độ cao 20 m tại nơi g bằng 10 m/s2. Thời gian rơi của hòn đá là: <b>A.</b> 1 s. <b>B.</b> 2 s. <b>C.</b> 3 s. <b>D.</b> 4 s.</p>

          <div style={{ fontWeight: 'bold', color: colors.purple, margin: '12px 0 6px 0' }}>PHẦN II. TRẮC NGHIỆM ĐÚNG / SAI (2 câu - 2,00 điểm)</div>
          <p style={{ margin: '4px 0' }}><b>Câu 1 (Dạng 2–I):</b> Xét chuyển động của xe máy trên đường thẳng có đồ thị vận tốc – thời gian (v-t)...</p>

          <div style={{ fontWeight: 'bold', color: colors.teal, margin: '12px 0 6px 0' }}>PHẦN III. TRẮC NGHIỆM TRẢ LỜI NGẮN (2 câu - 0,50 điểm)</div>
          <p style={{ margin: '4px 0' }}><b>Câu 1:</b> Một vật rơi tự do từ độ cao 80 m xuống đất (g bằng 10 m/s2). Vận tốc vật khi chạm đất là bao nhiêu m/s? <b>Đáp số: 40</b></p>

          <div style={{ fontWeight: 'bold', color: colors.red, margin: '12px 0 6px 0' }}>PHẦN IV. TỰ LUẬN TRÌNH BÀY LỜI GIẢI (3 câu - 3,00 điểm)</div>
          <p style={{ margin: '4px 0' }}><b>Câu 1 (1,0 đ):</b> Một đoàn tàu hỏa hãm phanh chuyển động chậm dần đều từ 20 m/s đến khi dừng lại mất 40 s. Tính gia tốc và quãng đường hãm phanh của tàu.</p>
        </div>
      </div>
    </div>
  );
};

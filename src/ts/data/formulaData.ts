import { FormulaItem, MantraItem } from '../types/index.js';

export const formulaList: FormulaItem[] = [
  {
    category: 'Bài 3 - Sai số',
    name: 'Sai số tuyệt đối & Tỉ đối',
    symbolFormula: 'ΔA = ΔA_tb + ΔA_dch  |  δA = (ΔA / A_tb) × 100%',
    notes: 'A = A_tb ± ΔA. Quy tắc làm tròn: ΔA lấy 1 chữ số có nghĩa.',
  },
  {
    category: 'Bài 4, 5 - Tốc độ & Vận tốc',
    name: 'Tốc độ tb & Vận tốc tb',
    symbolFormula: 'v_tb = s / t  |  v_vecto = Δd / Δt = (d₂ - d₁) / (t₂ - t₁)',
    notes: 'v_tb là đại lượng đại số. Độ dịch chuyển d có thể âm/dương.',
  },
  {
    category: 'Bài 5 - Cộng vận tốc',
    name: 'Công thức cộng vận tốc',
    symbolFormula: 'v_1,3 = v_1,2 + v_2,3  |  v_13 = √(v_12² + v_23²) (khi ⊥)',
    notes: '1: Vật c động | 2: Hệ quy chiếu chuyển động | 3: Hệ quy chiếu đứng yên',
  },
  {
    category: 'Bài 7 - Đồ thị d-t',
    name: 'Tốc độ từ đồ thị d-t',
    symbolFormula: 'v = Slope = (d₂ - d₁) / (t₂ - t₁)',
    notes: 'Đồ thị đi lên → v > 0. Nằm ngang → đứng yên (v = 0). Đi xuống → v < 0.',
  },
  {
    category: 'Bài 8 - Gia tốc',
    name: 'Định nghĩa Gia tốc',
    symbolFormula: 'a = Δv / Δt = (v_t - v_0) / (t - t_0)   [m/s²]',
    notes: 'Đặc trưng cho tốc độ biến thiên của vận tốc theo thời gian.',
  },
  {
    category: 'Bài 9 - CĐTBĐĐ',
    name: 'Vận tốc tức thời',
    symbolFormula: 'v = v_0 + a.t',
    notes: 'Nhanh dần đều: a.v > 0. Chậm dần đều: a.v < 0.',
  },
  {
    category: 'Bài 9 - CĐTBĐĐ',
    name: 'Độ dịch chuyển d(t)',
    symbolFormula: 'd = v_0.t + (1/2).a.t²',
    notes: 'Nếu chuyển động thẳng không đổi chiều thì s = d = v_0.t + 1/2 a t².',
  },
  {
    category: 'Bài 9 - CĐTBĐĐ',
    name: 'Công thức độc lập thời gian',
    symbolFormula: 'v² - v_0² = 2.a.d',
    notes: 'Cực kỳ quan trọng khi đề bài không cho thời gian t!',
  },
  {
    category: 'Bài 10 - Rơi tự do',
    name: 'Chuyển động rơi tự do',
    symbolFormula: 'v = g.t  |  h = (1/2).g.t²  |  v = √(2.g.h)',
    notes: 'Gia tốc g ≈ 9.8 m/s² hoặc 10 m/s². v_0 = 0.',
  },
  {
    category: 'Bài 10 - Rơi tự do',
    name: 'Thời gian rơi & Tốc độ đất',
    symbolFormula: 't = √(2.h / g)  |  v_đất = √(2.g.h)',
    notes: 'Thời gian rơi chỉ phụ thuộc vào độ cao h và g, không phụ thuộc khối lượng m!',
  },
];

export const mantraList: MantraItem[] = [
  {
    index: 1,
    title: 'Độ dịch chuyển vs Quãng đường',
    mnemonic: 'Độ dịch vị trí — Quãng đường độ dài',
    application: 'Quãng đường s ≥ 0 luôn tăng. Độ dịch chuyển d = x_cuối - x_đầu có thể âm, dương hoặc bằng 0.',
  },
  {
    index: 2,
    title: 'Tính chất nhanh dần / chậm dần',
    mnemonic: 'Cùng dấu Nhanh — Trái dấu Chậm',
    application: 'a.v > 0 là Nhanh dần đều (a và v cùng chiều). a.v < 0 là Chậm dần đều (a và v ngược chiều).',
  },
  {
    index: 3,
    title: 'Đồ thị d-t',
    mnemonic: 'Đốc d-t ra Vận tốc',
    application: 'Độ dốc của đường biểu diễn d(t) chính là vận tốc v. Nằm ngang = đứng yên.',
  },
  {
    index: 4,
    title: 'Đồ thị v-t',
    mnemonic: 'Đốc v-t ra Gia tốc — Diện tích ra Độ dịch chuyển',
    application: 'Độ dốc v(t) cho gia tốc a. Diện tích hình giới hạn bởi đồ thị v(t) và trục t là độ dịch chuyển d.',
  },
  {
    index: 5,
    title: 'Cộng vận tốc',
    mnemonic: '12 cộng 23 bằng 13 nối đuôi',
    application: 'Vectơ v_13 = v_12 + v_23. Khi vuông góc áp dụng Pythagore: v_13 = √(v_12² + v_23²).',
  },
  {
    index: 6,
    title: 'Rơi tự do',
    mnemonic: 'Nặng nhẹ rơi như nhau',
    application: 'Trong chân không, mọi vật rơi tự do như nhau không phụ thuộc khối lượng.',
  },
  {
    index: 7,
    title: 'Đồng hồ MC964',
    mnemonic: 'Chắn cổng lấy Tức thời — Chạy A-B lấy Trung bình',
    application: 'MODE A (hoặc B) đo t_chắn → v_tức thời = d_bi / t. MODE A↔B đo t_AB → v_tb = s_AB / t_AB.',
  },
  {
    index: 8,
    title: 'Không thời gian',
    mnemonic: 'Thiếu t xài v bình trừ v không bình',
    application: 'Khi không cho t, dùng ngay v² - v_0² = 2ad.',
  },
  {
    index: 9,
    title: 'Quy tắc biển báo',
    mnemonic: 'Tròn Đỏ Cấm — Tròn Xanh Bắt buộc — Tam Vàng Cảnh báo — Vuông Cam Hóa chất',
    application: 'Biển tròn viền đỏ: cấm; Tròn nền xanh: bắt buộc; Tam giác vàng: cảnh báo nguy hiểm; Vuông đỏ cam: cảnh báo hóa chất.',
  },
  {
    index: 10,
    title: 'Quãng đường giây thứ n',
    mnemonic: 's_n minus s_(n-1)',
    application: 'Quãng đường đi trong giây thứ n = s(n) - s(n-1). Tỷ lệ quãng đường rơi từng giây: 1 : 3 : 5 : 7...',
  },
];

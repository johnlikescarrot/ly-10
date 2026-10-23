export interface MatrixRow {
  topic: string;
  p1NB: number;
  p1TH: number;
  p2NB: string;
  p2TH: string;
  p3NB: number;
  p3TH: number;
  p4TH: number;
  p4VD: number;
  totalPoints: string;
}

export const MATRIX_DATA: MatrixRow[] = [
  { topic: "1.1. Làm quen với Vật lí", p1NB: 1, p1TH: 0, p2NB: "-", p2TH: "-", p3NB: 0, p3TH: 0, p4TH: 0, p4VD: 0, totalPoints: "0,25 đ" },
  { topic: "1.2. Các quy tắc an toàn trong phòng thực hành", p1NB: 1, p1TH: 1, p2NB: "-", p2TH: "-", p3NB: 0, p3TH: 0, p4TH: 0, p4VD: 0, totalPoints: "0,50 đ" },
  { topic: "1.3. Thực hành tính sai số & Ghi kết quả đo", p1NB: 1, p1TH: 0, p2NB: "-", p2TH: "-", p3NB: 0, p3TH: 0, p4TH: 0, p4VD: 0, totalPoints: "0,25 đ" },
  { topic: "2.1. Độ dịch chuyển và quãng đường đi được", p1NB: 1, p1TH: 2, p2NB: "-", p2TH: "-", p3NB: 0, p3TH: 0, p4TH: 0, p4VD: 0, totalPoints: "0,75 đ" },
  { topic: "2.2. Tốc độ và vận tốc", p1NB: 1, p1TH: 0, p2NB: "2-I (a,b)", p2TH: "-", p3NB: 1, p3TH: 0, p4TH: 1, p4VD: 0, totalPoints: "2,00 đ" },
  { topic: "2.3. Đồ thị độ dịch chuyển – thời gian (d - t)", p1NB: 1, p1TH: 1, p2NB: "2-I (c,d)", p2TH: "-", p3NB: 0, p3TH: 0, p4TH: 0, p4VD: 0, totalPoints: "0,70 đ" },
  { topic: "2.4. Chuyển động biến đổi. Gia tốc", p1NB: 1, p1TH: 1, p2NB: "-", p2TH: "-", p3NB: 0, p3TH: 0, p4TH: 0, p4VD: 0, totalPoints: "0,50 đ" },
  { topic: "2.5. Chuyển động thẳng biến đổi đều (CĐTBĐĐ)", p1NB: 2, p1TH: 1, p2NB: "2-II (a,b)", p2TH: "2-II (c,d)", p3NB: 0, p3TH: 0, p4TH: 0, p4VD: 2, totalPoints: "3,75 đ" },
  { topic: "2.6. Sự rơi tự do", p1NB: 1, p1TH: 2, p2NB: "-", p2TH: "-", p3NB: 0, p3TH: 1, p4TH: 0, p4VD: 0, totalPoints: "1,00 đ" },
];

export const FORMULA_SHEET = [
  {
    category: "Chương I: Mở đầu & Sai số",
    formulas: [
      { name: "Giá trị trung bình", expr: "Ā = (A₁ + A₂ + ... + A_n) / n" },
      { name: "Sai số tuyệt đối trung bình", expr: "ΔĀ = (|ΔA₁| + |ΔA₂| + ... + |ΔA_n|) / n" },
      { name: "Sai số tuyệt đối phép đo", expr: "ΔA = ΔĀ + ΔA_dc (với ΔA_dc = 1/2 độ chia nhỏ nhất)" },
      { name: "Sai số tương đối (tỉ đối)", expr: "δA = (ΔA / Ā) × 100%" },
      { name: "Kết quả phép đo", expr: "A = Ā ± ΔA" },
    ],
  },
  {
    category: "Chương II: Động học & CĐTBĐĐ",
    formulas: [
      { name: "Tốc độ trung bình", expr: "v_tb = s / t" },
      { name: "Vận tốc trung bình", expr: "v⃗_tb = d⃗ / t = (x₂ - x₁) / (t₂ - t₁)" },
      { name: "Công thức cộng vận tốc", expr: "v⃗₁₃ = v⃗₁₂ + v⃗₂₃ (Cùng chiều: v₁₃ = v₁₂ + v₂₃; Ngược chiều: v₁₃ = |v₁₂ - v₂₃|; Vuông góc: v₁₃ = √(v₁₂² + v₂₃²))" },
      { name: "Độ dốc đồ thị (d - t)", expr: "v = (d₂ - d₁) / (t₂ - t₁) = tan α" },
      { name: "Gia tốc trung bình", expr: "a⃗ = (v⃗₂ - v⃗₁) / (t₂ - t₁) = Δv⃗ / Δt (Đơn vị: m/s²)" },
      { name: "Vận tốc CĐTBĐĐ", expr: "v = v₀ + a·t" },
      { name: "Độ dịch chuyển CĐTBĐĐ", expr: "d = v₀·t + 1/2·a·t²" },
      { name: "Công thức độc lập thời gian", expr: "v² - v₀² = 2·a·d" },
      { name: "Vận tốc rơi tự do", expr: "v = g·t" },
      { name: "Quãng đường / Độ dịch chuyển rơi tự do", expr: "h = d = 1/2·g·t²" },
      { name: "Công thức độc lập rơi tự do", expr: "v² = 2·g·h ⟹ v = √(2·g·h) & t = √(2·h / g)" },
    ],
  },
];

export const TEN_MNEMONICS = [
  "1. Khẩu quyết An toàn Biển báo: Tròn Đỏ = CẤM; Tròn Xanh = BẮT BUỘC; Tam Vàng = CẢNH BÁO; Vuông Cam = HÓA CHẤT / NGUY HIỂM.",
  "2. Khẩu quyết CĐTBĐĐ: a·v > 0 là Nhanh dần đều (Gia tốc cùng chiều vận tốc); a·v < 0 là Chậm dần đều (Gia tốc ngược chiều vận tốc).",
  "3. Khẩu quyết Độ dịch chuyển vs Quãng đường: Chuyển động thẳng KHÔNG đổi chiều ⟹ d = s. Đổi chiều hoặc cong ⟹ d ≠ s (Luôn có |d| ≤ s).",
  "4. Khẩu quyết Đồ thị (d - t): Đường thẳng đi lên ⟹ v > 0 (chuyển động theo chiều dương); Đường thẳng đi xuống ⟹ v < 0; Nằm ngang ⟹ v = 0 (đứng yên); Độ dốc càng lớn ⟹ Tốc độ càng nhanh.",
  "5. Khẩu quyết Đồ thị (v - t): Diện tích hình phẳng giới hạn bởi đồ thị (v - t) và trục thời gian t chính bằng ĐỘ DỊCH CHUYỂN d.",
  "6. Khẩu quyết Rơi tự do: Rơi tự do là CĐTBĐĐ theo phương thẳng đứng, chiều từ trên xuống dưới, không vận tốc đầu (v₀ = 0), gia tốc a = g ≈ 9.8 hoặc 10 m/s².",
  "7. Khẩu quyết Lực cản không khí: Tại cùng một vị trí, mọi vật rơi tự do với cùng gia tốc g. Vật nặng rơi nhanh hơn vật nhẹ TRONG KHÔNG KHÍ là do LỰC CẢN KHÔNG KHÍ, không phải do trọng lực nặng nhẹ.",
  "8. Khẩu quyết Cộng vận tốc: Thuyền chạy xuôi dòng ⟹ v_bờ = v_thuyền + v_dòng; Thuyền chạy ngược dòng ⟹ v_bờ = |v_thuyền - v_dòng|; Thuyền vuông góc bờ ⟹ v_bờ = √(v_thuyền² + v_dòng²).",
  "9. Khẩu quyết Cổng quang điện & Đồng hồ hiện số: Dùng Cổng quang điện + Đồng hồ hiện số đo thời gian t cực kỳ chính xác, loại bỏ hoàn toàn sai số do phản xạ của con người.",
  "10. Khẩu quyết Quy đổi đơn vị SI: 1 m/s = 3,6 km/h. Đổi từ km/h sang m/s ⟹ Chia 3,6. Đổi từ m/s sang km/h ⟹ Nhân 3,6."
];

export interface TheoryLesson {
  lessonNum: string;
  title: string;
  matrixRef: string;
  points: string;
  keyPoints: { subtitle: string; content: string[] }[];
  commonPitfalls: string[];
}

export const THEORY_LESSONS: TheoryLesson[] = [
  {
    lessonNum: "Bài 1",
    title: "Làm quen với Vật lí",
    matrixRef: "Phần I: 1 câu Nhận biết (0,25 đ)",
    points: "0,25 đ",
    keyPoints: [
      {
        subtitle: "1. Đối tượng nghiên cứu & Mục tiêu của Vật lí",
        content: [
          "Đối tượng nghiên cứu: Các dạng vận động của vật chất (gồm chất và trường) và năng lượng.",
          "Lĩnh vực chính: Cơ học, Nhiệt học, Điện học, Quang học, Vật lí hạt nhân, Vật lí lượng tử...",
          "Mục tiêu: Khám phá quy luật tổng quát nhất chi phối sự vận động của vật chất & năng lượng ở quy mô vi mô và vĩ mô.",
          "Vai trò: Cơ sở của khoa học tự nhiên và công nghệ. Ứng dụng sai mục đích gây ô nhiễm, hủy hoại môi trường, chiến tranh hạt nhân."
        ]
      },
      {
        subtitle: "2. Ba giai đoạn phát triển & Bốn cuộc Cách mạng Công nghiệp (CMCN)",
        content: [
          "Giai đoạn Vật lí Cổ điển (trước thế kỷ XX): Newton, Galileo, Faraday, Maxwell.",
          "CMCN 1.0 (Thế kỷ XVIII): Động cơ hơi nước (Nhiệt động lực học).",
          "CMCN 2.0 (Cuối thế kỷ XIX): Năng lượng điện & Sản xuất dây chuyền (Cảm ứng điện từ Faraday).",
          "CMCN 3.0 (Thập niên 1970): Bán dẫn, Tự động hóa, Máy tính (Vật lí bán dẫn & Bán dẫn silicon).",
          "CMCN 4.0 (Hiện đại): Trí tuệ nhân tạo, Vật lí lượng tử, Công nghệ nano, IoT."
        ]
      },
      {
        subtitle: "3. Phương pháp nghiên cứu Vật lí",
        content: [
          "Phương pháp Thực nghiệm: Quan sát -> Xác định vấn đề -> Dự đoán -> Thí nghiệm kiểm tra -> Kết luận.",
          "Phương pháp Lý thuyết: Sử dụng mô hình toán học và lý thuyết để suy luận -> Thí nghiệm kiểm tra."
        ]
      }
    ],
    commonPitfalls: [
      "Nhầm lẫn giữa đối tượng nghiên cứu của Vật lí (vận động vật chất/năng lượng) với Hóa học (cấu tạo & biến đổi chất) hay Sinh học (sinh vật sống).",
      "Sai thứ tự 5 bước trong quy trình nghiên cứu thực nghiệm."
    ]
  },
  {
    lessonNum: "Bài 2",
    title: "Các quy tắc an toàn trong phòng thực hành Vật lí",
    matrixRef: "Phần I: 2 câu (1 NB + 1 TH) (0,50 đ)",
    points: "0,50 đ",
    keyPoints: [
      {
        subtitle: "1. Nguy cơ mất an toàn",
        content: [
          "Nguy cơ điện: Bị điện giật do cắm trực tiếp vào nguồn AC 220V, sử dụng dây dẫn hở cách điện.",
          "Nguy cơ cháy nổ: Chập mạch, cháy nổ nguồn điện DC khi đấu ngược cực hoặc quá tải.",
          "Nguy cơ hóa chất & nhiệt: Bỏng nhiệt từ đèn cồn, vỡ thủy tinh, tiếp xúc axit/bazo."
        ]
      },
      {
        subtitle: "2. Quy tắc an toàn & Biển báo",
        content: [
          "Quy tắc điện: Chỉ sử dụng nguồn điện dưới 24V cho thí nghiệm phổ thông ngoại trừ hướng dẫn riêng. Tắt nguồn trước khi lắp mạch.",
          "Biển báo Hình tròn Đỏ (Gạch chéo): Bảng CẤM (Cấm lửa, cấm vào...).",
          "Biển báo Hình tròn Xanh: Bắt buộc thực hiện (Mang kính bảo hộ, đeo găng tay...).",
          "Biển báo Tam giác Vàng (Viền đen): CẢNH BÁO nguy hiểm (Điện cao thế, chất độc, nguồn phóng xạ...).",
          "Biển báo Hình vuông / Chữ nhật: Chỉ dẫn / Hóa chất chất nguy hiểm."
        ]
      }
    ],
    commonPitfalls: [
      "Nhầm lẫn hình dạng và màu sắc của biển báo an toàn (Cấm: Tròn đỏ; Cảnh báo: Tam giác vàng; Bắt buộc: Tròn xanh).",
      "Lắp ráp dụng cụ thí nghiệm điện khi nguồn điện vẫn đang bật."
    ]
  },
  {
    lessonNum: "Bài 3",
    title: "Thực hành tính sai số trong phép đo & Ghi kết quả đo",
    matrixRef: "Phần I: 1 câu Nhận biết (0,25 đ)",
    points: "0,25 đ",
    keyPoints: [
      {
        subtitle: "1. Phép đo trực tiếp và gián tiếp",
        content: [
          "Phép đo trực tiếp: So sánh trực tiếp qua dụng cụ đo (đo chiều dài bằng thước, đo thời gian bằng đồng hồ).",
          "Phép đo gián tiếp: Xác định qua công thức liên hệ với các đại lượng đo trực tiếp (tính tốc độ v = s/t)."
        ]
      },
      {
        subtitle: "2. Phân loại Sai số & Công thức tính",
        content: [
          "Sai số hệ thống: Do dụng cụ đo (dụng cụ lệch vạch 0) hoặc do phương pháp đo.",
          "Sai số ngẫu nhiên: Do thao tác không chuẩn, phản xạ mắt, tác động môi trường.",
          "Công thức Giá trị trung bình: Ā = (A₁ + A₂ + ... + A_n) / n.",
          "Sai số tuyệt đối trung bình: ΔĀ = (|ΔA₁| + |ΔA₂| + ... + |ΔA_n|) / n.",
          "Sai số tuyệt đối của phép đo: ΔA = ΔĀ + ΔA_dụng cụ (với ΔA_dụng cụ thường lấy = 1/2 ĐCNN).",
          "Sai số tương đối (tỉ đối): δA = (ΔA / Ā) × 100%.",
          "Cách ghi kết quả: A = Ā ± ΔA (Chữ số có nghĩa của ΔA thường ghi đến 1-2 chữ số thập phân tương ứng với Ā)."
        ]
      }
    ],
    commonPitfalls: [
      "Quên cộng sai số dụng cụ ΔA_dụng cụ vào sai số tuyệt đối tổng cộng ΔA.",
      "Ghi kết quả đo lệch chữ số thập phân giữa giá trị trung bình Ā và sai số tuyệt đối ΔA."
    ]
  },
  {
    lessonNum: "Bài 4",
    title: "Độ dịch chuyển và quãng đường đi được",
    matrixRef: "Phần I: 3 câu (1 NB + 2 TH) (0,75 đ)",
    points: "0,75 đ",
    keyPoints: [
      {
        subtitle: "1. Định nghĩa Quãng đường (s) & Độ dịch chuyển (d⃗)",
        content: [
          "Quãng đường đi được (s): Độ dài toàn bộ quỹ đạo mà vật chuyển động. Là đại lượng đại số luôn s ≥ 0.",
          "Độ dịch chuyển (d⃗): Là một vectơ nối từ vị trí đầu đến vị trí cuối của chuyển động. d = x_cuối - x_đầu.",
          "So sánh: Độ dịch chuyển cho biết độ biến thiên vị trí và chiều chuyển động của vật."
        ]
      },
      {
        subtitle: "2. Mối quan hệ giữa s và d",
        content: [
          "Khi vật chuyển động thẳng và KHÔNG đổi chiều: Quãng đường s = |d|.",
          "Khi vật đổi chiều chuyển động hoặc chuyển động cong: s > |d|."
        ]
      }
    ],
    commonPitfalls: [
      "Coi độ dịch chuyển d luôn bằng quãng đường s (Chỉ đúng khi CĐ thẳng không đổi chiều).",
      "Quên rằng độ dịch chuyển d có thể mang giá trị âm (d < 0) khi vật chuyển động ngược chiều dương."
    ]
  },
  {
    lessonNum: "Bài 5 - 6",
    title: "Tốc độ và Vận tốc. Thực hành đo tốc độ",
    matrixRef: "Phần I: 1 câu NB + Phần II: 1 câu (2 ý NB) + Phần III: 1 câu NB + Phần IV: 1 câu TH (2,00 đ)",
    points: "2,00 đ",
    keyPoints: [
      {
        subtitle: "1. Tốc độ vs Vận tốc",
        content: [
          "Tốc độ trung bình: v_tb = s / t (Đặc trưng cho mức độ nhanh chậm của chuyển động, luôn ≥ 0).",
          "Vận tốc trung bình: v⃗_tb = d⃗ / t = Δx / Δt (Đặc trưng cho cả mức độ nhanh chậm và chiều chuyển động, có thể âm, dương hoặc bằng 0).",
          "Tốc độ tức thời: Tốc độ tại một thời điểm xác định (kim tốc độ kế ô tô)."
        ]
      },
      {
        subtitle: "2. Công thức Cộng vận tốc",
        content: [
          "Công thức vectơ: v⃗₁₃ = v⃗₁₂ + v⃗₂₃ (1: vật chuyển động, 2: hệ quy chiếu chuyển động, 3: hệ quy chiếu đứng yên).",
          "Hai vận tốc cùng chiều: v₁₃ = v₁₂ + v₂₃.",
          "Hai vận tốc ngược chiều: v₁₃ = |v₁₂ - v₂₃|.",
          "Hai vận tốc vuông góc: v₁₃ = √(v₁₂² + v₂₃²)."
        ]
      },
      {
        subtitle: "3. Đo tốc độ bằng Cổng quang điện & Đồng hồ hiện số",
        content: [
          "Nguyên lý: Tấm chắn sáng có độ rộng s đi qua cổng quang điện ngắt chùm hồng ngoại, đồng hồ đo thời gian t ngắt sáng.",
          "Tốc độ tức thời / ngắn: v = s / t.",
          "Ưu điểm: Độ chính xác cực cao, loại bỏ hoàn toàn sai số phản xạ người bấm."
        ]
      }
    ],
    commonPitfalls: [
      "Đồng nhất tốc độ trung bình s/t với vận tốc trung bình d/t khi vật đổi chiều.",
      "Nhầm lẫn chỉ số các hệ quy chiếu trong công thức cộng vận tốc v₁₃ = v₁₂ + v₂₃."
    ]
  },
  {
    lessonNum: "Bài 7",
    title: "Đồ thị độ dịch chuyển – thời gian (d - t)",
    matrixRef: "Phần I: 2 câu (1 NB + 1 TH) + Phần II: 1 câu (2 ý NB) (0,70 đ)",
    points: "0,70 đ",
    keyPoints: [
      {
        subtitle: "1. Đặc điểm Đồ thị (d - t)",
        content: [
          "Trục tung Od biểu diễn độ dịch chuyển d (m, km). Trục hoành Ot biểu diễn thời gian t (s, h).",
          "Đoạn đồ thị nghiêng đi lên: Vật chuyển động thẳng đều theo chiều dương (v > 0).",
          "Đoạn đồ thị nghiêng đi xuống: Vật chuyển động thẳng đều theo chiều âm (v < 0).",
          "Đoạn đồ thị nằm ngang parallel Ot: Vật đứng yên (v = 0)."
        ]
      },
      {
        subtitle: "2. Xác định Tốc độ & Vận tốc từ Đồ thị",
        content: [
          "Vận tốc v bằng độ dốc (hệ số góc) của đồ thị (d - t): v = (d₂ - d₁) / (t₂ - t₁) = Δd / Δt.",
          "Tốc độ v_tốc độ = |v| = |Δd / Δt|."
        ]
      }
    ],
    commonPitfalls: [
      "Đọc nhầm đồ thị (d - t) thành đồ thị (v - t). Trên đồ thị d-t, đường thẳng nằm ngang nghĩa là đứng yên, không phải chuyển động thẳng đều."
    ]
  },
  {
    lessonNum: "Bài 8",
    title: "Chuyển động biến đổi. Gia tốc",
    matrixRef: "Phần I: 2 câu (1 NB + 1 TH) (0,50 đ)",
    points: "0,50 đ",
    keyPoints: [
      {
        subtitle: "1. Gia tốc (a⃗)",
        content: [
          "Khái niệm: Đại lượng đặc trưng cho tốc độ biến thiên của vận tốc theo thời gian.",
          "Công thức: a⃗ = (v⃗₂ - v⃗₁) / (t₂ - t₁) = Δv⃗ / Δt. Đơn vị trong hệ SI: m/s².",
          "Hướng của gia tốc: a⃗ cùng hướng với Δv⃗."
        ]
      },
      {
        subtitle: "2. Phân loại Chuyển động Nhanh dần & Chậm dần",
        content: [
          "Chuyển động nhanh dần: Tốc độ tăng theo thời gian ⟹ a⃗ cùng chiều với v⃗ ⟹ a·v > 0.",
          "Chuyển động chậm dần: Tốc độ giảm theo thời gian ⟹ a⃗ ngược chiều với v⃗ ⟹ a·v < 0."
        ]
      }
    ],
    commonPitfalls: [
      "Cho rằng gia tốc âm (a < 0) luôn là chuyển động chậm dần. (Thực tế: nếu v < 0 và a < 0 thì a·v > 0 là chuyển động nhanh dần theo chiều âm!)."
    ]
  },
  {
    lessonNum: "Bài 9",
    title: "Chuyển động thẳng biến đổi đều (CĐTBĐĐ)",
    matrixRef: "Phần I: 3 câu (2 NB + 1 TH) + Phần II: 1 câu (2 NB + 2 TH) + Phần IV: 2 câu V D (3,75 đ)",
    points: "3,75 đ",
    keyPoints: [
      {
        subtitle: "1. Định nghĩa CĐTBĐĐ",
        content: [
          "Chuyển động thẳng biến đổi đều là chuyển động thẳng có gia tốc a = const (không đổi theo thời gian).",
          "Chuyển động thẳng nhanh dần đều (CTNDĐ): Tốc độ tăng đều theo thời gian, a·v > 0.",
          "Chuyển động thẳng chậm dần đều (CTCDĐ): Tốc độ giảm đều theo thời gian, a·v < 0."
        ]
      },
      {
        subtitle: "2. Hệ thống Công thức CĐTBĐĐ",
        content: [
          "Vận tốc: v = v₀ + a·t.",
          "Độ dịch chuyển: d = v₀·t + 1/2·a·t².",
          "Công thức liên hệ độc lập thời gian: v² - v₀² = 2·a·d.",
          "Phương trình tọa độ: x = x₀ + v₀·t + 1/2·a·t²."
        ]
      }
    ],
    commonPitfalls: [
      "Quên chọn chiều dương dẫn đến gán sai dấu của v₀ và a.",
      "Sử dụng nhầm công thức quãng đường khi vật đổi chiều chuyển động."
    ]
  },
  {
    lessonNum: "Bài 10",
    title: "Sự rơi tự do",
    matrixRef: "Phần I: 3 câu (1 NB + 2 TH) + Phần III: 1 câu TH (1,00 đ)",
    points: "1,00 đ",
    keyPoints: [
      {
        subtitle: "1. Khái niệm Sự rơi tự do",
        content: [
          "Sự rơi tự do là sự rơi chỉ chịu tác dụng của Trọng lực.",
          "Đặc điểm: Phương thẳng đứng, chiều từ trên xuống dưới. Bắt đầu từ trạng thái nghỉ (v₀ = 0).",
          "Tính chất: Là chuyển động thẳng nhanh dần đều với gia tốc rơi tự do a = g ≈ 9.8 m/s² (hoặc 10 m/s²)."
        ]
      },
      {
        subtitle: "2. Các công thức Rơi tự do",
        content: [
          "Vận tốc rơi tại thời điểm t: v = g·t.",
          "Quãng đường / Độ cao rơi: h = d = 1/2·g·t².",
          "Công thức liên hệ: v² = 2·g·h ⟹ v = √(2·g·h) & t = √(2·h / g)."
        ]
      }
    ],
    commonPitfalls: [
      "Cho rằng vật nặng rơi nhanh hơn vật nhẹ trong môi trường rơi tự do (chân không). Trong chân không mọi vật rơi tự do như nhau!",
      "Nhầm v₀ = 0 của rơi tự do khi ném thẳng đứng từ trên xuống."
    ]
  }
];

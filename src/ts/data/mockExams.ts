import { MCQQuestion, TrueFalseQuestion, ShortAnswerQuestion, EssayQuestion } from "./questions.js";

export interface MockExam {
  id: number;
  title: string;
  duration: string;
  part1MCQ: MCQQuestion[];
  part2TF: TrueFalseQuestion[];
  part3SA: ShortAnswerQuestion[];
  part4Essay: EssayQuestion[];
}

export const MOCK_EXAM_1: MockExam = {
  id: 1,
  title: "ĐỀ KIỂM TRA GIỮA HỌC KÌ I — ĐỀ SỐ 01 (CHUẨN MA TRẬN 2026)",
  duration: "50 phút",
  part1MCQ: [
    {
      id: 1,
      category: "Bài 1",
      level: "Nhận biết",
      question: "Đối tượng nghiên cứu chủ yếu của Vật lí là gì?",
      options: [
        "Các chất và sự biến đổi giữa các chất.",
        "Các dạng vận động của vật chất và năng lượng.",
        "Sự sinh trưởng và phát triển của các loài sinh vật.",
        "Lịch sử phát triển của xã hội loài người."
      ],
      correctIndex: 1,
      explanation: "Vật lí nghiên cứu các dạng vận động của vật chất và năng lượng."
    },
    {
      id: 2,
      category: "Bài 2",
      level: "Nhận biết",
      question: "Biển báo hình tam giác đều, viền đen, nền vàng thuộc nhóm biển báo nào?",
      options: ["Biển báo cấm.", "Biển cảnh báo nguy hiểm.", "Biển lệnh bắt buộc.", "Biển chỉ dẫn."],
      correctIndex: 1,
      explanation: "Hình tam giác nền vàng viền đen là biển cảnh báo nguy hiểm."
    },
    {
      id: 3,
      category: "Bài 2",
      level: "Thông hiểu",
      question: "Khi làm thí nghiệm về điện trong phòng thực hành Vật lí phổ thông, điện áp an toàn cho học sinh không được vượt quá:",
      options: ["24 V", "110 V", "220 V", "380 V"],
      correctIndex: 0,
      explanation: "Điện áp an toàn thí nghiệm học sinh không quá 24V."
    },
    {
      id: 4,
      category: "Bài 3",
      level: "Nhận biết",
      question: "Phép đo trực tiếp là:",
      options: [
        "Phép đo so sánh trực tiếp đại lượng cần đo với dụng cụ đo.",
        "Phép đo xác định qua công thức toán học.",
        "Phép đo không dùng dụng cụ đo.",
        "Phép đo chỉ thực hiện được trong chân không."
      ],
      correctIndex: 0,
      explanation: "Phép đo trực tiếp là so sánh trực tiếp đại lượng cần đo với dụng cụ."
    },
    {
      id: 5,
      category: "Bài 4",
      level: "Nhận biết",
      question: "Độ dịch chuyển d là:",
      options: [
        "Độ dài đường đi của vật.",
        "Một vectơ nối từ vị trí đầu đến vị trí cuối.",
        "Luôn là số dương.",
        "Đại lượng không có hướng."
      ],
      correctIndex: 1,
      explanation: "Độ dịch chuyển d là vectơ nối từ điểm đầu đến điểm cuối."
    },
    {
      id: 6,
      category: "Bài 4",
      level: "Thông hiểu",
      question: "Một người đi từ A đến B 4 km rồi quay lại A. Quãng đường s và độ dịch chuyển d là:",
      options: ["s = 8 km; d = 0 km", "s = 8 km; d = 8 km", "s = 4 km; d = 0 km", "s = 0 km; d = 8 km"],
      correctIndex: 0,
      explanation: "s = 4 + 4 = 8 km; Điểm cuối trùng điểm đầu ⟹ d = 0."
    },
    {
      id: 7,
      category: "Bài 4",
      level: "Thông hiểu",
      question: "Độ lớn độ dịch chuyển |d| bằng quãng đường s khi:",
      options: [
        "Vật chuyển động thẳng và không đổi chiều.",
        "Vật chuyển động tròn đều.",
        "Vật chuyển động thẳng đi rồi quay lại.",
        "Vật đứng yên."
      ],
      correctIndex: 0,
      explanation: "|d| = s khi chuyển động thẳng và không đổi chiều."
    },
    {
      id: 8,
      category: "Bài 5",
      level: "Nhận biết",
      question: "Tốc độ trung bình được tính bằng công thức:",
      options: ["v_tb = s / t", "v_tb = d / t", "v_tb = a·t", "v_tb = x / t"],
      correctIndex: 0,
      explanation: "Tốc độ trung bình v_tb = s / t."
    },
    {
      id: 9,
      category: "Bài 7",
      level: "Nhận biết",
      question: "Đồ thị (d - t) nằm ngang song song trục Ot cho biết vật đang:",
      options: ["Đứng yên.", "Chuyển động thẳng đều.", "Chuyển động nhanh dần.", "Chuyển động chậm dần."],
      correctIndex: 0,
      explanation: "d không đổi theo thời gian ⟹ Vật đang đứng yên."
    },
    {
      id: 10,
      category: "Bài 7",
      level: "Thông hiểu",
      question: "Hệ số góc của đồ thị (d - t) đại diện cho:",
      options: ["Vận tốc.", "Gia tốc.", "Quãng đường.", "Thời gian."],
      correctIndex: 0,
      explanation: "Hệ số góc k = Δd / Δt = Vận tốc v."
    },
    {
      id: 11,
      category: "Bài 8",
      level: "Nhận biết",
      question: "Gia tốc là đại lượng đặc trưng cho:",
      options: [
        "Tốc độ biến thiên của vận tốc theo thời gian.",
        "Quãng đường đi được trong 1 giây.",
        "Chiều của chuyển động.",
        "Vị trí của vật."
      ],
      correctIndex: 0,
      explanation: "Gia tốc đặc trưng cho sự biến thiên vận tốc theo thời gian."
    },
    {
      id: 12,
      category: "Bài 8",
      level: "Thông hiểu",
      question: "Chuyển động nhanh dần có gia tốc a và vận tốc v thỏa mãn:",
      options: ["a·v > 0", "a·v < 0", "a·v = 0", "a < 0"],
      correctIndex: 0,
      explanation: "Nhanh dần ⟹ a và v cùng dấu ⟹ a·v > 0."
    },
    {
      id: 13,
      category: "Bài 9",
      level: "Nhận biết",
      question: "Công thức độc lập thời gian trong CĐTBĐĐ là:",
      options: ["v² - v₀² = 2ad", "v - v₀ = 2ad", "v² + v₀² = 2ad", "d = v₀t + at²"],
      correctIndex: 0,
      explanation: "v² - v₀² = 2ad."
    },
    {
      id: 14,
      category: "Bài 9",
      level: "Nhận biết",
      question: "Chuyển động thẳng biến đổi đều có:",
      options: ["Gia tốc a = const không đổi.", "Vận tốc v = const.", "Quãng đường s tỉ lệ bậc nhất với t.", "Gia tốc a tăng đều."],
      correctIndex: 0,
      explanation: "CĐTBĐĐ có gia tốc không đổi a = const."
    },
    {
      id: 15,
      category: "Bài 9",
      level: "Thông hiểu",
      question: "Một xe tăng tốc từ 0 lên 20 m/s trong 10 s. Gia tốc của xe là:",
      options: ["2 m/s²", "1 m/s²", "0,5 m/s²", "4 m/s²"],
      correctIndex: 0,
      explanation: "a = (20 - 0) / 10 = 2 m/s²."
    },
    {
      id: 16,
      category: "Bài 10",
      level: "Nhận biết",
      question: "Phương và chiều của chuyển động rơi tự do là:",
      options: [
        "Phương thẳng đứng, chiều từ trên xuống dưới.",
        "Phương nằm ngang.",
        "Phương nghiêng 45°.",
        "Phương thẳng đứng, chiều từ dưới lên trên."
      ],
      correctIndex: 0,
      explanation: "Rơi tự do phương thẳng đứng, chiều từ trên xuống."
    },
    {
      id: 17,
      category: "Bài 10",
      level: "Thông hiểu",
      question: "Thả vật rơi tự do từ độ cao h = 20 m xuống đất (g = 10 m/s²). Thời gian rơi là:",
      options: ["2 s", "4 s", "1 s", "3 s"],
      correctIndex: 0,
      explanation: "t = √(2h/g) = √(40/10) = √4 = 2 s."
    },
    {
      id: 18,
      category: "Bài 10",
      level: "Thông hiểu",
      question: "Thả vật rơi tự do từ độ cao h (g = 10 m/s²), vận tốc khi chạm đất là 20 m/s. Độ cao h là:",
      options: ["20 m", "10 m", "40 m", "30 m"],
      correctIndex: 0,
      explanation: "v² = 2gh ⟹ 400 = 20h ⟹ h = 20 m."
    }
  ],
  part2TF: [
    {
      id: 1,
      category: "Đồ thị d-t & Vận tốc",
      context: "Một vật chuyển động thẳng có đồ thị độ dịch chuyển - thời gian (d - t): t từ 0 -> 2 s: d tăng từ 0 -> 10 m. t từ 2 -> 5 s: d giữ ở 10 m.",
      statements: [
        { label: "a", statement: "Trong 2 s đầu, vật chuyển động với vận tốc 5 m/s.", isCorrect: true, explanation: "v = 10/2 = 5 m/s." },
        { label: "b", statement: "Từ t = 2 s đến 5 s, vật chuyển động thẳng đều.", isCorrect: false, explanation: "Vật đứng yên (v = 0)." },
        { label: "c", statement: "Tốc độ trung bình trong 5 s đầu là 2 m/s.", isCorrect: true, explanation: "v_tb = s/t = 10/5 = 2 m/s." },
        { label: "d", statement: "Độ dịch chuyển tổng cộng sau 5 s là d = 10 m.", isCorrect: true, explanation: "d = 10 - 0 = 10 m." }
      ]
    },
    {
      id: 2,
      category: "Chuyển động thẳng biến đổi đều",
      context: "Một ô tô khởi hành từ trạng thái nghỉ với gia tốc a = 2 m/s².",
      statements: [
        { label: "a", statement: "Vận tốc của ô tô sau 4 s là 8 m/s.", isCorrect: true, explanation: "v = 2 × 4 = 8 m/s." },
        { label: "b", statement: "Quãng đường ô tô đi được sau 4 s là 16 m.", isCorrect: true, explanation: "s = 1/2 × 2 × 4² = 16 m." },
        { label: "c", statement: "Vận tốc trung bình trong 4 s đầu là 8 m/s.", isCorrect: false, explanation: "v_tb = 16 / 4 = 4 m/s." },
        { label: "d", statement: "Quãng đường xe đi trong giây thứ 4 là 7 m.", isCorrect: true, explanation: "s(4) - s(3) = 16 - (1/2 × 2 × 9) = 16 - 9 = 7 m." }
      ]
    }
  ],
  part3SA: [
    {
      id: 1,
      category: "Tốc độ",
      level: "Nhận biết",
      question: "Một xe chạy 36 km hết 0,5 giờ. Tốc độ trung bình theo m/s bằng bao nhiêu?",
      correctAnswer: "20",
      unit: "m/s",
      explanation: "v = 36 km / 0,5 h = 72 km/h = 20 m/s."
    },
    {
      id: 2,
      category: "Sự rơi tự do",
      level: "Thông hiểu",
      question: "Một vật rơi tự do từ độ cao h = 80 m (g = 10 m/s²). Thời gian rơi chạm đất bằng bao nhiêu giây?",
      correctAnswer: "4",
      unit: "s",
      explanation: "t = √(2h/g) = √(160/10) = √16 = 4 s."
    }
  ],
  part4Essay: [
    {
      id: 1,
      category: "Cộng vận tốc",
      title: "Bài toán thuyền xuôi dòng ngược dòng",
      problemStatement: "Một thuyền chuyển động từ A đến B cách nhau 18 km rồi quay về A. Vận tốc thuyền so với nước là 12 km/h, vận tốc nước so với bờ là 3 km/h. Tính tổng thời gian chuyến đi.",
      gradingGuide: [
        { step: "v_xuôi = 15 km/h; v_ngược = 9 km/h", points: "0,50 đ" },
        { step: "t_xuôi = 18/15 = 1,2 h; t_ngược = 18/9 = 2 h", points: "0,25 đ" },
        { step: "Tổng thời gian t = 3,2 h (3 giờ 12 phút)", points: "0,25 đ" }
      ],
      detailedSolution: "v_xuôi = 12 + 3 = 15 km/h. t_xuôi = 18 / 15 = 1,2 h.\nv_ngược = 12 - 3 = 9 km/h. t_ngược = 18 / 9 = 2 h.\nTổng thời gian t = 1,2 + 2 = 3,2 giờ."
    },
    {
      id: 2,
      category: "CĐTBĐĐ",
      title: "Bài toán ô tô hãm phanh",
      problemStatement: "Ô tô đang đi với vận tốc 20 m/s thì hãm phanh chậm dần đều với gia tốc a = -2 m/s².\na) Tính thời gian đến khi dừng hẳn.\nb) Tính quãng đường hãm phanh.",
      gradingGuide: [
        { step: "a) v = v₀ + at ⟹ 0 = 20 - 2t ⟹ t = 10 s", points: "0,50 đ" },
        { step: "b) v² - v₀² = 2as ⟹ 0 - 400 = -4s ⟹ s = 100 m", points: "0,50 đ" }
      ],
      detailedSolution: "a) t = (0 - 20) / (-2) = 10 s.\nb) s = (0 - 20²) / (2 × -2) = -400 / -4 = 100 m."
    },
    {
      id: 3,
      category: "CĐTBĐĐ Gặp nhau",
      title: "Hai xe xuất phát cùng lúc gặp nhau",
      problemStatement: "Hai địa điểm A và B cách nhau 100 m. Xe 1 từ A nhanh dần đều với gia tốc a = 2 m/s² không vận tốc đầu về B. Xe 2 từ B chuyển động thẳng đều về A với vận tốc 10 m/s. Tìm thời điểm và vị trí hai xe gặp nhau.",
      gradingGuide: [
        { step: "x₁ = t²; x₂ = 100 - 10t", points: "0,50 đ" },
        { step: "t² + 10t - 100 = 0 ⟹ t ≈ 6,18 s", points: "0,25 đ" },
        { step: "x = (6,18)² ≈ 38,2 m cách A", points: "0,25 đ" }
      ],
      detailedSolution: "x₁ = 1/2 × 2 × t² = t².\nx₂ = 100 - 10t.\nx₁ = x₂ ⟹ t² + 10t - 100 = 0 ⟹ t ≈ 6,18 s.\nVị trí gặp nhau x = 6,18² ≈ 38,2 m."
    }
  ]
};

export const MOCK_EXAM_2: MockExam = { ...MOCK_EXAM_1, id: 2, title: "ĐỀ KIỂM TRA GIỮA HỌC KÌ I — ĐỀ SỐ 02 (CHUẨN MA TRẬN 2026)" };

export interface MCQQuestion {
  id: number;
  category: string;
  level: "Nhận biết" | "Thông hiểu" | "Vận dụng";
  question: string;
  options: [string, string, string, string];
  correctIndex: number; // 0..3
  explanation: string;
}

export interface TrueFalseStatement {
  label: string; // 'a', 'b', 'c', 'd'
  statement: string;
  isCorrect: boolean;
  explanation: string;
}

export interface TrueFalseQuestion {
  id: number;
  category: string;
  context: string;
  statements: TrueFalseStatement[];
}

export interface ShortAnswerQuestion {
  id: number;
  category: string;
  level: "Nhận biết" | "Thông hiểu" | "Vận dụng";
  question: string;
  correctAnswer: string;
  unit: string;
  explanation: string;
}

export interface EssayQuestion {
  id: number;
  category: string;
  title: string;
  problemStatement: string;
  gradingGuide: { step: string; points: string }[];
  detailedSolution: string;
}

export const MCQ_BANK: MCQQuestion[] = [
  // Bài 1 (1..4)
  {
    id: 1,
    category: "Bài 1. Làm quen với Vật lí",
    level: "Nhận biết",
    question: "Đối tượng nghiên cứu chủ yếu của môn Vật lí là gì?",
    options: [
      "Cấu tạo chất và sự biến đổi của các chất.",
      "Các dạng vận động của vật chất và năng lượng.",
      "Sự sinh trưởng và phát triển của các loài sinh vật.",
      "Sự hình thành và biến đổi địa hình bề mặt Trái Đất."
    ],
    correctIndex: 1,
    explanation: "Vật lí nghiên cứu các dạng vận động của vật chất và năng lượng."
  },
  {
    id: 2,
    category: "Bài 1. Làm quen với Vật lí",
    level: "Nhận biết",
    question: "Thành tựu nghiên cứu nào của Vật lí đóng vai trò mở đầu cho cuộc Cách mạng công nghiệp lần thứ nhất (thế kỉ XVIII)?",
    options: [
      "Nghiên cứu về Nhiệt động lực học (sáng chế máy hơi nước của James Watt).",
      "Khám phá hiện tượng cảm ứng điện từ của Michael Faraday.",
      "Nghiên cứu về điện tử, chất bán dẫn và vi mạch tích hợp.",
      "Nghiên cứu vật lí lượng tử, trí tuệ nhân tạo và công nghệ nano."
    ],
    correctIndex: 0,
    explanation: "CMCN 1.0 gắn liền với động cơ hơi nước và Nhiệt động lực học."
  },
  {
    id: 3,
    category: "Bài 1. Làm quen với Vật lí",
    level: "Nhận biết",
    question: "Hiện tượng cảm ứng điện từ do Faraday khám phá (năm 1831) là cơ sở cho cuộc cách mạng công nghiệp lần thứ mấy?",
    options: ["Lần thứ nhất.", "Lần thứ hai.", "Lần thứ ba.", "Lần thứ tư."],
    correctIndex: 1,
    explanation: "Hiện tượng cảm ứng điện từ là nền tảng cho năng lượng điện và CMCN 2.0."
  },
  {
    id: 4,
    category: "Bài 1. Làm quen với Vật lí",
    level: "Nhận biết",
    question: "Thứ tự đúng của 5 bước trong quy trình nghiên cứu bằng phương pháp thực nghiệm là:",
    options: [
      "Quan sát ➔ Xác định vấn đề ➔ Thí nghiệm ➔ Dự đoán ➔ Kết luận.",
      "Xác định vấn đề ➔ Dự đoán ➔ Quan sát ➔ Thí nghiệm ➔ Kết luận.",
      "Quan sát / Xác định vấn đề ➔ Giả thuyết (Dự đoán) ➔ Thí nghiệm ➔ Rút ra kết luận.",
      "Thí nghiệm ➔ Quan sát ➔ Dự đoán ➔ Xác định vấn đề ➔ Kết luận."
    ],
    correctIndex: 2,
    explanation: "Quy trình thực nghiệm: Quan sát -> Giả thuyết -> Thí nghiệm -> Kết luận."
  },

  // Bài 2 (5..10)
  {
    id: 5,
    category: "Bài 2. Các quy tắc an toàn trong phòng thực hành",
    level: "Nhận biết",
    question: "Hành vi nào sau đây KHÔNG an toàn khi làm việc trong phòng thực hành Vật lí?",
    options: [
      "Kiểm tra kĩ dây dẫn điện trước khi cắm vào nguồn điện.",
      "Chạm tay trực tiếp vào dây điện trần đang có dòng điện chạy qua.",
      "Tắt công tắc nguồn điện trước khi thay đổi sơ đồ mạch điện.",
      "Sử dụng kính bảo hộ khi làm việc với hóa chất hoặc chất dễ vỡ."
    ],
    correctIndex: 1,
    explanation: "Chạm tay trực tiếp vào dây điện trần đang có điện gây nguy hiểm điện giật."
  },
  {
    id: 6,
    category: "Bài 2. Các quy tắc an toàn trong phòng thực hành",
    level: "Nhận biết",
    question: "Biển báo an toàn có hình tam giác đều, viền đen, nền vàng, bên trong có hình vẽ màu đen là loại biển báo nào?",
    options: ["Biển báo CẤM.", "Biển báo BẮT BUỘC.", "Biển báo CẢNH BÁO nguy hiểm.", "Biển báo CHỈ DẪN."],
    correctIndex: 2,
    explanation: "Hình tam giác vàng viền đen là biển báo cảnh báo nguy hiểm."
  },
  {
    id: 7,
    category: "Bài 2. Các quy tắc an toàn trong phòng thực hành",
    level: "Thông hiểu",
    question: "Khi làm thí nghiệm với nguồn điện xoay chiều trong phòng thực hành, để đảm bảo an toàn cho học sinh, nguồn điện sử dụng thường có điện áp tối đa là bao nhiêu?",
    options: ["Dưới 24 V.", "Dưới 110 V.", "Dưới 220 V.", "Dưới 380 V."],
    correctIndex: 0,
    explanation: "Học sinh làm thực hành điện dùng nguồn điện an toàn dưới 24 V."
  },
  {
    id: 8,
    category: "Bài 2. Các quy tắc an toàn trong phòng thực hành",
    level: "Thông hiểu",
    question: "Biển báo có hình tròn, nền xanh lam, bên trong có hình vẽ màu trắng thuộc nhóm biển báo nào?",
    options: ["Biển báo cấm.", "Biển báo lệnh (bắt buộc thực hiện).", "Biển cảnh báo nguy hiểm.", "Biển báo khu vực cháy nổ."],
    correctIndex: 1,
    explanation: "Hình tròn nền xanh lam là biển hiệu lệnh (bắt buộc thực hiện)."
  },
  {
    id: 9,
    category: "Bài 2. Các quy tắc an toàn trong phòng thực hành",
    level: "Nhận biết",
    question: "Để phòng tránh chập mạch và cháy nổ khi dùng nguồn điện DC (một chiều), người làm thí nghiệm tuyệt đối không được:",
    options: [
      "Nối trực tiếp hai cực âm và dương của nguồn điện bằng một dây dẫn có điện trở rất nhỏ.",
      "Nối nguồn điện qua một điện trở bảo vệ.",
      "Nối nguồn điện với ampe kế mắc nối tiếp với bóng đèn.",
      "Ngắt nguồn điện sau khi làm xong thí nghiệm."
    ],
    correctIndex: 0,
    explanation: "Nối trực tiếp 2 cực bằng dây dẫn trở nhỏ gây đoản mạch (chập điện) cháy nổ."
  },
  {
    id: 10,
    category: "Bài 2. Các quy tắc an toàn trong phòng thực hành",
    level: "Thông hiểu",
    question: "Yếu tố nào sau đây là nguyên nhân trực tiếp gây ra nguy hiểm về điện giật cho con người?",
    options: [
      "Cường độ dòng điện chạy qua cơ thể người.",
      "Chiều dài của dây dẫn điện.",
      "Khối lượng của thiết bị tiêu thụ điện.",
      "Tần số của âm thanh phát ra từ thiết bị."
    ],
    correctIndex: 0,
    explanation: "Cường độ dòng điện qua cơ thể người quyết định mức độ nguy hiểm điện giật."
  },

  // Bài 3 (11..16)
  {
    id: 11,
    category: "Bài 3. Thực hành tính sai số phép đo",
    level: "Nhận biết",
    question: "Phép đo nào sau đây là phép đo trực tiếp?",
    options: [
      "Dùng thước kẹp đo đường kính của một viên bi thép.",
      "Đo quãng đường s và thời gian t rồi tính tốc độ v = s/t.",
      "Tính thể tích hình lập phương V = a³ bằng cách đo cạnh a.",
      "Tính diện tích hình tròn S = π·r² bằng cách đo bán kính r."
    ],
    correctIndex: 0,
    explanation: "Đo chiều dài/đường kính trực tiếp bằng thước kẹp là phép đo trực tiếp."
  },
  {
    id: 12,
    category: "Bài 3. Thực hành tính sai số phép đo",
    level: "Nhận biết",
    question: "Sai số dụng cụ ΔA_dụng cụ thường được lấy bằng:",
    options: [
      "Một nửa độ chia nhỏ nhất (1/2 ĐCNN) hoặc bằng 1 ĐCNN của dụng cụ đo.",
      "Gấp hai lần độ chia nhỏ nhất của dụng cụ đo.",
      "Luôn luôn bằng 0.",
      "Giá trị trung bình của các lần đo."
    ],
    correctIndex: 0,
    explanation: "Sai số dụng cụ thông thường được lấy bằng 1/2 ĐCNN hoặc 1 ĐCNN."
  },
  {
    id: 13,
    category: "Bài 3. Thực hành tính sai số phép đo",
    level: "Thông hiểu",
    question: "Thực hiện đo thời gian rơi của một vật 5 lần thu được kết quả trung bình t̄ = 0,425 s và sai số tuyệt đối Δt = 0,008 s. Kết quả phép đo được ghi đúng là:",
    options: [
      "t = 0,425 ± 0,008 (s)",
      "t = 0,4255 ± 0,008 (s)",
      "t = 0,42 ± 0,01 (s)",
      "t = 0,425 ± 0,01 (s)"
    ],
    correctIndex: 0,
    explanation: "Cách ghi chuẩn: t = 0,425 ± 0,008 (s)."
  },
  {
    id: 14,
    category: "Bài 3. Thực hành tính sai số phép đo",
    level: "Thông hiểu",
    question: "Một học sinh đo chiều dài bàn học thu được L̄ = 1,20 m và sai số tuyệt đối ΔL = 0,02 m. Sai số tương đối δL của phép đo này bằng:",
    options: ["1,67%", "2,00%", "0,02%", "12,0%"],
    correctIndex: 0,
    explanation: "δL = (ΔL / L̄) × 100% = (0,02 / 1,20) × 100% = 1,67%."
  },
  {
    id: 15,
    category: "Bài 3. Thực hành tính sai số phép đo",
    level: "Nhận biết",
    question: "Sai số hệ thống là loại sai số:",
    options: [
      "Do đặc điểm cấu tạo dụng cụ đo hoặc do phương pháp đo gây ra, làm kết quả lệch về một phía.",
      "Do phản xạ chậm trễ không đều của người đo gây ra.",
      "Có thể loại bỏ hoàn toàn bằng cách đo nhiều lần rồi lấy trung bình.",
      "Do luồng gió ngẫu nhiên tác động khi làm thí nghiệm."
    ],
    correctIndex: 0,
    explanation: "Sai số hệ thống có tính quy luật do dụng cụ hoặc phương pháp."
  },
  {
    id: 16,
    category: "Bài 3. Thực hành tính sai số phép đo",
    level: "Thông hiểu",
    question: "Đo đại lượng A thông qua hai đại lượng B và C theo công thức A = B + C. Công thức tính sai số tuyệt đối ΔA là:",
    options: ["ΔA = ΔB + ΔC", "ΔA = ΔB - ΔC", "ΔA = ΔB × ΔC", "ΔA = ΔB / ΔC"],
    correctIndex: 0,
    explanation: "Sai số tuyệt đối của tổng/hiệu bằng tổng các sai số tuyệt đối: ΔA = ΔB + ΔC."
  },

  // Bài 4 (17..22)
  {
    id: 17,
    category: "Bài 4. Độ dịch chuyển & Quãng đường",
    level: "Nhận biết",
    question: "Độ dịch chuyển là gì?",
    options: [
      "Độ dài toàn bộ đường đi của vật trong thời gian chuyển động.",
      "Một đại lượng vectơ nối vị trí đầu và vị trí cuối của chuyển động.",
      "Đại lượng đặc trưng cho mức độ nhanh chậm của chuyển động.",
      "Khoảng cách lớn nhất mà vật đạt được trong quá trình chuyển động."
    ],
    correctIndex: 1,
    explanation: "Độ dịch chuyển là một đại lượng vectơ hướng từ điểm đầu đến điểm cuối."
  },
  {
    id: 18,
    category: "Bài 4. Độ dịch chuyển & Quãng đường",
    level: "Nhận biết",
    question: "Trong trường hợp nào sau đây, độ lớn của độ dịch chuyển |d| BẰNG quãng đường đi được s?",
    options: [
      "Vật chuyển động thẳng và không đổi chiều.",
      "Vật chuyển động tròn đều một vòng.",
      "Vật chuyển động thẳng đi rồi quay lại vị trí cũ.",
      "Vật chuyển động theo quỹ đạo đường cong bất kì."
    ],
    correctIndex: 0,
    explanation: "Khi chuyển động thẳng không đổi chiều thì |d| = s."
  },
  {
    id: 19,
    category: "Bài 4. Độ dịch chuyển & Quãng đường",
    level: "Thông hiểu",
    question: "Một người đi xe đạp từ A đến B theo một đường thẳng dài 3 km, sau đó quay lại A. Độ dịch chuyển tổng cộng d và quãng đường tổng cộng s của người đó là:",
    options: ["d = 0 km; s = 6 km", "d = 6 km; s = 6 km", "d = 3 km; s = 3 km", "d = 0 km; s = 0 km"],
    correctIndex: 0,
    explanation: "Quay về vị trí ban đầu A nên điểm đầu trùng điểm cuối ⟹ d = 0; s = 3 + 3 = 6 km."
  },
  {
    id: 20,
    category: "Bài 4. Độ dịch chuyển & Quãng đường",
    level: "Thông hiểu",
    question: "Một con rôbốt di chuyển 4 m về phía Bắc, sau đó rẽ phải di chuyển tiếp 3 m về phía Đông. Độ lớn độ dịch chuyển |d| của rôbốt là:",
    options: ["7 m", "5 m", "1 m", "12 m"],
    correctIndex: 1,
    explanation: "Hai hướng Bắc và Đông vuông góc nhau ⟹ |d| = √(4² + 3²) = 5 m."
  },
  {
    id: 21,
    category: "Bài 4. Độ dịch chuyển & Quãng đường",
    level: "Thông hiểu",
    question: "Một vận động viên bơi lội bơi từ đầu này đến đầu kia của bể bơi dài 50 m theo đường thẳng hết 25 s, sau đó bơi quay lại vị trí xuất phát hết 30 s. Tốc độ trung bình v_tb và vận tốc trung bình v_tb của vận động viên trong toàn bộ chuyến bơi là:",
    options: [
      "v_tb = 1,82 m/s; v_tb = 0 m/s",
      "v_tb = 1,82 m/s; v_tb = 1,82 m/s",
      "v_tb = 2,00 m/s; v_tb = 0 m/s",
      "v_tb = 0 m/s; v_tb = 1,82 m/s"
    ],
    correctIndex: 0,
    explanation: "s = 100m, t = 55s ⟹ v_tb = 100/55 ≈ 1,82 m/s. Điểm cuối trùng điểm đầu ⟹ d = 0 ⟹ v_tb = 0 m/s."
  },
  {
    id: 22,
    category: "Bài 4. Độ dịch chuyển & Quãng đường",
    level: "Thông hiểu",
    question: "Một người đi từ nhà đến siêu thị theo một đường thẳng. Chọn trục Ox trùng với đường thẳng đi, gốc O tại nhà, chiều dương từ nhà đến siêu thị. Tọa độ ban đầu x₁ = 0 m, tọa độ siêu thị x₂ = 800 m. Độ dịch chuyển của người đó là:",
    options: ["800 m", "-800 m", "0 m", "1600 m"],
    correctIndex: 0,
    explanation: "d = x₂ - x₁ = 800 - 0 = 800 m."
  },

  // Bài 5 - 6 (23..28)
  {
    id: 23,
    category: "Bài 5 - 6. Tốc độ, Vận tốc & Đo tốc độ",
    level: "Nhận biết",
    question: "Đại lượng nào sau đây đặc trưng cho tính chất nhanh hay chậm và CHIỀU của chuyển động?",
    options: ["Tốc độ trung bình.", "Vận tốc.", "Quãng đường.", "Thời gian chuyển động."],
    correctIndex: 1,
    explanation: "Vận tốc là đại lượng vectơ đặc trưng cho nhanh chậm và chiều chuyển động."
  },
  {
    id: 24,
    category: "Bài 5 - 6. Tốc độ, Vận tốc & Đo tốc độ",
    level: "Nhận biết",
    question: "Thiết bị nào sau đây dùng kết hợp với đồng hồ đo thời gian hiện số để đo thời gian chắn sáng của vật chuyển động một cách chính xác trong phòng thí nghiệm?",
    options: ["Thước dây.", "Cổng quang điện.", "Lực kế.", "Nhiệt kế."],
    correctIndex: 1,
    explanation: "Cổng quang điện kết hợp đồng hồ hiện số đo thời gian chắn sáng chuẩn xác."
  },
  {
    id: 25,
    category: "Bài 5 - 6. Tốc độ, Vận tốc & Đo tốc độ",
    level: "Thông hiểu",
    question: "Một chiếc thuyền chạy xuôi dòng nước từ A đến B với vận tốc của thuyền so với nước là 15 km/h, vận tốc của nước so với bờ là 3 km/h. Vận tốc của thuyền so with bờ là:",
    options: ["18 km/h", "12 km/h", "15 km/h", "45 km/h"],
    correctIndex: 0,
    explanation: "Xuôi dòng: v₁₃ = v₁₂ + v₂₃ = 15 + 3 = 18 km/h."
  },
  {
    id: 26,
    category: "Bài 5 - 6. Tốc độ, Vận tốc & Đo tốc độ",
    level: "Thông hiểu",
    question: "Một xe ô tô di chuyển đoạn đường đầu 60 km với tốc độ 60 km/h và đoạn đường sau 60 km tiếp theo với tốc độ 30 km/h. Tốc độ trung bình trên toàn bộ đoạn đường là:",
    options: ["45 km/h", "40 km/h", "50 km/h", "35 km/h"],
    correctIndex: 1,
    explanation: "t₁ = 60/60 = 1h; t₂ = 60/30 = 2h. Tốc độ TB = (60+60)/(1+2) = 120/3 = 40 km/h."
  },
  {
    id: 27,
    category: "Bài 5 - 6. Tốc độ, Vận tốc & Đo tốc độ",
    level: "Thông hiểu",
    question: "Máy bay đang bay theo phương ngang về phía Đông với vận tốc 800 km/h thì gặp một luồng gió thổi về phía Bắc với vận tốc 150 km/h. Tốc độ của máy bay so với mặt đất là:",
    options: ["814 km/h", "950 km/h", "650 km/h", "900 km/h"],
    correctIndex: 0,
    explanation: "Vuông góc: v = √(800² + 150²) ≈ 813,94 ≈ 814 km/h."
  },
  {
    id: 28,
    category: "Bài 5 - 6. Tốc độ, Vận tốc & Đo tốc độ",
    level: "Nhận biết",
    question: "Một chiếc ô tô đang di chuyển, kim tốc độ kế trên bảng điều khiển chỉ số 60 km/h. Số chỉ này cho biết đại lượng nào?",
    options: ["Tốc độ trung bình.", "Tốc độ tức thời.", "Vận tốc trung bình.", "Gia tốc của xe."],
    correctIndex: 1,
    explanation: "Tốc độ kế thể hiện tốc độ tức thời tại thời điểm quan sát."
  },

  // Bài 7 (29..34)
  {
    id: 29,
    category: "Bài 7. Đồ thị độ dịch chuyển – thời gian (d - t)",
    level: "Nhận biết",
    question: "Đồ thị độ dịch chuyển – thời gian (d - t) của một vật chuyển động thẳng đều có dạng là đường gì?",
    options: [
      "Một đường thẳng xiên góc xuất phát từ gốc tọa độ hoặc một điểm trên trục d.",
      "Một đường parabol.",
      "Một đường cong hyperbol.",
      "Một đường tròn."
    ],
    correctIndex: 0,
    explanation: "Chuyển động thẳng đều có d = v·t nên đồ thị d-t là đường thẳng xiên góc."
  },
  {
    id: 30,
    category: "Bài 7. Đồ thị độ dịch chuyển – thời gian (d - t)",
    level: "Nhận biết",
    question: "Độ dốc (hệ số góc) của đồ thị độ dịch chuyển – thời gian (d - t) cho biết đại lượng nào sau đây?",
    options: ["Gia tốc.", "Vận tốc.", "Quãng đường.", "Thời gian."],
    correctIndex: 1,
    explanation: "Hệ số góc k = Δd / Δt = v (Vận tốc)."
  },
  {
    id: 31,
    category: "Bài 7. Đồ thị độ dịch chuyển – thời gian (d - t)",
    level: "Thông hiểu",
    question: "Trên đồ thị (d - t), một đoạn đường song song với trục thời gian Ot cho biết trạng thái chuyển động nào của vật?",
    options: [
      "Vật đang đứng yên (v = 0).",
      "Vật đang chuyển động thẳng đều.",
      "Vật đang chuyển động nhanh dần.",
      "Vật đang chuyển động chậm dần."
    ],
    correctIndex: 0,
    explanation: "d không thay đổi theo thời gian ⟹ Vật đang đứng yên (v = 0)."
  },
  {
    id: 32,
    category: "Bài 7. Đồ thị độ dịch chuyển – thời gian (d - t)",
    level: "Thông hiểu",
    question: "Từ thời điểm t₁ = 2 s đến t₂ = 6 s, độ dịch chuyển của vật tăng đều từ d₁ = 10 m đến d₂ = 30 m. Vận tốc của vật trong khoảng thời gian này là:",
    options: ["5 m/s", "10 m/s", "2,5 m/s", "20 m/s"],
    correctIndex: 0,
    explanation: "v = (d₂ - d₁) / (t₂ - t₁) = (30 - 10) / (6 - 2) = 20 / 4 = 5 m/s."
  },
  {
    id: 33,
    category: "Bài 7. Đồ thị độ dịch chuyển – thời gian (d - t)",
    level: "Thông hiểu",
    question: "Hình vẽ đồ thị (d - t) đi xuống từ d = 40 m về d = 0 m trong thời gian 8 s. Vận tốc v và tốc độ v_tốc độ của vật là:",
    options: [
      "v = -5 m/s; tốc độ = 5 m/s",
      "v = 5 m/s; tốc độ = 5 m/s",
      "v = -5 m/s; tốc độ = -5 m/s",
      "v = 0 m/s; tốc độ = 5 m/s"
    ],
    correctIndex: 0,
    explanation: "v = (0 - 40) / 8 = -5 m/s; Tốc độ = |v| = 5 m/s."
  },
  {
    id: 34,
    category: "Bài 7. Đồ thị độ dịch chuyển – thời gian (d - t)",
    level: "Thông hiểu",
    question: "So sánh hai đồ thị (d - t) của vật A và vật B: Đường A có độ dốc lớn hơn đường B. Kết luận nào sau đây đúng?",
    options: [
      "Vật A có tốc độ lớn hơn vật B.",
      "Vật B có tốc độ lớn hơn vật A.",
      "Hai vật có tốc độ bằng nhau.",
      "Vật A có gia tốc lớn hơn vật B."
    ],
    correctIndex: 0,
    explanation: "Độ dốc của đồ thị d-t lớn hơn nghĩa là tốc độ lớn hơn."
  },

  // Bài 8 (35..40)
  {
    id: 35,
    category: "Bài 8. Chuyển động biến đổi & Gia tốc",
    level: "Nhận biết",
    question: "Gia tốc là đại lượng đặc trưng cho:",
    options: [
      "Mức độ nhanh hay chậm của sự biến thiên vận tốc theo thời gian.",
      "Mức độ nhanh hay chậm của chuyển động.",
      "Độ dài quãng đường đi được trong một đơn vị thời gian.",
      "Sự thay đổi vị trí của vật trong không gian."
    ],
    correctIndex: 0,
    explanation: "Gia tốc a = Δv / Δt đặc trưng cho tốc độ biến thiên của vận tốc."
  },
  {
    id: 36,
    category: "Bài 8. Chuyển động biến đổi & Gia tốc",
    level: "Nhận biết",
    question: "Đơn vị đo của gia tốc trong hệ đơn vị SI là:",
    options: ["m/s", "m/s²", "km/h", "m·s"],
    correctIndex: 1,
    explanation: "Đơn vị chuẩn của gia tốc là m/s²."
  },
  {
    id: 37,
    category: "Bài 8. Chuyển động biến đổi & Gia tốc",
    level: "Thông hiểu",
    question: "Một xe máy đang chuyển động với vận tốc 10 m/s thì tăng tốc, sau 5 s đạt vận tốc 20 m/s. Gia tốc trung bình của xe máy là:",
    options: ["2 m/s²", "4 m/s²", "1 m/s²", "0,5 m/s²"],
    correctIndex: 0,
    explanation: "a = (20 - 10) / 5 = 10 / 5 = 2 m/s²."
  },
  {
    id: 38,
    category: "Bài 8. Chuyển động biến đổi & Gia tốc",
    level: "Thông hiểu",
    question: "Chuyển động thẳng nào sau đây là chuyển động chậm dần?",
    options: [
      "a > 0 và v > 0",
      "a < 0 và v < 0",
      "a > 0 và v < 0",
      "a = 0 và v ≠ 0"
    ],
    correctIndex: 2,
    explanation: "Chậm dần khi a và v ngược dấu: a·v < 0 (ở đây a > 0 và v < 0 ⟹ a·v < 0)."
  },
  {
    id: 39,
    category: "Bài 8. Chuyển động biến đổi & Gia tốc",
    level: "Thông hiểu",
    question: "Một ô tô đang di chuyển với vận tốc 15 m/s thì hãm phanh chuyển động chậm dần, sau 10 s thì dừng hẳn. Gia tốc của ô tô là:",
    options: ["-1,5 m/s²", "1,5 m/s²", "-0,67 m/s²", "150 m/s²"],
    correctIndex: 0,
    explanation: "Dừng hẳn ⟹ v₂ = 0. a = (0 - 15) / 10 = -1,5 m/s²."
  },
  {
    id: 40,
    category: "Bài 8. Chuyển động biến đổi & Gia tốc",
    level: "Nhận biết",
    question: "Vectơ gia tốc a⃗ trong chuyển động thẳng nhanh dần có đặc điểm gì so với vectơ vận tốc v⃗?",
    options: ["Cùng chiều với v⃗.", "Ngược chiều với v⃗.", "Vuông góc với v⃗.", "Hợp với v⃗ một góc 45°."],
    correctIndex: 0,
    explanation: "Nhanh dần ⟹ Gia tốc a⃗ cùng chiều với vận tốc v⃗."
  },

  // Bài 9 (41..48)
  {
    id: 41,
    category: "Bài 9. Chuyển động thẳng biến đổi đều",
    level: "Nhận biết",
    question: "Công thức nào sau đây là công thức tính vận tốc của chuyển động thẳng biến đổi đều?",
    options: ["v = v₀ + a·t", "v = v₀ + 1/2·a·t²", "v = a·t²", "v = v₀² + 2ad"],
    correctIndex: 0,
    explanation: "Công thức vận tốc CĐTBĐĐ: v = v₀ + a·t."
  },
  {
    id: 42,
    category: "Bài 9. Chuyển động thẳng biến đổi đều",
    level: "Nhận biết",
    question: "Công thức liên hệ giữa gia tốc a, vận tốc ban đầu v₀, vận tốc cuối v và độ dịch chuyển d trong CĐTBĐĐ là:",
    options: ["v² - v₀² = 2ad", "v - v₀ = 2ad", "v² + v₀² = 2ad", "v² - v₀² = ad"],
    correctIndex: 0,
    explanation: "Công thức độc lập thời gian: v² - v₀² = 2·a·d."
  },
  {
    id: 43,
    category: "Bài 9. Chuyển động thẳng biến đổi đều",
    level: "Thông hiểu",
    question: "Một xe bắt đầu chuyển động nhanh dần đều từ trạng thái nghỉ (v₀ = 0) với gia tốc 2 m/s². Quãng đường xe đi được sau 4 s là:",
    options: ["16 m", "8 m", "32 m", "4 m"],
    correctIndex: 0,
    explanation: "d = s = 1/2·a·t² = 1/2 × 2 × 4² = 16 m."
  },
  {
    id: 44,
    category: "Bài 9. Chuyển động thẳng biến đổi đều",
    level: "Thông hiểu",
    question: "Một ô tô đang chạy với vận tốc 20 m/s thì hãm phanh chậm dần đều với gia tốc có độ lớn 2 m/s². Thời gian từ lúc hãm phanh đến khi xe dừng hẳn là:",
    options: ["10 s", "20 s", "5 s", "40 s"],
    correctIndex: 0,
    explanation: "v = v₀ + a·t ⟹ 0 = 20 - 2·t ⟹ t = 10 s."
  },
  {
    id: 45,
    category: "Bài 9. Chuyển động thẳng biến đổi đều",
    level: "Thông hiểu",
    question: "Một đoàn tàu bắt đầu rời ga chuyển động nhanh dần đều với gia tốc 0,5 m/s². Vận tốc của tàu khi đi được quãng đường 100 m là:",
    options: ["10 m/s", "20 m/s", "100 m/s", "5 m/s"],
    correctIndex: 0,
    explanation: "v² - 0 = 2 × 0,5 × 100 = 100 ⟹ v = √100 = 10 m/s."
  },
  {
    id: 46,
    category: "Bài 9. Chuyển động thẳng biến đổi đều",
    level: "Nhận biết",
    question: "Đồ thị vận tốc – thời gian (v - t) của một vật chuyển động thẳng biến đổi đều có dạng là:",
    options: [
      "Một đường thẳng xiên góc.",
      "Một đường parabol.",
      "Một đường thẳng song song trục Ot.",
      "Một đường tròn."
    ],
    correctIndex: 0,
    explanation: "v = v₀ + a·t là hàm bậc nhất theo t nên đồ thị v-t là đường thẳng xiên góc."
  },
  {
    id: 47,
    category: "Bài 9. Chuyển động thẳng biến đổi đều",
    level: "Thông hiểu",
    question: "Phương trình độ dịch chuyển của một vật là d = 5t + 2t² (m, s). Gia tốc a và vận tốc ban đầu v₀ của vật là:",
    options: [
      "a = 4 m/s²; v₀ = 5 m/s",
      "a = 2 m/s²; v₀ = 5 m/s",
      "a = 5 m/s²; v₀ = 2 m/s",
      "a = 4 m/s²; v₀ = 2 m/s"
    ],
    correctIndex: 0,
    explanation: "So sánh d = v₀·t + 1/2·a·t² ⟹ v₀ = 5 m/s; 1/2·a = 2 ⟹ a = 4 m/s²."
  },
  {
    id: 48,
    category: "Bài 9. Chuyển động thẳng biến đổi đều",
    level: "Thông hiểu",
    question: "Một xe chuyển động chậm dần đều có v₀ = 12 m/s và gia tốc a = -2 m/s². Quãng đường xe đi được trong giây thứ nhất (từ t = 0 đến t = 1 s) là:",
    options: ["11 m", "10 m", "12 m", "9 m"],
    correctIndex: 0,
    explanation: "s(1) = 12(1) + 1/2(-2)(1)² = 12 - 1 = 11 m."
  },

  // Bài 10 (49..54)
  {
    id: 49,
    category: "Bài 10. Sự rơi tự do",
    level: "Nhận biết",
    question: "Chuyển động rơi tự do là chuyển động:",
    options: [
      "Thẳng nhanh dần đều theo phương thẳng đứng, chiều từ trên xuống.",
      "Thẳng đều theo phương ngang.",
      "Thẳng chậm dần đều theo phương thẳng đứng.",
      "Cong đều trong không gian."
    ],
    correctIndex: 0,
    explanation: "Rơi tự do là CĐ thẳng nhanh dần đều phương thẳng đứng, chiều từ trên xuống."
  },
  {
    id: 50,
    category: "Bài 10. Sự rơi tự do",
    level: "Nhận biết",
    question: "Tại cùng một vị trí địa lí trên Trái Đất, mọi vật rơi tự do đều rơi với cùng một:",
    options: ["Gia tốc g.", "Vận tốc.", "Thời gian rơi.", "Quãng đường."],
    correctIndex: 0,
    explanation: "Tại cùng một vị trí, mọi vật rơi tự do có cùng gia tốc g."
  },
  {
    id: 51,
    category: "Bài 10. Sự rơi tự do",
    level: "Thông hiểu",
    question: "Thả một hòn đá rơi tự do từ độ cao h xuống đất tại nơi có g = 10 m/s². Tốc độ hòn đá khi chạm đất sau 3 s rơi là:",
    options: ["30 m/s", "45 m/s", "15 m/s", "90 m/s"],
    correctIndex: 0,
    explanation: "v = g·t = 10 × 3 = 30 m/s."
  },
  {
    id: 52,
    category: "Bài 10. Sự rơi tự do",
    level: "Thông hiểu",
    question: "Thả rơi tự do một vật từ độ cao h = 20 m xuống đất tại nơi có g = 10 m/s². Thời gian rơi t của vật là:",
    options: ["2 s", "4 s", "1 s", "2,83 s"],
    correctIndex: 0,
    explanation: "h = 1/2·g·t² ⟹ 20 = 5·t² ⟹ t² = 4 ⟹ t = 2 s."
  },
  {
    id: 53,
    category: "Bài 10. Sự rơi tự do",
    level: "Thông hiểu",
    question: "Một vật rơi tự do từ độ cao h. Nếu thời gian rơi tăng gấp đôi thì độ cao h ban đầu phải tăng lên mấy lần?",
    options: ["Gấp 4 lần.", "Gấp 2 lần.", "Gấp 8 lần.", "Không đổi."],
    correctIndex: 0,
    explanation: "h = 1/2·g·t² nên h tỉ lệ thuận với t². t tăng 2 lần ⟹ h tăng 2² = 4 lần."
  },
  {
    id: 54,
    category: "Bài 10. Sự rơi tự do",
    level: "Thông hiểu",
    question: "Một vật rơi tự do từ tầng cao tòa nhà hết 4 s chạm đất (g = 10 m/s²). Độ cao tầng nhà thả vật là:",
    options: ["80 m", "40 m", "160 m", "20 m"],
    correctIndex: 0,
    explanation: "h = 1/2·g·t² = 1/2 × 10 × 4² = 80 m."
  }
];

export const TRUE_FALSE_BANK: TrueFalseQuestion[] = [
  {
    id: 1,
    category: "Đồ thị (d - t) & Tốc độ vận tốc (Chuẩn Ma trận 2-I)",
    context: "Một vật chuyển động thẳng có đồ thị độ dịch chuyển – thời gian (d - t) như sau: Từ t = 0 đến t = 4 s, d tăng từ 0 đến 20 m. Từ t = 4 s đến t = 8 s, d giữ nguyên ở 20 m. Từ t = 8 s đến t = 10 s, d giảm từ 20 m về 0 m.",
    statements: [
      { label: "a", statement: "Trong 4 giây đầu tiên, vật chuyển động thẳng đều với vận tốc v = 5 m/s theo chiều dương.", isCorrect: true, explanation: "v₁ = (20 - 0) / 4 = 5 m/s > 0." },
      { label: "b", statement: "Trong khoảng thời gian từ t = 4 s đến t = 8 s, vật chuyển động chậm dần đều.", isCorrect: false, explanation: "d giữ nguyên ở 20 m nghĩa là vật đang ĐỨNG YÊN (v = 0)." },
      { label: "c", statement: "Trong 2 giây cuối (t = 8 s đến 10 s), vận tốc của vật là v = -10 m/s.", isCorrect: true, explanation: "v₃ = (0 - 20) / (10 - 8) = -10 m/s." },
      { label: "d", statement: "Độ dịch chuyển tổng cộng của vật sau 10 giây chuyển động là d = 40 m.", isCorrect: false, explanation: "Vật đi từ 0m đến 20m rồi về lại 0m nên điểm cuối trùng điểm đầu ⟹ d_tổng = 0 m (Quãng đường s = 40m)." }
    ]
  },
  {
    id: 2,
    category: "Chuyển động thẳng biến đổi đều (Chuẩn Ma trận 2-II)",
    context: "Một xe ô tô bắt đầu khởi hành từ trạng thái nghỉ (v₀ = 0) chuyển động thẳng nhanh dần đều với gia tốc a = 2 m/s² trên đường thẳng nằm ngang.",
    statements: [
      { label: "a", statement: "Sau 5 giây kể từ khi khởi hành, vận tốc của xe đạt 10 m/s.", isCorrect: true, explanation: "v = 0 + 2 × 5 = 10 m/s." },
      { label: "b", statement: "Quãng đường xe đi được trong 5 giây đầu tiên là s = 25 m.", isCorrect: true, explanation: "s = 1/2 × 2 × 5² = 25 m." },
      { label: "c", statement: "Vận tốc trung bình của xe trong khoảng thời gian từ t = 0 đến t = 5 s là 10 m/s.", isCorrect: false, explanation: "v_tb = s / t = 25 / 5 = 5 m/s." },
      { label: "d", statement: "Quãng đường xe đi được riêng trong giây thứ 5 (từ t = 4 s đến t = 5 s) là 9 m.", isCorrect: true, explanation: "s(4) = 1/2 × 2 × 4² = 16 m; s(5) = 25 m ⟹ Δs = 25 - 16 = 9 m." }
    ]
  },
  {
    id: 3,
    category: "Công thức cộng vận tốc & Chuyển động tháp thuyền",
    context: "Một con thuyền chuyển động trên dòng sông chảy với vận tốc của nước so với bờ là v_nb = 2 m/s. Vận tốc của thuyền so với nước là v_tn = 5 m/s.",
    statements: [
      { label: "a", statement: "Khi thuyền chạy xuôi dòng, tốc độ của thuyền so với bờ là 7 m/s.", isCorrect: true, explanation: "v_tb = 5 + 2 = 7 m/s." },
      { label: "b", statement: "Khi thuyền chạy ngược dòng, tốc độ của thuyền so với bờ là 3 m/s.", isCorrect: true, explanation: "v_tb = 5 - 2 = 3 m/s." },
      { label: "c", statement: "Khi chèo thuyền hướng vuông góc với dòng sông, tốc độ của thuyền so với bờ là 5,39 m/s.", isCorrect: true, explanation: "v = √(5² + 2²) = √29 ≈ 5,39 m/s." },
      { label: "d", statement: "Nếu thuyền tắt máy trôi tự do theo dòng nước, vận tốc của thuyền so với bờ bằng 0.", isCorrect: false, explanation: "Tắt máy trôi theo dòng thì v_tb = v_nước = 2 m/s." }
    ]
  },
  {
    id: 4,
    category: "Sự rơi tự do & Môi trường không khí",
    context: "Thả hai vật rơi từ cùng một độ cao h trong hai môi trường khác nhau: trong phòng thí nghiệm (có không khí) và trong ống hút chân không. Lấy g = 9,8 m/s².",
    statements: [
      { label: "a", statement: "Trong ống hút chân không, tờ giấy nhem và hòn bi thép sẽ rơi chạm đáy cùng một lúc.", isCorrect: true, explanation: "Trong chân không mọi vật rơi tự do như nhau." },
      { label: "b", statement: "Trong không khí, hòn bi thép rơi chạm đất trước tờ giấy vì trọng lực tác dụng lên hòn bi lớn hơn.", isCorrect: false, explanation: "Do lực cản không khí tác dụng lên tờ giấy lớn so với trọng lượng của nó, không phải do trọng lực." },
      { label: "c", statement: "Chuyển động rơi tự do trong chân không có gia tốc không đổi a = g = 9,8 m/s².", isCorrect: true, explanation: "Rơi tự do là CĐTBĐĐ với gia tốc g." },
      { label: "d", statement: "Vận tốc chạm đất của vật rơi tự do không phụ thuộc vào độ cao thả h.", isCorrect: false, explanation: "v = √(2gh) nên vận tốc chạm đất phụ thuộc căn bậc hai của độ cao h." }
    ]
  },
  {
    id: 5,
    category: "Chuyển động thẳng chậm dần đều & Ô tô hãm phanh",
    context: "Một ô tô đang di chuyển thẳng với vận tốc 72 km/h (20 m/s) thì người lái xe nhìn thấy chướng ngại vật và đạp phanh gấp. Xe chuyển động chậm dần đều với gia tốc a = -4 m/s².",
    statements: [
      { label: "a", statement: "Vận tốc ban đầu của xe khi đổi sang hệ SI là v₀ = 20 m/s.", isCorrect: true, explanation: "72 / 3,6 = 20 m/s." },
      { label: "b", statement: "Thời gian kể từ lúc đạp phanh đến khi xe dừng hẳn là 5 s.", isCorrect: true, explanation: "t = (0 - 20) / (-4) = 5 s." },
      { label: "c", statement: "Quãng đường xe đi được trong quá trình hãm phanh dừng hẳn là 50 m.", isCorrect: true, explanation: "s = (0² - 20²) / (2 × -4) = -400 / -8 = 50 m." },
      { label: "d", statement: "Sau 6 s kể từ lúc đạp phanh, vận tốc của xe là -4 m/s.", isCorrect: false, explanation: "Xe đã dừng hẳn sau 5 s (v = 0 m/s) và đứng yên, không chạy lùi." }
    ]
  },
  {
    id: 6,
    category: "Phép đo sai số & Đồng hồ cổng quang",
    context: "Một nhóm học sinh dùng Cổng quang điện và Đồng hồ hiện số để đo thời gian tấm chắn sáng d = 20 mm đi qua cổng. Kết quả 5 lần đo thu được thời gian t lần lượt là: 0,020 s; 0,021 s; 0,019 s; 0,020 s; 0,020 s.",
    statements: [
      { label: "a", statement: "Giá trị trung bình của thời gian đo được là t̄ = 0,020 s.", isCorrect: true, explanation: "(0,020+0,021+0,019+0,020+0,020)/5 = 0,020 s." },
      { label: "b", statement: "Tốc độ trung bình tính được của tấm chắn sáng là v̄ = 1,0 m/s.", isCorrect: true, explanation: "v̄ = d / t̄ = 0,020 m / 0,020 s = 1,0 m/s." },
      { label: "c", statement: "Sai số tuyệt đối ngẫu nhiên trung bình của thời gian Δt̄ = 0,0004 s.", isCorrect: true, explanation: "(|0|+|0,001|+|0,001|+|0|+|0|)/5 = 0,0004 s." },
      { label: "d", statement: "Sử dụng hai cổng quang điện giúp xác định trực tiếp gia tốc của vật.", isCorrect: true, explanation: "Hai cổng quang đo được v₁ và v₂ cùng khoảng thời gian t giữa 2 cổng ⟹ a = (v₂ - v₁) / t." }
    ]
  }
];

export const SHORT_ANSWER_BANK: ShortAnswerQuestion[] = [
  {
    id: 1,
    category: "Tốc độ & Vận tốc",
    level: "Nhận biết",
    question: "Một xe máy chạy trên đoạn đường thẳng dài 18 km mất thời gian 30 phút. Tốc độ trung bình của xe máy tính theo đơn vị m/s bằng bao nhiêu?",
    correctAnswer: "10",
    unit: "m/s",
    explanation: "s = 18000 m, t = 1800 s ⟹ v = 18000 / 1800 = 10 m/s."
  },
  {
    id: 2,
    category: "Sự rơi tự do",
    level: "Thông hiểu",
    question: "Thả rơi tự do một hòn bi từ độ cao h = 45 m xuống đất tại nơi có g = 10 m/s². Tính vận tốc chạm đất của hòn bi theo m/s.",
    correctAnswer: "30",
    unit: "m/s",
    explanation: "v = √(2gh) = √(2 × 10 × 45) = √900 = 30 m/s."
  },
  {
    id: 3,
    category: "Chuyển động thẳng biến đổi đều",
    level: "Thông hiểu",
    question: "Một ô tô bắt đầu chuyển động nhanh dần đều với gia tốc a = 3 m/s². Tính vận tốc của ô tô sau 6 s khởi hành (theo m/s).",
    correctAnswer: "18",
    unit: "m/s",
    explanation: "v = v₀ + a·t = 0 + 3 × 6 = 18 m/s."
  },
  {
    id: 4,
    category: "Chuyển động thẳng biến đổi đều",
    level: "Thông hiểu",
    question: "Một xe đạp đang đi với tốc độ 4 m/s thì xuống dốc chuyển động nhanh dần đều với gia tốc 0,5 m/s². Quãng đường xe đi được sau 10 s là bao nhiêu mét?",
    correctAnswer: "65",
    unit: "m",
    explanation: "s = v₀·t + 1/2·a·t² = 4(10) + 0,5 × 0,5 × (10)² = 40 + 25 = 65 m."
  },
  {
    id: 5,
    category: "Độ dịch chuyển",
    level: "Thông hiểu",
    question: "Một người đi bộ 6 km về phía Đông, sau đó rẽ Bắc đi tiếp 8 km. Độ lớn độ dịch chuyển của người đó bằng bao nhiêu kilomet?",
    correctAnswer: "10",
    unit: "km",
    explanation: "|d| = √(6² + 8²) = 10 km."
  },
  {
    id: 6,
    category: "Gia tốc",
    level: "Nhận biết",
    question: "Vận tốc của một vật tăng đều từ 5 m/s lên 25 m/s trong khoảng thời gian 4 s. Gia tốc của vật bằng bao nhiêu m/s²?",
    correctAnswer: "5",
    unit: "m/s²",
    explanation: "a = (25 - 5) / 4 = 5 m/s²."
  },
  {
    id: 7,
    category: "Sự rơi tự do",
    level: "Thông hiểu",
    question: "Một vật rơi tự do chạm đất mất thời gian t = 4 s tại nơi có g = 9,8 m/s². Độ cao thả vật bằng bao nhiêu mét? (Làm tròn đến hàng đơn vị)",
    correctAnswer: "78",
    unit: "m",
    explanation: "h = 1/2 × 9,8 × 4² = 78,4 ≈ 78 m."
  },
  {
    id: 8,
    category: "Cộng vận tốc",
    level: "Thông hiểu",
    question: "Một người đi trên băng chuyền động đang di chuyển với vận tốc 1 m/s so với đất. Nếu người đó đi cùng chiều băng chuyền với vận tốc 1,5 m/s so với mặt băng chuyền thì vận tốc người đó so với đất bằng bao nhiêu m/s?",
    correctAnswer: "2.5",
    unit: "m/s",
    explanation: "v_người_đất = 1,5 + 1 = 2,5 m/s."
  },
  {
    id: 9,
    category: "CĐTBĐĐ",
    level: "Vận dụng",
    question: "Một viên bi lăn xuống một máng nghiêng dài 2 m với gia tốc a = 1 m/s² không vận tốc đầu. Thời gian viên bi lăn hết máng nghiêng bằng bao nhiêu giây?",
    correctAnswer: "2",
    unit: "s",
    explanation: "s = 1/2·a·t² ⟹ 2 = 0,5 × 1 × t² ⟹ t² = 4 ⟹ t = 2 s."
  },
  {
    id: 10,
    category: "CĐTBĐĐ",
    level: "Vận dụng",
    question: "Một xe ô tô hãm phanh dừng hẳn sau khi đi được quãng đường 36 m. Gia tốc của xe là a = -2 m/s². Vận tốc ban đầu v₀ của xe trước khi hãm phanh bằng bao nhiêu m/s?",
    correctAnswer: "12",
    unit: "m/s",
    explanation: "v² - v₀² = 2ad ⟹ 0 - v₀² = 2(-2)(36) = -144 ⟹ v₀ = 12 m/s."
  },
  {
    id: 11,
    category: "Sai số phép đo",
    level: "Thông hiểu",
    question: "Một thước kẻ có độ chia nhỏ nhất (ĐCNN) là 1 mm. Bán kính một hình tròn đo được là R = 100 mm. Sai số tương đối dụng cụ của bán kính δR (%) bằng bao nhiêu?",
    correctAnswer: "0.5",
    unit: "%",
    explanation: "ΔR_dc = 1/2 ĐCNN = 0,5 mm. δR = (0,5 / 100) × 100% = 0,5%."
  },
  {
    id: 12,
    category: "Đồ thị (d - t)",
    level: "Thông hiểu",
    question: "Từ đồ thị d-t, vật di chuyển từ vị trí x₁ = 10 m lúc t₁ = 1 s đến vị trí x₂ = 40 m lúc t₂ = 7 s. Vận tốc của vật bằng bao nhiêu m/s?",
    correctAnswer: "5",
    unit: "m/s",
    explanation: "v = (40 - 10) / (7 - 1) = 30 / 6 = 5 m/s."
  }
];

export const ESSAY_BANK: EssayQuestion[] = [
  {
    id: 1,
    category: "Tốc độ, Vận tốc & Cộng vận tốc (Phần IV - Câu 1)",
    title: "Bài toán thuyền chuyển động trên sông",
    problemStatement: "Một con thuyền đi từ bến A đến bến B trên một đường thẳng sông dài 12 km rồi quay trở lại bến A. Vận tốc của thuyền so với nước yên lặng là 15 km/h, vận tốc của dòng nước so với bờ là 3 km/h. Tính:\na) Vận tốc của thuyền so với bờ khi đi xuôi dòng và khi đi ngược dòng.\nb) Tổng thời gian cả đi và về của con thuyền.",
    gradingGuide: [
      { step: "a) Viết đúng công thức cộng vận tốc v⃗₁₃ = v⃗₁₂ + v⃗₂₃ và tính v_xuôi = 18 km/h, v_ngược = 12 km/h", points: "0,50 đ" },
      { step: "b) Tính thời gian đi xuôi t_xuôi = 12/18 = 2/3 h (40 phút) và t_ngược = 12/12 = 1 h", points: "0,25 đ" },
      { step: "Tính tổng thời gian t_tổng = 2/3 + 1 = 5/3 h (1 giờ 40 phút) và kết luận đúng", points: "0,25 đ" }
    ],
    detailedSolution: "a) Gọi 1 là thuyền, 2 là nước, 3 là bờ.\nKhi xuôi dòng: v₁₃ = v₁₂ + v₂₃ = 15 + 3 = 18 km/h.\nKhi ngược dòng: v₁₃ = v₁₂ - v₂₃ = 15 - 3 = 12 km/h.\n\nb) Thời gian đi xuôi dòng: t₁ = s / v_xuôi = 12 / 18 = 2/3 h.\nThời gian đi ngược dòng: t₂ = s / v_ngược = 12 / 12 = 1 h.\nTổng thời gian chuyến đi: t = t₁ + t₂ = 2/3 + 1 = 5/3 h ≈ 1 giờ 40 phút."
  },
  {
    id: 2,
    category: "Chuyển động thẳng biến đổi đều (Phần IV - Câu 2)",
    title: "Bài toán xe hãm phanh tránh chướng ngại vật",
    problemStatement: "Một xe ô tô đang di chuyển thẳng với vận tốc 54 km/h thì người lái xe bất ngờ phát hiện chướng ngại vật cách xe 40 m. Người lái xe lập tức đạp phanh, xe chuyển động chậm dần đều với gia tốc a = -3 m/s².\na) Sau bao lâu kể từ lúc đạp phanh thì xe dừng hẳn?\nb) Xe có tông vào chướng ngại vật hay không? Xe dừng lại cách chướng ngại vật bao nhiêu mét?",
    gradingGuide: [
      { step: "Đổi đơn vị v₀ = 54 km/h = 15 m/s", points: "0,25 đ" },
      { step: "a) Áp dụng v = v₀ + a·t ⟹ 0 = 15 - 3·t ⟹ t = 5 s", points: "0,25 đ" },
      { step: "b) Áp dụng v² - v₀² = 2ad ⟹ s = -15² / (2 × -3) = 37,5 m", points: "0,25 đ" },
      { step: "So sánh s = 37,5 m < 40 m ⟹ Xe KHÔNG tông chướng ngại vật, dừng cách 2,5 m", points: "0,25 đ" }
    ],
    detailedSolution: "Đổi v₀ = 54 km/h = 15 m/s.\na) Thời gian đến khi dừng hẳn (v = 0):\nv = v₀ + a·t ⟹ 0 = 15 - 3t ⟹ t = 5 s.\n\nb) Quãng đường hãm phanh đến khi dừng hẳn:\nv² - v₀² = 2·a·s ⟹ 0² - 15² = 2·(-3)·s ⟹ -225 = -6·s ⟹ s = 37,5 m.\nVì s = 37,5 m < 40 m nên xe KHÔNG tông vào chướng ngại vật.\nKhoảng cách còn lại từ xe đến chướng ngại vật: Δd = 40 - 37,5 = 2,5 m."
  },
  {
    id: 3,
    category: "Bài toán Hai xe gặp nhau trong CĐTBĐĐ (Phần IV - Câu 3)",
    title: "Hai ô tô chuyển động ngược chiều gặp nhau",
    problemStatement: "Cùng một lúc tại hai điểm A và B cách nhau 120 m trên một đường thẳng, xe thứ nhất qua A chuyển động nhanh dần đều về B không vận tốc đầu với gia tốc a₁ = 1 m/s². Xe thứ hai qua B chuyển động thẳng đều về A với vận tốc v₂ = 10 m/s. Chọn gốc tọa độ O tại A, chiều dương từ A đến B, gốc thời gian t = 0 lúc hai xe bắt đầu chuyển động.\na) Lập phương trình chuyển động của hai xe.\nb) Xác định thời điểm và vị trí hai xe gặp nhau.",
    gradingGuide: [
      { step: "a) Viết đúng PT xe 1: x₁ = 0,5·t² (m) và PT xe 2: x₂ = 120 - 10·t (m)", points: "0,50 đ" },
      { step: "b) Cho x₁ = x₂ ⟹ 0,5·t² + 10·t - 120 = 0 ⟹ t = 12 s (loại t = -20)", points: "0,25 đ" },
      { step: "Thay t = 12 s vào x₁ tính vị trí gặp nhau x = 72 m cách A", points: "0,25 đ" }
    ],
    detailedSolution: "a) Phương trình chuyển động:\n- Xe 1 (tại A, v₀₁ = 0, a₁ = 1 m/s²): x₁ = x₀₁ + v₀₁·t + 1/2·a₁·t² = 0,5·t² (m).\n- Xe 2 (tại B, x₀₂ = 120 m, chuyển động ngược chiều dương v₂ = -10 m/s): x₂ = 120 - 10·t (m).\n\nb) Hai xe gặp nhau khi x₁ = x₂:\n0,5·t² = 120 - 10·t ⇔ 0,5·t² + 10·t - 120 = 0.\nGiải phương trình bậc hai thu được t = 12 s (nhận) hoặc t = -20 s (loại).\nThay t = 12 s vào x₁: x = 0,5 × (12)² = 72 m.\nVậy hai xe gặp nhau sau 12 giây kể từ lúc xuất phát, tại vị trí cách A một khoảng 72 m."
  },
  {
    id: 4,
    category: "Chuyển động thẳng biến đổi đều (Phần IV - VDC)",
    title: "Tính gia tốc và quãng đường từ hai khoảng thời gian liên tiếp",
    problemStatement: "Một vật chuyển động thẳng nhanh dần đều không vận tốc đầu (v₀ = 0). Trong giây đầu tiên vật đi được quãng đường s₁ = 2 m. Tính:\na) Gia tốc a của vật.\nb) Quãng đường s₂ vật đi được trong giây thứ 3.",
    gradingGuide: [
      { step: "a) s₁ = 1/2·a·(1)² = 2 m ⟹ a = 4 m/s²", points: "0,50 đ" },
      { step: "b) Quãng đường sau 3 giây: s(3) = 1/2·4·3² = 18 m", points: "0,25 đ" },
      { step: "Quãng đường sau 2 giây: s(2) = 1/2·4·2² = 8 m ⟹ s₂ = 18 - 8 = 10 m", points: "0,25 đ" }
    ],
    detailedSolution: "a) Quãng đường đi trong giây đầu tiên (t = 1 s):\ns₁ = 1/2·a·t₁² ⟹ 2 = 1/2·a·(1)² ⟹ a = 4 m/s².\n\nb) Quãng đường đi trong giây thứ 3:\n- Quãng đường sau 3s: s(3) = 1/2 × 4 × 3² = 18 m.\n- Quãng đường sau 2s: s(2) = 1/2 × 4 × 2² = 8 m.\n- Quãng đường trong giây thứ 3: Δs = s(3) - s(2) = 18 - 8 = 10 m."
  }
];

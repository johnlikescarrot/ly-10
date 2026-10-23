import { MCQuestion, TFQuestion, ShortAnswerQuestion, EssayQuestion } from '../types/index.js';

export const bankMCQs: MCQuestion[] = [
  // Lesson 1
  {
    id: 'bank-mcq-1',
    number: 1,
    lessonId: 'lesson-1',
    lessonName: 'Bài 1: Làm quen Vật lí',
    content: 'Đối tượng nghiên cứu chính của môn Vật lí là gì?',
    options: [
      { label: 'A', text: 'Sự phát triển của các loài sinh vật trong tự nhiên.' },
      { label: 'B', text: 'Các dạng vận động của vật chất và năng lượng.' },
      { label: 'C', text: 'Các phản ứng hóa học tạo ra chất mới.' },
      { label: 'D', text: 'Cấu tạo địa chất của vỏ Trái Đất.' }
    ],
    correctOption: 'B',
    explanation: 'Vật lí là ngành khoa học nghiên cứu về các dạng vận động của vật chất và năng lượng.',
    level: 'Nhận biết'
  },
  {
    id: 'bank-mcq-2',
    number: 2,
    lessonId: 'lesson-1',
    lessonName: 'Bài 1: Làm quen Vật lí',
    content: 'Phương pháp nghiên cứu truyền thống và đặc trưng của Vật lí bao gồm hai phương pháp chính nào?',
    options: [
      { label: 'A', text: 'Phương pháp thực nghiệm và phương pháp mô hình.' },
      { label: 'B', text: 'Phương pháp khảo sát và phương pháp phỏng vấn.' },
      { label: 'C', text: 'Phương pháp quy nạp và phương pháp diễn dịch.' },
      { label: 'D', text: 'Phương pháp thống kê và phương pháp dự báo.' }
    ],
    correctOption: 'A',
    explanation: 'Hai phương pháp nghiên cứu chính trong Vật lí là phương pháp thực nghiệm và phương pháp mô hình.',
    level: 'Nhận biết'
  },
  // Lesson 2
  {
    id: 'bank-mcq-3',
    number: 3,
    lessonId: 'lesson-2',
    lessonName: 'Bài 2: Quy tắc an toàn',
    content: 'Biển báo có dạng hình tròn, nền xanh dương, hình vẽ màu trắng thuộc nhóm biển báo nào?',
    options: [
      { label: 'A', text: 'Biển báo cấm.' },
      { label: 'B', text: 'Biển báo bắt buộc thực hiện.' },
      { label: 'C', text: 'Biển báo cảnh báo nguy hiểm.' },
      { label: 'D', text: 'Biển báo chỉ dẫn thông thường.' }
    ],
    correctOption: 'B',
    explanation: 'Hình tròn nền xanh dương, hình vẽ màu trắng là đặc nhận dạng của biển báo BẮT BUỘC THỰC HIỆN.',
    level: 'Nhận biết'
  },
  {
    id: 'bank-mcq-4',
    number: 4,
    lessonId: 'lesson-2',
    lessonName: 'Bài 2: Quy tắc an toàn',
    content: 'Khi sử dụng các thiết bị điện trong phòng thực hành Vật lí, hành vi nào sau đây MẤT AN TOÀN?',
    options: [
      { label: 'A', text: 'Rút phích cắm điện bằng cách cầm vào thân phích cắm.' },
      { label: 'B', text: 'Nối nguồn điện khi tay đang bị ướt.' },
      { label: 'C', text: 'Kiểm tra vỏ cách điện của dây dẫn trước khi cắm điện.' },
      { label: 'D', text: 'Tắt công tắc nguồn trước khi tháo lắp mạch điện.' }
    ],
    correctOption: 'B',
    explanation: 'Chạm tay ướt vào nguồn điện có nguy cơ cao bị điện giật nguy hiểm tính mạng.',
    level: 'Thông hiểu'
  },
  // Lesson 3
  {
    id: 'bank-mcq-5',
    number: 5,
    lessonId: 'lesson-3',
    lessonName: 'Bài 3: Sai số phép đo',
    content: 'Phép đo nào sau đây là phép đo TRỰC TIẾP?',
    options: [
      { label: 'A', text: 'Đo vận tốc bằng cách đo quãng đường và thời gian rồi chia.' },
      { label: 'B', text: 'Đo thể tích khối gỗ bằng cách lấy khối lượng chia cho khối lượng riêng.' },
      { label: 'C', text: 'Đo chiều dài bàn học bằng thước dây.' },
      { label: 'D', text: 'Đo diện tích phòng học bằng cách đo chiều dài và chiều rộng.' }
    ],
    correctOption: 'C',
    explanation: 'Đo chiều dài bằng thước dây là so sánh trực tiếp với dụng cụ đo, không qua công thức.',
    level: 'Nhận biết'
  },
  {
    id: 'bank-mcq-6',
    number: 6,
    lessonId: 'lesson-3',
    lessonName: 'Bài 3: Sai số phép đo',
    content: 'Kết quả đo chiều dài L của một vật được ghi là L = (12,45 ± 0,02) cm. Sai số tỉ đối δL của phép đo này bằng bao nhiêu?',
    options: [
      { label: 'A', text: '0,16%.' },
      { label: 'B', text: '0,02%.' },
      { label: 'C', text: '1,61%.' },
      { label: 'D', text: '0,25%.' }
    ],
    correctOption: 'A',
    explanation: 'δL = (ΔL / L_tb) × 100% = (0,02 / 12,45) × 100% ≈ 0,16%.',
    level: 'Thông hiểu'
  },
  // Lesson 4
  {
    id: 'bank-mcq-7',
    number: 7,
    lessonId: 'lesson-4',
    lessonName: 'Bài 4: Độ dịch chuyển & Quãng đường',
    content: 'Một học sinh đi bộ từ nhà A đến trường B cách nhà 3 km theo đường thẳng, sau đó quay lại nhà A. Quãng đường đi được (s) và độ dịch chuyển (d) của học sinh lần lượt là:',
    options: [
      { label: 'A', text: 's = 6 km; d = 6 km.' },
      { label: 'B', text: 's = 6 km; d = 0 km.' },
      { label: 'C', text: 's = 3 km; d = 3 km.' },
      { label: 'D', text: 's = 0 km; d = 6 km.' }
    ],
    correctOption: 'B',
    explanation: 's = 3 + 3 = 6 km. d = vị trí cuối - vị trí đầu = 0 km (vì về lại A).',
    level: 'Thông hiểu'
  },
  // Lesson 5
  {
    id: 'bank-mcq-8',
    number: 8,
    lessonId: 'lesson-5',
    lessonName: 'Bài 5: Tốc độ & Vận tốc',
    content: 'Công thức tính tốc độ trung bình v_tb của một vật chuyển động trên quãng đường s trong thời gian t là:',
    options: [
      { label: 'A', text: 'v_tb = s / t.' },
      { label: 'B', text: 'v_tb = d / t.' },
      { label: 'C', text: 'v_tb = s . t.' },
      { label: 'D', text: 'v_tb = 1/2 s.t.' }
    ],
    correctOption: 'A',
    explanation: 'Tốc độ trung bình là thương số giữa tổng quãng đường s và tổng thời gian t: v_tb = s / t.',
    level: 'Nhận biết'
  },
  {
    id: 'bank-mcq-9',
    number: 9,
    lessonId: 'lesson-5',
    lessonName: 'Bài 5: Tốc độ & Vận tốc',
    content: 'Một con thuyền chạy ngược dòng nước với tốc độ 10 km/h so với nước. Biết tốc độ dòng nước so với bờ là 3 km/h. Tốc độ của thuyền so với bờ là:',
    options: [
      { label: 'A', text: '13 km/h.' },
      { label: 'B', text: '7 km/h.' },
      { label: 'C', text: '30 km/h.' },
      { label: 'D', text: '10,4 km/h.' }
    ],
    correctOption: 'B',
    explanation: 'Chạy ngược dòng: v_13 = v_12 - v_23 = 10 - 3 = 7 km/h.',
    level: 'Thông hiểu'
  },
  // Lesson 6
  {
    id: 'bank-mcq-10',
    number: 10,
    lessonId: 'lesson-6',
    lessonName: 'Bài 6: Thực hành đo tốc độ',
    content: 'Để đo tốc độ TỨC THỜI của viên bi thép lăn trên máng nghiêng dùng đồng hồ đo thời gian hiện số MC964, ta cài đặt nút chọn MODE ở vị trí nào?',
    options: [
      { label: 'A', text: 'MODE A hoặc MODE B.' },
      { label: 'B', text: 'MODE A ↔ B.' },
      { label: 'C', text: 'MODE A + B.' },
      { label: 'D', text: 'MODE T.' }
    ],
    correctOption: 'A',
    explanation: 'MODE A (hoặc B) đo thời gian bi chắn 1 cổng quang điện → đo tốc độ tức thời v_t = d_bi / t_A.',
    level: 'Nhận biết'
  },
  // Lesson 7
  {
    id: 'bank-mcq-11',
    number: 11,
    lessonId: 'lesson-7',
    lessonName: 'Bài 7: Đồ thị d-t',
    content: 'Đồ thị độ dịch chuyển – thời gian (d – t) của một vật là đường thẳng NẰM NGANG song song với trục thời gian t. Trạng thái chuyển động của vật là:',
    options: [
      { label: 'A', text: 'Chuyển động thẳng đều với vận tốc dương.' },
      { label: 'B', text: 'Vật đang ĐỨNG YÊN (v = 0).' },
      { label: 'C', text: 'Chuyển động thẳng nhanh dần đều.' },
      { label: 'D', text: 'Chuyển động thẳng đều với vận tốc âm.' }
    ],
    correctOption: 'B',
    explanation: 'Đồ thị d-t nằm ngang nghĩa là độ dịch chuyển d không đổi theo thời gian → vật đứng yên.',
    level: 'Nhận biết'
  },
  {
    id: 'bank-mcq-12',
    number: 12,
    lessonId: 'lesson-7',
    lessonName: 'Bài 7: Đồ thị d-t',
    content: 'Dựa vào đồ thị (d – t), vận tốc v của vật chuyển động thẳng đều bằng:',
    options: [
      { label: 'A', text: 'Độ dốc (Slope) của đường biểu diễn (d – t).' },
      { label: 'B', text: 'Diện tích dưới đường biểu diễn.' },
      { label: 'C', text: 'Nửa độ dốc của đường biểu diễn.' },
      { label: 'D', text: 'Tích độ dịch chuyển và thời gian.' }
    ],
    correctOption: 'A',
    explanation: 'Vận tốc v = Δd / Δt chính là độ dốc (slope) của đồ thị (d - t).',
    level: 'Thông hiểu'
  },
  // Lesson 8
  {
    id: 'bank-mcq-13',
    number: 13,
    lessonId: 'lesson-8',
    lessonName: 'Bài 8: Gia tốc',
    content: 'Đơn vị đo của gia tốc trong hệ đơn vị SI là:',
    options: [
      { label: 'A', text: 'm/s.' },
      { label: 'B', text: 'm/s².' },
      { label: 'C', text: 'km/h.' },
      { label: 'D', text: 'm.s.' }
    ],
    correctOption: 'B',
    explanation: 'Gia tốc a = Δv / Δt có đơn vị là (m/s) / s = m/s².',
    level: 'Nhận biết'
  },
  {
    id: 'bank-mcq-14',
    number: 14,
    lessonId: 'lesson-8',
    lessonName: 'Bài 8: Gia tốc',
    content: 'Một ô tô tăng tốc từ v_0 = 10 m/s lên v = 20 m/s trong khoảng thời gian Δt = 5 s. Gia tốc của ô tô là:',
    options: [
      { label: 'A', text: '2 m/s².' },
      { label: 'B', text: '4 m/s².' },
      { label: 'C', text: '6 m/s².' },
      { label: 'D', text: '1 m/s².' }
    ],
    correctOption: 'A',
    explanation: 'a = (v - v_0) / Δt = (20 - 10) / 5 = 2 m/s².',
    level: 'Thông hiểu'
  },
  // Lesson 9
  {
    id: 'bank-mcq-15',
    number: 15,
    lessonId: 'lesson-9',
    lessonName: 'Bài 9: CĐTBĐĐ',
    content: 'Chuyển động thẳng biến đổi đều là chuyển động thẳng có:',
    options: [
      { label: 'A', text: 'Vận tốc không đổi theo thời gian.' },
      { label: 'B', text: 'Gia tốc không đổi theo thời gian (a = const).' },
      { label: 'C', text: 'Quãng đường đi được tỷ lệ nghịch với thời gian.' },
      { label: 'D', text: 'Gia tốc tăng đều theo thời gian.' }
    ],
    correctOption: 'B',
    explanation: 'Chuyển động thẳng biến đổi đều có gia tốc a là hằng số không đổi.',
    level: 'Nhận biết'
  },
  {
    id: 'bank-mcq-16',
    number: 16,
    lessonId: 'lesson-9',
    lessonName: 'Bài 9: CĐTBĐĐ',
    content: 'Công thức độc lập thời gian liên hệ giữa vận tốc, gia tốc và độ dịch chuyển trong CĐTBĐĐ là:',
    options: [
      { label: 'A', text: 'v - v_0 = 2ad.' },
      { label: 'B', text: 'v² - v_0² = 2ad.' },
      { label: 'C', text: 'v² + v_0² = 2ad.' },
      { label: 'D', text: 'v² - v_0² = ad.' }
    ],
    correctOption: 'B',
    explanation: 'Công thức liên hệ không chứa t: v² - v_0² = 2ad.',
    level: 'Nhận biết'
  },
  {
    id: 'bank-mcq-17',
    number: 17,
    lessonId: 'lesson-9',
    lessonName: 'Bài 9: CĐTBĐĐ',
    content: 'Một đoàn tàu bắt đầu rời ga (v_0 = 0) chuyển động nhanh dần đều với gia tốc a = 0,5 m/s². Vận tốc của tàu sau t = 20 s là:',
    options: [
      { label: 'A', text: '10 m/s.' },
      { label: 'B', text: '20 m/s.' },
      { label: 'C', text: '5 m/s.' },
      { label: 'D', text: '15 m/s.' }
    ],
    correctOption: 'A',
    explanation: 'v = v_0 + a.t = 0 + 0,5 × 20 = 10 m/s.',
    level: 'Thông hiểu'
  },
  // Lesson 10
  {
    id: 'bank-mcq-18',
    number: 18,
    lessonId: 'lesson-10',
    lessonName: 'Bài 10: Rơi tự do',
    content: 'Sự rơi tự do là sự rơi của một vật:',
    options: [
      { label: 'A', text: 'Trong không khí có sức cản lớn.' },
      { label: 'B', text: 'Chỉ chịu tác dụng của trọng lực.' },
      { label: 'C', text: 'Có lực đẩy Archimedes cân bằng với trọng lực.' },
      { label: 'D', text: 'Có vận tốc ban đầu v_0 > 0 theo hướng thẳng đứng.' }
    ],
    correctOption: 'B',
    explanation: 'Rơi tự do là sự rơi chỉ chịu tác dụng duy nhất của trọng lực.',
    level: 'Nhận biết'
  }
];

export const bankTFs: TFQuestion[] = [
  {
    id: 'bank-tf-1',
    number: 1,
    code: '2-I',
    lessonId: 'lesson-7',
    lessonName: 'Bài 7: Đồ thị d-t & Bài 5: Tốc độ, vận tốc',
    title: 'Khảo sát đồ thị độ dịch chuyển – thời gian của xe máy',
    scenario: 'Hình vẽ biểu diễn đồ thị (d - t) của một xe máy chuyển động thẳng. Đoạn OA từ t = 0 đến 2 h xe đi từ d = 0 đến 60 km. Đoạn AB từ t = 2 h đến 3 h nằm ngang d = 60 km. Đoạn BC từ t = 3 h đến 5 h đi từ d = 60 km về d = 0.',
    statements: [
      { key: 'a', text: 'Trên đoạn OA, xe chuyển động thẳng đều với vận tốc 30 km/h.', isCorrect: true, explanation: 'v_OA = (60 - 0) / (2 - 0) = 30 km/h.' },
      { key: 'b', text: 'Trên đoạn AB, xe chuyển động thẳng đều với vận tốc 60 km/h.', isCorrect: false, explanation: 'Đoạn AB nằm ngang d = 60 km không đổi → v_AB = 0 (xe đứng yên!).' },
      { key: 'c', text: 'Trên đoạn BC, xe đổi chiều chuyển động và đi với vận tốc -30 km/h.', isCorrect: true, explanation: 'v_BC = (0 - 60) / (5 - 3) = -30 km/h (đi theo chiều âm về gốc).' },
      { key: 'd', text: 'Tổng quãng đường đi được trong cả chuyến đi 5 h là 120 km.', isCorrect: true, explanation: 's = s_OA + s_AB + s_BC = 60 + 0 + 60 = 120 km.' }
    ],
    level: '2 Biết + 2 Hiểu',
    image: 'src/assets/graph_d2_q1.svg'
  },
  {
    id: 'bank-tf-2',
    number: 2,
    code: '2-II',
    lessonId: 'lesson-9',
    lessonName: 'Bài 9: Chuyển động thẳng biến đổi đều',
    title: 'Khảo sát ô tô hãm phanh chuyển động chậm dần đều',
    scenario: 'Một ô tô đang chạy với vận tốc v_0 = 20 m/s trên đường thẳng thì người lái xe hãm phanh. Xe chuyển động chậm dần đều với gia tốc a = -2 m/s².',
    statements: [
      { key: 'a', text: 'Tích a.v < 0 nên đây là chuyển động chậm dần đều.', isCorrect: true, explanation: 'a = -2 m/s², v_0 = +20 m/s → a.v < 0 chuẩn CTCDĐ.' },
      { key: 'b', text: 'Thời gian từ lúc hãm phanh đến khi xe dừng lại hẳn là 10 s.', isCorrect: true, explanation: 'v = v_0 + at = 0 → 20 - 2t = 0 → t = 10 s.' },
      { key: 'c', text: 'Quãng đường xe đi được trong 5 s đầu sau khi hãm phanh là 75 m.', isCorrect: true, explanation: 's = v_0 t + 1/2 a t² = 20(5) + 0,5(-2)(25) = 100 - 25 = 75 m.' },
      { key: 'd', text: 'Quãng đường xe đi được từ lúc hãm phanh đến khi dừng hẳn là 100 m.', isCorrect: true, explanation: 'v² - v_0² = 2as → 0 - 400 = 2(-2)s → s = 100 m.' }
    ],
    level: '2 Biết + 2 Hiểu'
  }
];

export const bankSAs: ShortAnswerQuestion[] = [
  {
    id: 'bank-sa-1',
    number: 1,
    lessonId: 'lesson-5',
    lessonName: 'Bài 5: Tốc độ & Vận tốc',
    content: 'Một xe ô tô chạy nửa quãng đường đầu với tốc độ v_1 = 40 km/h và nửa quãng đường sau với tốc độ v_2 = 60 km/h. Tốc độ trung bình v_tb của ô tô trên cả quãng đường là bao nhiêu km/h?',
    correctAnswer: '48',
    unit: 'km/h',
    calculationSteps: 's_1 = s_2 = s/2. t_1 = (s/2)/40, t_2 = (s/2)/60. v_tb = s / (t_1 + t_2) = (2 . v_1 . v_2) / (v_1 + v_2) = (2 × 40 × 60) / (40 + 60) = 4800 / 100 = 48 km/h.',
    level: 'Thông hiểu'
  },
  {
    id: 'bank-sa-2',
    number: 2,
    lessonId: 'lesson-10',
    lessonName: 'Bài 10: Sự rơi tự do',
    content: 'Một vật rơi tự do từ độ cao h = 45 m xuống đất tại nơi có gia tốc trọng trường g = 10 m/s². Thời gian rơi t của vật bằng bao nhiêu giây?',
    correctAnswer: '3',
    unit: 's',
    calculationSteps: 't = √(2h / g) = √(2 × 45 / 10) = √9 = 3 s.',
    level: 'Thông hiểu'
  }
];

export const bankEssays: EssayQuestion[] = [
  {
    id: 'bank-essay-1',
    number: 1,
    code: 'Câu 1 Phần IV',
    lessonId: 'lesson-5',
    lessonName: 'Bài 5: Tốc độ, vận tốc & Cộng vận tốc',
    content: 'Một chiếc ca nô chạy xuôi dòng từ bến A đến bến B mất t_1 = 2 h. Khi chạy ngược dòng từ B về A mất t_2 = 3 h. Biết khoảng cách giữa hai bến AB = 60 km.',
    parts: [
      { label: 'a', text: 'Tính tốc độ của ca nô so với dòng nước (v_12) và tốc độ của dòng nước so với bờ (v_23).', points: 0.5 },
      { label: 'b', text: 'Nếu ca nô tắt máy để trôi tự do theo dòng nước từ A đến B thì mất thời gian bao nhiêu giờ?', points: 0.5 }
    ],
    totalPoints: 1.0,
    detailedSolution: `a) Tốc độ khi xuôi dòng: v_xuôi = AB / t_1 = 60 / 2 = 30 km/h.
Ta có: v_xuôi = v_12 + v_23 = 30 km/h  (1)
Tốc độ khi ngược dòng: v_ngược = AB / t_2 = 60 / 3 = 20 km/h.
Ta có: v_ngược = v_12 - v_23 = 20 km/h  (2)
Từ (1) và (2), cộng hai phương trình: 2.v_12 = 50 → v_12 = 25 km/h.
Thay vào (1): v_23 = 30 - 25 = 5 km/h.

b) Khi ca nô tắt máy trôi tự do, nó chuyển động với tốc độ của dòng nước v_23 = 5 km/h.
Thời gian trôi từ A đến B: t_trôi = AB / v_23 = 60 / 5 = 12 giờ.`,
    markScheme: [
      { step: 'Tính v_xuôi = 30 km/h và v_ngược = 20 km/h', points: 0.25 },
      { step: 'Giải hệ ra v_12 = 25 km/h và v_23 = 5 km/h', points: 0.25 },
      { step: 'Nêu lý do v_trôi = v_23 = 5 km/h', points: 0.25 },
      { step: 'Tính t_trôi = 60 / 5 = 12 giờ', points: 0.25 }
    ],
    level: 'Thông hiểu'
  },
  {
    id: 'bank-essay-2',
    number: 2,
    code: 'Câu 2 Phần IV',
    lessonId: 'lesson-9',
    lessonName: 'Bài 9: Chuyển động thẳng biến đổi đều',
    content: 'Một xe ô tô bắt đầu khởi hành từ trạng thái nghỉ (v_0 = 0), chuyển động thẳng nhanh dần đều. Sau t_1 = 10 s xe đạt tốc độ v_1 = 15 m/s.',
    parts: [
      { label: 'a', text: 'Tính gia tốc a của xe và quãng đường s_1 xe đi được trong 10 s đó.', points: 0.5 },
      { label: 'b', text: 'Tính quãng đường s_giây10 mà xe đi được riêng trong giây thứ 10.', points: 0.5 }
    ],
    totalPoints: 1.0,
    detailedSolution: `a) Gia tốc của xe: a = (v_1 - v_0) / t_1 = (15 - 0) / 10 = 1,5 m/s².
Quãng đường s_1 đi trong 10 s: s_1 = v_0 t_1 + 1/2 a t_1² = 0 + 0,5 × 1,5 × 10² = 75 m.

b) Quãng đường xe đi trong 9 s đầu:
s_9 = 1/2 a (9)² = 0,5 × 1,5 × 81 = 60,75 m.
Quãng đường xe đi trong riêng giây thứ 10:
s_giây10 = s_10 - s_9 = 75 - 60,75 = 14,25 m.`,
    markScheme: [
      { step: 'Tính gia tốc a = 1,5 m/s²', points: 0.25 },
      { step: 'Tính quãng đường s_10 = 75 m', points: 0.25 },
      { step: 'Tính quãng đường s_9 = 60,75 m', points: 0.25 },
      { step: 'Tính s_giây10 = 14,25 m', points: 0.25 }
    ],
    level: 'Vận dụng'
  },
  {
    id: 'bank-essay-3',
    number: 3,
    code: 'Câu 3 Phần IV',
    lessonId: 'lesson-9',
    lessonName: 'Bài 9: Chuyển động thẳng biến đổi đều (Nâng cao)',
    content: 'Hai ô tô A và B chuyển động cùng chiều trên một đường thẳng. Xe A đang chạy với tốc độ không đổi v_A = 20 m/s thì vượt qua xe B đang đứng yên (v_0B = 0). Ngay lúc xe A vượt qua, xe B bắt đầu tăng tốc nhanh dần đều với gia tốc a_B = 2 m/s² đuổi theo xe A.',
    parts: [
      { label: 'a', text: 'Viết phương trình độ dịch chuyển d_A(t) và d_B(t) của hai xe (chọn gốc tọa độ tại vị trí xe B xuất phát, gốc thời gian t = 0 lúc xe A vượt B).', points: 0.5 },
      { label: 'b', text: 'Xác định thời điểm t và khoảng cách s_B từ điểm xuất phát đến vị trí xe B đuổi kịp xe A. Khi đó tốc độ xe B bằng bao nhiêu?', points: 0.5 }
    ],
    totalPoints: 1.0,
    detailedSolution: `a) Chọn gốc tọa độ O tại vị trí xe B xuất phát (cũng là vị trí xe A vượt B), chiều dương là chiều chuyển động.
Phương trình độ dịch chuyển xe A (CĐ thẳng đều): d_A = v_A . t = 20t (m).
Phương trình độ dịch chuyển xe B (CĐNDĐ): d_B = v_0B . t + 1/2 a_B t² = 0 + 1/2 (2) t² = t² (m).

b) Khi xe B đuổi kịp xe A: d_B = d_A
↔ t² = 20t → t = 20 s (do t > 0).
Khoảng cách từ điểm xuất phát đến vị trí đuổi kịp:
s = d_B(20) = 20² = 400 m.
Tốc độ xe B khi đó:
v_B = v_0B + a_B . t = 0 + 2 × 20 = 40 m/s.`,
    markScheme: [
      { step: 'Viết d_A = 20t và d_B = t²', points: 0.50 },
      { step: 'Giải d_A = d_B → t = 20 s', points: 0.25 },
      { step: 'Tính s = 400 m và v_B = 40 m/s', points: 0.25 }
    ],
    level: 'Vận dụng cao'
  }
];

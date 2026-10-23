import { MockExam } from '../types/index.js';
import { bankMCQs, bankTFs, bankSAs, bankEssays } from './questionBankData.js';

export const mockExam1: MockExam = {
  id: 'mock-exam-1',
  title: 'ĐỀ THI THỰC CHIẾN SỐ 01 — KTGK I VẬT LÍ 10 (2026–2027)',
  code: 'ĐỀ SỐ 01',
  durationMinutes: 50,
  totalPoints: 10.0,
  part1: bankMCQs, // 18 MCQs
  part2: bankTFs,  // 2 T/F Questions
  part3: bankSAs,  // 2 SA Questions
  part4: bankEssays, // 3 Essay Questions
};

export const mockExam2: MockExam = {
  id: 'mock-exam-2',
  title: 'ĐỀ THI THỰC CHIẾN SỐ 02 — KTGK I VẬT LÍ 10 (2026–2027)',
  code: 'ĐỀ SỐ 02',
  durationMinutes: 50,
  totalPoints: 10.0,
  part1: [
    {
      id: 'e2-mcq-1',
      number: 1,
      lessonId: 'lesson-1',
      lessonName: 'Bài 1: Làm quen Vật lí',
      content: 'Lĩnh vực nào sau đây KHÔNG thuộc đối tượng nghiên cứu của Vật lí học?',
      options: [
        { label: 'A', text: 'Cơ học và Chuyển động.' },
        { label: 'B', text: 'Nhiệt học và Khí động học.' },
        { label: 'C', text: 'Tâm lí học hành vi con người.' },
        { label: 'D', text: 'Điện từ học và Quang học.' }
      ],
      correctOption: 'C',
      explanation: 'Tâm lí học hành vi thuộc khoa học xã hội, không thuộc khoa học vật lí.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-2',
      number: 2,
      lessonId: 'lesson-2',
      lessonName: 'Bài 2: Quy tắc an toàn',
      content: 'Biển báo nguy hiểm hình tam giác đều nền vàng viền đen với hình vẽ tia sét cảnh báo nguy cơ nào?',
      options: [
        { label: 'A', text: 'Nguy hiểm nhiệt độ cao.' },
        { label: 'B', text: 'Nguy hiểm điện áp cao (Điện giật).' },
        { label: 'C', text: 'Nguy hiểm bức xạ laser.' },
        { label: 'D', text: 'Nguy hiểm hóa chất ăn mòn.' }
      ],
      correctOption: 'B',
      explanation: 'Hình tia sét trong tam giác vàng cảnh báo nguy hiểm điện áp cao / điện giật.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-3',
      number: 3,
      lessonId: 'lesson-2',
      lessonName: 'Bài 2: Quy tắc an toàn',
      content: 'Trong phòng thực hành, khi xảy ra sự cố chập điện gây cháy, thao tác ĐẦU TIÊN cần thực hiện là:',
      options: [
        { label: 'A', text: 'Dùng nước dội thẳng vào đám cháy điện.' },
        { label: 'B', text: 'Ngắt ngay cầu dao/công tắc nguồn điện tổng.' },
        { label: 'C', text: 'Dùng tay kéo dây điện ra khỏi ổ cắm.' },
        { label: 'D', text: 'Mở cửa phòng hô khoán và bỏ chạy ngay.' }
      ],
      correctOption: 'B',
      explanation: 'Thao tác đầu tiên bắt buộc phải là ngắt nguồn điện tổng để đảm bảo an toàn.',
      level: 'Thông hiểu'
    },
    {
      id: 'e2-mcq-4',
      number: 4,
      lessonId: 'lesson-3',
      lessonName: 'Bài 3: Sai số phép đo',
      content: 'Nguyên nhân nào sau đây gây ra sai số NGẪU NHIÊN trong phép đo Vật lí?',
      options: [
        { label: 'A', text: 'Thước đo bị cong vênh lệch gốc 0 cố định.' },
        { label: 'B', text: 'Đồng hồ chạy chậm do hết pin.' },
        { label: 'C', text: 'Khung cảnh môi trường biến động bất chợt (luồng gió, độ ẩm, phản xạ con người).' },
        { label: 'D', text: 'Dụng cụ đo chưa được hiệu chỉnh zero.' }
      ],
      correctOption: 'C',
      explanation: 'Sai số ngẫu nhiên do các yếu tố môi trường và thao tác biến động không đoán trước.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-5',
      number: 5,
      lessonId: 'lesson-4',
      lessonName: 'Bài 4: Độ dịch chuyển & Quãng đường',
      content: 'Vectơ độ dịch chuyển d cho ta biết thông tin gì về sự chuyển động của vật?',
      options: [
        { label: 'A', text: 'Chỉ cho biết độ dài quỹ đạo.' },
        { label: 'B', text: 'Cho biết cả độ dời vị trí và hướng chuyển động từ điểm đầu đến điểm cuối.' },
        { label: 'C', text: 'Chỉ cho biết thời gian chuyển động.' },
        { label: 'D', text: 'Chỉ cho biết tốc độ trung bình.' }
      ],
      correctOption: 'B',
      explanation: 'Vectơ độ dịch chuyển cho biết cả độ dài khoảng cách dời và hướng chuyển động.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-6',
      number: 6,
      lessonId: 'lesson-5',
      lessonName: 'Bài 5: Tốc độ & Vận tốc',
      content: 'Phương trình vận tốc v = d / t áp dụng đúng khi vật chuyển động:',
      options: [
        { label: 'A', text: 'Thẳng đều trong khoảng thời gian t.' },
        { label: 'B', text: 'Nhanh dần đều.' },
        { label: 'C', text: 'Tròn đều.' },
        { label: 'D', text: 'Biến đổi bất kỳ.' }
      ],
      correctOption: 'A',
      explanation: 'v = d / t là vận tốc trong chuyển động thẳng đều.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-7',
      number: 7,
      lessonId: 'lesson-6',
      lessonName: 'Bài 6: Thực hành đo tốc độ',
      content: 'Khi đo tốc độ bằng cổng quang điện và đồng hồ hiện số MC964, công thức v = d_bi / t dùng để đo:',
      options: [
        { label: 'A', text: 'Tốc độ tức thời tại vị trí cổng quang điện.' },
        { label: 'B', text: 'Tốc độ trung bình trên toàn máng nghiêng.' },
        { label: 'C', text: 'Gia tốc trọng trường.' },
        { label: 'D', text: 'Độ dịch chuyển tổng cộng.' }
      ],
      correctOption: 'A',
      explanation: 'v = d_bi / t là công thức tính tốc độ tức thời khi viên bi chắn 1 cổng quang điện.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-8',
      number: 8,
      lessonId: 'lesson-6',
      lessonName: 'Bài 6: Thực hành đo tốc độ',
      content: 'Một viên bi thép có đường kính d = 2,0 cm chắn cổng quang điện trong thời gian t = 0,04 s. Tốc độ tức thời của bi là:',
      options: [
        { label: 'A', text: '0,5 m/s.' },
        { label: 'B', text: '50 m/s.' },
        { label: 'C', text: '0,08 m/s.' },
        { label: 'D', text: '0,8 m/s.' }
      ],
      correctOption: 'A',
      explanation: 'v = d / t = 0,02 m / 0,04 s = 0,5 m/s.',
      level: 'Thông hiểu'
    },
    {
      id: 'e2-mcq-9',
      number: 9,
      lessonId: 'lesson-7',
      lessonName: 'Bài 7: Đồ thị d-t',
      content: 'Trong đồ thị độ dịch chuyển – thời gian (d – t), nếu đường biểu diễn có độ dốc DƯƠNG (xiên lên), điều này nghĩa là:',
      options: [
        { label: 'A', text: 'Vật đang chuyển động theo chiều dương (v > 0).' },
        { label: 'B', text: 'Vật đang đứng yên.' },
        { label: 'C', text: 'Vật đang chuyển động theo chiều âm (v < 0).' },
        { label: 'D', text: 'Vật chuyển động chậm dần đều.' }
      ],
      correctOption: 'A',
      explanation: 'Độ dốc dương (Δd > 0) tương ứng với v = Δd / Δt > 0 (chuyển động theo chiều dương).',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-10',
      number: 10,
      lessonId: 'lesson-7',
      lessonName: 'Bài 7: Đồ thị d-t',
      content: 'Đồ thị d-t của một người đi xe đạp là đường thẳng đi từ điểm (0 s, 20 m) đến điểm (10 s, 60 m). Vận tốc của xe đạp là:',
      options: [
        { label: 'A', text: '4 m/s.' },
        { label: 'B', text: '6 m/s.' },
        { label: 'C', text: '2 m/s.' },
        { label: 'D', text: '8 m/s.' }
      ],
      correctOption: 'A',
      explanation: 'v = (60 - 20) / (10 - 0) = 40 / 10 = 4 m/s.',
      level: 'Thông hiểu'
    },
    {
      id: 'e2-mcq-11',
      number: 11,
      lessonId: 'lesson-8',
      lessonName: 'Bài 8: Gia tốc',
      content: 'Gia tốc là đại lượng đặc trưng cho:',
      options: [
        { label: 'A', text: 'Sự nhanh hay chậm của chuyển động.' },
        { label: 'B', text: 'Sự biến thiên nhanh hay chậm của vận tốc theo thời gian.' },
        { label: 'C', text: 'Quãng đường vật đi được trong một giây.' },
        { label: 'D', text: 'Độ dịch chuyển của vật trong một đơn vị thời gian.' }
      ],
      correctOption: 'B',
      explanation: 'Gia tốc đặc trưng cho sự thay đổi nhanh hay chậm của vận tốc.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-12',
      number: 12,
      lessonId: 'lesson-8',
      lessonName: 'Bài 8: Gia tốc',
      content: 'Một vật chuyển động có vận tốc giảm từ 15 m/s xuống 5 m/s trong 2 s. Gia tốc của vật là:',
      options: [
        { label: 'A', text: '-5 m/s².' },
        { label: 'B', text: '5 m/s².' },
        { label: 'C', text: '-10 m/s².' },
        { label: 'D', text: '10 m/s².' }
      ],
      correctOption: 'A',
      explanation: 'a = (5 - 15) / 2 = -10 / 2 = -5 m/s².',
      level: 'Thông hiểu'
    },
    {
      id: 'e2-mcq-13',
      number: 13,
      lessonId: 'lesson-9',
      lessonName: 'Bài 9: CĐTBĐĐ',
      content: 'Đồ thị vận tốc – thời gian (v – t) của chuyển động thẳng biến đổi đều có dạng là:',
      options: [
        { label: 'A', text: 'Một đường parabol.' },
        { label: 'B', text: 'Một đường thẳng xiên góc so với trục thời gian.' },
        { label: 'C', text: 'Một đường cong hyperbol.' },
        { label: 'D', text: 'Một đường tròn.' }
      ],
      correctOption: 'B',
      explanation: 'v = v_0 + at có hàm bậc nhất theo t nên đồ thị v-t là đường thẳng xiên góc.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-14',
      number: 14,
      lessonId: 'lesson-9',
      lessonName: 'Bài 9: CĐTBĐĐ',
      content: 'Một ô tô hãm phanh chuyển động chậm dần đều với v_0 = 10 m/s và a = -1 m/s². Quãng đường ô tô đi được đến khi dừng hẳn (v = 0) là:',
      options: [
        { label: 'A', text: '50 m.' },
        { label: 'B', text: '100 m.' },
        { label: 'C', text: '25 m.' },
        { label: 'D', text: '10 m.' }
      ],
      correctOption: 'A',
      explanation: 'v² - v_0² = 2ad → 0 - 100 = 2(-1)d → d = 50 m.',
      level: 'Thông hiểu'
    },
    {
      id: 'e2-mcq-15',
      number: 15,
      lessonId: 'lesson-9',
      lessonName: 'Bài 9: CĐTBĐĐ',
      content: 'Xe máy tăng tốc từ 0 đến 36 km/h (10 m/s) trong 5 s. Gia tốc của xe máy là:',
      options: [
        { label: 'A', text: '2 m/s².' },
        { label: 'B', text: '7.2 m/s².' },
        { label: 'C', text: '1.8 m/s².' },
        { label: 'D', text: '4 m/s².' }
      ],
      correctOption: 'A',
      explanation: 'v_0 = 0, v = 10 m/s, t = 5 s → a = (10 - 0)/5 = 2 m/s².',
      level: 'Thông hiểu'
    },
    {
      id: 'e2-mcq-16',
      number: 16,
      lessonId: 'lesson-10',
      lessonName: 'Bài 10: Rơi tự do',
      content: 'Nhận định nào sau đây SAI khi nói về sự rơi tự do?',
      options: [
        { label: 'A', text: 'Là chuyển động thẳng nhanh dần đều.' },
        { label: 'B', text: 'Vận tốc ban đầu luôn bằng 0.' },
        { label: 'C', text: 'Vật nặng rơi nhanh hơn vật nhẹ trong chân không.' },
        { label: 'D', text: 'Gia tốc rơi tự do phụ thuộc vĩ độ địa lý.' }
      ],
      correctOption: 'C',
      explanation: 'Trong chân không, mọi vật rơi với cùng gia tốc g không phụ thuộc khối lượng nặng nhẹ.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-mcq-17',
      number: 17,
      lessonId: 'lesson-10',
      lessonName: 'Bài 10: Rơi tự do',
      content: 'Một hòn đá rơi tự do từ đỉnh tháp sau 2 s thì chạm đất (g = 10 m/s²). Độ cao của tháp là:',
      options: [
        { label: 'A', text: '20 m.' },
        { label: 'B', text: '40 m.' },
        { label: 'C', text: '10 m.' },
        { label: 'D', text: '80 m.' }
      ],
      correctOption: 'A',
      explanation: 'h = 1/2 g t² = 0,5 × 10 × 2² = 20 m.',
      level: 'Thông hiểu'
    },
    {
      id: 'e2-mcq-18',
      number: 18,
      lessonId: 'lesson-10',
      lessonName: 'Bài 10: Rơi tự do',
      content: 'Tốc độ của vật rơi tự do khi chạm đất từ độ cao h = 20 m (g = 10 m/s²) là:',
      options: [
        { label: 'A', text: '20 m/s.' },
        { label: 'B', text: '10 m/s.' },
        { label: 'C', text: '40 m/s.' },
        { label: 'D', text: '200 m/s.' }
      ],
      correctOption: 'A',
      explanation: 'v = √(2gh) = √(2 × 10 × 20) = √400 = 20 m/s.',
      level: 'Thông hiểu'
    }
  ],
  part2: [
    {
      id: 'e2-tf-1',
      number: 1,
      code: '2-I',
      lessonId: 'lesson-7',
      lessonName: 'Bài 7: Đồ thị d-t',
      title: 'Phân tích chuyển động người đi xe đạp từ đồ thị d-t',
      scenario: 'Đồ thị d-t gồm 3 đoạn: OA từ (0 s, 0 m) đến (10 s, 50 m); AB nằm ngang từ (10 s, 50 m) đến (20 s, 50 m); BC đi từ (20 s, 50 m) về (30 s, 0 m).',
      statements: [
        { key: 'a', text: 'Trải qua đoạn OA, xe chuyển động với vận tốc 5 m/s.', isCorrect: true, explanation: 'v_OA = (50 - 0)/10 = 5 m/s.' },
        { key: 'b', text: 'Trên đoạn AB, xe đứng yên không chuyển động.', isCorrect: true, explanation: 'd = 50 m không đổi → v = 0.' },
        { key: 'c', text: 'Trên đoạn BC, xe quay trở về điểm xuất phát với vận tốc -5 m/s.', isCorrect: true, explanation: 'v_BC = (0 - 50)/(30 - 20) = -5 m/s.' },
        { key: 'd', text: 'Độ dịch chuyển tổng cộng sau 30 s là 100 m.', isCorrect: false, explanation: 'd_tổng = 0 m (quay về gốc). Quãng đường s mới bằng 100 m!' }
      ],
      level: '2 Biết + 2 Hiểu',
      image: 'src/assets/exam2_dt_graph.svg'
    },
    {
      id: 'e2-tf-2',
      number: 2,
      code: '2-II',
      lessonId: 'lesson-9',
      lessonName: 'Bài 9: CĐTBĐĐ',
      title: 'Chuyển động của xe máy tăng tốc',
      scenario: 'Xe máy bắt đầu v_0 = 0 m/s tăng tốc với a = 1 m/s² trong 20 s.',
      statements: [
        { key: 'a', text: 'Đây là chuyển động thẳng nhanh dần đều.', isCorrect: true, explanation: 'a.v > 0.' },
        { key: 'b', text: 'Vận tốc xe sau 20 s là 20 m/s.', isCorrect: true, explanation: 'v = 0 + 1 × 20 = 20 m/s.' },
        { key: 'c', text: 'Quãng đường xe đi trong 20 s là 200 m.', isCorrect: true, explanation: 's = 1/2 (1)(20²) = 200 m.' },
        { key: 'd', text: 'Tốc độ trung bình trên 20 s là 20 m/s.', isCorrect: false, explanation: 'v_tb = s/t = 200/20 = 10 m/s.' }
      ],
      level: '2 Biết + 2 Hiểu'
    }
  ],
  part3: [
    {
      id: 'e2-sa-1',
      number: 1,
      lessonId: 'lesson-5',
      lessonName: 'Bài 5: Tốc độ & Vận tốc',
      content: 'Một ô tô chạy 1 giờ đầu với tốc độ 60 km/h và 2 giờ sau với tốc độ 45 km/h. Tốc độ trung bình trên cả chuyến đi 3 giờ là bao nhiêu km/h?',
      correctAnswer: '50',
      unit: 'km/h',
      calculationSteps: 's_1 = 60 × 1 = 60 km. s_2 = 45 × 2 = 90 km. s_tổng = 150 km, t_tổng = 3 h → v_tb = 150 / 3 = 50 km/h.',
      level: 'Nhận biết'
    },
    {
      id: 'e2-sa-2',
      number: 2,
      lessonId: 'lesson-10',
      lessonName: 'Bài 10: Rơi tự do',
      content: 'Một hòn đá rơi tự do từ độ cao h. Trong giây cuối cùng trước khi chạm đất, hòn đá rơi được quãng đường 35 m (lấy g = 10 m/s²). Độ cao h bằng bao nhiêu mét?',
      correctAnswer: '80',
      unit: 'm',
      calculationSteps: 'Δh_cuối = 1/2 g (2t - 1) = 5 (2t - 1) = 35 → 2t - 1 = 7 → t = 4 s. h = 1/2 g t² = 0,5 × 10 × 4² = 80 m.',
      level: 'Thông hiểu'
    }
  ],
  part4: [
    {
      id: 'e2-essay-1',
      number: 1,
      code: 'Câu 1 Phần IV',
      lessonId: 'lesson-5',
      lessonName: 'Bài 5: Tốc độ & Vận tốc',
      content: 'Một chiếc thuyền máy chạy trên sông rộng. Tốc độ của thuyền so với nước là v_12 = 12 km/h, tốc độ của dòng nước so với bờ là v_23 = 5 km/h. Thuyền chèo vuông góc với dòng nước.',
      parts: [
        { label: 'a', text: 'Tính tốc độ v_13 của thuyền so với bờ sông.', points: 0.5 },
        { label: 'b', text: 'Tính góc lệch α giữa hướng chuyển động thực tế của thuyền với bờ sông.', points: 0.5 }
      ],
      totalPoints: 1.0,
      detailedSolution: `a) Do v_12 ⊥ v_23, áp dụng quy tắc Pythagore:
v_13 = √(v_12² + v_23²) = √(12² + 5²) = √(144 + 25) = √169 = 13 km/h.

b) Gọi α là góc hợp bởi vectơ v_13 và đường vuông góc với bờ (hoặc so với bờ):
tan α = v_23 / v_12 = 5 / 12 ≈ 0,4167 → α ≈ 22,6°.`,
      markScheme: [
        { step: 'Viết v_13 = √(v_12² + v_23²)', points: 0.25 },
        { step: 'Tính ra v_13 = 13 km/h', points: 0.25 },
        { step: 'Viết công thức tan α = v_23 / v_12', points: 0.25 },
        { step: 'Tính góc α ≈ 22.6°', points: 0.25 }
      ],
      level: 'Thông hiểu'
    },
    {
      id: 'e2-essay-2',
      number: 2,
      code: 'Câu 2 Phần IV',
      lessonId: 'lesson-9',
      lessonName: 'Bài 9: CĐTBĐĐ',
      content: 'Một ô tô hãm phanh chuyển động chậm dần đều với v_0 = 20 m/s. Sau khi đi được s = 75 m thì tốc độ giảm xuống còn v = 10 m/s.',
      parts: [
        { label: 'a', text: 'Tính gia tốc a của ô tô.', points: 0.5 },
        { label: 'b', text: 'Tính thời gian t từ lúc hãm phanh đến khi xe dừng hẳn (v = 0) và tổng quãng đường s_tổng xe đi được.', points: 0.5 }
      ],
      totalPoints: 1.0,
      detailedSolution: `a) Dùng công thức độc lập: v² - v_0² = 2as
10² - 20² = 2 . a . 75 → 100 - 400 = 150a → -300 = 150a → a = -2 m/s².

b) Thời gian đến khi dừng hẳn (v = 0):
v = v_0 + at → 0 = 20 + (-2)t → t = 10 s.
Tổng quãng đường từ lúc hãm phanh đến khi dừng hẳn:
v² - v_0² = 2a s_tổng → 0 - 20² = 2(-2) s_tổng → -400 = -4 s_tổng → s_tổng = 100 m.`,
      markScheme: [
        { step: 'Tính gia tốc a = -2 m/s²', points: 0.50 },
        { step: 'Tính thời gian t = 10 s', points: 0.25 },
        { step: 'Tính s_tổng = 100 m', points: 0.25 }
      ],
      level: 'Vận dụng'
    },
    {
      id: 'e2-essay-3',
      number: 3,
      code: 'Câu 3 Phần IV',
      lessonId: 'lesson-9',
      lessonName: 'Bài 9: CĐTBĐĐ (Nâng cao)',
      content: 'Một vật chuyển động thẳng nhanh dần đều không vận tốc ban đầu (v_0 = 0). Biết quãng đường vật đi được trong giây thứ 4 lớn hơn quãng đường vật đi được trong giây thứ 3 là 3 m.',
      parts: [
        { label: 'a', text: 'Tính gia tốc a của vật.', points: 0.5 },
        { label: 'b', text: 'Tính quãng đường s_5 vật đi được sau 5 giây kể từ lúc bắt đầu chuyển động.', points: 0.5 }
      ],
      totalPoints: 1.0,
      detailedSolution: `a) Quãng đường đi trong giây thứ n: Δs_n = s(n) - s(n-1) = 1/2 a [n² - (n-1)²] = 1/2 a (2n - 1).
Trong giây thứ 4: Δs_4 = 1/2 a (2 × 4 - 1) = 3,5 a.
Trong giây thứ 3: Δs_3 = 1/2 a (2 × 3 - 1) = 2,5 a.
Theo đề bài: Δs_4 - Δs_3 = 3 m
↔ 3,5 a - 2,5 a = 3 → a = 3 m/s².

b) Quãng đường vật đi được sau 5 s:
s_5 = 1/2 a t_5² = 0,5 × 3 × (5)² = 0,5 × 3 × 25 = 37,5 m.`,
      markScheme: [
        { step: 'Lập biểu thức Δs_4 = 3,5a và Δs_3 = 2,5a', points: 0.25 },
        { step: 'Giải phương trình ra gia tốc a = 3 m/s²', points: 0.25 },
        { step: 'Viết công thức s_5 = 1/2 a t_5²', points: 0.25 },
        { step: 'Tính s_5 = 37,5 m', points: 0.25 }
      ],
      level: 'Vận dụng cao'
    }
  ]
};

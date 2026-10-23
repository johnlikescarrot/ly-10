export interface MCQ {
  id: number;
  level: 'NB' | 'TH' | 'VD' | 'VDC';
  question: string;
  options: [string, string, string, string];
  cols?: 1 | 2 | 4;
  answer: string;
  explanation: string;
  topic: string;
}

export const mcqQuestions: MCQ[] = [
  // Bài 1
  {
    id: 1,
    level: 'NB',
    topic: 'Bài 1: Làm quen với Vật lí',
    question: 'Đối tượng nghiên cứu chủ yếu của môn Vật lí là gì?',
    options: [
      'A. Cấu tạo chất và sự biến đổi của các chất.',
      'B. Các dạng vận động của vật chất và năng lượng.',
      'C. Sự sinh trưởng và phát triển của các loài sinh vật.',
      'D. Sự hình thành và biến đổi địa hình bề mặt Trái Đất.'
    ],
    cols: 2,
    answer: 'B',
    explanation: 'Vật lí nghiên cứu các dạng vận động của vật chất và năng lượng.'
  },
  {
    id: 2,
    level: 'NB',
    topic: 'Bài 1: Làm quen với Vật lí',
    question: 'Thành tựu nghiên cứu nào của Vật lí đóng vai trò mở đầu cho cuộc Cách mạng công nghiệp lần thứ nhất (thế kỉ XVIII)?',
    options: [
      'A. Nghiên cứu về Nhiệt động lực học (sáng chế máy hơi nước của James Watt).',
      'B. Khám phá hiện tượng cảm ứng điện từ của Michael Faraday.',
      'C. Nghiên cứu về điện tử, chất bán dẫn và vi mạch tích hợp.',
      'D. Nghiên cứu vật lí lượng tử, trí tuệ nhân tạo và công nghệ nano.'
    ],
    cols: 1,
    answer: 'A',
    explanation: 'Sáng chế máy hơi nước nhờ nghiên cứu Nhiệt động lực học mở đầu CMCN 1.0.'
  },
  {
    id: 3,
    level: 'NB',
    topic: 'Bài 1: Làm quen với Vật lí',
    question: 'Việc nhà vật lí Faraday khám phá ra hiện tượng cảm ứng điện từ (năm 1831) là cơ sở trực tiếp cho sự ra đời của cuộc cách mạng công nghiệp lần thứ mấy?',
    options: ['A. Lần thứ nhất.', 'B. Lần thứ hai.', 'C. Lần thứ ba.', 'D. Lần thứ tư.'],
    cols: 4,
    answer: 'B',
    explanation: 'Cảm ứng điện từ là cơ sở sản xuất điện năng, mở đầu CMCN 2.0.'
  },
  // Bài 2
  {
    id: 4,
    level: 'NB',
    topic: 'Bài 2: An toàn thực hành',
    question: 'Biển báo cảnh báo bề mặt nóng có đặc điểm hình dạng và màu sắc nào sau đây?',
    options: [
      'A. Hình tròn viền đỏ, nền trắng.',
      'B. Hình tam giác đều viền đen, nền vàng, biểu tượng màu đen.',
      'C. Hình vuông nền xanh lá cây.',
      'D. Hình chữ nhật nền cam.'
    ],
    cols: 2,
    answer: 'B',
    explanation: 'Biển báo cảnh báo nguy hiểm/chú ý có dạng hình tam giác viền đen, nền vàng.'
  },
  {
    id: 5,
    level: 'TH',
    topic: 'Bài 2: An toàn thực hành',
    question: 'Hành động nào sau đây tuân thủ đúng quy tắc an toàn trong phòng thực hành Vật lí?',
    options: [
      'A. Tự ý cắm thiết bị điện vào nguồn 220V khi chưa có chỉ dẫn của giáo viên.',
      'B. Lau khô tay trước khi thao tác với các thiết bị điện.',
      'C. Nhìn trực tiếp vào chùm tia laser phát ra từ nguồn phát.',
      'D. Rút phích cắm điện bằng cách kéo mạnh dây dẫn.'
    ],
    cols: 1,
    answer: 'B',
    explanation: 'Nước dẫn điện nên cần lau khô tay trước khi dùng thiết bị điện để tránh điện giật.'
  },
  // Bài 3
  {
    id: 6,
    level: 'NB',
    topic: 'Bài 3: Sai số phép đo',
    question: 'Phép đo nào sau đây là phép đo trực tiếp?',
    options: [
      'A. Đo vận tốc bằng cách đo độ dịch chuyển và thời gian.',
      'B. Đo khối lượng bằng cân tiểu ly.',
      'C. Đo diện tích hình chữ nhật bằng cách đo chiều dài và chiều rộng.',
      'D. Đo khối lượng riêng bằng cách đo khối lượng và thể tích.'
    ],
    cols: 2,
    answer: 'B',
    explanation: 'Đo khối lượng bằng cân đọc trực tiếp số đo trên thước/màn hình.'
  },
  // Bài 4
  {
    id: 7,
    level: 'NB',
    topic: 'Bài 4: Độ dịch chuyển & Quãng đường',
    question: 'Độ dịch chuyển là một đại lượng vectơ biểu diễn:',
    options: [
      'A. Độ dài quãng đường vật đi được trong toàn bộ thời gian.',
      'B. Độ biến thiên vị trí của vật, có hướng từ vị trí đầu đến vị trí cuối.',
      'C. Tốc độ chuyển động của vật theo thời gian.',
      'D. Quãng đường vật đi được trong 1 giây.'
    ],
    cols: 2,
    answer: 'B',
    explanation: 'Độ dịch chuyển d⃗ = x⃗_sau - x⃗_đầu.'
  },
  {
    id: 8,
    level: 'TH',
    topic: 'Bài 4: Độ dịch chuyển & Quãng đường',
    question: 'Một người đi bộ 3 km về phía Bắc, sau đó rẽ đông đi tiếp 4 km. Độ lớn độ dịch chuyển tổng cộng của người đó là:',
    options: ['A. 7 km.', 'B. 1 km.', 'C. 5 km.', 'D. 12 km.'],
    cols: 4,
    answer: 'C',
    explanation: 'Hai hướng vuông góc: d = √(3² + 4²) = 5 km.'
  },
  {
    id: 9,
    level: 'TH',
    topic: 'Bài 4: Độ dịch chuyển & Quãng đường',
    question: 'Một vận động viên bơi từ đầu bể đến cuối bể dài 50 m rồi quay trở lại vị trí xuất phát. Quãng đường s và độ dịch chuyển d lần lượt là:',
    options: [
      'A. s = 100 m; d = 0 m.',
      'B. s = 100 m; d = 100 m.',
      'C. s = 50 m; d = 50 m.',
      'D. s = 0 m; d = 100 m.'
    ],
    cols: 2,
    answer: 'A',
    explanation: 'Về lại chỗ cũ thì d = 0, còn quãng đường s = 50 + 50 = 100 m.'
  },
  // Bài 5, 6
  {
    id: 10,
    level: 'NB',
    topic: 'Bài 5 & 6: Tốc độ & Vận tốc',
    question: 'Công thức tính vận tốc trung bình là:',
    options: [
      'A. v_tb = s / Δt',
      'B. v⃗_tb = Δd⃗ / Δt',
      'C. v_tb = Δt / Δd',
      'D. v_tb = s . Δt'
    ],
    cols: 4,
    answer: 'B',
    explanation: 'Vận tốc trung bình bằng thương số giữa độ dịch chuyển và khoảng thời gian.'
  },
  // Bài 7
  {
    id: 11,
    level: 'NB',
    topic: 'Bài 7: Đồ thị độ dịch chuyển - thời gian',
    question: 'Độ dốc (hệ số góc) của đồ thị độ dịch chuyển - thời gian (d - t) cho biết đại lượng nào?',
    options: ['A. Gia tốc.', 'B. Quãng đường.', 'C. Vận tốc.', 'D. Thời gian.'],
    cols: 4,
    answer: 'C',
    explanation: 'v = Δd / Δt = tan(θ).'
  },
  {
    id: 12,
    level: 'TH',
    topic: 'Bài 7: Đồ thị độ dịch chuyển - thời gian',
    question: 'Đồ thị (d - t) là một đường thẳng song song với trục thời gian Ot chứng tỏ vật đang:',
    options: [
      'A. Chuyển động thẳng đều.',
      'B. Đứng yên.',
      'C. Chuyển động nhanh dần đều.',
      'D. Chuyển động chậm dần đều.'
    ],
    cols: 2,
    answer: 'B',
    explanation: 'd không đổi theo thời gian => vật đứng yên.'
  },
  // Bài 8
  {
    id: 13,
    level: 'NB',
    topic: 'Bài 8: Gia tốc',
    question: 'Đơn vị đo gia tốc trong hệ SI là:',
    options: ['A. m/s', 'B. m/s²', 'C. km/h', 'D. m.s²'],
    cols: 4,
    answer: 'B',
    explanation: 'Gia tốc a = Δv / Δt có đơn vị là m/s².'
  },
  {
    id: 14,
    level: 'TH',
    topic: 'Bài 8: Gia tốc',
    question: 'Một ô tô đang chuyển động với vận tốc 10 m/s thì tăng tốc lên 20 m/s trong 5 giây. Gia tốc của ô tô là:',
    options: ['A. 2 m/s²', 'B. 4 m/s²', 'C. 6 m/s²', 'D. 1 m/s²'],
    cols: 4,
    answer: 'A',
    explanation: 'a = (20 - 10) / 5 = 2 m/s².'
  },
  // Bài 9
  {
    id: 15,
    level: 'NB',
    topic: 'Bài 9: Chuyển động thẳng biến đổi đều',
    question: 'Trong chuyển động thẳng nhanh dần đều, véctơ gia tốc a⃗ và véctơ vận tốc v⃗ luôn:',
    options: [
      'A. Ngược chiều nhau (a.v < 0).',
      'B. Cùng chiều nhau (a.v > 0).',
      'C. Vuông góc với nhau.',
      'D. Tùy thuộc vào gốc tọa độ.'
    ],
    cols: 2,
    answer: 'B',
    explanation: 'Chuyển động nhanh dần đều: a⃗ và v⃗ cùng chiều (a.v > 0).'
  },
  {
    id: 16,
    level: 'NB',
    topic: 'Bài 9: Chuyển động thẳng biến đổi đều',
    question: 'Công thức liên hệ giữa gia tốc, vận tốc và độ dịch chuyển trong CĐTBĐĐ là:',
    options: [
      'A. v² - v₀² = a.d',
      'B. v² - v₀² = 2.a.d',
      'C. v - v₀ = 2.a.d',
      'D. v² + v₀² = 2.a.d'
    ],
    cols: 2,
    answer: 'B',
    explanation: 'Công thức độc lập thời gian v² - v₀² = 2ad.'
  },
  {
    id: 17,
    level: 'TH',
    topic: 'Bài 9: Chuyển động thẳng biến đổi đều',
    question: 'Một xe máy bắt đầu khởi hành từ nghỉ (v₀ = 0) với gia tốc 1,5 m/s². Vận tốc xe sau 4 giây là:',
    options: ['A. 6 m/s', 'B. 3 m/s', 'C. 12 m/s', 'D. 4.5 m/s'],
    cols: 4,
    answer: 'A',
    explanation: 'v = v₀ + at = 0 + 1,5 × 4 = 6 m/s.'
  },
  // Bài 10
  {
    id: 18,
    level: 'NB',
    topic: 'Bài 10: Sự rơi tự do',
    question: 'Sự rơi tự do là sự rơi của vật:',
    options: [
      'A. Trong không khí có lực cản lớn.',
      'B. Chỉ chịu tác dụng của trọng lực.',
      'C. Dưới tác dụng của lực đẩy Archimed.',
      'D. Theo phương nằm ngang.'
    ],
    cols: 2,
    answer: 'B',
    explanation: 'Rơi tự do là chuyển động chỉ chịu tác dụng của trọng lực.'
  }
];

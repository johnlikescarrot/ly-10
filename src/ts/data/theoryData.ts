import { LessonTheory } from '../types/index.js';

export const theoryLessons: LessonTheory[] = [
  {
    id: 'lesson-1',
    number: 1,
    title: 'Làm quen với Vật lí',
    chapter: 'Chương I: Mở đầu',
    keyConcepts: [
      'Đối tượng nghiên cứu của Vật lí: Các dạng vận động của vật chất và năng lượng.',
      'Mục tiêu: Khám phá quy luật tổng quát của tự nhiên.',
      'Phương pháp nghiên cứu: Phương pháp thực nghiệm (quan sát, thí nghiệm) và Phương pháp mô hình (mô hình toán học, mô hình vật chất, mô hình lý thuyết).',
      'Quá trình phát triển: Vật lí cổ điển (Galileo, Newton) → Vật lí hiện đại (Thuyết tương đối Einstein, Cơ học lượng tử Plancki/Bohr).'
    ],
    formulas: [],
    commonTraps: [
      'Bẫy 1: Nhầm lẫn phương pháp thực nghiệm với phương pháp mô hình. (Thực nghiệm dựa trên thí nghiệm thực tế; Mô hình dựa trên giả thuyết và mô phỏng lý thuyết).',
      'Bẫy 2: Cho rằng Vật lí chỉ nghiên cứu máy móc kĩ thuật. (Đúng: Nghiên cứu từ hạt cơ bản đến vũ trụ bao la).'
    ]
  },
  {
    id: 'lesson-2',
    number: 2,
    title: 'Các quy tắc an toàn trong phòng thực hành Vật lí',
    chapter: 'Chương I: Mở đầu',
    keyConcepts: [
      '1. Biển báo CẤM: Hình tròn, viền đỏ, nền trắng, gạch chéo đỏ, hình đen (Cấm lửa, cấm nước...).',
      '2. Biển báo BẮT BUỘC: Hình tròn, nền xanh dương, hình trắng (Đeo kính bảo hộ, găng tay...).',
      '3. Biển báo CẢNH BÁO NGUY HIỂM: Hình tam giác đều, viền đen/đỏ, nền vàng, hình đen (Điện cao thế, laser, nhiệt độ cao...).',
      '4. Biển báo CẢNH BÁO HÓA CHẤT: Hình vuông/thoi, viền đen, nền đỏ cam, hình đen (Ăn mòn, độc hại, dễ cháy...).',
      'Quy tắc an toàn thiết bị điện: Không chạm tay ướt vào phích cắm, kiểm tra dây dẫn trước khi cắm, ngắt nguồn khi có sự cố.'
    ],
    formulas: [],
    commonTraps: [
      'Bẫy 1: Nhầm biển báo Cấm (Hình tròn viền đỏ) với biển Cảnh báo nguy hiểm (Hình tam giác vàng).',
      'Bẫy 2: Cắm thiết bị điện trực tiếp vào nguồn khi công tắc chưa tắt.'
    ],
    visualAsset: 'src/assets/safety_signs.svg'
  },
  {
    id: 'lesson-3',
    number: 3,
    title: 'Thực hành tính sai số trong phép đo. Ghi kết quả đo',
    chapter: 'Chương I: Mở đầu',
    keyConcepts: [
      'Phép đo trực tiếp: So sánh trực tiếp qua dụng cụ đo (đo chiều dài bằng thước).',
      'Phép đo gián tiếp: Xung quanh công thức toán học từ các phép đo trực tiếp (tính vận tốc v = s / t).',
      'Sai số hệ thống: Do dụng cụ (chủ yếu) hoặc thao tác sai lệch cố định. Sai số dụng cụ ΔA_dch lấy bằng một nửa hoặc một độ chia nhỏ nhất (ĐCNNT).',
      'Sai số ngẫu nhiên: Do tác động bên ngoài không kiểm soát được, tính bằng trung bình các độ lệch: ΔA_tb = (|A_1 - A_tb| + |A_2 - A_tb| + ...) / n.',
      'Sai số tuyệt đối: ΔA = ΔA_tb + ΔA_dch. Cách ghi kết quả: A = A_tb ± ΔA (ΔA quy tròn đến 1 chữ số có nghĩa).',
      'Sai số tỉ đối: δA = (ΔA / A_tb) × 100% (Đánh giá mức độ chính xác của phép đo).'
    ],
    formulas: [
      {
        category: 'Sai số tuyệt đối',
        name: 'Công thức ΔA',
        symbolFormula: 'ΔA = ΔA_tb + ΔA_dch',
        notes: 'ΔA_tb là sai số ngẫu nhiên trung bình, ΔA_dch là sai số dụng cụ.'
      },
      {
        category: 'Sai số tỉ đối',
        name: 'Công thức δA',
        symbolFormula: 'δA = (ΔA / A_tb) × 100%',
        notes: 'Đơn vị %.'
      }
    ],
    commonTraps: [
      'Bẫy 1: Ghi chữ số thập phân của A_tb khác với số chữ số thập phân của ΔA. (Quy tắc: A_tb và ΔA phải có cùng số chữ số sau dấu phẩy!).',
      'Bẫy 2: Nhầm sai số dụng cụ lấy bằng 1 ĐCNNT thay vì nửa ĐCNNT khi đề bài quy định.'
    ]
  },
  {
    id: 'lesson-4',
    number: 4,
    title: 'Độ dịch chuyển và quãng đường đi được',
    chapter: 'Chương II: Động học',
    keyConcepts: [
      'Quãng đường đi được (s): Độ dài quỹ đạo thực tế vật đã đi. s luôn ≥ 0.',
      'Độ dịch chuyển (d): Vectơ nối từ vị trí đầu đến vị trí cuối: d = x_cuối - x_đầu. Độ lớn d = |x_cuối - x_đầu|.',
      'Mối quan hệ: Khi vật chuyển động thẳng và KHÔNG ĐỔI CHIỀU thì d = s. Khi vật đổi chiều hoặc đi đường cong thì s > d.',
      'Tổng hợp độ dịch chuyển: d_tổng = d_1 + d_2 (Cộng vectơ).'
    ],
    formulas: [
      {
        category: 'Độ dịch chuyển',
        name: 'Tọa độ độ dịch chuyển',
        symbolFormula: 'd = Δx = x_2 - x_1',
        notes: 'Có thể mang giá trị dương, âm hoặc bằng 0.'
      }
    ],
    commonTraps: [
      'Bẫy 1: Mặc định độ dịch chuyển luôn bằng quãng đường. (Chỉ bằng nhau khi chuyển động thẳng và không quay đầu!).',
      'Bẫy 2: Tính độ dịch chuyển khi vật đi từ A đến B rồi quay lại A bằng 2AB. (Đúng: d = 0 vì vị trí đầu trùng vị trí cuối).'
    ],
    visualAsset: 'src/assets/displacement_velocity.svg'
  },
  {
    id: 'lesson-5',
    number: 5,
    title: 'Tốc độ và vận tốc',
    chapter: 'Chương II: Động học',
    keyConcepts: [
      'Tốc độ trung bình: v_tb = s / t (Đặc trưng cho độ nhanh chậm trên quãng đường s, vô hướng ≥ 0).',
      'Vận tốc trung bình: v_vecto = d / t (Đặc trưng cho tốc độ và chiều chuyển động, đại lượng vectơ).',
      'Tốc độ tức thời: Tốc độ tại một thời điểm xác định.',
      'Công thức cộng vận tốc: v_1,3 = v_1,2 + v_2,3. Trong đó: 1 là vật chuyển động, 2 là hệ quy chiếu chuyển động (nước, tàu), 3 là hệ quy chiếu đứng yên (bờ, đường).'
    ],
    formulas: [
      {
        category: 'Vận tốc',
        name: 'Cộng vận tốc vuông góc',
        symbolFormula: 'v_1,3 = √(v_1,2² + v_2,3²)',
        notes: 'Khi v_1,2 ⊥ v_2,3 (Ví dụ ca nô chạy vuông góc với dòng nước chảy).'
      }
    ],
    commonTraps: [
      'Bẫy 1: Lấy trung bình cộng hai tốc độ (v_1 + v_2)/2 để tính tốc độ trung bình trên toàn bộ chuyến đi. (Đúng: v_tb = (s_1 + s_2) / (t_1 + t_2)).',
      'Bẫy 2: Nhầm lẫn vị trí 1, 2, 3 trong công thức cộng vận tốc.'
    ],
    visualAsset: 'src/assets/displacement_velocity.svg'
  },
  {
    id: 'lesson-6',
    number: 6,
    title: 'Thực hành: Đo tốc độ của vật chuyển động',
    chapter: 'Chương II: Động học',
    keyConcepts: [
      'Dụng cụ: Đồng hồ đo thời gian hiện số MC964, cổng quang điện (E, F), máng nghiêng, viên bi thép, thước đo.',
      'Chế độ MODE A/B: Đo thời gian chắn 1 cổng quang điện → Đo tốc độ tức thời v_t = d_bi / t_chắn.',
      'Chế độ MODE A↔B: Đo thời gian bi đi từ cổng E đến cổng F → Đo tốc độ trung bình v_tb = s_EF / t_AB.',
      'Chế độ MODE A+B: Tổng thời gian bi chắn cả 2 cổng.',
      'Ưu điểm: Độ chính xác cực cao (0,001 s), loại bỏ sai số do phản xạ con người. Nhược điểm: Đắt tiền, cồng kềnh.'
    ],
    formulas: [
      {
        category: 'Đo tốc độ',
        name: 'Tốc độ tức thời',
        symbolFormula: 'v = d_bi / t_A',
        notes: 'd_bi là đường kính viên bi, t_A là thời gian bi chắn cổng A.'
      }
    ],
    commonTraps: [
      'Bẫy 1: Nhầm giữa MODE A (đo tốc độ tức thời) và MODE A↔B (đo tốc độ trung bình trên quãng đường s_EF).',
      'Bẫy 2: Tính tốc độ tức thời dùng chiều dài máng nghiêng thay vì đường kính viên bi d_bi.'
    ],
    visualAsset: 'src/assets/photogate_setup.svg'
  },
  {
    id: 'lesson-7',
    number: 7,
    title: 'Đồ thị độ dịch chuyển – thời gian (d – t)',
    chapter: 'Chương II: Động học',
    keyConcepts: [
      'Ý nghĩa: Biểu diễn sự phụ thuộc của độ dịch chuyển d theo thời gian t.',
      'Độ dốc (Slope) của đồ thị (d – t): Vận tốc v = (d_2 - d_1) / (t_2 - t_1).',
      'Đặc điểm các đoạn đồ thị:',
      '  - Đồ thị là đường thẳng xiên lên: v > 0 (vật chuyển động thẳng đều theo chiều dương).',
      '  - Đồ thị nằm ngang: v = 0 (vật đứng yên).',
      '  - Đồ thị xiên xuống: v < 0 (vật chuyển động thẳng đều theo chiều âm, quay về gốc).'
    ],
    formulas: [
      {
        category: 'Đồ thị d-t',
        name: 'Vận tốc từ đồ thị',
        symbolFormula: 'v = Slope = Δd / Δt = (d_2 - d_1) / (t_2 - t_1)',
        notes: 'Góc nghiêng α lớn hơn → vận tốc lớn hơn.'
      }
    ],
    commonTraps: [
      'Bẫy 1: Nhầm đồ thị (d - t) là quỹ đạo chuyển động thực tế của vật.',
      'Bẫy 2: Nhầm đồ thị (d - t) nằm ngang là vật chuyển động đều (Đúng: nằm ngang nghĩa là d không đổi → v = 0 → ĐỨNG YÊN!).'
    ],
    visualAsset: 'src/assets/dt_vs_vt_graphs.svg'
  },
  {
    id: 'lesson-8',
    number: 8,
    title: 'Chuyển động biến đổi. Gia tốc',
    chapter: 'Chương II: Động học',
    keyConcepts: [
      'Chuyển động biến đổi: Chuyển động có vận tốc thay đổi theo thời gian.',
      'Gia tốc: Đại lượng đặc trưng cho sự biến thiên nhanh hay chậm của vận tốc: a_vecto = Δv_vecto / Δt.',
      'Đơn vị gia tốc: m/s².',
      'Vectơ gia tốc: Cùng chiều với vectơ vận tốc khi chuyển động nhanh dần (a.v > 0). Ngược chiều với vectơ vận tốc khi chuyển động chậm dần (a.v < 0).'
    ],
    formulas: [
      {
        category: 'Gia tốc',
        name: 'Công thức gia tốc trung bình',
        symbolFormula: 'a = (v - v_0) / (t - t_0)',
        notes: 'v_0 là vận tốc ban đầu, v là vận tốc lúc sau.'
      }
    ],
    commonTraps: [
      'Bẫy 1: Cho rằng gia tốc âm (a < 0) luôn là chuyển động chậm dần đều. (Đúng: Tùy thuộc dấu của v! Nếu a < 0 và v < 0 thì a.v > 0 → Nhanh dần đều theo chiều âm!).',
      'Bẫy 2: Nhầm gia tốc bằng 0 là dừng lại. (a = 0 nghĩa là vận tốc KHÔNG ĐỔI → Chuyển động thẳng đều hoặc đứng yên).'
    ]
  },
  {
    id: 'lesson-9',
    number: 9,
    title: 'Chuyển động thẳng biến đổi đều',
    chapter: 'Chương II: Động học',
    keyConcepts: [
      'Định nghĩa: Chuyển động thẳng có gia tốc a không đổi theo thời gian (a = const).',
      'Chuyển động thẳng nhanh dần đều (CTNDĐ): Tốc độ tăng đều theo thời gian, a.v > 0.',
      'Chuyển động thẳng chậm dần đều (CTCDĐ): Tốc độ giảm đều theo thời gian, a.v < 0.',
      'Bộ 3 công thức cốt lõi:',
      '  1) v = v_0 + a.t',
      '  2) d = v_0.t + (1/2).a.t²',
      '  3) v² - v_0² = 2.a.d',
      'Đồ thị (v - t): Đường thẳng xiên góc. Độ dốc = Gia tốc a. Diện tích dưới đồ thị (v - t) = Độ dịch chuyển d.'
    ],
    formulas: [
      {
        category: 'CĐTBĐĐ',
        name: 'Bộ công thức độc lập',
        symbolFormula: 'v² - v_0² = 2.a.d',
        notes: 'Dùng khi đề không cho biến t.'
      }
    ],
    commonTraps: [
      'Bẫy 1: Quên đổi đơn vị km/h ra m/s (chia cho 3.6) trước khi thế vào công thức.',
      'Bẫy 2: Nhầm lẫn dấu của gia tốc a khi vật chuyển động chậm dần đều.',
      'Bẫy 3: Vật hãm phanh đến khi dừng lại thì v = 0. Nếu t lớn hơn thời gian dừng lại thì s chỉ tính đến lúc v = 0.'
    ],
    visualAsset: 'src/assets/dt_vs_vt_graphs.svg'
  },
  {
    id: 'lesson-10',
    number: 10,
    title: 'Sự rơi tự do',
    chapter: 'Chương II: Động học',
    keyConcepts: [
      'Định nghĩa: Sự rơi tự do là sự rơi chỉ chịu tác dụng của trọng lực.',
      'Đặc điểm:',
      '  - Phương thẳng đứng, chiều từ trên xuống dưới.',
      '  - Là chuyển động thẳng nhanh dần đều với vận tốc ban đầu v_0 = 0.',
      '  - Tại cùng một vị trí địa lý, mọi vật rơi tự do với cùng gia tốc g (g ≈ 9.8 m/s² hoặc 10 m/s²).',
      'Công thức:',
      '  - v = g.t',
      '  - h = (1/2).g.t²',
      '  - v² = 2.g.h → v = √(2gh)',
      'Quãng đường rơi trong giây thứ n: Δh_n = h(n) - h(n - 1) = (1/2).g.[n² - (n - 1)²] = (1/2).g.(2n - 1).'
    ],
    formulas: [
      {
        category: 'Rơi tự do',
        name: 'Thời gian rơi từ độ cao h',
        symbolFormula: 't = √(2h / g)',
        notes: 'Chỉ phụ thuộc h và g, không phụ thuộc m!'
      }
    ],
    commonTraps: [
      'Bẫy 1: Cho rằng vật nặng rơi nhanh hơn vật nhẹ trong chân không. (Đúng: Rơi như nhau vì gia tốc g như nhau!).',
      'Bẫy 2: Nhầm "quãng đường đi trong n giây" với "quãng đường đi trong giây thứ n".'
    ]
  }
];

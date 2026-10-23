# -*- coding: utf-8 -*-
"""Bộ câu hỏi – đáp án của bài kiểm tra giữa kỳ I (Vật lí 10, 2026–2027).

Bộ câu hỏi được xây dựng để **hiện thực hoá 100% các ô của ma trận đặc tả**:
  • Phần I  – Trắc nghiệm : 18 câu (10 "Biết" + 8 "Hiểu")
  • Phần II – Tự luận      : 2 câu × 4 ý (6 ý "Biết" + 2 ý "Hiểu")
  • Phần III               : 2 câu (1 "Biết" + 1 "Hiểu")
  • Phần IV                : 3 câu (1 "Hiểu" + 2 "Vận dụng")
"""

# --------------------------------------------------------------------------
# PHẦN I – TRẮC NGHIỆM (18 câu)
# --------------------------------------------------------------------------
MC = [
    {
        'no': 1, 'unit': '1.1', 'level': 'Biết',
        'stem': 'Đối tượng nghiên cứu chủ yếu của vật lí là',
        'options': [
            'Cấu trúc hóa học và thành phần của các chất',
            'Các hiện tượng vật lý xảy ra trong tự nhiên, trong đời sống và trong sản xuất',
            'Quá trình sinh sản, di truyền và phát triển của sinh vật',
            'Cơ chế kinh tế – xã hội của một nước',
        ],
        'answer': 'B',
        'explain': 'Vật lí nghiên cứu các hiện tượng vật lý, cấu trúc và các quy luật vận động – '
                   'tương tác của vật chất. Hoá học nghiên cứu thành phần và tính chất của chất '
                   '(phương án A), sinh học nghiên cứu cơ sở vật chất của sự sống (phương án C).',
    },
    {
        'no': 2, 'unit': '1.2', 'level': 'Biết',
        'stem': 'Trong phòng thực hành vật lí, tai nạn điện giật thường xảy ra khi',
        'options': [
            'Bật quạt thông gió cho phòng thí nghiệm',
            'Làm việc dưới ánh sáng của đèn LED',
            'Mở cửa sổ thông gió cho phòng thí nghiệm',
            'Cầm dây dẫn có dòng điện hoặc chạm tay vào vỏ dụng cụ bị rò rỉ điện',
        ],
        'answer': 'D',
        'explain': 'Điện giật xảy ra khi cơ thể tiếp xúc với vật đang mang điện (dây dẫn hở, '
                   'vỏ dụng cụ bị rò rỉ điện). Vì vậy phải nối đất các thiết bị và cắt nguồn điện '
                   'khi có sự cố.',
    },
    {
        'no': 3, 'unit': '1.3', 'level': 'Biết',
        'stem': 'Sai số tuyệt đối của phép đo được tính theo công thức nào?',
        'options': [
            'δ = (Δx/x̄) × 100%',
            'Δx = x̄ − x',
            'x̄ = (x<sub>1</sub> + x<sub>2</sub> + … + x<sub>n</sub>)/n',
            'Δx = |x̄ − x|',
        ],
        'answer': 'D',
        'explain': 'Sai số tuyệt đối Δx = |x̄ − x| luôn **không âm** nên phải lấy giá trị tuyệt đối. '
                   'Phương án A là sai số tỉ đối, phương án C là công thức giá trị trung bình. '
                   'Phương án B sai vì thiếu dấu giá trị tuyệt đối.',
    },
    {
        'no': 4, 'unit': '2.1', 'level': 'Biết',
        'stem': 'Quan hệ giữa độ dịch chuyển và quãng đường đi được là',
        'options': [
            'Độ lớn độ dịch chuyển luôn lớn hơn quãng đường đi được',
            'Độ lớn độ dịch chuyển không lớn hơn quãng đường đi được và bằng nó khi vật chuyển động thẳng',
            'Độ lớn độ dịch chuyển luôn bằng quãng đường đi được',
            'Quãng đường đi được luôn bằng 0 khi vật chuyển động thẳng',
        ],
        'answer': 'B',
        'explain': 'Luôn có |Δr| ≤ s. Khi vật đi thẳng từ A đến B thì đường đi chính là đoạn thẳng AB '
                   'nên |Δr| = s. Nếu vật đi vòng, quãng đường đi được lớn hơn độ dịch chuyển.',
    },
    {
        'no': 5, 'unit': '2.2', 'level': 'Biết',
        'stem': 'Vận tốc của một vật khác tốc độ của vật đó ở điểm nào?',
        'options': [
            'Vận tốc có hướng, còn tốc độ không có hướng',
            'Vận tốc không có hướng, còn tốc độ có hướng',
            'Vận tốc và tốc độ đều có hướng',
            'Vận tốc và tốc độ đều không có hướng',
        ],
        'answer': 'A',
        'explain': 'Vận tốc (**vectơ**) **v** = **Δr**/Δt là **vectơ** (có hướng và độ lớn), còn tốc độ v = s/t '
                   'là **đại lượng vô hướng** chỉ có độ lớn.',
    },
    {
        'no': 6, 'unit': '2.3', 'level': 'Biết',
        'stem': 'Trên đồ thị độ dịch chuyển – thời gian (x–t), độ dốc của đường thẳng biểu thị đại lượng nào?',
        'options': [
            'Vận tốc của vật',
            'Gia tốc của vật',
            'Quãng đường đi được của vật',
            'Thời gian vật chuyển động',
        ],
        'answer': 'A',
        'explain': 'v = Δx/Δt chính là **độ dốc** của đồ thị x–t. Gia tốc là độ dốc của đồ thị v–t.',
    },
    {
        'no': 7, 'unit': '2.4', 'level': 'Biết',
        'stem': 'Gia tốc là đại lượng đặc trưng cho',
        'options': [
            'quãng đường đi được của vật',
            'tốc độ thay đổi của vật theo thời gian',
            'vị trí của vật trong không gian',
            'thời gian vật chuyển động',
        ],
        'answer': 'B',
        'explain': '**a** = Δ**v**/Δt đặc trưng cho **tốc độ thay đổi** của vật theo thời gian; '
                   'đơn vị đo của gia tốc là **m/s²**.',
    },
    {
        'no': 8, 'unit': '2.5', 'level': 'Biết',
        'stem': 'Chuyển động thẳng biến đổi đều là chuyển động thẳng có gia tốc',
        'options': [
            'không đổi theo thời gian',
            'tăng đều theo thời gian',
            'giảm đều theo thời gian',
            'bằng không trong suốt quá trình chuyển động',
        ],
        'answer': 'A',
        'explain': 'Điểm mấu chốt của CĐTBĐĐ là **gia tốc không đổi** (hằng số theo thời gian); '
                   'vận tốc thì thay đổi đều đặc biệt khi a ≠ 0.',
    },
    {
        'no': 9, 'unit': '2.5', 'level': 'Biết',
        'stem': 'Trong chuyển động thẳng biến đổi đều, vận tốc của vật ở thời điểm t được tính theo công thức',
        'options': [
            'v = v<sub>0</sub> − at',
            'v = 2s/t',
            'v = ½at<sup>2</sup>',
            'v = v<sub>0</sub> + at',
        ],
        'answer': 'D',
        'explain': 'v = v<sub>0</sub> + at là công thức liên hệ giữa vận tốc và thời gian trong CĐTBĐĐ. '
                   'Phương án B chỉ đúng khi v là vận tốc trung bình, phương án C là công thức quãng đường.',
    },
    {
        'no': 10, 'unit': '2.6', 'level': 'Biết',
        'stem': 'Vật rơi tự do trong không khí có gia tốc',
        'options': [
            'bằng g và có hướng thẳng xuống',
            'bằng g và có hướng thẳng lên',
            'bằng 0 và có hướng thẳng xuống',
            'tùy thuộc vào khối lượng và hình dạng của vật',
        ],
        'answer': 'A',
        'explain': 'Rơi tự do là rơi không chịu lực cản không khí nên vật chỉ chịu trọng lực: '
                   'a = g ≈ 9,8 m/s², vectơ gia tốc hướng thẳng xuống và **không phụ thuộc** '
                   'khối lượng, hình dạng của vật.',
    },
    {
        'no': 11, 'unit': '1.2', 'level': 'Hiểu',
        'stem': 'Biển báo an toàn có hình tròn nền xanh dương, mang ký hiệu bắt buộc '
                '(ví dụ ký hiệu đeo kính bảo hộ) có ý nghĩa là',
        'options': [
            'Bắt buộc phải thực hiện đúng quy tắc đó khi làm thí nghiệm',
            'Cảnh báo về nguy hiểm có thể xảy ra trong phòng thí nghiệm',
            'Cấm hoàn toàn việc thực hiện thao tác đó',
            'Chỉ dẫn lối thoát hiểm khi xảy ra sự cố',
        ],
        'answer': 'A',
        'explain': 'Biển báo **bắt buộc** (xanh dương) yêu cầu phải tuân thủ; **cảnh báo** là hình '
                   'tam giác vàng; **cấm** là hình tròn đỏ có gạch chéo; **thoát hiểm** là hình chữ '
                   'nhật xanh lá.',
    },
    {
        'no': 12, 'unit': '2.1', 'level': 'Hiểu',
        'stem': 'Một người đi bộ được 3 km từ A đến B theo đường thẳng, sau đó quay lại A được 1 km. '
                'Quãng đường đi được và độ dịch chuyển của người đó là',
        'options': [
            's = 3 km ; Δr = 4 km',
            's = 2 km ; Δr = 4 km',
            's = 4 km ; Δr = 4 km',
            's = 4 km ; Δr = 2 km',
        ],
        'answer': 'D',
        'explain': 'Quãng đường đi được s = 3 + 1 = 4 km. Độ dịch chuyểc có hướng từ A về phía B '
                   'với độ lớn Δr = 3 − 1 = 2 km (vì người đó đã quay ngược lại 1 km).',
    },
    {
        'no': 13, 'unit': '2.1', 'level': 'Hiểu',
        'stem': 'Một vật chuyển động trên một quỹ đạo tròn đều. Khi đó vận độ dịch chuyển và tốc độ '
                'của vật thay đổi như thế nào?',
        'options': [
            'Vận độ dịch chuyển không đổi, tốc độ thay đổi',
            'Vận độ dịch chuyển thay đổi, tốc độ không đổi',
            'Vận độ dịch chuyển không đổi, tốc độ không đổi',
            'Cả vận độ dịch chuyển và tốc độ đều thay đổi',
        ],
        'answer': 'B',
        'explain': 'Đi trên quỹ đạo tròn thì **Δr** liên tục đổi hướng ⇒ vận độ dịch chuyển thay đổi; '
                   'còn độ lớn vận tốc không đổi ⇒ tốc độ không đổi. Đây là **chuyển động cong đều**.',
    },
    {
        'no': 14, 'unit': '2.3', 'level': 'Hiểu',
        'stem': 'Trên đồ thị độ dịch chuyển – thời gian (x–t) của một vật, có một đoạn là đường thẳng '
                'đi xuống. Vật đang chuyển động',
        'options': [
            'theo chiều dương và tốc độ tăng dần',
            'đứng yên',
            'theo chiều âm và với tốc độ không đổi',
            'theo chiều dương và tốc độ giảm dần',
        ],
        'answer': 'C',
        'explain': 'Đồ thị đi xuống ⇒ x giảm ⇒ vận tốc **âm** (vật đi ngược chiều dương). '
                   'Vì đoạn đồ thị là **đường thẳng** nên độ dốc không đổi ⇒ tốc độ không đổi.',
    },
    {
        'no': 15, 'unit': '2.4', 'level': 'Hiểu',
        'stem': 'Một vật đang chuyển động theo chiều dương với vận tốc 6 m/s và gia tốc 2 m/s². '
                'Phát biểu nào sau đây đúng?',
        'options': [
            'Vật chuyển động nhanh dần vì gia tốc cùng hướng với vận tốc',
            'Vật chuyển động nhanh dần vì gia tốc luôn dương',
            'Vật chuyển động chậm dần vì gia tốc ngược chiều với vận tốc',
            'Vật chuyển động đều vì gia tốc không đổi theo thời gian',
        ],
        'answer': 'A',
        'explain': 'Vật đang đi theo chiều dương (v = +6 m/s) và a = +2 m/s² cũng theo chiều dương ⇒ '
                   'a và v **cùng hướng** ⇒ vận tốc tăng dần ⇒ chuyển động nhanh dần. '
                   'Phương án B chỉ đúng nếu vật đang chạy theo chiều dương.',
    },
    {
        'no': 16, 'unit': '2.5', 'level': 'Hiểu',
        'stem': 'Trong chuyển động thẳng biến đổi đều, trường hợp nào vật chuyển động nhanh dần đều?',
        'options': [
            'a > 0 và v<sub>0</sub> < 0',
            'a và v<sub>0</sub> ngược dấu',
            'a = 0 và v<sub>0</sub> ≠ 0',
            'a và v<sub>0</sub> cùng dấu',
        ],
        'answer': 'D',
        'explain': 'Chuyển động nhanh dần đều khi **gia tốc và vận tốc đầu cùng dấu** (|v| tăng đều). '
                   'Nếu a và v<sub>0</sub> ngược dấu thì vật chuyển động chậm dần đều.',
    },
    {
        'no': 17, 'unit': '2.6', 'level': 'Hiểu',
        'stem': 'Trong cùng điều kiện, một viên bi và một tờ giấy có cùng khối lượng được thả rơi '
                'cùng lúc. Tờ giấy rơi chậm hơn viên bi. Nguyên nhân chính là',
        'options': [
            'Gia tốc rơi tự do phụ thuộc vào khối lượng riêng của vật',
            'Gia tốc rơi tự do phụ thuộc vào hình dạng của vật',
            'Lực cản của không khí lớn hơn đối với tờ giấy có diện tích mặt cắn ngang lớn',
            'Tờ giấy nhẹ hơn nên rơi chậm hơn',
        ],
        'answer': 'C',
        'explain': 'Gia tốc g **không** phụ thuộc khối lượng, khối lượng riêng hay hình dạng. '
                   'Tờ giấy có diện tích mặt cắn ngang lớn nên chịu **lực cản không khí** lớn hơn ⇒ '
                   'a < g ⇒ rơi chậm hơn ⇒ chỉ **gần đúng tự do**.',
    },
    {
        'no': 18, 'unit': '2.6', 'level': 'Hiểu',
        'stem': 'Thả cùng một vật trong ống chân không (không có không khí) và trong không khí. '
                'Kết luận nào sau đây đúng?',
        'options': [
            'Trong ống chân không vật rơi chậm hơn vì không có không khí đẩy vật lên',
            'Vật rơi giống nhau trong cả hai trường hợp vì g không đổi',
            'Trong ống chân không vật rơi nhanh hơn, gia tốc bằng g; trong không khí vật chỉ rơi '
            'gần đúng tự do',
            'Trong không khí vật rơi nhanh hơn vì lực cản không khí sinh gia tốc',
        ],
        'answer': 'C',
        'explain': 'Trong ống chân không không có lực cản không khí ⇒ vật rơi **tự do hoàn toàn**, '
                   'a = g. Trong không khí, lực cản làm a < g ⇒ vật chỉ rơi **gần đúng tự do**, '
                   'rơi chậm hơn và tốc độ chạm đất nhỏ hơn.',
    },
]

# --------------------------------------------------------------------------
# PHẦN II – TỰ LUẬN (2 câu, mỗi câu 4 ý)
# --------------------------------------------------------------------------
PHAN_II = [
    {
        'no': 1,
        'unit': '2.2 (2 ý) + 2.3 (2 ý)',
        'topic': 'Tốc độ trung bình và đồ thị độ dịch chuyển – thời gian',
        'stem': 'Một người đi bộ từ nhà đến trường theo đường thẳng với tốc độ 4 km/h; '
                'nhà cách trường 2 km. Người đó tới trường rồi quay lại nhà với tốc độ 6 km/h.',
        'parts': [
            ('a)', 'Tính thời gian người đó đi từ nhà đến trường và thời gian quay lại nhà.',
             ['t<sub>1</sub> = s/v = 2/4 = **0,5 h = 30 phút**.',
              't<sub>2</sub> = s/v = 2/6 = 1/3 h ≈ **20 phút**.']),
            ('b)', 'Tính tốc độ trung bình của người đó trên toàn bộ chặng đường đi và về '
                   '(trình bày cả km/h và m/s).',
             ['Quãng đường đi được: s = 2 + 2 = **4 km**.',
              'Tổng thời gian: t = 0,5 + 1/3 = 5/6 h = **50 phút**.',
              'v<sub>tb</sub> = s/t = 4/(5/6) = **4,8 km/h**.',
              'Đổi sang m/s: v = 4,8/3,6 ≈ **1,33 m/s**.']),
            ('c)', 'Vẽ đồ thị độ dịch chuyển – thời gian của chuyển động trên (chọn gốc tọa độ tại '
                   'nhà, chiều dương hướng từ nhà về trường) và giải thích ý nghĩa của đồ thị.',
             ['Các điểm đặc biệt: O(0 h; 0 km) → A(0,5 h; 2 km) → B(5/6 h; 0 km).',
              'Vẽ **O–A–B**: đoạn OA đi lên (độ dốc dương, vật đi theo chiều dương), '
              'đoạn AB đi xuống (độ dốc âm, vật quay lại).',
              'Độ dốc OA = 2/0,5 = 4 km/h (tốc độ khi đi); độ dốc AB = −2/(1/3) = −6 km/h '
              '(vận tốc −6 km/h khi về).',
              'Điểm B trùng O ⇒ vật đã trở về đúng điểm xuất phát.']),
            ('d)', 'Tính quãng đường đi được và độ dịch chuyển của người đó trong toàn bộ hành trình.',
             ['Quãng đường đi được: s = 2 + 2 = **4 km** (đi 2 km tới trường, 2 km quay lại).',
              'Độ dịch chuyển: Δx = x<sub>cuối</sub> − x<sub>đầu</sub> = 0 − 0 = **0** '
              '(người đó trở về đúng nhà).',
              'Kiểm tra: |Δr| = 0 ≤ s = 4 km ✔']),
        ],
    },
    {
        'no': 2,
        'unit': '2.5 (2 ý Biết + 2 ý Hiểu)',
        'topic': 'Chuyển động thẳng biến đổi đều',
        'stem': 'Một ô tô chuyển động thẳng biến đổi đều trên đường thẳng với vận tốc ban đầu '
                'v<sub>0</sub> = 20 m/s và gia tốc a = −2 m/s².',
        'parts': [
            ('a)', 'Tính vận tốc của ô tô sau 5 s chuyển động.',
             ['v = v<sub>0</sub> + at = 20 + (−2)×5 = **10 m/s**.',
              'Vận tốc vẫn dương ⇒ ô tô vẫn đang đi theo chiều dương.']),
            ('b)', 'Tính quãng đường ô tô đi được trong 5 s đó.',
             ['s = v<sub>0</sub>t + ½at<sup>2</sup> = 20×5 + ½×(−2)×25 = 100 − 25 = **75 m**.',
              '(Có thể dùng công thức s = ½(v<sub>0</sub> + v)t = ½(20 + 10)×5 = 75 m.)']),
            ('c)', 'Tìm thời điểm ô tô dừng lại và quãng đường ô tô đi được từ lúc xuất phát '
                   'đến lúc dừng.',
             ['Khi dừng: v = 0 ⇒ 0 = 20 + (−2)t ⇒ **t = 10 s**.',
              'Quãng đường đến lúc dừng: s = 20×10 + ½×(−2)×100 = 200 − 100 = **100 m**.',
              '(Có thể dùng công thức ④: 0 − 20² = 2×(−2)×s ⇒ s = 100 m.)']),
            ('d)', 'Trong 5 s đầu, ô tô chuyển động nhanh dần hay chậm dần? Giải thích. Vẽ đồ thị '
                   'vận tốc – thời gian và dùng đồ thị để xác định quãng đường ô tô đi được trong 5 s đầu.',
             ['a = −2 m/s² ngược hướng v<sub>0</sub> (= +20 m/s) ⇒ **chậm dần đều** trong 5 s đầu.',
              'Đồ thị v–t là **đường thẳng** đi xuống, đi qua (0 s; 20 m/s) và (5 s; 10 m/s), '
              'cắt trục hoành tại t = 10 s; độ dốc = a = −2 m/s².',
              'Quãng đường trong 5 s đầu = **diện tích hình thang** dưới đồ thị: '
              'S = ½(20 + 10)×5 = **75 m** ✔ (khớp với ý b).',
              'Lưu ý: sau giây thứ 10, ô tô đổi chiều (v < 0) nên quãng đường tiếp tục tăng '
              'nhưng độ dịch chuyển âm.']),
        ],
    },
]

# --------------------------------------------------------------------------
# PHẦN III – 2 câu
# --------------------------------------------------------------------------
PHAN_III = [
    {
        'no': 1,
        'unit': '2.2',
        'level': 'Biết',
        'topic': 'Đo tốc độ bằng hai cổng quang điện',
        'stem': 'Trong phòng thí nghiệm, hai cổng quang điện được đặt cách nhau L = 1,2 m. '
                'Đồng hồ đo thời gian hiện số ghi thời gian vật chặn cổng 1 là t<sub>1</sub> = 0,50 s '
                'và thời gian vật chặn cổng 2 là t<sub>2</sub> = 1,10 s. '
                'Tính tốc độ của vật khi nó đi giữa hai cổng.',
        'parts': [
            ('a)', 'Tính thời gian vật đi giữa hai cổng.',
             ['Δt = t<sub>2</sub> − t<sub>1</sub> = 1,10 − 0,50 = **0,60 s**.',
              '(Chú ý: không được dùng trực tiếp t<sub>1</sub> hay t<sub>2</sub>.)']),
            ('b)', 'Tính tốc độ của vật giữa hai cổng.',
             ['v = L/Δt = 1,2/0,60 = **2,0 m/s**.',
              'Đơn vị: m/s (nếu dùng km/h thì v = 7,2 km/h).']),
            ('c)', 'Giải thích ý nghĩa của việc dùng **hai** cổng quang điện và ưu điểm của phép đo này '
                   'so với dùng đồng hồ đo thời gian hiện số.',
             ['Hai cổng cho phép **đo tự động** thời gian vật đi qua từng vị trí, nhờ đó tính được '
              '**tốc độ tức thời** của vật tại vị trí giữa hai cổng.',
              'Ưu điểm: **không ảnh hưởng** tới chuyển động của vật, độ chính xác cao, không cần '
              'phản ứng bấm đồng hồ.',
              'Nhược điểm: phải bố trí đúng vị trí hai cổng, chỉ đo được vật đi xuyên qua cổng.']),
        ],
    },
    {
        'no': 2,
        'unit': '2.6',
        'level': 'Hiểu',
        'topic': 'Rơi tự do và so sánh với rơi gần đúng tự do',
        'stem': 'Một vật được thả rơi tự do từ độ cao h = 20 m, lấy g = 10 m/s².',
        'parts': [
            ('a)', 'Thời gian để vật rơi đến khi chạm đất.',
             ['h = ½gt<sup>2</sup> ⇒ 20 = ½×10×t<sup>2</sup> ⇒ t<sup>2</sup> = 4 ⇒ **t = 2 s**.']),
            ('b)', 'Tốc độ của vật ngay trước khi chạm đất.',
             ['v = gt = 10×2 = **20 m/s**.',
              '(Kiểm tra: v = √(2gh) = √(2×10×20) = 20 m/s ✔)']),
            ('c)', 'Nếu thả vật đó trong ống chân không thì kết quả ở a) và b) có thay đổi không? '
                   'Giải thích bằng cách so sánh với trường hợp thả trong không khí.',
             ['**Trong ống chân không:** không có lực cản không khí ⇒ rơi tự do hoàn toàn, a = g ⇒ '
              '**kết quả a) và b) không thay đổi** (t = 2 s, v = 20 m/s).',
              '**Trong không khí:** có lực cản không khí ⇒ a < g ⇒ thời gian rơi **lớn hơn 2 s**, '
              'tốc độ chạm đất **nhỏ hơn 20 m/s** ⇒ vật chỉ rơi **gần đúng tự do**.',
              'Kết luận: chỉ khi không có lực cản không khí, vật mới rơi tự do hoàn toàn.']),
        ],
    },
]

# --------------------------------------------------------------------------
# PHẦN IV – 3 câu
# --------------------------------------------------------------------------
PHAN_IV = [
    {
        'no': 1,
        'unit': '2.2',
        'level': 'Hiểu',
        'topic': 'Tổng hợp vận tốc cùng phương',
        'stem': 'Trên cùng một đường thẳng, một xe khách chạy với vận tốc 54 km/h và một xe máy '
                'chạy với vận tốc 36 km/h.',
        'parts': [
            ('a)', 'Nếu hai xe chạy **cùng chiều**, tính vận tốc của xe khách đối với xe máy.',
             ['Cùng phương, cùng chiều: v = v<sub>1</sub> + v<sub>2</sub> = 54 + 36 = **90 km/h**.',
              'Đổi đơn vị: 90 km/h = 25 m/s (và 54 km/h = 15 m/s; 36 km/h = 10 m/s).']),
            ('b)', 'Nếu hai xe chạy **ngược chiều**, tính vận tốc của xe khách đối với xe máy.',
             ['Cùng phương, ngược chiều: v = |v<sub>1</sub> − v<sub>2</sub>| = |54 − 36| = **18 km/h**.',
              'Đổi đơn vị: 18 km/h = 5 m/s.']),
            ('c)', 'Nếu một xe khách và một xe đạp chạy **vuông góc** với nhau tại một giao lộ với '
                   'vận tốc lần lượt là 54 km/h và 36 km/h, tính vận tốc của xe khách đối với xe đạp.',
             ['Hai vận tốc vuông góc: v = √(v<sub>1</sub><sup>2</sup> + v<sub>2</sub><sup>2</sup>) '
              '= √(54² + 36²) = √(2916 + 1296) = √4212 ≈ **64,9 km/h**.',
              '(Hoặc: v = √(15² + 10²) = √325 ≈ 18,0 m/s.)']),
        ],
    },
    {
        'no': 2,
        'unit': '2.5',
        'level': 'Vận dụng',
        'topic': 'Chuyển động thẳng biến đổi đều – bài toán cơ bản',
        'stem': 'Một xe khởi hành từ trạng thái đứng yên trên đường thẳng với gia tốc không đổi '
                'a = 2 m/s².',
        'parts': [
            ('a)', 'Sau 5 s, vận tốc và quãng đường của xe là bao nhiêu?',
             ['v<sub>0</sub> = 0, a = 2 m/s², t = 5 s.',
              'v = v<sub>0</sub> + at = 0 + 2×5 = **10 m/s**.',
              's = v<sub>0</sub>t + ½at<sup>2</sup> = 0 + ½×2×25 = **25 m**.']),
            ('b)', 'Sau bao lâu kể từ lúc xuất phát thì xe đi được 50 m?',
             ['s = ½at<sup>2</sup> ⇒ 50 = ½×2×t<sup>2</sup> ⇒ t<sup>2</sup> = 50 ⇒ t = √50 ≈ **7,07 s**.',
              'Kiểm tra: v = 2×7,07 ≈ 14,1 m/s ; s = ½(0 + 14,1)×7,07 ≈ 50 m ✔']),
            ('c)', 'Vẽ đồ thị vận tốc – thời gian của chuyển động này và giải thích ý nghĩa hình phẳng '
                   'dưới đồ thị.',
             ['Đồ thị v–t là **đường thẳng qua gốc O** (v = 0 khi t = 0), đi qua điểm (5 s; 10 m/s); '
              'độ dốc = a = 2 m/s².',
              '**Diện tích hình phẳng dưới đồ thị** chính là **quãng đường đi được** trong khoảng '
              'thời gian đó (tam giác vuông: ½×5×10 = 25 m ✔).']),
        ],
    },
    {
        'no': 3,
        'unit': '2.5',
        'level': 'Vận dụng',
        'topic': 'Chuyển động thẳng biến đổi đều – bài toán nâng cao',
        'stem': 'Một ô tô đang chạy với vận tốc 30 km/h trên đường thẳng thì bắt đầu tăng tốc đều, '
                'sau thời gian t đi được quãng đường 100 m thì vận tốc đạt 50 km/h. '
                'Tính gia tốc của ô tô và thời gian tăng tốc.',
        'parts': [
            ('a)', 'Đổi đơn vị hai vận tốc đầu và cuối.',
             ['v<sub>1</sub> = 30 km/h = 30/3,6 ≈ **8,33 m/s**.',
              'v<sub>2</sub> = 50 km/h = 50/3,6 ≈ **13,89 m/s**.']),
            ('b)', 'Tính thời gian tăng tốc.',
             ['Cách 1 (dùng s = ½(v<sub>1</sub> + v<sub>2</sub>)t): '
              'v<sub>tb</sub> = (30 + 50)/2 = 40 km/h = 11,11 m/s ⇒ t = s/v<sub>tb</sub> = 100/11,11 = **9 s**.',
              'Cách 2 (dùng a ở ý c rồi suy ra t) cho cùng kết quả.']),
            ('c)', 'Tính gia tốc của ô tô.',
             ['Cách 1: a = (v<sub>2</sub> − v<sub>1</sub>)/t = (13,89 − 8,33)/9 ≈ **0,62 m/s²**.',
              'Cách 2 (dùng công thức ④): a = (v<sub>2</sub><sup>2</sup> − v<sub>1</sub><sup>2</sup>)/(2s) '
              '= (13,89² − 8,33²)/(2×100) = (192,9 − 69,4)/200 ≈ **0,62 m/s²**.',
              'Vậy a ≈ 0,617 m/s² và t = 9 s (kiểm tra: 8,33 + 0,617×9 ≈ 13,89 m/s ✔).']),
        ],
    },
]

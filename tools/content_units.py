# -*- coding: utf-8 -*-
"""Nội dung đề cương ôn tập: 10 đơn vị kiến thức theo ma trận đặc tả KTGK I.

Mọi yêu cầu trong ``spec`` được trích nguyên văn từ
``MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx`` (bảng "ĐẶC TẢ ĐỀ KIỂM TRA GIỮA HKI").
"""

# --------------------------------------------------------------------------
# 1.1 – 1.3 : Vật lí và thực hành
# --------------------------------------------------------------------------
UNITS = [
    {
        'id': '1.1',
        'title': 'Làm quen với Vật lí',
        'matrix': '1.1. Làm quen với Vật lí',
        'badge': 'TN – Biết: 1 câu · Câu 1',
        'spec': [
            ('Nhận biết', [
                'Nêu được đối tượng nghiên cứu chủ yếu của vật lí.',
                'Biết được các thành tựu nghiên cứu của vật lí tương ứng với các cuộc cách mạng công nghiệp.',
                'Nêu được các quá trình phát triển của vật lí.',
                'Nêu được phương pháp nghiên cứu vật lí.',
            ]),
            ('Thông hiểu', [
                'Hiểu được quá trình nghiên cứu của vật lí.',
            ]),
        ],
        'objectives': [
            'Nêu được **đối tượng nghiên cứu chủ yếu** của vật lí: các hiện tượng vật chất, cấu trúc và '
            'quy luật vận động – tương tác của vật chất trong tự nhiên và đời sống.',
            'Kể tên được các **thành tựu nghiên cứu vật lí** gắn với từng cuộc cách mạng công nghiệp.',
            'Nêu được **quá trình phát triển** của vật lí qua các giai đoạn chủ yếu.',
            'Nêu được **phương pháp nghiên cứu** vật lí và giải thích được vì sao vật lí cần dựa vào thực nghiệm.',
        ],
        'knowledge': [
            ('Đối tượng nghiên cứu của vật lí',
             'Hiện tượng vật lý (cơ, nhiệt, điện, quang, âm…) trong tự nhiên, trong đời sống và trong sản xuất; '
             'cấu trúc, tính chất của vật chất; các quy luật vật lý và ứng dụng của chúng.'),
            ('Quá trình phát triển của vật lí',
             'Cổ điển (Aristotle, Archimedes, Newton) → thế kỷ XIX (điện từ, nhiệt động lực, sóng) → '
             'thế kỷ XX (lượng tử, nguyên tử, hạt nhân, tương đối) → hiện đại (vật lý nano, vật lý lượng tử, '
             'vũ trụ học, vật liệu mới).'),
            ('Phương pháp nghiên cứu vật lí',
             'Quan sát → mô tả → giải thích → dự đoán → **thí nghiệm kiểm chứng** → lý luận → đối chiếu, '
             'hoàn thiện mô hình. Thí nghiệm là phương pháp đặc thù, là cơ sở để kiểm chứng mọi quy luật vật lý.'),
            ('Thành tựu vật lí ứng dụng trong cách mạng công nghiệp',
             'Cách mạng công nghiệp lần 1: máy hơi nước, điện. Lần 2: điện – điện tử, bán dẫn, transistor, '
             'mạch tích hợp (IC), laze. Lần 3: điện tử – tin học, tự động hoá, robot, vật liệu nano. '
             'Lần 4: trí tuệ nhân tạo, vật lý lượng tử, y tế chính xác.'),
        ],
        'memory': [
            '**Ghi nhớ 3 câu hỏi then chốt:** *Vật lí nghiên cứu cái gì? → Hiện tượng vật lý.* '
            '*Nghiên cứu bằng cách nào? → Quan sát – thí nghiệm – lý luận.* '
            '*Vì sao phải thí nghiệm? → Để kiểm chứng tính đúng của quy luật.*',
            '**Mẹo liên hệ:** Thành tựu vật lí ⇔ công nghiệp: *điện tử* (IC, transistor) ⇔ máy tính, điện thoại; '
            '*quang học* (laze, kính hiển vi) ⇔ y tế, truyền thông; *hạt nhân* ⇔ y tế, năng lượng; '
            '*vật liệu nano* ⇔ điện tử hiện đại.',
            '**Câu nói hay dùng trong bài thi:** “Thí nghiệm vật lí là phương pháp nghiên cứu đặc thù của vật lí, '
            'giúp kiểm chứng tính đúng đắn của các quy luật vật lý.”',
        ],
        'example': None,
        'pitfalls': [
            'Đừng nhầm **“đối tượng nghiên cứu”** (hiện tượng vật lý) với **“đối tượng vật lý”** '
            '(vật thể đang nghiên cứu).',
            'Câu hỏi “nhận biết” về vật lí thường hỏi về **định nghĩa**, nên chỉ cần nêu đúng, không cần giải thích dài.',
            'Khi hỏi về **phương pháp nghiên cứu**, phải nêu được chuỗi: quan sát → giải thích → dự đoán → '
            'thí nghiệm kiểm chứng → lý luận.',
        ],
        'links': ['Câu 1 (TN – Biết, mục 1.1)'],
    },

    {
        'id': '1.2',
        'title': 'Các quy tắc an toàn trong phòng thực hành Vật lí',
        'matrix': '1.2. Các quy tắc an toàn trong phòng thực hành Vật lí',
        'badge': 'TN – Biết: 1 câu · Hiểu: 1 câu · Câu 2, 11',
        'spec': [
            ('Nhận biết', [
                'Nêu được các nguy cơ mất an toàn trong sử dụng thiết bị thí nghiệm vật lí.',
                'Nêu được các quy tắc an toàn trong phòng thực hành.',
            ]),
            ('Thông hiểu', [
                'Hiểu và sử dụng được các thiết bị thí nghiệm.',
                'Hiểu và sử dụng các biển báo.',
            ]),
        ],
        'objectives': [
            'Nêu được các **nguy cơ mất an toàn** và **quy tắc an toàn** khi làm thí nghiệm vật lí.',
            'Nhận biết và sử dụng được các **biển báo an toàn** trong phòng thực hành.',
            'Hiểu cách **sử dụng đúng** các thiết bị thí nghiệm cơ bản và xử lý được tình huống sự cố.',
        ],
        'knowledge': [
            ('Các nguy cơ mất an toàn thường gặp',
             '① **Điện giật** (tiếp xúc dây dẫn, vỏ dụng cụ bị rò rỉ). ② **Bỏng** (bình nước nóng, bếp điện, '
             'đốt). ③ **Bỏng hóa học / hóa chất bắn vào mắt**. ④ **Kính vỡ, vật sắc gây cắt**. '
             '⑤ **Vật nặng rơi, chân bị đè**. ⑥ **Cháy nổ** (hơi nước, dung dịch loãng).'),
            ('Quy tắc an toàn cần nhớ',
             '– Không tự ý thực hiện thí nghiệm ngoài hướng dẫn; luôn nghe giáo viên.\n'
             '– **Mặc áo khoác/tạp dề, đeo kính bảo hộ** khi làm thí nghiệm.\n'
             '– Kiểm tra thiết bị trước khi sử dụng; dây dẫn, đầu cắm phải còn nguyên.\n'
             '– Không hút thuốc, không dùng lửa trong phòng thí nghiệm.\n'
             '– Cầm, nâng dụng cụ bằng **hai tay**; dụng cụ nóng dùng **kẹp gắn**.\n'
             '– Khi xảy ra sự cố: **báo ngay giáo viên**, dùng bình chữa cháy, sơ cứu, cắt nguồn điện.'),
            ('Các biển báo an toàn (phải nhận biết – hiểu – sử dụng)',
             '| **Hình dạng / màu** | **Ý nghĩa** |\n'
             '| Hình tam giác vàng, viền đen | Cảnh báo: chú ý nguy hiểm |\n'
             '| Hình tròn đỏ, gạch chéo | Cấm: không được phép |\n'
             '| Hình tròn xanh dương | Bắt buộc: phải tuân thủ |\n'
             '| Hình chữ nhật xanh lá | Chỉ dẫn lối thoát hiểm |\n'
             '| Hình tam giác đen – vàng | Nguy hiểm: chất độc, phóng xạ |'),
            ('Thiết bị thí nghiệm cơ bản và cách dùng đúng',
             'Cân (đặt trên bàn, chỉnh số 0 trước khi cân), thước kẻ (đặt thẳng, thẳng góc với vật), '
             'đồng hồ đo thời gian hiện số (bấm **START** trước, **STOP** sau), bình định mức (đặt ở mắt, '
             'chỉnh nút dưới đáy), ampe kế (mắc **nối tiếp**, chọn đúng thang đo), '
             'kẹp gắn (kẹp chắt, để ống nghiệm không chạm đáy bể nước).'),
        ],
        'memory': [
            '**Mẹo nhớ 4 biển báo** – “**Vàng** cảnh báo, **Đỏ** cấm, **Xanh dương** bắt buộc, **Xanh lá** lối thoát”.',
            '**“Cứng – 3 chữ S”:** **S**ử dụng đúng thiết bị, **S**ử dụng đúng biển báo, '
            '**S**ử dụng đúng quy trình (thí nghiệm, kết luận, báo cáo).',
            '**Ghi nhớ nhanh các nguy cơ:** *Điện – Nóng – Hóa chất – Kính vỡ – Vật nặng – Cháy nổ* '
            '(đọc theo vần: **Đ – N – H – K – V – C**).',
        ],
        'example': {
            'title': 'Tình huống thực hành (rất dễ ra đề thi)',
            'problem': 'Bạn An cầm bình nước nóng rót ra cốc để làm thí nghiệm đo nhiệt độ. '
                       'Bạn An không đeo kính bảo hộ và cầm bình bằng một tay.',
            'solution': [
                '**Nguy cơ:** bỏng tay (nước nóng), bình có thể trượt, vỡ bình gây cắt, nước nóng bắn vào mắt.',
                '**Vi phạm:** không đeo kính bảo hộ (biển báo bắt buộc), cầm bình nóng bằng một tay, '
                'không dùng kẹp gắn.',
                '**Cách làm đúng:** đeo kính bảo hộ + tạp dề, dùng kẹp gắn hoặc đặt khay xuống, '
                'cầm bằng hai tay, rót từ từ sang vật liệu chịu nhiệt, để nguội trước khi rửa.',
            ],
            'answer': 'Có nguy cơ bỏng và bỏng hóa học; phải đeo kính bảo hộ, dùng kẹp gắn, cầm hai tay.',
        },
        'pitfalls': [
            'Phân biệt: **“nguy cơ mất an toàn”** (điều có thể xảy ra) với **“quy tắc an toàn”** '
            '(hành động phải tuân thủ).',
            'Khi hỏi về biển báo, trả lời đúng **hình – màu – ý nghĩa**, không chỉ nói màu.',
            '“Đeo kính bảo hộ” là quy tắc cho **mọi** thí nghiệm, không riêng thí nghiệm hóa chất.',
        ],
        'links': ['Câu 2 (TN – Biết, mục 1.2)', 'Câu 11 (TN – Hiểu, mục 1.2)'],
    },

    {
        'id': '1.3',
        'title': 'Thực hành tính sai số trong phép đo. Ghi kết quả đo',
        'matrix': '1.3 Thực hành tính sai số trong phép đo. Ghi kết quả đo',
        'badge': 'TN – Biết: 1 câu · Câu 3',
        'spec': [
            ('Nhận biết', [
                'Nêu được phép đo trực tiếp và phép đo gián tiếp.',
                'Biết được các loại sai số của phép đo.',
                'Nêu được một số nguyên nhân gây ra sai số khi tiến hành thí nghiệm vật lí.',
                'Biết được công thức giá trị trung bình, sai số tỉ đổi, sai số tuyệt đối.',
            ]),
            ('Thông hiểu', [
                'Cách ghi đúng kết quả phép đo và sai số phép đo.',
                'Tính được sai số tuyệt đối và sai số tỉ đối của phép đo.',
            ]),
            ('Vận dụng', [
                'Tính giá trị đo.',
                'Tính sai số của phép đo.',
            ]),
        ],
        'objectives': [
            'Phân biệt được **phép đo trực tiếp** và **phép đo gián tiếp**.',
            'Nêu được các **nguyên nhân gây sai số** và các **loại sai số** của phép đo.',
            'Tính được **giá trị trung bình**, **sai số tuyệt đối** Δx, **sai số tỉ đối** δ.',
            '**Ghi đúng kết quả đo** theo quy ước: x̄ ± Δx.',
        ],
        'knowledge': [
            ('Phép đo trực tiếp và phép đo gián tiếp',
             '– **Trực tiếp**: đo trực tiếp đại lượng cần tìm bằng dụng cụ có sẵn (đo độ dài bằng thước, '
             'đo khối lượng bằng cân, đo thời gian bằng đồng hồ).\n'
             '– **Gián tiếp**: đo một đại lượng trung gian rồi dùng quan hệ toán học để suy ra đại lượng cần tìm '
             '(đo số vòng quay của bánh xe để tính quãng đường, đo chu kì dao động để tính tần số).'),
            ('Giá trị trung bình của nhiều lần đo',
             'x̄ = (x<sub>1</sub> + x<sub>2</sub> + … + x<sub>n</sub>) / n'),
            ('Sai số tuyệt đối và sai số tỉ đối',
             'Δx = |x̄ − x| (độ lớn sai số tuyệt đối của phép đo x)\n'
             'δ = Δx / |x̄| ; thường biểu diễn bằng **δ (%) = Δx / x̄ × 100%**'),
            ('Quy tắc ghi kết quả đo',
             'Ghi: **x̄ ± Δx**.\n'
             '– Sai số tuyệt đối chỉ nên giữ **một chữ số đầu tiên**; nếu chữ số đầu tiên là **1** thì giữ **hai chữ số**.\n'
             '– Sai số tỉ đối thường ghi **1 hoặc 2 chữ số đầu tiên**.\n'
             '– Giá trị đo và sai số tuyệt đối phải cùng **đơn vị** và cùng **số chữ số thập phân**.'),
            ('Nguyên nhân gây sai số',
             '– **Do dụng cụ**: giới hạn độ chính xác của dụng cụ (sai số dụng cụ).\n'
             '– **Do người đo**: đọc số, ngắm thẳng góc, dùng phép đo, thao tác bấm đồng hồ.\n'
             '– **Do yếu tố ngẫu nhiên**: dao động, từ trường, nhiệt độ, ánh sáng, rung động.\n'
             '– **Do phương pháp**: cách chọn dụng cụ, cách bố trí thí nghiệm.'),
        ],
        'memory': [
            '**Công thức “3 chữ S”:** **S**ai số tuyệt đối **T**uyệt đối → **T**rung bình; '
            'công thức “**TB – TT**”: **T**rung bình trừ **T**rung thực.',
            '**Ghi nhớ độ chính xác của dụng cụ:** dụng cụ có **số nhỏ nhất** (độ chia nhỏ nhất) thì có '
            '**sai số nhỏ nhất**. Ví dụ: thước 1 mm sai số 0,5 mm; cân điện tử độ chính xác 0,01 g.',
            '**Mẹo làm bài:** Với nhiều lần đo, hãy **sắp xếp các giá trị đo** rồi lấy trung bình – '
            'cách này ít sai sót hơn là cộng từng số lớn.',
        ],
        'example': {
            'title': 'Bài toán mẫu (rất giống câu hỏi vận dụng trong đề)',
            'problem': 'Đo 5 lần độ dài một sợi dây được các giá trị (cm): '
                       '12,2 ; 12,4 ; 12,3 ; 12,3 ; 12,4.',
            'solution': [
                '**Giá trị trung bình:** x̄ = (12,2 + 12,4 + 12,3 + 12,3 + 12,4)/5 = 61,6/5 = **12,32 cm**.',
                '**Sai số tuyệt đối của từng lần đo:** Δx₁ = |12,32 − 12,2| = 0,12 cm ; '
                'Δx₂ = |12,32 − 12,4| = 0,08 cm ; Δx₃ = |12,32 − 12,3| = 0,02 cm.',
                '**Sai số tuyệt đối của phép đo** lấy giá trị lớn nhất: Δx = **0,12 cm**.',
                '**Sai số tỉ đối:** δ = 0,12/12,32 × 100% ≈ **0,97%**.',
                '**Ghi kết quả:** x̄ ± Δx = 12,32 ± 0,12 cm → làm tròn (Δx giữ một chữ số): '
                '**12,3 ± 0,1 cm**.',
            ],
            'answer': 'x̄ = 12,32 cm ; Δx = 0,12 cm ; δ ≈ 0,97% ; ghi kết quả: 12,3 ± 0,1 cm.',
        },
        'pitfalls': [
            '**Sai số tuyệt đối luôn ≥ 0**, nên phải lấy **giá trị tuyệt đối** |x̄ − x|, không được lấy x − x̄.',
            'Khi tính δ, mẫu số là **giá trị trung bình** |x̄|, không phải giá trị đo từng lần.',
            '**Sai số tỉ đối không có đơn vị**; chỉ khi quy ra **%** mới ghi được %.',
            'Khi ghi kết quả, **giá trị đo phải làm tròn** sao cho số chữ số thập phân của nó **bằng** số chữ số '
            'thập phân của sai số tuyệt đối.',
        ],
        'links': ['Câu 3 (TN – Biết, mục 1.3)'],
    },

    # ----------------------------------------------------------------------
    # 2.1 – 2.6 : Cơ học
    # ----------------------------------------------------------------------
    {
        'id': '2.1',
        'title': 'Độ dịch chuyển và quãng đường đi được',
        'matrix': '2.1. Độ dịch chuyển và quãng đường đi được',
        'badge': 'TN – Biết: 1 câu · Hiểu: 2 câu · Câu 4, 12, 13',
        'spec': [
            ('Nhận biết', [
                'Nêu được độ dịch chuyển là gì?',
                'So sánh được độ dịch chuyển và quãng đường đi được.',
            ]),
            ('Thông hiểu', [
                'Xác định được độ dịch chuyển và quãng đường đi được.',
            ]),
            ('Vận dụng', [
                'Tính độ dịch chuyển.',
            ]),
            ('Vận dụng cao', [
                'Tính được độ dịch chuyển và quãng đường trong các bài toán.',
            ]),
        ],
        'objectives': [
            'Nêu được **định nghĩa** độ dịch chuyển (có vectơ, có độ lớn và hướng).',
            'So sánh được **độ dịch chuyển** và **quãng đường đi được**; biết điều kiện chúng bằng nhau.',
            'Xác định, tính được độ dịch chuyển và quãng đường đi được trong các tình huống thực tế.',
            'Phân biệt được **chuyển động thẳng** và **chuyển động cong** dựa vào vectơ độ dịch chuyển.',
        ],
        'knowledge': [
            ('Độ dịch chuyển Δr',
             'Độ dịch chuyển là **vectơ** nối vị trí đầu A với vị trí cuối B của chuyển động.\n'
             '– Có **độ lớn** (=|Δr|, đơn vị m) và có **hướng** (từ A sang B).\n'
             '– Chỉ phụ thuộc vị trí đầu và vị trí cuối, **không** phụ thuộc đường đi.'),
            ('Quãng đường đi được s',
             'Quãng đường đi được là **tổng độ dài** của đường đi trong không gian (đơn vị m).\n'
             '– Là **đại lượng vô hướng**, luôn **≥ 0**.\n'
             '– Phụ thuộc **đường đi** (đi vòng hay đi thẳng).'),
            ('So sánh',
             '**|Δr| ≤ s**, và **|Δr| = s** khi vật chuyển động **thẳng** (đi thẳng, không đổi chiều).\n'
             'Nếu vật đi vòng quay lại điểm xuất phát: s > 0 nhưng Δr = 0.'),
            ('Nhận biết dạng chuyển động',
             '– **Vận độ dịch chuyển không đổi** → chuyển động **thẳng**.\n'
             '– Vận độ dịch chuyển không đổi **và** |v| không đổi → chuyển động **thẳng đều**.\n'
             '– |v| không đổi nhưng **hướng vận tốc** thay đổi → chuyển động **cong đều** (tròn đều).'),
        ],
        'memory': [
            '**Mẹo nhớ 1 câu:** “**Độ dịch chuyển có hướng – Quãng đường không có hướng**” '
            '(độ dịch chuyển là vectơ; quãng đường là số đo vô hướng).',
            '**“Hình vẽ luôn thắng”:** vẽ đường đi, đánh dấu A → B, đo **đường thẳng** A–B là độ lớn '
            'độ dịch chuyển; đo **đường cong** đi thật là quãng đường.',
            '**Bài toán hay gặp:** “đi 3 km rồi quay lại 1 km” → s = 4 km, |Δr| = 2 km '
            '(và nếu hỏi *độ dịch chuyển có hướng*, phải chỉ ra hướng về điểm xuất phát).',
        ],
        'example': {
            'title': 'Bài toán mẫu',
            'problem': 'Một vật chuyển động trên quỹ đạo hình vuông cạnh 40 cm (hai lần quay góc '
                       '90° cùng chiều): đi thẳng 60 cm, rồi đi thẳng 30 cm, rồi đi ngược lại 40 cm.',
            'solution': [
                '**Quãng đường đi được:** s = 60 + 30 + 40 = **130 cm**.',
                '**Độ dịch chuyển:** Δr = vectơ nối vị trí đầu A với vị trí cuối B. Chọn A làm gốc, '
                'trục Ox theo đoạn đi đầu: B có toạ độ (20 cm; −30 cm).',
                '|Δr| = √(20² + 30²) = √1300 ≈ **36,1 cm**.',
                '**Kiểm tra:** |Δr| = 36,1 cm < s = 130 cm ✔ (vì có quay ngược chiều).',
            ],
            'answer': 's = 130 cm ; |Δr| = √1300 ≈ 36,1 cm.',
        },
        'pitfalls': [
            '**Sai số phổ biến nhất:** lấy **quãng đường** làm **độ dịch chuyển** khi vật đi vòng.',
            'Độ dịch chuyển **có thể bằng 0** (vật về đúng điểm xuất phát) trong khi quãng đường đi được khác 0.',
            'Khi so sánh phải so sánh **|Δr|** (độ lớn) với s, chứ không so sánh vectơ với số.',
        ],
        'links': ['Câu 4 (TN – Biết)', 'Câu 12, 13 (TN – Hiểu)', 'Phần II – Câu 1 (ý d)'],
    },

    {
        'id': '2.2',
        'title': 'Tốc độ và vận tốc',
        'matrix': '2.2 Tốc độ và vận tốc (kèm Thực hành: Đo tốc độ của vật chuyển động)',
        'badge': 'TN – Biết: 1 câu · TL: 2 ý (câu 1) · P3: 1 câu · P4: 1 câu · Câu 5',
        'spec': [
            ('Nhận biết', [
                'Biết được ý nghĩa và công thức của tốc độ trung bình.',
                'Biết tốc độ tức thời.',
                'Biết cách đo tốc độ trong cuộc sống và trong phòng thí nghiệm.',
                'Nêu được định nghĩa vận tốc và viết được công thức tính vận tốc.',
                'Biết được công thức cộng vận tốc.',
            ]),
            ('Thông hiểu', [
                'Tính được tốc độ trung bình.',
                'Phân biệt được tốc độ và vận tốc.',
                'Xác định được vectơ vận tốc.',
            ]),
            ('Vận dụng', [
                'Giải được các bài toán về tổng hợp hai vận tốc cùng phương và hai vận tốc vuông góc với nhau.',
            ]),
            ('Thực hành: Đo tốc độ của vật chuyển động', [
                'Nêu được ưu điểm và nhược điểm khi sử dụng đồng hồ đo thời gian hiện số và cổng quang điện.',
                'Cách sử dụng đồng hồ đo thời gian hiện số.',
                'Ý nghĩa của việc sử dụng hai cổng quang điện.',
                'Đo được tốc độ bằng dụng cụ thực hành.',
            ]),
        ],
        'objectives': [
            'Phân biệt được **tốc độ** (vô hướng) và **vận tốc** (có hướng); xác định được vectơ vận tốc.',
            'Tính được **tốc độ trung bình**, **tốc độ tức thời** và quy đổi đơn vị km/h ↔ m/s.',
            'Vận dụng được **công thức cộng vận tốc**: cùng phương cùng chiều, cùng phương ngược chiều, vuông góc.',
            'Hiểu và thực hiện được phép **đo tốc độ bằng đồng hồ hiện số** và **hai cổng quang điện**.',
        ],
        'knowledge': [
            ('Tốc độ trung bình',
             'v = s / t ; đơn vị **m/s** (hoặc km/h).\n'
             'Đây là **đại lượng vô hướng**, phụ thuộc vào cả quãng đường và thời gian, không phụ thuộc đường đi.'),
            ('Tốc độ tức thời',
             'v = Δs / Δt khi Δt **rất nhỏ**; là giới hạn của tốc độ trung bình trong khoảng thời gian rất ngắn. '
             'Vẫn là **đại lượng vô hướng**.'),
            ('Vận tốc',
             '**v** = **Δr**/Δt (cả hai vế đều là vectơ) (hướng của **Δr**) và **độ lớn** bằng tốc độ tức thời. '
             'Trong THPT gọi tắt “vận tốc” là độ lớn kèm hướng.'),
            ('Quy đổi đơn vị',
             '1 m/s = 3,6 km/h ⇔ v(km/h) = 3,6 × v(m/s)'),
            ('Công thức cộng vận tốc',
             '– Hai vận tốc **cùng phương, cùng chiều**: v = v<sub>1</sub> + v<sub>2</sub>\n'
             '– Hai vận tốc **cùng phương, ngược chiều**: v = |v<sub>1</sub> − v<sub>2</sub>|\n'
             '– Hai vận tốc **vuông góc**: v = √(v<sub>1</sub><sup>2</sup> + v<sub>2</sub><sup>2</sup>)'),
            ('Thực hành đo tốc độ',
             '**Đồng hồ đo thời gian hiện số**\n'
             '– *Ưu điểm*: độ chính xác cao (tới 0,01 s), đọc nhanh, ghi kết quả bằng số.\n'
             '– *Nhược điểm*: phải bấm BẮT ĐẦU / DỪNG bằng tay, dễ lệch thời điểm, gây ảnh hưởng tới chuyển động.\n'
             '– *Cách dùng*: bấm **START** đúng lúc vật bắt đầu chuyển động, bấm **STOP** khi vật tới đích, '
             'đọc giá trị Δt, rồi tính v = s/Δt.\n\n'
             '**Hai cổng quang điện (photogate)**\n'
             '– *Ưu điểm*: đo tự động, chính xác, **không ảnh hưởng** tới chuyển động của vật.\n'
             '– *Nhược điểm*: phải đặt cổng đúng vị trí, chỉ đo được vật đi xuyên qua cổng, tốn thiết bị.\n'
             '– *Ý nghĩa của hai cổng*: đồng hồ ghi thời gian vật **chặn cổng 1** (t<sub>1</sub>) và '
             '**chặn cổng 2** (t<sub>2</sub>). Thời gian vật đi giữa hai cổng là Δt = t<sub>2</sub> − t<sub>1</sub>, '
             'nên **tốc độ trung bình giữa hai cổng**: v = L / (t<sub>2</sub> − t<sub>1</sub>) với L là khoảng cách '
             'giữa hai cổng. Đây chính là **tốc độ tức thời** của vật tại vị trí giữa hai cổng.'),
        ],
        'memory': [
            '**Phân biệt trong 1 giây:** “**T**ốc độ → **T**hao **t**ính quãng đường (**t**rung bình), '
            '**không** có hướng. **V**ận tốc → có **V**ector, **V**ị trí đầu–cuối quyết định hướng.”',
            '**Công thức cộng vận tốc – mẹo nhớ hình:** *cùng chiều → **cộng**; ngược chiều → **trừ**; '
            'vuông góc → **căn bình phương*** (tam giác vuông cạnh v1, v2, cạnh huyền v).',
            '**Quy đổi nhanh:** chia cho 3,6 (km/h → m/s); nhân 3,6 (m/s → km/h). Ví dụ 36 km/h = 10 m/s.',
            '**“Hai cổng” = đo tốc độ tức thời ở giữa:** Δt = t<sub>2</sub> − t<sub>1</sub>, v = L/Δt.',
        ],
        'example': {
            'title': 'Bài toán mẫu – tổng hợp vận tốc',
            'problem': 'Một xe khách đang đi với vận tốc 54 km/h. Một xe máy chạy cùng chiều với vận tốc 36 km/h. '
                       'a) Vận tốc của xe khách đối với xe máy? b) Nếu xe máy chạy ngược chiều, '
                       'vận tốc của xe khách đối với xe máy là bao nhiêu?',
            'solution': [
                'Đổi đơn vị (nếu cần): 54 km/h = 15 m/s ; 36 km/h = 10 m/s.',
                '**a)** Cùng phương, cùng chiều: v = 54 + 36 = **90 km/h** (hay 15 + 10 = 25 m/s).',
                '**b)** Cùng phương, ngược chiều: v = |54 − 36| = **18 km/h** (hay 15 − 10 = 5 m/s).',
            ],
            'answer': 'a) 90 km/h ; b) 18 km/h.',
        },
        'pitfalls': [
            '**Quên quy đổi đơn vị** khi cộng vận tốc (km/h với m/s) – đây là lỗi mất điểm số 1.',
            'Với hai vận tốc **vuông góc**, dùng công thức **căn bình phương**, không dùng cộng.',
            'Ở cấp THPT, khi nói “vận tốc” phải kèm **hướng**; chỉ nói “tốc độ” thì không cần hướng.',
            'Khi đo bằng hai cổng quang điện, thời gian đo là **t<sub>2</sub> − t<sub>1</sub>**, '
            '**không phải** t<sub>1</sub> hay t<sub>2</sub> riêng lẻ.',
        ],
        'links': ['Câu 5 (TN – Biết)',
                  'Phần II – Câu 1 (ý a, ý b)', 'Phần III – Câu 1', 'Phần IV – Câu 1'],
    },

    {
        'id': '2.3',
        'title': 'Đồ thị độ dịch chuyển – thời gian',
        'matrix': '2.3 Đồ thị độ dịch chuyển – thời gian',
        'badge': 'TN – Biết: 1 câu · Hiểu: 1 câu · TL: 2 ý (câu 1) · Câu 6, 14',
        'spec': [
            ('Nhận biết', [
                'Mô tả được chuyển động của vật dựa vào đồ thị dịch chuyển – thời gian.',
            ]),
            ('Thông hiểu', [
                'Tính được tốc độ từ độ dốc của đồ thị độ dịch chuyển – thời gian.',
                'Xác định được vị trí và vận tốc của vật ở bất kì thời điểm nào dựa vào đồ thị.',
            ]),
            ('Vận dụng', [
                'Vẽ được đồ thị độ dịch chuyển – thời gian trong chuyển động thẳng.',
                'Xác định được quãng đường đi được và độ dịch chuyển của vật.',
            ]),
        ],
        'objectives': [
            'Đọc được đồ thị: xác định **vị trí**, **quãng đường đi được**, **độ dịch chuyển** và **vận tốc** tại một thời điểm.',
            'Tính được tốc độ bằng **độ dốc** của đồ thị.',
            'Vẽ và giải thích được đồ thị s–t và x–t của chuyển động thẳng.',
        ],
        'knowledge': [
            ('Cách vẽ và đọc đồ thị',
             '– Trục hoành **Ox: thời gian t (s)**; trục tung **Oy: độ dịch chuyển x (m)** hoặc **quãng đường s (m)**.\n'
             '– **Độ dốc** của đồ thị = tốc độ: v = Δx/Δt (hay Δs/Δt).\n'
             '– Đường thẳng → **chuyển động thẳng đều**; đường cong (parabol) → **chuyển động thẳng biến đổi đều**.'),
            ('Các trường hợp đặc biệt trên đồ thị x–t',
             '– Đồ thị **đi lên** ⇒ x tăng ⇒ vật đi theo **chiều dương** ⇒ vận tốc **dương**.\n'
             '– Đồ thị **đi xuống** ⇒ x giảm ⇒ vật đi theo **chiều âm** ⇒ vận tốc **âm**.\n'
             '– Đồ thị **ngang** (khoảng thời gian) ⇒ x không đổi ⇒ vật **đứng yên** (v = 0).\n'
             '– Đồ thị **xiên dốc** ⇒ vận tốc không đổi (đều); độ dốc càng lớn ⇒ vận tốc càng lớn.'),
            ('Quãng đường đi được và độ dịch chuyển trên đồ thị',
             '– **Quãng đường đi được** = tổng các độ dài “đi được” trên trục x = Σ|Δx| (đi lên và đi xuống đều cộng).\n'
             '– **Độ dịch chuyển** = x<sub>cuối</sub> − x<sub>đầu</sub> (lấy hiệu, có thể âm).'),
            ('Mối liên hệ giữa các đồ thị',
             '– Đồ thị **v–t**: diện tích dưới đồ thị = **quãng đường đi được**.\n'
             '– Đồ thị **a–t**: diện tích dưới đồ thị = **độ biến thiên vận tốc**.\n'
             '– Đồ thị **s–t** của CĐTBĐĐ là **parabol** (a > 0 → nhánh lên; a < 0 → nhánh xuống).'),
        ],
        'memory': [
            '**“Độ dốc là tốc độ”** – luôn nhớ: **v = độ dốc** của đồ thị x–t (hay s–t).',
            '**Mẹo đọc nhanh:** đồ thị đi **lên** → vận tốc **dương**; đi **xuống** → vận tốc **âm**; '
            '**ngang** → đứng yên. (Lên – Dương, Xuống – Âm, Ngang – Yên.)',
            '**“Đi lên đi xuống đều là đường đi”** – dùng cho **quãng đường**; còn **độ dịch chuyển** '
            'chỉ lấy **hiệu** giữa hai điểm đầu – cuối.',
            '**Nhớ:** đồ thị s–t chỉ cho biết **độ dốc tuyệt đối** (tốc độ); muốn biết **vận tốc có dấu** '
            'thì phải nhìn **đồ thị x–t**.',
        ],
        'example': {
            'title': 'Bài toán mẫu – đọc đồ thị',
            'problem': 'Một vật chuyển động theo đồ thị độ dịch chuyển – thời gian có tọa độ các điểm: '
                       'A(0 s; 0 m), B(2 s; 10 m), C(4 s; 4 m), D(6 s; 4 m).',
            'solution': [
                '**Quãng đường đi được:** A → B: 10 m ; B → C: |4 − 10| = 6 m ; C → D: 0 m ⇒ s = **16 m**.',
                '**Độ dịch chuyển:** Δx = x<sub>D</sub> − x<sub>A</sub> = 4 − 0 = **4 m** (dương, theo chiều dương).',
                '**Vận tốc trên đoạn A → B:** v = (10 − 0)/(2 − 0) = **5 m/s**.',
                '**Vận tốc trên đoạn B → C:** v = (4 − 10)/(4 − 2) = **−3 m/s** (vật đi ngược chiều dương).',
                '**Trên đoạn C → D:** v = 0 ⇒ vật đứng yên trong 2 s.',
            ],
            'answer': 's = 16 m ; Δx = 4 m ; v<sub>AB</sub> = 5 m/s ; v<sub>BC</sub> = −3 m/s ; v<sub>CD</sub> = 0.',
        },
        'pitfalls': [
            '**Nhầm tốc độ với vận tốc:** độ dốc của đồ thị **s–t** cho **tốc độ** (luôn dương), '
            'còn **vận tốc** (có dấu) phải đọc từ đồ thị **x–t**.',
            '**Tính quãng đường bằng hiệu** là sai khi vật đổi chiều (phải cộng các độ dài).',
            '**Quên đơn vị** khi tính độ dốc: kết quả phải là **m/s** (hoặc km/h).',
        ],
        'links': ['Câu 6 (TN – Biết)', 'Câu 14 (TN – Hiểu)', 'Phần II – Câu 1 (ý c, ý d)'],
    },

    {
        'id': '2.4',
        'title': 'Chuyển động biến đổi. Gia tốc',
        'matrix': '2.4 Chuyển động biến đổi. Gia tốc',
        'badge': 'TN – Biết: 1 câu · Hiểu: 1 câu · Câu 7, 15',
        'spec': [
            ('Nhận biết', [
                'Biết được thế nào là chuyển động biến đổi.',
                'Biết được quan hệ về phương và chiều của gia tốc với vận tốc.',
                'Biết được khái niệm gia tốc, công thức tính gia tốc và đơn vị của gia tốc.',
            ]),
            ('Thông hiểu', [
                'Tính được độ biến thiên vận tốc, gia tốc của chuyển động.',
                'Phân biệt được chuyển động nhanh dần và chậm dần dựa vào vận tốc và gia tốc.',
            ]),
        ],
        'objectives': [
            'Nêu được **khái niệm gia tốc**, công thức và đơn vị (**m/s²**).',
            'Tính được **độ biến thiên vận tốc** và **gia tốc** của chuyển động.',
            'Phân biệt được **nhanh dần – chậm dần – đều** dựa vào quan hệ phương, chiều của gia tốc và vận tốc.',
        ],
        'knowledge': [
            ('Chuyển động biến đổi',
             'Là chuyển động mà **vận tốc thay đổi** theo thời gian (có thể độ lớn thay đổi, hướng thay đổi, '
             'hoặc cả hai).'),
            ('Gia tốc',
             '**a** = **Δv**/Δt (cả hai vế đều là vectơ), đặc trưng cho **tốc độ thay đổi**.\n'
             'Đơn vị: **m/s²**. Gia tốc bằng 1 m/s² nghĩa là mỗi giây vận tốc thay đổi 1 m/s.'),
            ('Quan hệ giữa gia tốc và vận tốc',
             '| **Quan hệ** | **Phương, chiều** | **Kết luận** |\n'
             '| a và v cùng hướng | a·v > 0 | Vận tốc tăng dần ⇒ **chuyển động nhanh dần** |\n'
             '| a và v ngược hướng | a·v < 0 | Vận tốc giảm dần ⇒ **chuyển động chậm dần** |\n'
             '| a vuông góc v | a·v = 0 | Độ lớn v không đổi, chỉ đổi hướng ⇒ **chuyển động cong đều** |'),
            ('Cơ sở phân biệt bằng dấu',
             '– Chuyển động theo **chiều dương** (v > 0): a > 0 → **nhanh dần**; a < 0 → **chậm dần**.\n'
             '– Chuyển động theo **chiều âm** (v < 0): a < 0 → **nhanh dần**; a > 0 → **chậm dần**.\n'
             '⇒ Quy tắc chung: **nhanh dần ⇔ a và v cùng dấu**.'),
        ],
        'memory': [
            '**“Cùng dấu thì nhanh, ngược dấu thì chậm”** – dùng đúng khi vật chuyển động trên trục có dấu.',
            '**Mẹo vẽ:** vẽ vectơ **v** trước, vẽ vectơ **a** sau; nếu **a cùng hướng v** ⇒ tăng tốc '
            '(nhanh dần), **a ngược hướng v** ⇒ giảm tốc (chậm dần).',
            '**Đơn vị gia tốc:** **m/s²** (đọc: mét trên giây bình phương) – đừng nhầm với **m/s**.',
            '**“Cong đều”** là trường hợp riêng: tốc độ **không đổi**, chỉ **đổi hướng** (a vuông góc v).',
        ],
        'example': {
            'title': 'Bài toán mẫu',
            'problem': 'Một xe đang chạy theo chiều dương với vận tốc 12 m/s. Sau 4 s, vận tốc của xe là 20 m/s.',
            'solution': [
                '**Độ biến thiên vận tốc:** Δv = 20 − 12 = **8 m/s**.',
                '**Gia tốc:** a = Δv/Δt = 8/4 = **2 m/s²**.',
                '**Nhận xét:** a = 2 m/s² > 0 và v = 12 m/s > 0 ⇒ a cùng hướng v ⇒ xe **chuyển động nhanh dần**.',
            ],
            'answer': 'Δv = 8 m/s ; a = 2 m/s² ; chuyển động nhanh dần.',
        },
        'pitfalls': [
            '**Sai lớn nhất:** nói “gia tốc dương ⇒ nhanh dần” là **không đúng nếu vật chuyển động ngược chiều âm**.',
            '**Gia tốc luôn có thể âm** – âm không phải là “sai”, mà là dấu của vectơ theo hệ trục đã chọn.',
            'Đừng nhầm **độ biến thiên vận tốc** (Δv, đơn vị m/s) với **gia tốc** (a, đơn vị m/s²).',
        ],
        'links': ['Câu 7 (TN – Biết)', 'Câu 15 (TN – Hiểu)'],
    },

    {
        'id': '2.5',
        'title': 'Chuyển động thẳng biến đổi đều',
        'matrix': '2.5 Chuyển động thẳng biến đổi đều',
        'badge': 'TN – Biết: 2 câu · Hiểu: 1 câu · TL: 4 ý (câu 2) · P4: 2 câu · Câu 8, 9, 16',
        'spec': [
            ('Nhận biết', [
                'Biết được định nghĩa của chuyển động thẳng biến đổi đều.',
                'Biết được định nghĩa chuyển động nhanh dần đều và chuyển động chậm dần đều.',
                'Biết được các công thức của chuyển động thẳng biến đổi đều.',
            ]),
            ('Thông hiểu', [
                'Sử dụng được các công thức để tính được vận tốc, gia tốc, độ dịch chuyển của vật.',
            ]),
            ('Vận dụng', [
                'Vận dụng giải các bài toán cơ bản về chuyển động thẳng biến đổi đều.',
            ]),
            ('Vận dụng cao', [
                'Vận dụng giải các bài toán nâng cao về chuyển động thẳng biến đổi đều.',
            ]),
        ],
        'objectives': [
            'Nêu được định nghĩa **CĐTBĐĐ**, **chuyển động nhanh dần đều**, **chuyển động chậm dần đều**.',
            'Thuộc và vận dụng **4 công thức** của CĐTBĐĐ để tính v, a, s, t.',
            'Nhận biết được dấu của các đại lượng và **điều kiện vật dừng lại** (v = 0).',
            'Đọc và vẽ được các đồ thị **v–t**, **s–t**, **a–t** của CĐTBĐĐ.',
        ],
        'knowledge': [
            ('Định nghĩa',
             '**Chuyển động thẳng biến đổi đều (CĐTBĐĐ)** là chuyển động thẳng mà **gia tốc không đổi** theo thời gian.\n'
             '– **Nhanh dần đều**: a và v<sub>0</sub> cùng dấu (|v| tăng đều).\n'
             '– **Chậm dần đều**: a và v<sub>0</sub> ngược dấu (|v| giảm đều).'),
            ('Bốn công thức cần nhớ',
             '① **v = v<sub>0</sub> + at**  (liên hệ vận tốc – thời gian)\n'
             '② **s = v<sub>0</sub>t + ½at<sup>2</sup>**  (quan hệ quãng đường – thời gian)\n'
             '③ **s = ½(v<sub>0</sub> + v)t**  (quan hệ quãng đường – vận tốc trung bình)\n'
             '④ **v² − v<sub>0</sub><sup>2</sup> = 2as**  (quan hệ vận tốc – quãng đường)\n'
             '⇒ Ngoài ra: **v<sub>tb</sub> = (v<sub>0</sub> + v)/2** và **s = v<sub>tb</sub>t**.'),
            ('Điều kiện vật dừng lại',
             'Từ ①: v = 0 ⇔ t = −v<sub>0</sub>/a (cần t > 0). Khi đó quãng đường đến lúc dừng: '
             's = −v<sub>0</sub><sup>2</sup>/(2a) = v<sub>0</sub><sup>2</sup>/(2|a|).'),
            ('Đồ thị của CĐTBĐĐ',
             '– **v–t**: đường thẳng; **độ dốc = a**; **diện tích dưới đường thẳng = s**; '
             'giao trục hoành tại thời điểm v = 0.\n'
             '– **s–t**: **parbol**; a > 0 → nhánh **lên**, a < 0 → nhánh **xuống**.\n'
             '– **a–t**: đường thẳng **song song** với trục hoành (a hằng số).'),
        ],
        'memory': [
            '**Công thức “3 – 1 – 2”:** v = v<sub>0</sub> + at ; s = v<sub>0</sub>t + ½at<sup>2</sup> ; '
            'v² − v<sub>0</sub><sup>2</sup> = 2as ; và s = ½(v<sub>0</sub> + v)t.',
            '**Chọn công thức theo dữ kiện cho có** (bảng “cứu vãn”):\n'
            '– Biết **a, v₀, t** → cần **v** ⇒ dùng ①; cần **s** ⇒ dùng ②.\n'
            '– Biết **a, v₀, v** → cần **s** ⇒ dùng ④.\n'
            '– Biết **v₀, v, t** → cần **s** ⇒ dùng ③ (dễ nhất!).\n'
            '– Biết **a, v, t** → cần **s** ⇒ dùng ③ sau khi tìm v₀ từ ①.',
            '**“Đồ thị v–t là bậc nhất, s–t là bậc hai, a–t là đường ngang.”**',
            '**Chốt dừng:** khi xe **phanh**, a luôn **ngược chiều v** ⇒ a < 0 nếu xe chạy theo chiều dương. '
            'Dùng v = 0 để tìm thời điểm dừng.',
        ],
        'example': {
            'title': 'Bài toán mẫu (dạng nâng cao – dùng nhiều công thức)',
            'problem': 'Một xe khởi hành từ trạng thái đứng yên với gia tốc không đổi 2 m/s². '
                       'a) Sau 5 s, vận tốc và quãng đường của xe là bao nhiêu? '
                       'b) Sau bao lâu xe đi được 50 m?',
            'solution': [
                '**a)** v<sub>0</sub> = 0, a = 2 m/s², t = 5 s.\n'
                'v = v<sub>0</sub> + at = 0 + 2×5 = **10 m/s**.\n'
                's = v<sub>0</sub>t + ½at<sup>2</sup> = 0 + ½×2×25 = **25 m**.',
                '**b)** s = ½at<sup>2</sup> ⇒ 50 = ½×2×t<sup>2</sup> ⇒ t<sup>2</sup> = 50 ⇒ t = √50 ≈ **7,07 s** '
                '(chọn nghiệm dương).',
                '**Kiểm tra bằng công thức ③:** v = 2×7,07 ≈ 14,14 m/s ; s = ½(0 + 14,14)×7,07 ≈ 50 m ✔.',
            ],
            'answer': 'a) v = 10 m/s ; s = 25 m. b) t ≈ 7,07 s.',
        },
        'pitfalls': [
            '**Quên điều kiện “gia tốc không đổi”** khi dùng các công thức trên.',
            '**Vận tốc âm** vẫn là vận tốc hợp lệ; khi xe vượt quá mốc đã định (v = 0) thì vận tốc đổi dấu, '
            'lúc đó xe **chuyển động ngược chiều** đã chọn.',
            '**Sai phổ biến:** lấy s = v<sub>0</sub>t (thiếu ½at<sup>2</sup>) hoặc lấy s = vt khi v là vận tốc cuối.',
            'Khi v = 0, **không được** dùng công thức ③ với v<sub>0</sub> và v khác nhau mà quên kỹ năng “thời gian”.',
        ],
        'links': ['Câu 8, 9 (TN – Biết)', 'Câu 16 (TN – Hiểu)',
                  'Phần II – Câu 2 (4 ý)', 'Phần IV – Câu 2, 3'],
    },

    {
        'id': '2.6',
        'title': 'Sự rơi tự do',
        'matrix': '2.6 Sự rơi tự do',
        'badge': 'TN – Biết: 1 câu · Hiểu: 2 câu · P3: 1 câu · Câu 10, 17, 18',
        'spec': [
            ('Nhận biết', [
                'Biết được định nghĩa rơi tự do.',
                'Biết được đặc điểm của chuyển động rơi trong không khí.',
                'Biết được các công thức của rơi tự do.',
            ]),
            ('Thông hiểu', [
                'Phân biệt được vật rơi gần đúng tự do và không phải rơi tự do.',
                'Áp dụng các công thức rơi tự do tính toán các bài đơn giản.',
            ]),
            ('Vận dụng', [
                'Vận dụng giải quyết các bài toán về rơi tự do.',
            ]),
        ],
        'objectives': [
            'Nêu được **định nghĩa rơi tự do** và các **đặc điểm** của chuyển động rơi trong không khí.',
            'Phân biệt được vật **rơi tự do**, **gần đúng tự do** và **không phải rơi tự do**.',
            'Áp dụng được các **công thức rơi tự do** để giải các bài toán đơn giản.',
        ],
        'knowledge': [
            ('Định nghĩa',
             '**Rơi tự do** là chuyển động rơi trong không khí của vật khi **không chịu lực cản của không khí** '
             '(chỉ chịu trọng lực).'),
            ('Đặc điểm của chuyển động rơi tự do',
             '– **Gia tốc a = g**, không đổi, vectơ gia tốc hướng **thẳng xuống**.\n'
             '– Gia tốc **không phụ thuộc** vào khối lượng, vào hình dạng, vào khối lượng riêng của vật.\n'
             '– Nếu thả vật (v<sub>0</sub> = 0) ⇒ vật rơi **nhanh dần đều** theo phương thẳng đứng.\n'
             '– Chọn gốc tọa độ tại điểm thả, trục hướng xuống dương thì: v = gt , s = ½gt<sup>2</sup>.'),
            ('Phân biệt các loại rơi',
             '– **Rơi tự do hoàn toàn**: trong ống chân không (chân không) – không có không khí.\n'
             '– **Rơi gần đúng tự do**: trong không khí nhưng lực cản rất nhỏ so với trọng lực '
             '(vật nhỏ, nhẹ, tỷ lệ mặt cắn ngang nhỏ).\n'
             '– **Không phải rơi tự do**: khi lực cản không khí đáng kể (mảnh giấy, vật có cánh, vật rơi trong '
             'chất lỏng) ⇒ a < g, vật rơi chậm hơn, không rơi thẳng đứng.'),
            ('Công thức rơi tự do (v₀ = 0)',
             'v = gt ; s = h = ½gt<sup>2</sup> ; v² = 2gs\n'
             'Suy ra: t = √(2h/g) và v = √(2gh).\n'
             '**g = 9,8 m/s²** (một số bài dùng **g = 10 m/s²** – phải đọc kỹ đề).'),
            ('Công thức tổng quát khi v₀ ≠ 0 (ném lên / ném xuống)',
             'v = v<sub>0</sub> + gt ; s = v<sub>0</sub>t + ½gt<sup>2</sup> (vẫn dùng đúng công thức '
             'CĐTBĐĐ với a = g).'),
        ],
        'memory': [
            '**“Rơi tự do = CĐTBĐĐ có a = g”** – mọi công thức CĐTBĐĐ đều dùng được với a = g.',
            '**“g không đổi – g không phụ thuộc khối lượng”** – vật nặng rơi nhanh hơn vật nhẹ **chỉ vì** '
            'lực cản không khí tương đối nhỏ hơn, không phải vì g khác nhau.',
            '**Trong chân không:** mọi vật rơi **như nhau** (cùng gia tốc, cùng thời gian rơi).',
            '**Công thức hay dùng:** t = √(2h/g) ; v = √(2gh). Chú ý **ghi nhớ h = ½gt<sup>2</sup>** '
            '(quãng đường đi được bằng độ dịch chuyển khi rơi thẳng đứng).',
            '**Ghi nhớ dấu:** chọn trục hướng xuống là dương thì v = gt **luôn dương**; '
            'khi **ném lên** thì v<sub>0</sub> < 0 so với trục này.',
        ],
        'example': {
            'title': 'Bài toán mẫu',
            'problem': 'Một vật được thả rơi tự do từ độ cao h = 20 m (g = 10 m/s²). '
                       'a) Thời gian rơi đến khi chạm đất? b) Tốc độ ngay trước khi chạm đất?',
            'solution': [
                '**a)** h = ½gt<sup>2</sup> ⇒ 20 = ½×10×t<sup>2</sup> ⇒ t<sup>2</sup> = 4 ⇒ **t = 2 s**.',
                '**b)** v = gt = 10 × 2 = **20 m/s** (kiểm tra: v = √(2gh) = √(2×10×20) = 20 m/s ✔).',
                '**Lưu ý:** nếu thả trong không khí (có lực cản) thì a < g nên thời gian rơi **lớn hơn** 2 s '
                'và tốc độ chạm đất **nhỏ hơn** 20 m/s.',
            ],
            'answer': 't = 2 s ; v = 20 m/s.',
        },
        'pitfalls': [
            '**Quên rằng trong không khí có lực cản** → vật không rơi tự do, a < g.',
            '**Nhầm “rơi nhanh hơn vì nặng hơn”**: gia tốc g **không** phụ thuộc khối lượng.',
            '**Sai đơn vị g**: g = 9,8 m/s² hay 10 m/s² tùy đề – phải đọc kỹ và dùng đúng giá trị.',
            '**Nhầm công thức**: khi rơi tự do có v<sub>0</sub> = 0 nên s = ½gt<sup>2</sup> '
            '(**không** phải s = gt<sup>2</sup>).',
        ],
        'links': ['Câu 10 (TN – Biết)', 'Câu 17, 18 (TN – Hiểu)', 'Phần III – Câu 2'],
    },
]

# Gộp đơn vị "Thực hành: Đo tốc độ của vật chuyển động" (mục 6 trong đặc tả)
THUC_HANH_TOC_DO = {
    'id': '2.2b',
    'title': 'Thực hành: Đo tốc độ của vật chuyển động',
    'matrix': '2.2 Tốc độ và vận tốc (thực hành đo tốc độ)',
    'badge': 'Được kiểm tra trong các câu về 2.2',
    'spec': [
        ('Nhận biết', [
            'Nêu được ưu điểm và nhược điểm khi sử dụng đồng hồ đo thời gian hiện số và cổng quang điện.',
            'Cách sử dụng đồng hồ đo thời gian hiện số.',
            'Ý nghĩa của việc sử dụng hai cổng quang điện.',
        ]),
        ('Thông hiểu', [
            'Đo được tốc độ bằng dụng cụ thực hành.',
        ]),
    ],
    'objectives': [
        'Thực hiện được phép đo tốc độ bằng **đồng hồ đo thời gian hiện số**.',
        'Giải thích được **ưu – nhược điểm** của đồng hồ hiện số và cổng quang điện.',
        'Giải thích được **ý nghĩa** của việc dùng **hai cổng quang điện** và tính được tốc độ giữa hai cổng.',
    ],
    'knowledge': [
        ('Quy trình đo bằng đồng hồ hiện số',
         '① Xác định điểm đầu và điểm cuối của đoạn đường. ② Bấm **START** đúng lúc vật bắt đầu chuyển động. '
         '③ Bấm **STOP** khi vật tới đích. ④ Đọc Δt. ⑤ Tính v = s/Δt. ⑥ Lặp lại nhiều lần và lấy giá trị trung bình.'),
        ('Đo bằng hai cổng quang điện',
         'Đặt cổng 1 và cổng 2 cách nhau L. Đồng hồ hiện số ghi t<sub>1</sub> (thời gian vật chặn cổng 1) và '
         't<sub>2</sub> (thời gian vật chặn cổng 2). Thời gian vật đi giữa hai cổng: Δt = t<sub>2</sub> − t<sub>1</sub>. '
         'Tốc độ trung bình giữa hai cổng: **v = L/(t<sub>2</sub> − t<sub>1</sub>)**.'),
    ],
    'memory': [
        '**“Hai cổng – một khoảng cách – một hiệu thời gian”**: v = L/Δt, Δt = t<sub>2</sub> − t<sub>1</sub>.',
        '**Ưu điểm lớn nhất của cổng quang điện:** đo **tự động**, **không ảnh hưởng** chuyển động của vật.',
    ],
    'example': None,
    'pitfalls': [
        '**Đặt nhầm t<sub>1</sub> là thời gian vật đi giữa hai cổng** – phải lấy **hiệu** t<sub>2</sub> − t<sub>1</sub>.',
        '**Đặt cổng quang điện** phải đúng vị trí, cùng độ cao, vật đi qua **giữa** cổng.',
    ],
    'links': ['Phần III – Câu 1 (đo tốc độ bằng hai cổng quang điện)'],
}

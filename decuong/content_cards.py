# -*- coding: utf-8 -*-
"""PHẦN 4 – Thẻ nhớ; PHẦN 5 – Chống mất điểm; PHẦN 6 – Trang bỏ túi; Phụ lục."""
from style import *


def _cards(rows):
    data = [["Câu hỏi", "Trả lời"]]
    data += [[a, b] for a, b in rows]
    return table(data, [CONTENT_W * 0.38, CONTENT_W * 0.62], font=7.4, first_col_bold=False, pad=2.2)


def story():
    s = []
    s.append(H1("PHẦN 4 · 70 THẺ NHỚ NHANH"))
    s.append(P("Cách dùng: gấp đôi tờ giấy theo đường kẻ giữa, che cột phải, đọc câu hỏi và tự trả lời. "
               "Thẻ nào quên thì đánh dấu sao và quay lại đúng mục lý thuyết tương ứng. "
               "Mỗi lượt mất khoảng 8 phút – làm 2 lượt/ngày là nhớ hết.", "lead"))
    s.append(SP(3))

    s.append(H2(toc=False, text="Nhóm A – Bài 1, 2, 3 (Lý thuyết, an toàn, sai số)"))
    s.append(_cards([
        ("Đối tượng nghiên cứu của Vật lí?", "Các dạng <b>vận động của vật chất (chất, trường)</b> và <b>năng lượng</b>."),
        ("Kể 5 lĩnh vực của Vật lí?", "Cơ học, điện học – điện từ học, quang học, âm học, nhiệt học "
                                      "(và còn: vật lí nguyên tử, lượng tử, thuyết tương đối)."),
        ("Giai đoạn 1 của Vật lí dựa vào gì?", "Quan sát và <b>suy luận chủ quan</b> (từ 350 TCN đến thế kỉ XVI)."),
        ("Giai đoạn 2 dựa vào gì?", "<b>Phương pháp thực nghiệm</b> (thế kỉ XVII → cuối XIX)."),
        ("Giai đoạn 3 (cuối XIX → nay)?", "Xây dựng <b>mô hình lí thuyết</b> cho thế giới vi mô, dùng "
                                          "<b>thí nghiệm kiểm chứng</b>."),
        ("Ai là “cha đẻ” phương pháp thực nghiệm?", "<b>Galilei</b>."),
        ("5 bước phương pháp thực nghiệm?", "Xác định vấn đề → quan sát, thu thập thông tin → dự đoán → "
                                            "thí nghiệm kiểm tra → kết luận."),
        ("4 bước phương pháp mô hình?", "Xác định đối tượng → xây dựng mô hình → kiểm tra sự phù hợp → kết luận."),
        ("CMCN lần 1 dựa trên thành tựu nào?", "Nghiên cứu về <b>nhiệt</b> → máy hơi nước của James Watt (1765)."),
        ("CMCN lần 2?", "<b>Cảm ứng điện từ</b> (Faraday, 1831) → máy phát điện, thiết bị dùng điện."),
        ("CMCN lần 3?", "<b>Điện tử, chất bán dẫn, vi mạch</b> → tự động hoá sản xuất (thập niên 1970)."),
        ("CMCN lần 4?", "<b>AI, robot, internet toàn cầu, công nghệ nano</b> → thiết bị thông minh (đầu XXI)."),
        ("Màu đỏ trên biển báo nghĩa là gì?", "<b>Cấm</b> thực hiện."),
        ("Tam giác vàng nghĩa là gì?", "<b>Cảnh báo nguy hiểm</b>."),
        ("Hình tròn nền xanh nghĩa là gì?", "<b>Bắt buộc</b> thực hiện."),
        ("Hình vuông nền xanh lá nghĩa là gì?", "<b>Chỉ dẫn / thông báo</b> (lối thoát hiểm, bình chữa cháy)."),
        ("Khi phòng thực hành cháy, việc đầu tiên?", "<b>Ngắt toàn bộ hệ thống điện</b>, báo giáo viên, "
                                                     "tổ chức thoát nạn và cứu người."),
        ("Có được dùng nước dập cháy thiết bị điện?", "<b>Không</b> – nước dẫn điện, gây điện giật và cháy lan."),
        ("Phép đo trực tiếp là gì?", "Đọc <b>trực tiếp</b> giá trị trên dụng cụ đo (thước, cân, đồng hồ)."),
        ("Phép đo gián tiếp là gì?", "Tính qua <b>công thức</b> từ các đại lượng đo trực tiếp (v = s/t)."),
        ("Sai số hệ thống do đâu?", "Do <b>dụng cụ</b>, cấu tạo, mẫu vật – lặp lại như nhau, lệch một phía."),
        ("Sai số ngẫu nhiên do đâu?", "Do <b>thao tác, điều kiện, giác quan</b> – mỗi lần một khác; "
                                      "giảm bằng đo nhiều lần lấy trung bình."),
        ("Sai số dụng cụ thường lấy bằng?", "<b>Nửa độ chia nhỏ nhất (ĐCNN)</b> hoặc theo nhà sản xuất."),
        ("Công thức sai số tỉ đối?", "δA = (ΔA/Ā)·100% (%) – càng nhỏ càng chính xác."),
        ("Cộng/hiệu thì sai số thế nào?", "<b>Cộng sai số tuyệt đối</b>: ΔA = ΔB + ΔC."),
        ("Nhân/chia thì sai số thế nào?", "<b>Cộng sai số tỉ đối</b>: δA = δB + δC."),
        ("Cách ghi kết quả đo?", "A = Ā ± ΔA, với Ā và ΔA <b>cùng bậc thập phân</b>."),
    ]))

    s.append(PageBreak())
    s.append(H2(toc=False, text="Nhóm B – Bài 4, 5, 7 (Độ dịch chuyển, tốc độ – vận tốc, đồ thị)"))
    s.append(_cards([
        ("Độ dịch chuyển là gì?", "Vectơ nối <b>vị trí đầu → vị trí cuối</b>; đặc trưng cho sự thay đổi vị trí."),
        ("Quãng đường là gì?", "Đại lượng <b>vô hướng</b>, bằng <b>tổng độ dài</b> đường đi; luôn ≥ 0."),
        ("Khi nào d = s?", "Khi vật chuyển động <b>thẳng và không đổi chiều</b>."),
        ("Đi 3 km đông rồi 4 km bắc: d bằng?", "5 km (Pitago), s = 7 km."),
        ("Đi 100 m rồi quay lại: d và s?", "d = 0; s = 200 m."),
        ("Tốc độ trung bình là gì?", "Đại lượng <b>vô hướng</b>: v = s/Δt, cho biết nhanh/chậm."),
        ("Vận tốc trung bình là gì?", "Đại lượng <b>vectơ</b>: v = Δd/Δt, cho biết nhanh/chậm và hướng."),
        ("Tốc độ tức thời là gì?", "Tốc độ tại một thời điểm: v = Δs/Δt với Δt rất nhỏ."),
        ("1 m/s bằng bao nhiêu km/h?", "<b>3,6 km/h</b> (ngược lại: chia 3,6)."),
        ("Công thức cộng vận tốc?", "v̅<sub>13</sub> = v̅<sub>12</sub> + v̅<sub>23</sub> (tuyệt đối = tương đối + kéo theo)."),
        ("Hai vận tốc ngược chiều thì độ lớn?", "v₁₃ = |v₁₂ − v₂₃|."),
        ("Hai vận tốc vuông góc thì độ lớn?", "v₁₃ = √(v₁₂² + v₂₃²)."),
        ("Thuyền xuôi dòng 5 m/s, nước 3 m/s?", "v = 5 + 3 = 8 m/s (ngược dòng: 2 m/s)."),
        ("Đi nửa đường 60 km/h, nửa đường 40 km/h?", "v<sub>tb</sub> = 2·60·40/(60+40) = <b>48 km/h</b>."),
        ("Trên đồ thị s–t, vận tốc là gì?", "<b>Độ dốc</b> của đường biểu diễn: v = Δx/Δt."),
        ("Đồ thị s–t nằm ngang nghĩa là?", "Vật <b>đứng yên</b> (x không đổi)."),
        ("Đồ thị s–t dốc xuống nghĩa là?", "Vật chuyển động <b>ngược chiều dương</b> (v &lt; 0)."),
        ("Hai đồ thị s–t cắt nhau nghĩa là?", "Hai vật <b>gặp nhau</b>."),
        ("Từ đồ thị s–t, muốn tính quãng đường?", "Cộng <b>|Δx|</b> của từng đoạn."),
        ("Đồ thị s–t cong lên nghĩa là?", "Chuyển động <b>không đều</b> (vận tốc thay đổi)."),
    ]))
    s.append(SP(5))

    s.append(H2(toc=False, text="Nhóm C – Bài 8, 9, 10 (Gia tốc, biến đổi đều, rơi tự do)"))
    s.append(_cards([
        ("Chuyển động biến đổi là gì?", "Chuyển động có <b>vận tốc thay đổi</b> (độ lớn hoặc hướng)."),
        ("Công thức gia tốc?", "a = Δv/Δt = (v₂ − v₁)/(t₂ − t₁); đơn vị m/s²."),
        ("Gia tốc là đại lượng gì?", "<b>Vectơ</b>; đặc trưng cho mức độ biến thiên của vận tốc."),
        ("a cùng chiều v thì sao?", "Chuyển động <b>nhanh dần</b>."),
        ("a ngược chiều v thì sao?", "Chuyển động <b>chậm dần</b>."),
        ("a vuông góc v thì sao?", "Vận tốc <b>đổi hướng</b>, độ lớn không đổi (tròn đều)."),
        ("a = −2 m/s², v = −5 m/s: nhanh hay chậm?", "<b>Nhanh dần</b> – vì a và v cùng dấu."),
        ("Định nghĩa chuyển động thẳng biến đổi đều?", "Quỹ đạo thẳng, <b>gia tốc không đổi</b>."),
        ("Nhanh dần đều là gì?", "a cùng chiều v → độ lớn vận tốc <b>tăng đều</b>."),
        ("Chậm dần đều là gì?", "a ngược chiều v → độ lớn vận tốc <b>giảm đều</b>."),
        ("3 công thức của chuyển động biến đổi đều?", "v = v₀ + at; d = v₀t + ½at²; v² − v₀² = 2ad."),
        ("Thiếu t thì dùng công thức nào?", "v² − v₀² = 2ad."),
        ("Quãng đường đến khi dừng?", "s = v₀²/(2|a|); thời gian dừng t = v₀/|a|."),
        ("Quãng đường trong giây thứ n?", "Δs = s(n) − s(n−1) = v₀ + a(n − 0,5)."),
        ("Vật đổi chiều khi nào?", "Khi vận tốc đổi dấu (v = 0 rồi ngược dấu)."),
        ("Khi vật đổi chiều, s và |d| thế nào?", "<b>s &gt; |d|</b> (s là tổng quãng đường các chặng)."),
        ("Rơi tự do là gì?", "Sự rơi <b>chỉ dưới tác dụng của trọng lực</b> (bỏ qua sức cản không khí)."),
        ("Rơi tự do có tính chất gì?", "Thẳng đứng, chiều xuống, <b>nhanh dần đều</b> với a = g."),
        ("Công thức rơi tự do?", "v = gt; h = ½gt²; v² = 2gh; t = √(2h/g)."),
        ("g thường lấy bằng?", "<b>9,8 m/s²</b> (nhiều đề cho 10 m/s²)."),
        ("Quãng đường trong giây cuối?", "Δh = h(t) − h(t−1) = g(t − 0,5)."),
        ("Trong chân không, vật nặng nhẹ rơi thế nào?", "<b>Như nhau</b> – cùng gia tốc g."),
        ("Vật nào không phải rơi tự do?", "Chiếc lá, tờ giấy phẳng, lông chim… (sức cản đáng kể)."),
    ]))
    s.append(PageBreak())

    # ===================================================== PHẦN 5
    s.append(H1("PHẦN 5 · 12 LỖI MẤT ĐIỂM & QUY TRÌNH LÀM BÀI"))
    s.append(H2("5.1. Mười hai lỗi “kinh điển”"))
    s.append(table([
        ["#", "Lỗi", "Cách tránh"],
        ["1", "Không đổi km/h → m/s trước khi thay số",
         "Ghi ngay ở lề: 36 km/h = 10 m/s; 54 km/h = 15 m/s; 72 km/h = 20 m/s. Chia 3,6."],
        ["2", "Dùng v<sub>tb</sub> = s/t với s là <b>độ dịch chuyển</b>",
         "Tốc độ dùng <b>quãng đường</b>; vận tốc dùng <b>độ dịch chuyển</b>."],
        ["3", "Cho rằng vận tốc trung bình = trung bình cộng các vận tốc",
         "Chỉ đúng khi các đoạn có <b>cùng thời gian</b>; cùng quãng đường thì dùng 2v₁v₂/(v₁+v₂)."],
        ["4", "Nghĩ “a &lt; 0 là chậm dần”", "Xét <b>dấu tương đối</b> của a và v."],
        ["5", "Quên v₀ trong d = v₀t + ½at²", "Viết công thức chữ trước, thay số sau."],
        ["6", "Lẫn d = v₀t + ½at² với s = v·t", "Chỉ dùng s = vt khi v <b>không đổi</b>."],
        ["7", "Tính “giây thứ n” bằng s(n)/n", "Dùng s(n) − s(n−1)."],
        ["8", "Không phát hiện vật dừng rồi đổi chiều", "Tính t<sub>dừng</sub> = v₀/|a| trước khi thay t lớn."],
        ["9", "Dùng h = v·t cho rơi tự do", "Rơi tự do: h = ½gt², v = gt."],
        ["10", "Ghi kết quả đo không cùng bậc thập phân",
         "Ā và ΔA phải cùng số chữ số sau dấu phẩy; ΔA thường 1–2 chữ số có nghĩa."],
        ["11", "Nhầm sai số hệ thống với sai số ngẫu nhiên",
         "Hệ thống = dụng cụ (lệch một phía); ngẫu nhiên = thao tác (mỗi lần một khác)."],
        ["12", "Không ghi đơn vị ở đáp số", "Mỗi con số vật lí phải có đơn vị; thiếu đơn vị là mất điểm."],
    ], [20, 190, CONTENT_W - 210], font=7.9, align=["c", "l", "l"]))
    s.append(SP(6))

    s.append(H2("5.2. Quy trình 4 bước cho mọi bài tự luận"))
    s.append(table([
        ["Bước", "Viết gì trên bài làm", "Ví dụ"],
        ["1. Tóm tắt", "Liệt kê đại lượng đã cho và cần tìm, kèm đơn vị", "v₀ = 10 m/s; a = 2 m/s²; t = 10 s. Tìm v, s"],
        ["2. Chọn chiều dương", "Ghi rõ chiều dương đã chọn", "Chọn chiều dương là chiều chuyển động"],
        ["3. Công thức chữ", "Viết công thức tổng quát <b>trước</b> khi thay số", "v = v₀ + at"],
        ["4. Thay số – kết luận", "Thay số, tính, ghi đáp số có đơn vị", "v = 10 + 2·10 = 30 m/s"],
    ], [84, 200, CONTENT_W - 284], font=8.0, align=["l", "l", "l"]))
    s.append(SP(6))

    s.append(H2("5.3. Checklist trước khi nộp bài"))
    s.extend(BULL([
        "Đã tô đủ <b>18 câu</b> Phần I chưa? Không bỏ trống câu nào (đoán vẫn có 25% cơ hội).",
        "Phần II: mỗi câu đã ghi đủ <b>4 ý</b> Đ/S chưa?",
        "Các đáp số tự luận đã có <b>đơn vị</b> và đúng <b>số chữ số</b> chưa?",
        "Đã kiểm tra lại việc đổi đơn vị (km/h → m/s) ở mọi bài chưa?",
        "Câu nào còn nghi ngờ thì đã đánh dấu để xem lại chưa?",
        "Phiếu trả lời đã tô đúng ô, không tô nhầm dòng chưa?",
    ]))
    s.append(CondPageBreak(330))
    s.append(H2("5.4. Chữa một bài làm sai – học từ chính lỗi của mình"))
    s.append(P("Dưới đây là một bài làm thật của học sinh và cách chữa. Hãy so sánh để thấy: điểm không "
               "nằm ở chỗ “làm ra đáp số”, mà nằm ở <b>cách trình bày và kiểm tra</b>.", "body"))
    _tb = table([
        ["Đề", "Bài làm chưa đạt", "Chỗ sai", "Bài làm đạt"],
        ["Một xe đạp đang chạy 18 km/h thì hãm phanh, chuyển động chậm dần đều với gia tốc 0,5 m/s². "
         "Tính quãng đường xe đi được đến khi dừng lại.",
         "“s = v/a = 18/0,5 = 36 m”",
         "• Chưa đổi 18 km/h → 5 m/s.<br/>• Dùng sai công thức: s = v²/(2a) chứ không phải v/a.<br/>"
         "• Thiếu đơn vị ở v.",
         "18 km/h = 5 m/s.<br/>Chọn chiều dương là chiều chuyển động.<br/>"
         "Áp dụng v² − v₀² = 2a·s với v = 0:<br/>0 − 5² = 2·(−0,5)·s → s = 25/1 = <b>25 m</b>."],
    ], [CONTENT_W * 0.25, CONTENT_W * 0.18, CONTENT_W * 0.28, CONTENT_W * 0.29],
        font=7.8, align=["l", "l", "l", "l"])
    s.append(KeepTogether([_tb]))
    s.append(SP(4))
    s.append(box("Sai ở đâu thì chữa đúng chỗ đó: bài trên mất điểm vì <b>đơn vị</b> và <b>công thức</b>, "
                 "không phải vì không biết hiện tượng chậm dần đều là gì. Ghi hai lỗi này vào "
                 "“Sổ ghi lỗi” ở Phần 3B.", "meo"))
    s.append(SP(8))

    s.append(H2(toc=False, text="5.5. Bảng tự đánh giá mức độ sẵn sàng"))
    s.append(P("Đánh dấu vào ô phù hợp với bản thân. Nếu có bất kì dòng nào ở cột “Chưa làm được”, "
               "hãy quay lại đúng mục lý thuyết tương ứng trước khi thi.", "body"))
    s.append(table([
        ["Năng lực", "Mục lý thuyết", "Tự tin", "Cần ôn lại", "Chưa làm được"],
        ["Kể tên 4 cuộc CMCN và thành tựu tương ứng", "Bài 1", "[   ]", "[   ]", "[   ]"],
        ["Nêu 5 bước phương pháp thực nghiệm", "Bài 1", "[   ]", "[   ]", "[   ]"],
        ["Phân biệt 4 loại biển báo + xử lí sự cố cháy, điện giật", "Bài 2", "[   ]", "[   ]", "[   ]"],
        ["Viết đúng 5 công thức sai số và ghi kết quả đo", "Bài 3", "[   ]", "[   ]", "[   ]"],
        ["Phân biệt độ dịch chuyển – quãng đường; tính cả hai", "Bài 4", "[   ]", "[   ]", "[   ]"],
        ["Tính tốc độ/vận tốc trung bình, cộng vận tốc 3 trường hợp", "Bài 5", "[   ]", "[   ]", "[   ]"],
        ["Đọc và vẽ đồ thị s–t, tính v từ độ dốc", "Bài 7", "[   ]", "[   ]", "[   ]"],
        ["Xác định dấu của gia tốc, phân biệt nhanh/chậm dần", "Bài 8", "[   ]", "[   ]", "[   ]"],
        ["Giải 5 dạng bài chuyển động thẳng biến đổi đều", "Bài 9", "[   ]", "[   ]", "[   ]"],
        ["Giải bài rơi tự do: t, v, h, giây cuối", "Bài 10", "[   ]", "[   ]", "[   ]"],
    ], [CONTENT_W * 0.44, 62, 54, 58, CONTENT_W - CONTENT_W * 0.44 - 174],
        font=7.8, align=["l", "c", "c", "c", "c"], pad=4))
    s.append(SP(6))

    s.append(H2(toc=False, text="5.6. Ba lời khuyên trước giờ vào phòng thi"))
    s.extend(BULL([
        "<b>Đừng học thêm kiến thức mới trong 24 giờ cuối.</b> Chỉ đọc lại Trang bỏ túi và Sổ tay công thức – "
        "não cần thời gian “ổn định” những gì đã học, không cần thêm dữ liệu.",
        "<b>Ngủ đủ 7–8 tiếng.</b> Một giờ ngủ đêm trước đề thi có giá trị hơn hai giờ học vẹt, vì hầu hết "
        "lỗi mất điểm là lỗi <b>đọc sai đề và tính nhầm</b> – đều do mệt mỏi.",
        "<b>Vào phòng thi, viết ngay ra lề phiếu 5 dòng:</b> công thức sai số, cộng vận tốc, 3 công thức "
        "chuyển động biến đổi đều, công thức rơi tự do, và ba cặp đổi km/h → m/s. Đó là “phao kiến thức hợp lệ” "
        "giúp bạn không phải nhớ trong lúc căng thẳng.",
    ]))
    s.append(PageBreak())

    # ===================================================== PHẦN 6
    s.append(H1("PHẦN 6 · TRANG BỎ TÚI"))
    s.append(SP(2))
    s.append(box("<b>1. BỐN CẶP MÀU BIỂN BÁO</b> — Đỏ tròn = CẤM · Vàng tam giác = CẢNH BÁO · "
                 "Xanh tròn = BẮT BUỘC · Xanh vuông = CHỈ DẪN.<br/>"
                 "<b>2. BỐN CUỘC CMCN</b> — Máy hơi nước (nhiệt) → Điện (cảm ứng điện từ) → "
                 "Tự động hoá (bán dẫn) → AI – robot (nano).<br/>"
                 "<b>3. NĂM BƯỚC THỰC NGHIỆM</b> — Xác định vấn đề · Quan sát · Dự đoán · Thí nghiệm · Kết luận.",
                 "meo", "NHỚ NHANH LÝ THUYẾT"))
    s.append(SP(2))
    s.append(formula("δA = (ΔA/Ā)·100%   |   ΔA = Δ̄A + ΔA<sub>đc</sub>   |   A = Ā ± ΔA",
                     "Sai số: tổng/hiệu → cộng tuyệt đối; tích/thương → cộng tỉ đối"))
    s.append(formula("v<sub>tb</sub> = s/Δt (tốc độ)   |   v̅<sub>tb</sub> = Δd̅/Δt (vận tốc)",
                     "Độ dịch chuyển: Δx = x₂ − x₁; d ≤ s"))
    s.append(formula("v̅<sub>13</sub> = v̅<sub>12</sub> + v̅<sub>23</sub>", "Cùng chiều: + · Ngược chiều: |−| · Vuông góc: √(a² + b²)"))
    s.append(formula("a = Δv/Δt", "Cùng chiều v → nhanh dần; ngược chiều v → chậm dần"))
    s.append(formula("v = v₀ + at      d = v₀t + ½at²      v² − v₀² = 2ad",
                     "Thiếu t → dùng (3); thiếu v → dùng (2); thiếu d → dùng (1)"))
    s.append(formula("v = gt      h = ½gt²      v² = 2gh      t = √(2h/g)", "Rơi tự do, g ≈ 9,8 hoặc 10 m/s²"))
    s.append(SP(3))
    s.append(box("<b>Đổi đơn vị:</b> 36 km/h = 10 m/s · 54 km/h = 15 m/s · 72 km/h = 20 m/s · "
                 "1 m/s = 3,6 km/h.<br/>"
                 "<b>Ba câu tự vấn trước mỗi bài toán:</b> (1) Chuyển động loại nào? (2) Chiều dương ở đâu? "
                 "(3) Công thức nào chứa đủ 3 đại lượng đã biết + 1 cần tìm?", "thi", "TRƯỚC KHI BẤM MÁY"))
    s.append(SP(4))
    s.append(H2(toc=False, text="Lịch ôn 7 ngày (dán lên góc học tập)"))
    s.append(table([
        ["Ngày", "Nội dung", "Sản phẩm cần đạt"],
        ["1", "Bài 1, 2, 3 + Nhóm thẻ A", "Thuộc 4 cặp màu biển báo; viết đúng 5 công thức sai số"],
        ["2", "Bài 4, 5 (độ dịch chuyển, tốc độ – vận tốc)", "Phân biệt s và d; làm 5 bài cộng vận tốc"],
        ["3", "Bài 7 (đồ thị) + Bài 8 (gia tốc)", "Đọc được vận tốc từ độ dốc; xác định dấu a"],
        ["4", "Bài 9 – dạng 1, 2, 3", "Làm thành thạo 3 dạng đầu, không quên v₀"],
        ["5", "Bài 9 – dạng 4, 5 + Bài 10", "Xử lí được bài đổi chiều và bài hai vật gặp nhau"],
        ["6", "Làm <b>Đề mô phỏng</b> trong 50 phút", "Tự chấm, ghi ra 3 lỗi sai chính"],
        ["7", "Chữa lỗi + 70 thẻ nhớ + Trang bỏ túi", "Làm lại đề lần 2, mục tiêu ≥ 80%"],
    ], [40, 230, CONTENT_W - 270], font=8.0, align=["c", "l", "l"]))
    s.append(PageBreak())

    # ===================================================== PHỤ LỤC
    s.append(H1("PHỤ LỤC · ĐẶC TẢ YÊU CẦU CẦN ĐẠT"))
    s.append(P("Bảng dưới đây tóm lược <b>đúng</b> các yêu cầu về kiến thức – kĩ năng mà đề kiểm tra sẽ hỏi, "
               "xếp theo mức độ nhận thức. Dùng bảng này để tự kiểm tra: mỗi dòng bạn phải trả lời được "
               "mà không cần mở sách.", "body"))
    s.append(SP(3))
    spec = [
        ["Đơn vị kiến thức", "Nhận biết", "Thông hiểu – Vận dụng"],
        ["1.1. Làm quen với Vật lí",
         "Đối tượng nghiên cứu; thành tựu ứng với các cuộc CMCN; quá trình phát triển; phương pháp nghiên cứu",
         "Hiểu và trình bày lại được quá trình nghiên cứu Vật lí"],
        ["1.2. Quy tắc an toàn",
         "Nguy cơ mất an toàn; các quy tắc an toàn trong phòng thực hành",
         "Sử dụng được thiết bị thí nghiệm; đọc và hiểu các biển báo"],
        ["1.3. Sai số phép đo",
         "Phép đo trực tiếp/gián tiếp; các loại sai số; nguyên nhân gây sai số; công thức giá trị trung bình, "
         "sai số tỉ đối, sai số tuyệt đối",
         "Cách ghi đúng kết quả; tính được sai số tuyệt đối và tỉ đối; tính giá trị đo"],
        ["2.1. Độ dịch chuyển – quãng đường",
         "Độ dịch chuyển là gì; so sánh với quãng đường",
         "Xác định và tính được độ dịch chuyển, quãng đường trong các bài toán"],
        ["2.2. Tốc độ và vận tốc",
         "Ý nghĩa, công thức tốc độ trung bình; tốc độ tức thời; cách đo tốc độ; định nghĩa và công thức "
         "vận tốc; công thức cộng vận tốc",
         "Tính tốc độ trung bình; phân biệt tốc độ – vận tốc; xác định vectơ vận tốc; giải bài toán tổng hợp "
         "hai vận tốc cùng phương và vuông góc"],
        ["2.3. Đồ thị độ dịch chuyển – thời gian",
         "Mô tả chuyển động dựa vào đồ thị",
         "Tính tốc độ từ độ dốc; xác định vị trí, vận tốc tại thời điểm bất kì; vẽ đồ thị; xác định quãng "
         "đường và độ dịch chuyển"],
        ["2.4. Chuyển động biến đổi – gia tốc",
         "Khái niệm chuyển động biến đổi; quan hệ phương – chiều của a và v; khái niệm, công thức, đơn vị gia tốc",
         "Tính độ biến thiên vận tốc và gia tốc; phân biệt nhanh dần – chậm dần"],
        ["2.5. Chuyển động thẳng biến đổi đều",
         "Định nghĩa chuyển động thẳng biến đổi đều, nhanh dần đều, chậm dần đều; các công thức",
         "Tính v, a, d bằng công thức; giải bài toán cơ bản và nâng cao (đổi chiều, gặp nhau, giây thứ n)"],
        ["2.6. Sự rơi tự do",
         "Định nghĩa; đặc điểm chuyển động rơi trong không khí; các công thức",
         "Phân biệt vật rơi gần đúng tự do; áp dụng công thức tính thời gian, vận tốc, độ cao, quãng đường"],
    ]
    s.append(table(spec, [104, 168, CONTENT_W - 272], font=7.8))
    s.append(SP(5))
    s.append(box("<b>Ghi chú về Bài 6 (Thực hành đo tốc độ):</b> đặc tả có nêu nhưng ma trận <b>không</b> "
                 "phân bổ câu hỏi. Vẫn nên đọc Mục “Bài 6” ở Phần 1 (1 trang) để phòng trường hợp nội dung "
                 "này được lồng vào câu hỏi về đo tốc độ / sai số.", "thi"))

    s.append(SP(10))
    s.append(P("<b>Lời kết.</b> Đề giữa kì I Vật lí 10 không khó nếu bạn chia đúng sức: <b>thuộc bảng – "
               "nhớ công thức – luyện 5 dạng bài</b>. Ba việc đó, làm đủ trong 7 ngày, là đủ để tự tin "
               "bước vào phòng thi. Chúc bạn làm bài tốt!", "lead"))
    return s

# -*- coding: utf-8 -*-
"""Module B – Lý thuyết trọng tâm 10 đơn vị kiến thức."""
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (CondPageBreak, KeepTogether, PageBreak, Spacer,
                                Table, TableStyle)

from style import (AMBER, BODY, BODY_L, GREEN, INK, LINE, LM, MUTED, PAGE_W,
                   PRIMARY, RM, SMALL, TEAL, SectionBanner, H2, H3, P, box,
                   bullets, formula, numbered, table)

W = PAGE_W - LM - RM


# --------------------------------------------------------------------------- helpers
def unit(number, title, tagline, matrix, color=PRIMARY):
    """Banner mở đầu một đơn vị kiến thức."""
    out = [CondPageBreak(11.5 * cm)]
    b = SectionBanner("PHẦN B · ĐƠN VỊ %s/10" % number, title, tagline,
                      color=color, height=86)
    out.append(b)
    out.append(Spacer(1, 6))
    st = ParagraphStyle("mx", fontName="BVP", fontSize=8.2, leading=11.6,
                        textColor=MUTED)
    t = Table([[P('<font color="#B3261E">◆</font>&nbsp; <b>Theo ma trận:</b> ' + matrix, st)]],
              colWidths=[W])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                           ("LINEBELOW", (0, 0), (-1, -1), 0.6, LINE)]))
    out.append(t)
    out.append(Spacer(1, 4))
    return out


def defn(text):
    """Câu định nghĩa cốt lõi – in đậm nhẹ, nền vàng."""
    if isinstance(text, str):
        text = [text]
    return box("Ghi nhớ cốt lõi", [P(t) for t in text], kind="amber")


def memo(items, title="Mẹo nhớ nhanh"):
    return box(title, bullets(items), kind="teal")


def bay(items, title="Bẫy thường gặp"):
    return box(title, bullets(items), kind="red")


def vd(title, lines, answer=None):
    body = []
    for i, ln in enumerate(lines):
        body.append(P(ln))
    if answer:
        body.append(Spacer(1, 2))
        body.append(P('<font color="#1B7A45"><b>→</b></font> ' + answer,
                      ParagraphStyle("ans", parent=BODY, textColor=GREEN)))
    return box("Ví dụ mẫu · " + title, body, kind="primary")


def quiz(items, answers):
    rows = []
    for i, q in enumerate(items):
        rows.append([P("<b>%d.</b> " % (i + 1) + q, BODY)])
    t = Table([[P("<b>%d.</b> " % (i + 1) + q, BODY)] for i, q in enumerate(items)],
              colWidths=[W - 12])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)]))
    out = [Spacer(1, 3)]
    out += box("Tự kiểm tra (30 giây/câu)",
               [t, Spacer(1, 4),
                P('<font color="#586180"><i>Đáp án:</i> %s</font>' % answers,
                  ParagraphStyle("qa", parent=SMALL, fontSize=8.2))],
               kind="grey")
    return out


def cols(items, widths=None):
    """Chia nội dung thành 2 cột đều nhau."""
    widths = widths or [W / 2 - 4, W / 2 - 4]
    half = (len(items) + 1) // 2
    left = items[:half]
    right = items[half:]
    t = Table([[left, right]], colWidths=widths)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (0, -1), 0),
                           ("LEFTPADDING", (1, 0), (1, -1), 12),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return [t]


# --------------------------------------------------------------------------- B1
def b1():
    o = unit("1", "Làm quen với Vật lí",
             "Đối tượng – 3 giai đoạn phát triển – 4 cuộc cách mạng công nghiệp – phương pháp nghiên cứu",
             "2 câu trắc nghiệm (1 Biết, 1 Hiểu) · nội dung: đối tượng nghiên cứu, thành tựu gắn với "
             "các cuộc cách mạng công nghiệp, các giai đoạn phát triển, phương pháp nghiên cứu.")
    o.append(H3("1. Đối tượng nghiên cứu của Vật lí"))
    o.append(P("Vật lí là môn khoa học tự nhiên nghiên cứu <b>các dạng vận động của vật chất "
               "(chất, trường) và năng lượng</b>. Mọi hiện tượng vật lí đều gắn với một dạng vận "
               "động: cơ học, điện học, điện từ học, quang học, âm học, nhiệt học, nhiệt động lực "
               "học, vật lí nguyên tử – hạt nhân, vật lí lượng tử, thuyết tương đối."))
    o.extend(box("Phân biệt nhanh hai cụm dễ lẫn",
                 [P("<b>Đối tượng nghiên cứu</b> = “nghiên cứu cái gì” → các dạng vận động của "
                    "vật chất và năng lượng.<br/><b>Mục tiêu của môn Vật lí</b> = “học để làm gì” → "
                    "hình thành năng lực vật lí: có kiến thức – kĩ năng cơ bản; vận dụng giải quyết "
                    "vấn đề thực tiễn; định hướng nghề nghiệp.")], kind="primary"))

    o.append(H3("2. Ba giai đoạn phát triển của Vật lí"))
    data = [["GIAI ĐOẠN", "THỜI GIAN", "CÁCH NGHIÊN CỨU", "THÀNH TỰU TIÊU BIỂU"],
            ["Tiền Vật lí", "Trước Công nguyên → thế kỉ XV",
             "Quan sát thiên nhiên và suy luận chủ quan; chưa có thực nghiệm",
             "Đo đạc thiên văn, hình học, cơ học sơ khai (Archimedes); triết học tự nhiên"],
            ["Vật lí cổ điển", "Thế kỉ XV → cuối thế kỉ XIX",
             "Phương pháp <b>thực nghiệm</b> kết hợp toán học",
             "Galileo (rơi tự do), Newton (3 định luật + vạn vật hấp dẫn), "
             "nhiệt động lực học, điện từ học (Faraday – Maxwell)"],
            ["Vật lí hiện đại", "Đầu thế kỉ XX → nay",
             "Thực nghiệm + mô hình trừu tượng, nghiên cứu cấu trúc vi mô",
             "Thuyết lượng tử (Planck 1900), thuyết tương đối (Einstein 1905), "
             "vật lí hạt nhân, vật lí chất rắn"]]
    o.append(table(data, [2.6 * cm, 3.3 * cm, 4.5 * cm, 6.3 * cm], size=8.2))
    o.extend(memo(["<b>3 giai đoạn</b> – nhớ theo từ khóa: <b>“TIỀN – CỔ ĐIỂN – HIỆN ĐẠI”</b>.",
                   "Mốc chia: <b>thế kỉ XV</b> (thực nghiệm ra đời) và <b>đầu thế kỉ XX</b> "
                   "(lượng tử + tương đối).",
                   "Tiền Vật lí = <i>suy luận</i>; Cổ điển = <i>thực nghiệm</i>; Hiện đại = "
                   "<i>vi mô + tương đối</i>."]))

    o.append(H3("3. Bốn cuộc cách mạng công nghiệp – “gương mặt” Vật lí"))
    data = [["CMCN", "THỜI ĐIỂM", "THÀNH TỰU VẬT LÍ then chốt", "ĐẶC TRƯNG"],
            ["Lần 1", "1765", "Máy hơi nước của <b>James Watt</b> (dựa trên nghiên cứu Nhiệt học, "
                              "sự dãn nở vì nhiệt)", "Thay sức lực cơ bắp bằng sức lực máy móc"],
            ["Lần 2", "1831 → cuối XIX", "<b>Faraday</b> phát hiện hiện tượng cảm ứng điện từ → "
                                          "máy phát điện, động cơ điện",
             "Xuất hiện ngày càng nhiều thiết bị dùng điện"],
            ["Lần 3", "Những năm 70 của thế kỉ XX", "Điện tử, <b>chất bán dẫn</b>, vi mạch",
             "Tự động hóa quá trình sản xuất"],
            ["Lần 4", "Đầu thế kỉ XXI", "Trí tuệ nhân tạo, robot, internet toàn cầu, công nghệ nano, "
                                        "thiết bị thông minh", "Sản xuất thông minh, kết nối vạn vật"]]
    o.append(table(data, [1.6 * cm, 3.1 * cm, 6.4 * cm, 5.6 * cm], size=8.2,
                     head_bg=TEAL))
    o.extend(memo(["Nhớ cặp <b>“số – người”</b>: 1–Watt (hơi nước), 2–Faraday (điện), "
                   "3–bán dẫn (tự động), 4–AI (thông minh).",
                   "Câu hỏi hay ra: “thành tựu nào mở đầu CMCN lần thứ <i>nhất</i>?” → "
                   "<b>máy hơi nước Watt 1765</b>; “lần thứ <i>hai</i>?” → "
                   "<b>cảm ứng điện từ Faraday 1831</b>."]))
    o.extend(bay(["Đừng nhầm <b>Newton – lực vạn vật hấp dẫn</b> với thành tựu mở đầu CMCN. "
                  "Newton là Vật lí cổ điển nhưng không phải “máy móc của CMCN lần 1”.",
                  "Cuộc CMCN lần 1 gắn với <b>Nhiệt học</b>, không phải Cơ học.",
                  "“Ba giai đoạn” ≠ “bốn cuộc cách mạng”: một bên là <i>lịch sử Vật lí</i>, "
                  "một bên là <i>lịch sử công nghiệp</i>."]))

    o.append(H3("4. Phương pháp nghiên cứu Vật lí"))
    o.append(P("<b>a) Phương pháp thực nghiệm</b> – quy trình 6 bước:"))
    o.extend(numbered([
        "<b>Quan sát</b> hiện tượng, xác định vấn đề cần nghiên cứu.",
        "<b>Xây dựng giả thuyết</b> (dự đoán có căn cứ) trả lời câu hỏi đặt ra.",
        "<b>Thiết kế phương án thí nghiệm</b>: chọn dụng cụ, xác định đại lượng cần đo, "
        "cách đo, các điều kiện giữ nguyên.",
        "<b>Tiến hành thí nghiệm</b>, thu thập và xử lý số liệu (bảng, đồ thị, tính sai số).",
        "<b>Kiểm tra giả thuyết</b>: so sánh kết quả với dự đoán – đúng thì chấp nhận, "
        "sai thì sửa giả thuyết và làm lại.",
        "<b>Kết luận</b>, trình bày kết quả (định luật, công thức)."]))
    o.append(Spacer(1, 3))
    o.append(P("<b>b) Phương pháp mô hình</b> – dùng vật/mô hình thay cho đối tượng thật khi "
               "không thể quan sát trực tiếp:"))
    data = [["LOẠI MÔ HÌNH", "BẢN CHẤT", "VÍ DỤ"],
            ["Mô hình vật chất", "Vật thu nhỏ/phóng to của vật thật, giữ một số đặc điểm chính",
             "Quả địa cầu, mô hình hệ Mặt Trời, mô hình động cơ"],
            ["Mô hình lí thuyết", "Khái niệm trừu tượng thay cho vật thật",
             "<b>Chất điểm</b>, tia sáng, đường sức điện"],
            ["Mô hình toán học", "Công thức, phương trình, đồ thị, kí hiệu toán học",
             "d = v·t; đồ thị độ dịch chuyển – thời gian"]]
    o.append(table(data, [3.2 * cm, 7.0 * cm, 6.5 * cm], size=8.3,
                     head_bg=colors.HexColor("#5B4B8A")))
    o.append(Spacer(1, 4))
    o.extend(box("Bốn bước xây dựng mô hình",
                 [P("(1) Xác định đối tượng nghiên cứu → (2) Xây dựng mô hình (chọn yếu tố "
                    "giữ lại, bỏ qua yếu tố phụ) → (3) Kiểm tra sự phù hợp của mô hình với "
                    "thực nghiệm → (4) Vận dụng mô hình để suy ra kết quả, dự đoán.")], kind="grey"))
    o.append(P("<b>Lưu ý về vai trò:</b> Vật lí là <i>cơ sở của khoa học tự nhiên</i> và "
               "<i>cơ sở của công nghệ</i>; là mũi nhọn then chốt của các cuộc cách mạng công "
               "nghiệp. Tuy nhiên, ứng dụng Vật lí nếu không đúng mục đích có thể gây ô nhiễm "
               "môi trường, hủy hoại hệ sinh thái – ví dụ chất thải phóng xạ, khí thải nhà máy "
               "nhiệt điện."))
    o.extend(quiz(["Đối tượng nghiên cứu của Vật lí là gì?",
                   "Quá trình phát triển của Vật lí gồm mấy giai đoạn chính?",
                   "Thành tựu nào mở đầu cuộc cách mạng công nghiệp lần thứ nhất?",
                   "Phương pháp nào là phương pháp quan trọng nhất của Vật lí?"],
                  "1. Các dạng vận động của vật chất (chất, trường) và năng lượng · "
                  "2. Ba giai đoạn · 3. Máy hơi nước của James Watt (1765) · "
                  "4. Phương pháp thực nghiệm."))
    return o


# --------------------------------------------------------------------------- B2
def b2():
    o = unit("2", "Các quy tắc an toàn trong phòng thực hành Vật lí",
             "Nguy cơ mất an toàn – quy tắc – biển báo – xử lý sự cố",
             "2 câu trắc nghiệm (1 Biết, 1 Hiểu) · nội dung: nguy cơ khi dùng thiết bị, quy tắc an toàn, "
             "nhận biết biển báo và sử dụng thiết bị đúng cách.")
    o.append(H3("1. Các nguy cơ mất an toàn thường gặp"))
    left = bullets([
        "<b>Điện giật</b>: chạm dây trần, tay ướt, dùng điện áp cao, nối đất không tốt.",
        "<b>Cháy – nổ</b>: dùng lửa gần hóa chất dễ cháy, đun nóng bình kín.",
        "<b>Bỏng</b>: tiếp xúc vật nóng, hóa chất ăn mòn, hơi nước.",
    ])
    right = bullets([
        "<b>Hóa chất độc</b>: hít phải, dính da, nuốt phải.",
        "<b>Vỡ dụng cụ</b>: thủy tinh vỡ gây cắt, đâm.",
        "<b>Bức xạ – ánh sáng mạnh</b>: tia laser, hồ quang, đèn thủy ngân.",
        "<b>Chấn thương cơ học</b>: vật nặng rơi, kẹp tay vào giá đỡ, cháy nổ bình áp suất.",
    ])
    t = Table([[left, right]], colWidths=[W / 2 - 6, W / 2 - 6])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (0, -1), 0),
                           ("LEFTPADDING", (1, 0), (1, -1), 14),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    o.append(t)

    o.append(H3("2. Mười quy tắc an toàn – “vào phòng thí nghiệm là nhớ”"))
    rules = [
        "Đọc kĩ <b>hướng dẫn</b> và nắm rõ mục đích thí nghiệm trước khi làm.",
        "Biết vị trí và cách dùng <b>bình cứu hỏa, hộp sơ cứu, vòi rửa mắt, cầu dao điện</b>.",
        "Mặc <b>áo bảo hộ</b>, đeo <b>kính bảo hộ, găng tay</b>, khẩu trang khi cần; buộc gọn tóc dài.",
        "<b>Không ăn, uống, không nếm hay ngửi trực tiếp</b> hóa chất; không đưa tay lên mặt.",
        "<b>Không tự ý</b> làm thí nghiệm ngoài hướng dẫn; không đùa nghịch, chạy nhảy.",
        "Chỉ dùng thiết bị <b>đúng chức năng</b>; kiểm tra dây dẫn, vỏ thiết bị trước khi cắm điện.",
        "Lắp mạch ở <b>điện áp an toàn</b> (nguồn một chiều ≤ 12 V khi thực hành), tay khô, "
        "không chạm vào phần kim loại trần.",
        "Đun nóng chất lỏng: <b>không đổ đầy quá 2/3</b>, hướng miệng ống nghiệm ra xa người.",
        "<b>Ngắt nguồn – tắt công tắc</b> trước khi tháo lắp, thu dọn dụng cụ, rửa tay bằng xà phòng.",
        "<b>Báo ngay cho giáo viên</b> khi có sự cố; đổ chất thải đúng nơi quy định, không đổ vào bồn rửa.",
    ]
    o.extend(numbered(rules))
    o.extend(memo(["Nhóm 4 chữ <b>“ĐỌC – MẶC – KHÔNG – BÁO”</b>: đọc hướng dẫn, mặc đồ bảo hộ, "
                   "không ăn uống/đùa nghịch, báo giáo viên khi có sự cố.",
                   "Trước khi rời phòng: <b>tắt nguồn → thu dọn → rửa tay</b> (đúng thứ tự)."]))

    o.append(H3("3. Biển báo an toàn – nhận dạng theo hình và màu"))
    data = [["HÌNH – MÀU", "LOẠI BIỂN", "Ý NGHĨA", "VÍ DỤ"],
            ["Tam giác đều, viền đen, nền vàng", "Biển <b>cảnh báo</b>",
             "Nguy hiểm có thể xảy ra, cần chú ý", "Cảnh báo điện cao áp, cảnh báo cháy nổ, "
                                                     "cảnh báo chất độc"],
            ["Hình tròn, viền đỏ, nền trắng, gạch chéo đỏ", "Biển <b>cấm</b>",
             "Hành vi bị nghiêm cấm", "Cấm lửa, cấm hút thuốc, cấm ăn uống"],
            ["Hình tròn, nền xanh", "Biển <b>bắt buộc</b>",
             "Phải thực hiện (bảo hộ bắt buộc)", "Đeo kính bảo hộ, đeo găng tay, đội mũ"],
            ["Hình vuông/chữ nhật, nền xanh", "Biển <b>chỉ dẫn</b>",
             "Thông tin an toàn, lối thoát hiểm", "Lối ra thoát hiểm, vị trí bình cứu hỏa, "
                                                   "trạm sơ cứu"],
            ["Nền đỏ, chữ/hình trắng", "Biển <b>thiết bị chữa cháy</b>",
             "Vị trí phương tiện chữa cháy", "Bình chữa cháy, họng nước chữa cháy"]]
    o.append(table(data, [4.3 * cm, 3.0 * cm, 4.3 * cm, 5.1 * cm], size=8.2,
                     head_bg=colors.HexColor("#B3261E")))
    o.extend(memo(["<b>Vàng tam giác = cảnh báo · Đỏ tròn = cấm · Xanh tròn = bắt buộc · "
                   "Xanh vuông = chỉ dẫn.</b>",
                   "Mẹo: “<b>tam – cảnh, tròn đỏ – cấm, tròn xanh – phải, vuông xanh – chỉ</b>”."]))
    o.extend(bay(["Biển <b>cấm</b> và biển <b>bắt buộc</b> đều <b>hình tròn</b> – chỉ khác màu: "
                  "đỏ là cấm, xanh là phải làm.",
                  "“Đeo kính bảo hộ” là biển <b>bắt buộc</b> (tròn xanh), không phải cảnh báo."]))

    o.append(H3("4. Xử lý sự cố – 4 tình huống hay hỏi"))
    data = [["SỰ CỐ", "XỬ LÝ ĐÚNG"],
            ["Bị điện giật", "Ngắt nguồn ngay (cầu dao/công tắc) hoặc dùng vật cách điện khô "
                             "gạt dây ra; <b>không chạm trực tiếp</b> vào người bị nạn; gọi hỗ trợ, "
                             "sơ cứu rồi đưa đi cấp cứu."],
            ["Hóa chất dính da/mắt", "Rửa ngay bằng nhiều nước sạch liên tục 15 phút; với mắt thì "
                                     "rửa từ trong khóe mắt ra ngoài; báo giáo viên."],
            ["Cháy nhỏ trong phòng", "Ngắt điện, dùng bình chữa cháy/bình cát; <b>không dùng nước</b> "
                                     "khi cháy thiết bị điện hoặc hóa chất tan trong dầu."],
            ["Vỡ dụng cụ thủy tinh", "Không dùng tay nhặt mảnh vỡ; dùng chổi/kẹp gắp, bọc giấy báo "
                                     "và bỏ đúng nơi quy định; báo giáo viên."]]
    o.append(table(data, [4.0 * cm, 12.7 * cm], size=8.4, head_bg=colors.HexColor("#0E7C86")))
    o.extend(quiz(["Vì sao không được ăn uống trong phòng thực hành?",
                   "Biển tam giác vàng viền đen là loại biển gì?",
                   "Việc đầu tiên cần làm khi thấy bạn bị điện giật là gì?"],
                  "1. Tránh hóa chất độc lẫn vào thức ăn, gây ngộ độc · 2. Biển cảnh báo · "
                  "3. Ngắt nguồn điện ngay (không chạm trực tiếp vào người bị nạn)."))
    return o


# --------------------------------------------------------------------------- B3
def b3():
    o = unit("3", "Thực hành tính sai số trong phép đo. Ghi kết quả đo",
             "Phép đo trực tiếp – gián tiếp · sai số tuyệt đối – tỉ đối · cách ghi kết quả",
             "1 câu trắc nghiệm (Biết) + 1 ý Đúng/Sai + câu trả lời ngắn · nội dung: khái niệm phép đo, "
             "các loại sai số, công thức tính và cách ghi kết quả.")
    o.append(H3("1. Phép đo – dụng cụ đo"))
    o.append(P("<b>Phép đo</b> là so sánh một đại lượng với đại lượng cùng loại được chọn làm "
               "đơn vị. <b>Phép đo trực tiếp</b>: đọc kết quả ngay trên dụng cụ (đo chiều dài bằng "
               "thước, đo thời gian bằng đồng hồ). <b>Phép đo gián tiếp</b>: đo các đại lượng "
               "liên quan rồi tính qua công thức (đo v = s/t; đo khối lượng riêng D = m/V)."))
    o.append(P("Mỗi dụng cụ có <b>GHĐ</b> (giá trị lớn nhất đo được) và <b>ĐCNN</b> (độ dài giữa "
               "hai vạch chia liên tiếp). Khi đọc, phải ghi kết quả theo đúng ĐCNN – ví dụ thước "
               "có ĐCNN 1 mm thì ghi 12,4 cm chứ không ghi 12,43 cm."))
    o.append(H3("2. Bốn loại sai số"))
    data = [["LOẠI SAI SỐ", "NGUYÊN NHÂN / ĐẶC ĐIỂM", "CÁCH XÁC ĐỊNH"],
            ["<b>Sai số hệ thống</b> (dụng cụ)", "Do dụng cụ chế tạo không chuẩn, vạch chia lệch, "
                                                  "kim chưa về 0 – kết quả <i>lệch một phía</i>",
             "Hiệu chỉnh dụng cụ; lấy ΔA<sub>dc</sub> ≈ nửa ĐCNN (hoặc một ĐCNN)"],
            ["<b>Sai số ngẫu nhiên</b>", "Do người đo (phản xạ bấm giây, đọc lệch), điều kiện môi "
                                         "trường thay đổi – kết quả <i>lệch cả hai phía</i>",
             "Đo nhiều lần rồi lấy trung bình; tính ΔA<sub>i</sub> = |Ā − A<sub>i</sub>|"],
            ["<b>Sai số tuyệt đối</b> ΔA", "Độ lệch giữa giá trị đo và giá trị thực, <b>cùng đơn vị</b> "
                                            "với A", "ΔA = ΔA<sub>ngẫu nhiên TB</sub> + ΔA<sub>dc</sub>"],
            ["<b>Sai số tỉ đối</b> δA", "Cho biết <b>mức độ chính xác</b> của phép đo, không có đơn vị "
                                        "(%)", "δA = (ΔA / Ā).100%"]]
    o.append(table(data, [3.3 * cm, 8.4 * cm, 5.0 * cm], size=8.2))
    o.extend(memo(["<b>Tuyệt đối – có đơn vị, cộng trừ được. Tỉ đối – có %, so sánh được.</b>",
                   "δA càng <b>nhỏ</b> → phép đo càng <b>chính xác</b>.",
                   "Sai số hệ thống sửa được bằng hiệu chỉnh dụng cụ; sai số ngẫu nhiên giảm "
                   "bằng cách đo nhiều lần."]))

    o.append(H3("3. Quy trình tính sai số của phép đo trực tiếp"))
    o.extend(numbered([
        "Đo <b>n lần</b> (thường n ≥ 3), ghi các giá trị A<sub>1</sub>, A<sub>2</sub>, …, A<sub>n</sub>.",
        "Tính giá trị trung bình: <b>Ā = (A<sub>1</sub> + A<sub>2</sub> + … + A<sub>n</sub>)/n</b>.",
        "Tính sai số ngẫu nhiên tuyệt đối của từng lần: <b>ΔA<sub>i</sub> = |Ā − A<sub>i</sub>|</b>.",
        "Tính sai số ngẫu nhiên trung bình: <b>Δ̄A = (ΔA<sub>1</sub> + … + ΔA<sub>n</sub>)/n</b>.",
        "Cộng sai số dụng cụ: <b>ΔA = Δ̄A + ΔA<sub>dc</sub></b> (ΔA<sub>dc</sub> ≈ nửa ĐCNN).",
        "Ghi kết quả: <b>A = Ā ± ΔA</b> – ΔA lấy 1 hoặc 2 chữ số có nghĩa, Ā làm tròn đến "
        "cùng hàng thập phân với ΔA.",
        "Tính sai số tỉ đối: <b>δA = ΔA/Ā.100%</b>.",
    ]))
    o.append(Spacer(1, 3))
    o.extend(formula(["Ā = (A₁ + A₂ + … + Aₙ)/n",
                      "ΔA = Δ̄A + ΔA<sub>dc</sub>&nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp;"
                      "δA = (ΔA/Ā).100%",
                      "A = Ā ± ΔA&nbsp;&nbsp;&nbsp;hay&nbsp;&nbsp;&nbsp;"
                      "(Ā − ΔA) ≤ A ≤ (Ā + ΔA)"],
                     label="BỘ CÔNG THỨC BẮT BUỘC THUỘC"))
    o.extend(vd("Đo chiều dài một vật bằng thước có ĐCNN 0,1 cm, 5 lần: "
                "12,4 – 12,5 – 12,3 – 12,4 – 12,4 (cm).",
                ["<b>Bước 1.</b> Ā = (12,4 + 12,5 + 12,3 + 12,4 + 12,4)/5 = 62,0/5 = "
                 "<b>12,40 cm</b>.",
                 "<b>Bước 2.</b> ΔA<sub>i</sub> = 0,00; 0,10; 0,10; 0,00; 0,00 (cm) → "
                 "Δ̄A = 0,20/5 = <b>0,04 cm</b>.",
                 "<b>Bước 3.</b> ΔA<sub>dc</sub> = 0,05 cm (nửa ĐCNN) → ΔA = 0,04 + 0,05 = "
                 "0,09 ≈ <b>0,1 cm</b>.",
                 "<b>Bước 4.</b> δA = 0,1/12,4.100% ≈ <b>0,8%</b> → phép đo rất chính xác."],
                "Kết quả: <b>A = 12,4 ± 0,1 cm</b> hay 12,3 cm ≤ A ≤ 12,5 cm."))

    o.append(H3("4. Sai số của phép đo gián tiếp – quy tắc lan truyền"))
    data = [["PHÉP TÍNH", "CÔNG THỨC SAI SỐ", "GHI NHỚ"],
            ["Tổng / hiệu: A = B ± C", "ΔA = ΔB + ΔC",
             "Cộng <b>sai số tuyệt đối</b>"],
            ["Tích / thương: A = B.C hoặc A = B/C", "δA = δB + δC",
             "Cộng <b>sai số tỉ đối</b>"],
            ["Lũy thừa: A = B<sup>n</sup>", "δA = n.δB", "Nhân hệ số mũ"],
            ["Hệ số nhân: A = k.B", "ΔA = |k|.ΔB", "Sai số nhân theo hệ số"],
            ["Từ tỉ đối ra tuyệt đối", "ΔA = δA.Ā", "Dùng để ghi kết quả cuối"]]
    o.append(table(data, [5.6 * cm, 5.2 * cm, 5.9 * cm], size=8.4,
                     head_bg=colors.HexColor("#5B4B8A")))
    o.extend(vd("Đo tốc độ bằng v = s/t: s = 0,550 ± 0,005 m; t = 3,20 ± 0,05 s.",
                ["δs = 0,005/0,550.100% ≈ 0,91%; δt = 0,05/3,20.100% ≈ 1,56%.",
                 "δv = δs + δt ≈ 2,47% → Δv = 0,0247 × 0,172 ≈ 0,004 m/s."],
                "v = 0,172 m/s → ghi <b>v = 0,172 ± 0,004 m/s</b> (hay v ≈ 0,17 m/s, sai số 2,5%)."))
    o.extend(bay(["<b>Quên cộng sai số dụng cụ</b> – chỉ tính sai số ngẫu nhiên là thiếu bước 5.",
                  "<b>Ghi quá nhiều chữ số</b>: ΔA = 0,09 thì Ā phải là 12,40 chứ không phải "
                  "12,3982.",
                  "<b>Nhầm đơn vị khi tính δ</b>: δ là tỉ số nên <b>không có đơn vị</b>, chỉ viết %.",
                  "Với phép <b>trừ</b> hai số gần bằng nhau, sai số tỉ đối có thể rất lớn dù sai số "
                  "tuyệt đối nhỏ – cần tránh thiết kế phép đo kiểu này."]))
    o.extend(quiz(["Sai số dụng cụ thường được lấy bằng bao nhiêu ĐCNN?",
                   "Sai số tỉ đối được tính bằng công thức nào?",
                   "Phép đo nào là phép đo gián tiếp: đo chiều dài bằng thước hay đo vận tốc "
                   "bằng s/t?"],
                  "1. Nửa ĐCNN · 2. δA = (ΔA/Ā).100% · 3. Đo vận tốc bằng s/t (gián tiếp)."))
    return o


# --------------------------------------------------------------------------- B4
def b4():
    o = unit("4", "Độ dịch chuyển và quãng đường đi được",
             "Vị trí – độ dịch chuyển (vectơ) – quãng đường (vô hướng) – tổng hợp độ dịch chuyển",
             "3 câu trắc nghiệm (1 Biết, 2 Hiểu) + tự luận vận dụng · nội dung: khái niệm, so sánh, "
             "xác định và tính độ dịch chuyển, quãng đường.")
    o.append(H3("1. Hai khái niệm – một chỗ khác nhau cốt lõi"))
    o.append(P("Để xác định vị trí của vật, ta chọn một <b>vật mốc</b> và một <b>hệ trục toạ độ</b> "
               "(thường trục Ox). Vị trí của vật là toạ độ x của nó trên trục đó."))
    data = [["TIÊU CHÍ", "ĐỘ DỊCH CHUYỂN (Δd)", "QUÃNG ĐƯỜNG ĐI ĐƯỢC (s)"],
            ["Định nghĩa", "Vectơ nối vị trí đầu với vị trí cuối: "
                           "<b>Δd = d₂ − d₁</b> (độ dịch chuyển = toạ độ sau − toạ độ trước)",
             "Tổng độ dài quỹ đạo mà vật đã đi"],
            ["Bản chất", "<b>Vectơ</b> – có điểm đầu, điểm cuối, hướng, độ lớn",
             "<b>Vô hướng</b> – chỉ có độ lớn"],
            ["Dấu", "Có thể <b>dương, âm hoặc bằng 0</b> (tuỳ chiều dương)",
             "<b>Luôn ≥ 0</b>, không bao giờ âm"],
            ["Phụ thuộc", "Chỉ phụ thuộc vị trí đầu và cuối",
             "Phụ thuộc toàn bộ đường đi"],
            ["Vật quay về chỗ cũ", "Δd = 0", "s = 2 × độ dài đường đi (khác 0)"],
            ["Đơn vị", "mét (m), kilomet (km)", "mét (m), kilomet (km)"]]
    o.append(table(data, [3.2 * cm, 6.9 * cm, 6.6 * cm], size=8.3,
                     head_bg=colors.HexColor("#1B7A45")))
    o.extend(defn(["Độ dịch chuyển là một đại lượng <b>vectơ</b>; quãng đường là đại lượng "
                   "<b>vô hướng</b>. Vì vậy luôn có <b>|Δd| ≤ s</b>, dấu “=” xảy ra khi vật "
                   "chuyển động <b>thẳng và không đổi chiều</b>."]))

    o.append(H3("2. Ba dạng bài tính độ dịch chuyển"))
    o.append(P("<b>a) Chuyển động thẳng, một chiều:</b> chọn chiều dương, tính Δd = x₂ − x₁; "
               "nếu vật không đổi chiều thì |Δd| = s."))
    o.append(P("<b>b) Chuyển động thẳng có đổi chiều:</b> tính riêng từng chặng rồi cộng đại số "
               "các độ dịch chuyển; quãng đường thì cộng độ dài (luôn dương)."))
    o.append(P("<b>c) Chuyển động trong mặt phẳng (hai phương vuông góc):</b> dùng định lí Pythagore."))
    o.extend(formula(["|Δd| = √(Δx² + Δy²)&nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp;"
                      "tanα = Δy/Δx"],
                     label="TỔNG HỢP HAI ĐỘ DỊCH CHUYỂN VUÔNG GÓC"))
    o.extend(vd("Một người đi 4 km về phía bắc rồi 3 km về phía đông.",
                ["Quãng đường: s = 4 + 3 = <b>7 km</b>.",
                 "Độ dịch chuyển: hai chặng vuông góc → |Δd| = √(4² + 3²) = <b>5 km</b>, "
                 "hướng đông – bắc, lệch 37° về phía đông so với hướng bắc.",
                 "Nhận xét: |Δd| = 5 km &lt; s = 7 km → đúng với hệ thức |Δd| ≤ s."],
                "s = 7 km; |Δd| = 5 km."))
    o.extend(vd("Một vận động viên chạy 100 m theo chiều dương rồi quay lại chạy 40 m.",
                ["Chặng 1: Δd₁ = +100 m, s₁ = 100 m.",
                 "Chặng 2: Δd₂ = −40 m, s₂ = 40 m.",
                 "Tổng: Δd = 100 − 40 = <b>+60 m</b>; s = 100 + 40 = <b>140 m</b>."],
                "Độ dịch chuyển 60 m (cùng chiều ban đầu), quãng đường 140 m."))
    o.extend(memo(["<b>“Dịch chuyển nối hai đầu – quãng đường đo cả đường”</b>.",
                   "Bài cho “đi rồi quay lại” → Δd nhỏ hơn s rất nhiều; bài cho “thẳng, không "
                   "đổi chiều” → lấy |Δd| = s cho nhanh.",
                   "Trong chuyển động tròn <b>một vòng</b>: s = 2πR nhưng Δd = 0."]))
    o.extend(bay(["Nhầm <b>độ dịch chuyển</b> với <b>quãng đường</b> khi vật đổi chiều – đây là "
                  "bẫy số 1 của bài này.",
                  "Bỏ dấu khi tính Δd: nếu chọn chiều dương ngược chiều chuyển động thì Δd âm, "
                  "đó là kết quả đúng chứ không phải sai.",
                  "Cộng độ lớn khi hai chặng <b>ngược chiều</b> – phải trừ."]))
    o.extend(quiz(["Độ dịch chuyển có thể âm không? Quãng đường có thể âm không?",
                   "Vật đi 10 m về đông rồi 10 m về tây. Tính s và Δd.",
                   "Khi nào |Δd| = s?"],
                  "1. Δd có thể âm/0; s luôn ≥ 0 · 2. s = 20 m; Δd = 0 · "
                  "3. Khi vật chuyển động thẳng và không đổi chiều."))
    return o


# --------------------------------------------------------------------------- B5
def b5():
    o = unit("5", "Tốc độ và vận tốc",
             "Tốc độ trung bình – tốc độ tức thời – vận tốc – công thức cộng vận tốc",
             "1 câu Biết + 2 ý Đúng/Sai + 1 câu trắc nghiệm Hiểu + 1 ý tự luận Hiểu · nội dung: "
             "ý nghĩa và công thức tốc độ, phân biệt tốc độ – vận tốc, tổng hợp vận tốc.")
    o.append(H3("1. Tốc độ trung bình – đại lượng vô hướng"))
    o.append(P("<b>Tốc độ trung bình</b> cho biết mức độ nhanh, chậm của chuyển động, được tính "
               "bằng quãng đường đi được chia cho thời gian đi hết quãng đường đó:"))
    o.extend(formula(["v<sub>tb</sub> = s/Δt"], label="TỐC ĐỘ TRUNG BÌNH (m/s)"))
    o.append(P("Đơn vị hợp pháp: <b>m/s</b>; thực tế dùng km/h. Đổi: <b>1 m/s = 3,6 km/h</b>; "
               "1 km/h ≈ 0,278 m/s. Tốc độ trung bình <b>không</b> cho biết hướng chuyển động và "
               "nói chung <b>khác</b> trung bình cộng các tốc độ (chỉ bằng khi các đoạn có cùng "
               "thời gian)."))
    o.append(H3("2. Tốc độ tức thời"))
    o.append(P("<b>Tốc độ tức thời</b> là tốc độ tại một thời điểm (hoặc rất gần thời điểm đó), "
               "được tính với Δt rất nhỏ. Độ lớn của tốc độ tức thời chính là số chỉ trên "
               "<b>tốc kế</b> (đồng hồ đo tốc độ) của xe. Trong chuyển động thẳng đều, tốc độ "
               "tức thời bằng tốc độ trung bình trên mọi đoạn."))
    o.append(H3("3. Vận tốc – đại lượng vectơ"))
    o.extend(formula(["v = Δd/Δt"], label="VẬN TỐC TRUNG BÌNH (vectơ)"))
    data = [["TIÊU CHÍ", "TỐC ĐỘ", "VẬN TỐC"],
            ["Bản chất", "Vô hướng (chỉ độ lớn)", "Vectơ (độ lớn + hướng)"],
            ["Công thức", "v<sub>tb</sub> = s/Δt (quãng đường)", "v = Δd/Δt (độ dịch chuyển)"],
            ["Dấu", "Luôn dương hoặc 0", "Có thể âm, 0 hoặc dương"],
            ["Cho biết", "Chỉ mức nhanh chậm", "Mức nhanh chậm <b>và</b> hướng chuyển động"],
            ["Khi vật đổi chiều", "Vẫn dương", "Có thể triệt tiêu hoặc đổi dấu"]]
    o.append(table(data, [3.5 * cm, 6.4 * cm, 6.8 * cm], size=8.4,
                     head_bg=colors.HexColor("#16357A")))
    o.extend(memo(["<b>Tốc độ = “bao nhiêu mét mỗi giây”. Vận tốc = “bao nhiêu mét mỗi giây "
                   "theo hướng nào”.</b>",
                   "Trong chuyển động thẳng đều (không đổi chiều): |v| = v<sub>tb</sub>.",
                   "Trong chuyển động tròn đều: tốc độ không đổi nhưng <b>vận tốc luôn đổi</b> "
                   "vì đổi hướng."]))

    o.append(H3("4. Công thức cộng vận tốc"))
    o.append(P("Gọi vật 1 chuyển động so với vật 2, vật 2 chuyển động so với vật 3 (thường là "
               "mặt đường – hệ quy chiếu đứng yên). Khi đó: "
               "<b>v⃗₁₃ = v⃗₁₂ + v⃗₂₃</b> – vận tốc của vật 1 so với vật 3 bằng tổng vectơ vận tốc "
               "của vật 1 so với vật 2 và của vật 2 so với vật 3."))
    data = [["TRƯỜNG HỢP", "ĐỘ LỚN", "VÍ DỤ"],
            ["Cùng phương, cùng chiều", "v₁₃ = v₁₂ + v₂₃",
             "Ca nô xuôi dòng: v = v<sub>ca nô/nước</sub> + v<sub>nước/bờ</sub>"],
            ["Cùng phương, ngược chiều", "v₁₃ = |v₁₂ − v₂₃|",
             "Ca nô ngược dòng; người đi ngược chiều thang cuốn"],
            ["Vuông góc", "v₁₃ = √(v₁₂² + v₂₃²)",
             "Ca nô qua sông khi nước chảy vuông góc bờ"]]
    o.append(table(data, [4.4 * cm, 5.2 * cm, 7.1 * cm], size=8.4,
                     head_bg=colors.HexColor("#0E7C86")))
    o.extend(vd("Ca nô đi xuôi dòng 24 km trong 1 giờ. Biết vận tốc dòng nước là 4 km/h. "
                "Tính vận tốc ca nô khi nước yên lặng và khi đi ngược dòng 24 km.",
                ["Xuôi dòng: v = v<sub>cn</sub> + v<sub>n</sub> → 24 = v<sub>cn</sub> + 4 → "
                 "v<sub>cn</sub> = <b>20 km/h</b>.",
                 "Ngược dòng: v' = 20 − 4 = <b>16 km/h</b> → thời gian = 24/16 = <b>1,5 giờ</b>."],
                "v<sub>cn</sub> = 20 km/h; đi ngược dòng hết 1,5 h."))
    o.extend(vd("Một người bơi với vận tốc 3 m/s so với nước, nước chảy 4 m/s vuông góc với bờ. "
                "Tính vận tốc của người so với bờ và thời gian qua sông rộng 60 m.",
                ["v = √(3² + 4²) = <b>5 m/s</b> (hợp với bờ góc α với tanα = 3/4).",
                 "Thời gian qua sông chỉ phụ thuộc vận tốc vuông góc bờ: "
                 "t = 60/3 = <b>20 s</b>."],
                "v = 5 m/s; t = 20 s."))
    o.extend(bay(["Dùng <b>quãng đường</b> thay cho <b>độ dịch chuyển</b> khi tính vận tốc → sai "
                  "dấu và sai hướng.",
                  "Trung bình cộng hai tốc độ: chỉ đúng khi hai đoạn có <b>cùng thời gian</b>. "
                  "Nếu cùng quãng đường thì v<sub>tb</sub> = 2v₁v₂/(v₁ + v₂).",
                  "Quên rằng <b>vận tốc tương đối</b> phải cộng theo vectơ, không cộng đại số "
                  "khi khác phương."]))
    o.extend(quiz(["Đổi 54 km/h ra m/s.", "Một xe đi 120 km trong 2 h. Tốc độ trung bình?",
                   "Vật chuyển động tròn đều: tốc độ và vận tốc có đổi không?"],
                  "1. 15 m/s · 2. 60 km/h ≈ 16,7 m/s · 3. Tốc độ không đổi, vận tốc đổi hướng."))
    return o


# --------------------------------------------------------------------------- B6
def b6():
    o = unit("6", "Thực hành: Đo tốc độ của vật chuyển động",
             "Đồng hồ đo thời gian hiện số – cổng quang điện – quy trình đo – ưu nhược điểm",
             "Thuộc phần thực hành của đơn vị 2.2/2.3: câu hỏi về ưu nhược điểm của đồng hồ hiện số, "
             "cách dùng, ý nghĩa của hai cổng quang điện.")
    o.append(H3("1. Bộ thí nghiệm gồm những gì"))
    o.append(P("<b>Đồng hồ đo thời gian hiện số</b> (đếm thời gian bằng xung điện, hiển thị số), "
               "<b>hai cổng quang điện</b> (A và B – mỗi cổng có một đèn phát tia hồng ngoại và một "
               "cảm biến thu), <b>thước</b> đo quãng đường, <b>xe trượt</b> (hoặc viên bi, vật rơi), "
               "<b>giá đỡ – máng nghiêng</b>, nguồn điện."))
    o.append(P("Nguyên lí: khi vật chuyển động <b>che khuất tia hồng ngoại</b>, cảm biến phát tín "
               "hiệu → đồng hồ bắt đầu/ kết thúc đếm. Nhờ vậy thời gian được đo tự động, không phụ "
               "thuộc phản xạ bấm đồng hồ của người làm thí nghiệm."))

    o.append(H3("2. Ưu điểm và nhược điểm của đồng hồ hiện số + cổng quang điện"))
    data = [["ƯU ĐIỂM", "NHƯỢC ĐIỂM"],
            ["Đo được những <b>khoảng thời gian rất ngắn</b> (cỡ mili giây) mà bấm tay không đo được",
             "<b>Giá thành cao</b> hơn đồng hồ bấm giây thông thường"],
            ["<b>Tự động</b> ghi thời điểm bắt đầu và kết thúc → loại bỏ sai số do phản xạ của "
             "người đo", "Cần <b>nguồn điện</b>, dễ hỏng nếu va đập, ẩm"],
            ["Độ chính xác cao, kết quả hiển thị số nên <b>dễ đọc</b>, hạn chế sai số thị sai",
             "Dễ bị ảnh hưởng bởi <b>ánh sáng mạnh</b> chiếu vào cảm biến, bụi bẩn thấu kính"],
            ["Đo được nhiều chế độ: thời gian chắn một cổng, thời gian giữa hai cổng",
             "Vật phải <b>che đúng tia</b>; cổng phải đặt đúng vị trí, đúng độ cao"]]
    o.append(table(data, [8.35 * cm, 8.35 * cm], size=8.4,
                     head_bg=colors.HexColor("#0E7C86")))
    o.extend(memo(["Ưu điểm cốt lõi – nhớ một câu: <b>“nhanh, tự động, chính xác”</b>.",
                   "Nhược điểm cốt lõi: <b>“đắt, cần điện, nhạy sáng”</b>."]))

    o.append(H3("3. Ý nghĩa của việc dùng HAI cổng quang điện"))
    data = [["CÁCH BỐ TRÍ", "ĐẠI LƯỢNG ĐO ĐƯỢC", "CÔNG THỨC", "Ý NGHĨA"],
            ["Một cổng + tấm chắn sáng rộng d đặt trên vật", "Thời gian vật đi qua cổng (Δt rất nhỏ)",
             "v = d/Δt", "Đo <b>tốc độ tức thời</b> tại vị trí đặt cổng"],
            ["Hai cổng A và B cách nhau đoạn s", "Thời gian vật đi từ A đến B (Δt)",
             "v = s/Δt", "Đo <b>tốc độ trung bình</b> trên đoạn AB"]]
    o.append(table(data, [5.8 * cm, 4.6 * cm, 2.4 * cm, 3.9 * cm], size=8.3,
                     head_bg=colors.HexColor("#5B4B8A")))
    o.append(Spacer(1, 3))
    o.append(P("Dùng hai cổng cho phép xác định thời gian chuyển động <b>giữa hai vị trí xác định "
               "trước</b> mà không cần bấm giây, đồng thời kiểm tra được tính đều/không đều của "
               "chuyển động: nếu tốc độ trên các đoạn bằng nhau ngắn liên tiếp xấp xỉ bằng nhau thì "
               "có thể coi là chuyển động đều."))

    o.append(H3("4. Quy trình đo tốc độ – 6 bước"))
    o.extend(numbered([
        "Nối hai cổng quang điện vào đồng hồ; bật nguồn, chọn <b>thang đo thời gian</b> phù hợp "
        "(mili giây hoặc giây).",
        "Đặt cổng A và B trên máng, dùng thước đo khoảng cách <b>s</b> giữa hai cổng (đọc theo "
        "đúng ĐCNN).",
        "Ấn <b>RESET</b> để đồng hồ về 0; kiểm tra tia hồng ngoại của hai cổng đã thẳng hàng.",
        "Thả xe (hoặc cho vật chuyển động) qua cổng A rồi cổng B.",
        "Đọc thời gian <b>Δt</b> trên màn hình; tính <b>v = s/Δt</b>.",
        "Lặp lại <b>3 – 5 lần</b>, ghi vào bảng, tính giá trị trung bình và sai số.",
    ]))
    o.append(Spacer(1, 3))
    o.extend(vd("Đặt hai cổng cách nhau s = 0,400 m. Đồng hồ hiện Δt = 0,285 s. Tính tốc độ.",
                ["v = s/Δt = 0,400/0,285 ≈ <b>1,40 m/s</b>.",
                 "Nếu đo 3 lần được 1,40; 1,41; 1,39 m/s → v<sub>tb</sub> = 1,40 m/s, "
                 "kết quả ghi v = 1,40 ± 0,01 m/s."],
                "v ≈ 1,4 m/s."))
    o.extend(bay(["Nhầm <b>thời gian chắn một cổng</b> (đo tốc độ tức thời) với <b>thời gian đi "
                  "giữa hai cổng</b> (đo tốc độ trung bình).",
                  "Quên RESET về 0 trước mỗi lần đo → cộng dồn thời gian của lần trước.",
                  "Đặt hai cổng quá gần nhau: Δt quá nhỏ, sai số tương đối lớn."]))
    o.extend(quiz(["Vì sao dùng cổng quang điện lại chính xác hơn bấm đồng hồ bấm giây?",
                   "Hai cổng cách nhau 1 m, vật đi hết 0,5 s. Tốc độ trung bình?"],
                  "1. Vì loại bỏ sai số phản xạ của người bấm giờ, đo được khoảng thời gian rất "
                  "ngắn · 2. 2 m/s."))
    return o


# --------------------------------------------------------------------------- B7
def b7():
    o = unit("7", "Đồ thị độ dịch chuyển – thời gian",
             "Đọc đồ thị – tính tốc độ từ độ dốc – vẽ đồ thị – nhận dạng chuyển động",
             "1 câu Biết + 1 câu Hiểu + 2 ý Đúng/Sai · nội dung: mô tả chuyển động từ đồ thị, tính "
             "tốc độ từ độ dốc, xác định vị trí – vận tốc tại một thời điểm.")
    o.append(H3("1. Cách dựng đồ thị"))
    o.append(P("Trục hoành biểu diễn <b>thời gian t</b> (s), trục tung biểu diễn <b>độ dịch chuyển d</b> "
               "(m). Mỗi điểm trên đồ thị cho biết tại thời điểm t vật ở vị trí d. Các bước vẽ: "
               "(1) lập bảng giá trị (t, d); (2) chọn tỉ lệ xích hai trục; (3) xác định các điểm; "
               "(4) nối các điểm bằng đường phù hợp nhất."))
    o.extend(defn(["Trong đồ thị độ dịch chuyển – thời gian, <b>độ dốc của đường biểu diễn bằng "
                   "vận tốc</b> của vật: v = Δd/Δt. Độ dốc càng lớn → vật chuyển động càng nhanh."]))

    o.append(H3("2. Đọc đồ thị – bảng “hình dạng nói gì”"))
    data = [["HÌNH DẠNG ĐỒ THỊ d – t", "CHUYỂN ĐỘNG", "VẬN TỐC"],
            ["Đường thẳng <b>nằm ngang</b> (song song trục Ot)", "Vật <b>đứng yên</b>", "v = 0"],
            ["Đường thẳng <b>dốc lên</b>", "Thẳng đều, theo chiều dương", "v &gt; 0, không đổi"],
            ["Đường thẳng <b>dốc xuống</b>", "Thẳng đều, ngược chiều dương", "v &lt; 0, không đổi"],
            ["Đường <b>gấp khúc</b>", "Thẳng đều nhưng <b>đổi chiều</b> tại điểm gấp", "v đổi dấu"],
            ["Đường <b>cong (parabol)</b>", "Thẳng <b>biến đổi đều</b> (vận tốc thay đổi)", "v thay đổi liên tục"],
            ["Hai đường song song", "Hai vật chuyển động cùng vận tốc, cách nhau không đổi", "v₁ = v₂"]]
    o.append(table(data, [5.9 * cm, 6.2 * cm, 4.6 * cm], size=8.3,
                     head_bg=colors.HexColor("#5B4B8A")))
    o.extend(memo(["<b>“Ngang đứng yên – dốc lên đi tới – dốc xuống đi lui – gấp khúc quay đầu.”</b>",
                   "Muốn biết vật nhanh hơn: so <b>độ dốc</b>, đừng so độ cao của đường.",
                   "Giao điểm hai đồ thị = hai vật <b>gặp nhau</b> (cùng vị trí, cùng thời điểm)."]))

    o.append(H3("3. Ba dạng câu hỏi thường gặp"))
    o.append(P("<b>a) Tính vận tốc từ độ dốc:</b> chọn hai điểm (t₁, d₁) và (t₂, d₂) trên một đoạn "
               "thẳng, tính v = (d₂ − d₁)/(t₂ − t₁)."))
    o.append(P("<b>b) Xác định vị trí – vận tốc tại thời điểm t:</b> gióng từ t lên đồ thị (đọc d), "
               "và xét độ dốc của đoạn chứa thời điểm đó (đọc v)."))
    o.append(P("<b>c) Viết phương trình chuyển động:</b> từ đồ thị lấy d₀ (tung độ gốc) và v (độ dốc) "
               "→ <b>d = d₀ + v.t</b>."))
    o.extend(vd("Đồ thị d – t là đường thẳng đi qua A(0 s; 2 m) và B(4 s; 10 m).",
                ["v = (10 − 2)/(4 − 0) = <b>2 m/s</b>.",
                 "Phương trình: <b>d = 2 + 2t</b> (m).",
                 "Tại t = 3 s: d = 2 + 6 = <b>8 m</b>; quãng đường trong 4 s đầu = 8 m."],
                "v = 2 m/s; d = 2 + 2t; tại t = 3 s thì d = 8 m."))
    o.extend(vd("Đồ thị gồm: từ t = 0 đến t = 4 s vật đi từ d = 0 đến d = 8 m; từ t = 4 s đến "
                "t = 6 s vật đứng yên; từ t = 6 s đến t = 10 s vật đi về d = 0.",
                ["0 – 4 s: v₁ = 8/4 = <b>2 m/s</b> (chiều dương).",
                 "4 – 6 s: v₂ = <b>0</b>.",
                 "6 – 10 s: v₃ = (0 − 8)/4 = <b>−2 m/s</b> (ngược chiều dương).",
                 "Quãng đường cả hành trình: 8 + 0 + 8 = <b>16 m</b>; độ dịch chuyển = <b>0</b>."],
                "v lần lượt 2; 0; −2 m/s; s = 16 m; Δd = 0."))
    o.extend(bay(["Tính vận tốc bằng <b>d/t</b> thay vì Δd/Δt → sai khi đồ thị không đi qua gốc.",
                  "Nhầm <b>độ dốc</b> với <b>độ cao</b>: đường ở trên cao chưa chắc đã nhanh hơn.",
                  "Khi vật đổi chiều, quãng đường <b>không</b> bằng |d<sub>cuối</sub> − d<sub>đầu</sub>|."]))
    o.extend(quiz(["Đồ thị d – t là đường nằm ngang, vật chuyển động thế nào?",
                   "Hai đồ thị cắt nhau tại một điểm có ý nghĩa gì?",
                   "Đường cong parabol trên đồ thị d – t ứng với chuyển động gì?"],
                  "1. Vật đứng yên (v = 0) · 2. Hai vật gặp nhau · 3. Chuyển động thẳng biến đổi đều."))
    return o


# --------------------------------------------------------------------------- B8
def b8():
    o = unit("8", "Chuyển động biến đổi. Gia tốc",
             "Chuyển động biến đổi – gia tốc – quan hệ phương chiều của a và v",
             "1 câu Biết + 1 câu Hiểu · nội dung: khái niệm chuyển động biến đổi, công thức và đơn vị "
             "gia tốc, phân biệt nhanh dần – chậm dần.")
    o.append(H3("1. Chuyển động biến đổi"))
    o.append(P("<b>Chuyển động biến đổi</b> là chuyển động có vận tốc thay đổi (về độ lớn hoặc về "
               "hướng hoặc cả hai) theo thời gian. Nếu trong những khoảng thời gian bằng nhau liên "
               "tiếp, độ biến thiên vận tốc bằng nhau thì chuyển động là <b>biến đổi đều</b>."))
    o.append(P("Chuyển động tròn đều có tốc độ không đổi nhưng <b>vận tốc vẫn biến đổi</b> (vì "
               "hướng luôn thay đổi) → nó cũng là chuyển động biến đổi."))

    o.append(H3("2. Gia tốc"))
    o.extend(formula(["a = Δv/Δt = (v − v₀)/(t − t₀)"],
                     label="GIA TỐC TRUNG BÌNH (m/s²)"))
    data = [["ĐẠI LƯỢNG", "Ý NGHĨA", "ĐƠN VỊ"],
            ["Δv = v − v₀", "Độ biến thiên vận tốc (vectơ)", "m/s"],
            ["Δt = t − t₀", "Khoảng thời gian xảy ra biến thiên", "s"],
            ["a", "Gia tốc – đặc trưng cho <b>mức độ thay đổi nhanh hay chậm của vận tốc</b>", "m/s²"]]
    o.append(table(data, [4.2 * cm, 9.4 * cm, 3.0 * cm], size=8.4))
    o.append(Spacer(1, 3))
    o.append(P("<b>Gia tốc là đại lượng vectơ</b>: a⃗ = Δv⃗/Δt, có gốc tại vật, hướng cùng hướng "
               "với Δv⃗ (không phải hướng của v⃗)."))
    o.extend(memo(["Đơn vị gia tốc: <b>m/s²</b> – đọc là “mét trên giây bình phương”.",
                   "a &gt; 0 chưa chắc nhanh dần: phải so <b>dấu của a với dấu của v</b>.",
                   "1 m/s² nghĩa là mỗi giây vận tốc thay đổi 1 m/s."]))

    o.append(H3("3. Quan hệ phương – chiều giữa gia tốc và vận tốc"))
    data = [["QUAN HỆ a⃗ VÀ v⃗", "TÍNH CHẤT CHUYỂN ĐỘNG", "ĐỘ LỚN VẬN TỐC", "VÍ DỤ"],
            ["Cùng phương, <b>cùng chiều</b>", "Chuyển động <b>nhanh dần</b>", "Tăng đều",
             "Xe khởi hành, vật rơi"],
            ["Cùng phương, <b>ngược chiều</b>", "Chuyển động <b>chậm dần</b>", "Giảm đều",
             "Xe hãm phanh, ném vật lên"],
            ["<b>Vuông góc</b>", "Đổi hướng, độ lớn vận tốc không đổi", "Không đổi",
             "Chuyển động tròn đều"],
            ["a = 0", "Chuyển động <b>thẳng đều</b>", "Không đổi", "Xe chạy đều trên đường thẳng"]]
    o.append(table(data, [4.6 * cm, 4.9 * cm, 3.6 * cm, 3.6 * cm], size=8.2,
                     head_bg=colors.HexColor("#1B7A45")))
    o.extend(defn(["Quy tắc vàng: <b>a⃗ cùng chiều v⃗ → nhanh dần; a⃗ ngược chiều v⃗ → chậm dần.</b> "
                   "Trong chuyển động thẳng, chỉ cần so <b>dấu</b> của a và v (tích a.v &gt; 0 là "
                   "nhanh dần, a.v &lt; 0 là chậm dần)."]))
    o.extend(vd("Một ô tô đang chạy 10 m/s thì tăng tốc, sau 5 s đạt 20 m/s. Sau đó hãm phanh và "
                "dừng lại sau 4 s.",
                ["Giai đoạn tăng tốc: a₁ = (20 − 10)/5 = <b>+2 m/s²</b> (a cùng chiều v → nhanh dần).",
                 "Giai đoạn hãm: a₂ = (0 − 20)/4 = <b>−5 m/s²</b> (a ngược chiều v → chậm dần).",
                 "Độ lớn gia tốc khi hãm lớn hơn → vận tốc giảm nhanh hơn."],
                "a₁ = 2 m/s²; a₂ = −5 m/s²."))
    o.extend(bay(["Kết luận “a âm thì chậm dần” là <b>sai</b> khi chiều dương chọn ngược chiều "
                  "chuyển động.",
                  "Cho rằng gia tốc là “vận tốc chia thời gian” – gia tốc là <b>độ biến thiên</b> "
                  "vận tốc chia thời gian.",
                  "Nhầm <b>độ lớn gia tốc</b> với <b>độ lớn vận tốc</b>: xe chạy đều 100 km/h có "
                  "a = 0."]))
    o.extend(quiz(["Xe từ 0 lên 15 m/s trong 5 s. Tính gia tốc.",
                   "Vật chuyển động chậm dần đều thì a và v cùng dấu hay trái dấu?",
                   "Đơn vị của gia tốc?"],
                  "1. 3 m/s² · 2. Trái dấu (ngược chiều) · 3. m/s²."))
    return o


# --------------------------------------------------------------------------- B9
def b9():
    o = unit("9", "Chuyển động thẳng biến đổi đều",
             "Ba công thức cốt lõi – đồ thị vận tốc – thời gian – dạng bài hai giai đoạn",
             "2 câu Biết + 1 câu Hiểu + 4 ý Đúng/Sai + 2 câu VẬN DỤNG tự luận · đơn vị kiến thức "
             "chiếm nhiều câu nhất trong đề.")
    o.append(H3("1. Định nghĩa"))
    o.append(P("<b>Chuyển động thẳng biến đổi đều</b> là chuyển động có quỹ đạo là đường thẳng và "
               "có <b>độ lớn vận tốc</b> tăng đều hoặc giảm đều theo thời gian – tức là "
               "<b>gia tốc không đổi</b> (về độ lớn và hướng) trong suốt quá trình chuyển động."))
    o.append(P("<b>Nhanh dần đều</b>: vận tốc tăng đều (a cùng chiều v). <b>Chậm dần đều</b>: vận "
               "tốc giảm đều (a ngược chiều v). Cả hai đều có a = const."))

    o.append(H3("2. Hệ công thức – phần phải thuộc lòng nhất của chương"))
    o.extend(formula(["v = v₀ + a.t",
                      "d = v₀.t + ½.a.t²",
                      "v² − v₀² = 2.a.d",
                      "d = (v₀ + v).t/2&nbsp;&nbsp;&nbsp;(khi a = const)"],
                     label="BỐN CÔNG THỨC CHUYỂN ĐỘNG THẲNG BIẾN ĐỔI ĐỀU"))
    data = [["KÍ HIỆU", "TÊN GỌI", "ĐƠN VỊ", "DẤU CẦN LƯU Ý"],
            ["v₀", "Vận tốc ban đầu (t = 0)", "m/s", "Âm nếu vật đang đi ngược chiều dương"],
            ["v", "Vận tốc ở thời điểm t", "m/s", "Có thể âm – đó là chiều, không phải độ lớn"],
            ["a", "Gia tốc", "m/s²", "Nhanh dần: a cùng dấu v₀; chậm dần: a trái dấu v₀"],
            ["t", "Thời gian chuyển động", "s", "Luôn ≥ 0"],
            ["d", "Độ dịch chuyển", "m", "Với vật không đổi chiều: d chính là quãng đường s"]]
    o.append(table(data, [1.7 * cm, 5.4 * cm, 1.8 * cm, 7.7 * cm], size=8.3))
    o.extend(memo(["<b>“Vận tốc – Quãng đường – Không thời gian”</b>: ba công thức đầu ứng với ba "
                   "câu hỏi “cần tìm gì, biết gì”. Không có t → dùng v² − v₀² = 2ad.",
                   "Công thức số 4 (d = (v₀+v)t/2) rất nhanh khi đề cho v₀, v, t.",
                   "Quãng đường trong <b>giây thứ n</b>: Δs = v₀ + a(n − 0,5) – chỉ dùng khi a không đổi."]))

    o.append(H3("3. Đồ thị vận tốc – thời gian"))
    o.append(P("Đồ thị v – t của chuyển động thẳng biến đổi đều là một <b>đường thẳng</b>: độ dốc "
               "của đường bằng <b>gia tốc</b>; <b>diện tích</b> giữa đường biểu diễn và trục Ot "
               "bằng <b>độ dịch chuyển</b> (khi v không đổi dấu, diện tích đó bằng quãng đường)."))
    data = [["ĐỒ THỊ v – t", "Ý NGHĨA"],
            ["Đường thẳng dốc lên, cắt trục tung tại v₀ &gt; 0", "Nhanh dần đều, a &gt; 0, xuất phát "
                                                                "với vận tốc v₀"],
            ["Đường thẳng đi qua gốc toạ độ", "Nhanh dần đều từ trạng thái nghỉ (v₀ = 0)"],
            ["Đường thẳng dốc xuống", "Chậm dần đều, a &lt; 0"],
            ["Đường nằm ngang", "Thẳng đều, a = 0"],
            ["Diện tích hình thang dưới đồ thị", "Quãng đường đi được trong khoảng thời gian đó"]]
    o.append(table(data, [7.4 * cm, 9.3 * cm], size=8.4,
                     head_bg=colors.HexColor("#5B4B8A")))

    o.append(H3("4. Quy trình giải bài toán tự luận – 6 bước ăn điểm"))
    o.extend(numbered([
        "<b>Chọn chiều dương</b> và gốc thời gian (ghi rõ vào bài).",
        "<b>Viết tóm tắt</b> các đại lượng đã biết, đổi đơn vị về m/s, m, s.",
        "<b>Chọn công thức</b> phù hợp ẩn – không có t thì dùng v² − v₀² = 2ad.",
        "<b>Thay số</b> và giải; chú ý dấu của a (chậm dần → a ngược dấu v₀).",
        "<b>Kiểm tra</b> đơn vị và tính hợp lí (thời gian dương, quãng đường không âm).",
        "<b>Kết luận</b> có đơn vị; nếu đề hỏi quãng đường thì chỉ lấy |d| khi vật không đổi chiều.",
    ]))
    o.extend(vd("Một xe đang chạy 10 m/s thì hãm phanh, chuyển động chậm dần đều với a = −2 m/s². "
                "Tính thời gian và quãng đường từ lúc hãm đến khi dừng.",
                ["Chọn chiều dương là chiều chuyển động: v₀ = 10 m/s, a = −2 m/s², v = 0.",
                 "Thời gian: t = (v − v₀)/a = (0 − 10)/(−2) = <b>5 s</b>.",
                 "Quãng đường: d = 10.5 + ½.(−2).25 = 50 − 25 = <b>25 m</b> "
                 "(hoặc dùng v² − v₀² = 2ad → 0 − 100 = −4d → d = 25 m)."],
                "t = 5 s; s = 25 m."))
    o.extend(vd("Xe khởi hành từ trạng thái nghỉ, a = 2 m/s². Tính quãng đường trong 3 s đầu và "
                "trong giây thứ 4.",
                ["3 s đầu: d = ½.2.3² = <b>9 m</b>.",
                 "Trong giây thứ 4: s₄ = d(4) − d(3) = ½.2.4² − 9 = 16 − 9 = <b>7 m</b> "
                 "(kiểm tra: v₀ + a(n − 0,5) = 0 + 2.3,5 = 7 m)."],
                "9 m trong 3 s đầu; 7 m trong giây thứ 4."))
    o.extend(vd("Xe chuyển động 5 s đầu tăng tốc đều từ 0 đến 10 m/s, sau đó chạy đều 4 s. "
                "Tính tổng quãng đường.",
                ["Giai đoạn 1 (nhanh dần): a = 10/5 = 2 m/s²; s₁ = ½.2.5² = <b>25 m</b>.",
                 "Giai đoạn 2 (đều, v = 10 m/s): s₂ = 10.4 = <b>40 m</b>.",
                 "Tổng: s = 25 + 40 = <b>65 m</b>."],
                "s = 65 m."))
    o.extend(bay(["<b>Quên đổi đơn vị</b> km/h → m/s (chia 3,6) – lỗi mất điểm phổ biến nhất.",
                  "Đặt <b>a dương</b> cho chuyển động <b>chậm dần</b> → ra t và d sai dấu.",
                  "Cho rằng “dừng lại” vẫn có a – khi dừng hẳn (v = 0, phanh hết tác dụng) thì "
                  "vật đứng yên, a = 0.",
                  "Với bài có <b>đổi chiều</b> (ví dụ ném vật lên rồi rơi xuống), quãng đường ≠ độ "
                  "dịch chuyển – phải tính riêng từng chặng."]))
    o.extend(quiz(["Xe từ 0 lên 20 m/s trong 8 s. Tính gia tốc và quãng đường.",
                   "Một vật có v₀ = 5 m/s, a = 2 m/s². Vận tốc sau 3 s? Quãng đường 3 s đầu?",
                   "Công thức nào dùng khi đề không cho thời gian?"],
                  "1. a = 2,5 m/s²; s = 80 m · 2. v = 11 m/s; s = 24 m · 3. v² − v₀² = 2ad."))
    return o


# --------------------------------------------------------------------------- B10
def b10():
    o = unit("10", "Sự rơi tự do",
             "Định nghĩa – đặc điểm rơi trong không khí – công thức – bài toán rơi",
             "1 câu Biết + 2 câu Hiểu + 1 ý tự luận Hiểu · nội dung: định nghĩa, đặc điểm, công thức "
             "và phân biệt rơi tự do với rơi có lực cản.")
    o.append(H3("1. Định nghĩa"))
    o.append(P("<b>Sự rơi tự do</b> là sự rơi của một vật <b>chỉ dưới tác dụng của trọng lực</b>, "
               "bỏ qua mọi lực cản (lực cản của không khí không đáng kể). Chuyển động rơi tự do là "
               "chuyển động <b>thẳng nhanh dần đều</b> với gia tốc rơi tự do g."))
    o.append(P("<b>Đặc điểm của chuyển động rơi trong không khí:</b> phương <b>thẳng đứng</b>, "
               "chiều <b>từ trên xuống</b>; trong không khí lực cản làm các vật rơi <b>không hoàn "
               "toàn như nhau</b> – vật nhẹ, diện tích lớn (lá cây, lông chim, tờ giấy) rơi chậm "
               "hơn rõ rệt so với vật nặng, gọn (viên bi, hòn sỏi). Trong <b>chân không</b>, mọi vật "
               "rơi nhanh như nhau (thí nghiệm ống Newton với lông chim và viên bi chì)."))
    o.extend(memo(["<b>“Chỉ trọng lực – không lực cản”</b> là điều kiện để gọi là rơi tự do.",
                   "Trong chân không: mọi vật rơi như nhau, không phụ thuộc khối lượng.",
                   "g phụ thuộc vị trí: ở mặt đất g ≈ 9,8 m/s² (thường lấy 10 m/s²); càng lên cao "
                   "g càng giảm."]))

    o.append(H3("2. Các công thức của rơi tự do"))
    o.append(P("Chọn chiều dương hướng <b>xuống</b>, gốc thời gian lúc bắt đầu rơi (v₀ = 0), "
               "gốc toạ độ tại điểm thả:"))
    o.extend(formula(["v = g.t",
                      "s = ½.g.t²&nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp;h = ½.g.t²",
                      "v² = 2.g.s&nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp;v = √(2gh)",
                      "t = √(2h/g)"],
                     label="BỐN CÔNG THỨC RƠI TỰ DO (v₀ = 0)"))
    data = [["ĐẠI LƯỢNG", "CÔNG THỨC", "GHI CHÚ"],
            ["Vận tốc sau thời gian t", "v = g.t", "Tăng đều, không phụ thuộc khối lượng"],
            ["Quãng đường (độ cao) rơi sau t", "s = ½.g.t²", "Tỉ lệ với bình phương thời gian"],
            ["Thời gian rơi từ độ cao h", "t = √(2h/g)", "Không phụ thuộc khối lượng vật"],
            ["Vận tốc chạm đất", "v = √(2gh)", "Bằng vận tốc ném lên để đạt độ cao h"]]
    o.append(table(data, [6.0 * cm, 4.6 * cm, 6.1 * cm], size=8.4,
                     head_bg=colors.HexColor("#0E7C86")))
    o.append(Spacer(1, 2))
    o.append(P("<b>Mẹo tỉ lệ:</b> trong rơi tự do, quãng đường sau các khoảng thời gian bằng nhau "
               "liên tiếp tỉ lệ với <b>1 : 3 : 5 : 7 …</b> (các số lẻ liên tiếp). Quãng đường đi "
               "trong giây thứ n là Δs = g(n − 0,5)."))

    o.append(H3("3. Ba dạng bài và cách trình bày"))
    o.extend(vd("Vật rơi tự do từ độ cao 45 m, g = 10 m/s². Tính thời gian rơi và vận tốc khi "
                "chạm đất.",
                ["t = √(2h/g) = √(2.45/10) = √9 = <b>3 s</b>.",
                 "v = g.t = 10.3 = <b>30 m/s</b> (kiểm tra: √(2.10.45) = 30 m/s)."],
                "t = 3 s; v = 30 m/s."))
    o.extend(vd("Vật rơi tự do, sau 2 s đi được bao nhiêu? Trong giây thứ 3 đi thêm bao nhiêu?",
                ["s₂ = ½.10.2² = <b>20 m</b>.",
                 "s₃ = ½.10.3² = 45 m → trong giây thứ 3: 45 − 20 = <b>25 m</b>.",
                 "Kiểm tra tỉ lệ 1 : 3 : 5 → 5 m; 15 m; 25 m (đúng)."],
                "20 m trong 2 s đầu; 25 m trong giây thứ 3."))
    o.extend(vd("Từ một đỉnh tháp, vật rơi mất 4 s để chạm đất. Tính chiều cao tháp và vận tốc "
                "chạm đất (g = 9,8 m/s²).",
                ["h = ½.9,8.4² = <b>78,4 m</b>.",
                 "v = 9,8.4 = <b>39,2 m/s</b>."],
                "h = 78,4 m; v = 39,2 m/s."))
    o.extend(bay(["Gọi mọi vật rơi trong không khí là “rơi tự do” – sai khi lực cản đáng kể "
                  "(tờ giấy, lông chim).",
                  "Nghĩ vật nặng rơi nhanh hơn trong <b>chân không</b> – trong chân không mọi vật "
                  "rơi như nhau.",
                  "Dùng công thức rơi tự do cho vật được <b>ném</b> lên/xuống với v₀ ≠ 0 – phải "
                  "dùng hệ công thức chuyển động biến đổi đều.",
                  "Nhầm “quãng đường trong giây thứ 3” với “quãng đường trong 3 giây”."]))
    o.extend(quiz(["Vật rơi tự do từ 80 m, g = 10 m/s². Thời gian rơi?",
                   "Trong chân không, hòn bi chì và lông chim rơi thế nào?",
                   "Quãng đường rơi sau 1 s, 2 s, 3 s (g = 10) là bao nhiêu?"],
                  "1. t = √(2.80/10) = 4 s · 2. Rơi nhanh như nhau · 3. 5 m; 20 m; 45 m."))
    return o

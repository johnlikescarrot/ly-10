# -*- coding: utf-8 -*-
"""PHẦN A – Kiến thức cốt lõi theo đúng 9 đơn vị của ma trận + đặc tả."""
from reportlab.platypus import PageBreak
from helpers import (P, h1, h2, h3, bullets, numbered, sp, hr, callout, formula,
                     styled_table, make_dt_graph, make_vt_graph,
                     make_vector_diagram, make_path_diagram,
                     BG_TEAL, BG_ORANGE, BG_GREEN, BG_RED, BG_PURPLE, BG_YELLOW,
                     TEAL, ORANGE, GREEN, RED, PURPLE, NAVY)
from reportlab.lib.units import mm


def get_story():
    s = []
    s.append(h1("PHẦN A \u00b7 KIẾN THỨC CỐT LÕI DỄ NHỚ"))
    s.append(P("Đọc Phần A theo đúng thứ tự của ma trận: <b>Chương I \u2013 Mở đầu</b> (1.1\u20131.3) rồi "
               "<b>Chương II \u2013 Động học</b> (2.1\u20132.6). Mỗi bài đều có cùng một khung dễ học: "
               "<b>Nhớ nhanh</b> (đọc 30 giây trước khi làm bài) \u2192 <b>Hiểu đúng</b> \u2192 "
               "<b>Mẹo nhớ</b> \u2192 <b>Bẫy hay gặp</b> \u2192 <b>Ví dụ mẫu có lời giải từng bước</b>. "
               "Kí hiệu: <b>d</b> là độ dịch chuyển, <b>s</b> là quãng đường, <b>v</b> là vận tốc/tốc độ tuỳ ngữ cảnh "
               "(đề sẽ nói rõ), <b>a</b> là gia tốc, <b>t</b> là thời gian. Trong sách giáo khoa, các đại lượng vectơ "
               "được viết kèm mũi tên ở trên đầu kí hiệu; trong tài liệu này, khi cần nhấn mạnh tính vectơ sẽ ghi rõ chữ \u201cvectơ\u201d bên cạnh kí hiệu."))
    s.append(sp(2))
    s.append(callout("\u2605 Cách học Phần A hiệu quả nhất",
                     ["<b>Bước 1:</b> Che phần lời giải của ví dụ mẫu, tự làm trong 2\u20133 phút rồi mới đối chiếu.",
                      "<b>Bước 2:</b> Đọc to \u201ccâu thần chú\u201d ở mỗi bài \u2014 đó là câu sẽ cứu điểm ở câu Nhận biết.",
                      "<b>Bước 3:</b> Đánh dấu \u2717 vào \u201cBẫy hay gặp\u201d nào em từng mắc; trước ngày thi chỉ đọc lại các \u2717 đó."],
                     bg=BG_YELLOW, accent=ORANGE))
    s.append(sp(4))

    # ---------------------------------------------------------------- A1
    s.append(h2("A1 \u00b7 1.1 LÀM QUEN VỚI VẬT LÍ \u2014 <i>Ma trận: Phần I, 1 câu Biết</i>"))
    s.append(callout("NHỚ NHANH (30 giây)",
                     ["<b>Đối tượng nghiên cứu của Vật lí:</b> các dạng <b>vận động của vật chất (chất, trường)</b> và <b>năng lượng</b>.",
                      "<b>4 cuộc cách mạng công nghiệp (CMCN) \u2013 nhớ theo \u201cHơi \u2013 Điện \u2013 Tự động \u2013 Thông minh\u201d:</b> "
                      "1) máy hơi nước \u00b7 2) điện (cảm ứng điện từ) \u00b7 3) tự động hoá (điện tử, bán dẫn, vi mạch) \u00b7 4) AI, robot, Internet, nano.",
                      "<b>2 phương pháp nghiên cứu chính:</b> <b>thực nghiệm</b> và <b>mô hình</b> (SGK Kết nối tri thức nêu phương pháp thực nghiệm và phương pháp mô hình; nhiều tài liệu gọi nhóm thứ hai là lí thuyết/mô hình)."],
                     bg=BG_TEAL, accent=TEAL))
    s.append(h3("1. Đối tượng, lĩnh vực và mục tiêu"))
    s.extend(bullets([
        "Vật lí là môn <b>khoa học tự nhiên</b>. Các lĩnh vực: cơ học, điện học, điện từ học, quang học, âm học, nhiệt học, nhiệt động lực học, vật lí nguyên tử \u2013 hạt nhân, vật lí lượng tử, thuyết tương đối.",
        "Phân biệt nhanh: nghiên cứu <b>chất và sự biến đổi chất</b> \u2192 Hoá học; <b>vật sống</b> \u2192 Sinh học; <b>cấu tạo Trái Đất</b> \u2192 Địa lí/Địa chất. Gặp \u201cchuyển động, lực, năng lượng, điện, từ, ánh sáng, nhiệt\u201d \u2192 Vật lí.",
        "Mục tiêu học Vật lí: có kiến thức \u2013 kĩ năng cơ bản; vận dụng để giải quyết vấn đề học tập và đời sống; nhận biết năng lực, sở trường để định hướng nghề nghiệp.",
    ]))
    s.append(h3("2. Quá trình phát triển của Vật lí (đặc tả yêu cầu \u201cnêu được\u201d)"))
    s.append(styled_table([
        ["Giai đoạn", "Đặc trưng dễ nhớ", "Gương mặt / mốc tiêu biểu"],
        [" Cổ đại \u2192 thế kỉ XVI", "Quan sát, suy luận triết học; chưa có thí nghiệm kiểm chứng hệ thống", "Các nhà triết học Hy Lạp cổ đại"],
        ["Thế kỉ XVII \u2013 XIX: Vật lí cổ điển", "Phương pháp <b>thực nghiệm</b> ra đời; cơ học Newton, nhiệt học, điện từ học phát triển", "Galilei (cha đẻ của phương pháp thực nghiệm), Newton, Faraday (1831: cảm ứng điện từ)"],
        ["Cuối XIX \u2013 đầu XX trở đi: Vật lí hiện đại", "Khủng hoảng của vật lí cổ điển (vật đen, quang điện, cộng vận tốc) \u2192 thuyết lượng tử (Planck, 1900) và thuyết tương đối (Einstein, 1905/1916); nghiên cứu thế giới vi mô", "Planck, Einstein"],
    ], [32 * mm, 62 * mm, 62 * mm]))
    s.append(sp(2))
    s.append(h3("3. Thành tựu Vật lí \u2194 các cuộc CMCN (câu hỏi \u201cgắn mốc\u201d rất hay ra)"))
    s.append(styled_table([
        ["CMCN", "Thời điểm", "Thành tựu Vật lí nền tảng", "Đặc trưng"],
        ["Lần 1", "Thế kỉ XVIII (máy hơi nước của James Watt, 1765)", "Nhiệt học: dãn nở vì nhiệt, nhiệt động lực học", "Cơ giới hoá \u2013 thay sức người bằng máy móc"],
        ["Lần 2", "Thế kỉ XIX", "Faraday tìm ra <b>cảm ứng điện từ</b> (1831) \u2192 máy phát điện, động cơ điện", "Điện khí hoá \u2013 thiết bị dùng điện khắp nơi"],
        ["Lần 3", "Thập niên 1970, thế kỉ XX", "Điện tử, chất bán dẫn, vi mạch", "Tự động hoá quá trình sản xuất"],
        ["Lần 4", "Đầu thế kỉ XXI", "Vật lí hiện đại + công nghệ nano, vật liệu mới", "AI, robot, Internet toàn cầu, thiết bị thông minh"],
    ], [18 * mm, 38 * mm, 55 * mm, 45 * mm], align_center_cols={0}))
    s.append(callout("\u26a0 Bẫy hay gặp",
                     ["\u201cNghiên cứu về nhiệt động lực học mở đầu CMCN lần 1\u201d mới đúng; <b>cảm ứng điện từ</b> mở đầu <b>lần 2</b> \u2014 đề rất thích đổi hai mốc này cho nhau.",
                      "Galilei gắn với <b>phương pháp thực nghiệm</b>, Newton gắn với <b>cơ học cổ điển</b>; đừng gán ngược."],
                     bg=BG_RED, accent=RED))
    s.append(h3("4. Phương pháp nghiên cứu Vật lí"))
    s.append(P("<b>a) Phương pháp thực nghiệm \u2013 5 bước (thuộc lòng theo thứ tự):</b> "
               "(1) Xác định vấn đề cần nghiên cứu \u2192 (2) Quan sát, thu thập thông tin \u2192 "
               "(3) Đưa ra dự đoán (giả thuyết) \u2192 (4) Thí nghiệm kiểm tra dự đoán \u2192 (5) Kết luận. "
               "Đây cũng chính là \u201cquá trình nghiên cứu\u201d mà đặc tả yêu cầu ở mức Thông hiểu."))
    s.append(P("<b>b) Phương pháp mô hình \u2013 3 loại mô hình ở trường phổ thông:</b>"))
    s.append(styled_table([
        ["Loại mô hình", "Là gì", "Ví dụ \u201cnhìn là nhận ra\u201d"],
        ["Vật chất", "Vật thu nhỏ / phóng to của vật thật, giống vật thật ở một số đặc điểm", "Quả địa cầu; mô hình hệ Mặt Trời"],
        ["Lí thuyết", "Khái niệm thay thế vật thật để nghiên cứu", "Chất điểm; tia sáng"],
        ["Toán học", "Công thức, phương trình, đồ thị, kí hiệu", "s = v\u00b7t; đồ thị d\u2013t"],
    ], [30 * mm, 62 * mm, 64 * mm]))
    s.append(P("Các bước xây dựng mô hình: xác định đối tượng cần mô hình hoá \u2192 xây dựng mô hình (giả thuyết) \u2192 "
               "kiểm tra sự phù hợp \u2192 điều chỉnh nếu cần \u2192 kết luận. Mô hình tốt phải vừa <b>giải thích</b> được cái đã biết, "
               "vừa <b>tiên đoán</b> được cái chưa biết."))
    s.append(callout("\u2726 Ví dụ mẫu",
                     ["<b>Đề:</b> Thành tựu nào của Vật lí được coi là mở đầu cho CMCN lần thứ hai? "
                      "A. Nghiên cứu về nhiệt động lực học. &nbsp; B. Phát hiện cảm ứng điện từ. &nbsp; C. Thuyết tương đối. &nbsp; D. Công nghệ nano.",
                      "<b>Lời giải:</b> Gắn mốc \u201cHơi \u2013 Điện \u2013 Tự động \u2013 Thông minh\u201d: lần 2 = Điện \u2192 cảm ứng điện từ của Faraday (1831), cơ sở của máy phát điện và động cơ điện. <b>Đáp án B.</b>"],
                     bg=BG_GREEN, accent=GREEN))

    # ---------------------------------------------------------------- A2
    s.append(h2("A2 \u00b7 1.2 CÁC QUY TẮC AN TOÀN TRONG PHÒNG THỰC HÀNH \u2014 <i>Ma trận: Phần I, 1 Biết + 1 Hiểu</i>"))
    s.append(callout("NHỚ NHANH (30 giây)",
                     ["<b>Trước \u2013 Trong \u2013 Sau:</b> Trước: đọc hướng dẫn, kiểm tra thiết bị, chờ giáo viên cho phép. "
                      "Trong: tắt nguồn trước khi cắm/tháo, đúng điện áp định mức, dây gọn, tránh nước \u2013 chất dễ cháy gần điện, giữ khoảng cách với vật nóng / tia laser. "
                      "Sau: vệ sinh, sắp xếp, bỏ chất thải đúng nơi quy định.",
                      "<b>Biển báo đọc bằng hình + màu:</b> tròn \u2013 viền đỏ = <b>CẤM</b>; tam giác \u2013 nền vàng = <b>CẢNH BÁO NGUY HIỂM</b>; vuông \u2013 nền đỏ cam = <b>nguy hại do hoá chất</b>; chữ nhật \u2013 nền xanh/đỏ = <b>chỉ dẫn thực hiện</b>."],
                     bg=BG_TEAL, accent=TEAL))
    s.append(h3("1. Ba nhóm nguy cơ mất an toàn (đặc tả: \u201cnêu được các nguy cơ\u201d)"))
    s.append(styled_table([
        ["Nhóm nguy cơ", "Tình huống điển hình trong đề", "Hậu quả"],
        ["Nguy hiểm cho người", "Tay chạm phần kim loại của phích khi cắm; cầm vào chỗ dây sờn; rút phích bằng cách kéo dây; nhìn trực tiếp vào tia laser; đun cốc thuỷ tinh chịu nhiệt kém trên đèn cồn", "Điện giật, bỏng, hại mắt, đứt dây \u2013 hở điện"],
        ["Hỏng thiết bị đo điện", "Dùng sai thang đo, sai chức năng, điện áp vượt giới hạn cho phép, cắm lỏng lẻo gây phóng tia lửa điện", "Cháy/hỏng đồng hồ đo, chập điện"],
        ["Cháy, nổ", "Để chất dễ cháy, nước/dung dịch dẫn điện gần thiết bị điện; để thiết bị gần nguồn nhiệt; thổi miệng tắt đèn cồn; bình đun cạn nước", "Cháy nổ, nứt vỡ dụng cụ thuỷ tinh"],
    ], [32 * mm, 78 * mm, 46 * mm]))
    s.append(P("Khi dùng <b>thiết bị nhiệt và thuỷ tinh</b>: kiểm tra nứt/vỡ trước khi đun, tránh để bình cạn nước, không chạm trực tiếp vào vật nóng khi không có bảo hộ. "
               "Khi dùng <b>thiết bị quang học</b>: tránh mốc, xước, nứt vỡ, bụi bẩn vì làm lệch đường truyền sáng và sai kết quả."))
    s.append(h3("2. Biển báo \u2014 học bằng \u201chình dạng nói trước, màu sắc nói sau\u201d"))
    s.append(styled_table([
        ["Kí hiệu", "Hình dạng \u2013 màu sắc", "Ý nghĩa / ví dụ"],
        ["Cấm", "Hình tròn, viền đỏ, nền trắng (thường có gạch chéo đỏ)", "Cấm lửa; cấm ăn uống trong phòng thí nghiệm; không uống nước từ vòi thí nghiệm"],
        ["Cảnh báo khu vực nguy hiểm", "Tam giác đều, viền đen hoặc đỏ, nền vàng", "Nguy hiểm có điện; khu vực cần thận trọng"],
        ["Cảnh báo nguy hại do hoá chất", "Hình vuông, viền đen, nền đỏ cam", "Hoá chất ăn mòn / độc hại"],
        ["Chỉ dẫn thực hiện", "Hình chữ nhật, nền xanh hoặc đỏ", "Vị trí bình chữa cháy, lối thoát hiểm, hướng dẫn thao tác"],
    ], [36 * mm, 58 * mm, 62 * mm]))
    s.append(callout("\u2605 Mẹo nhớ", ["\u201c<b>Tròn đỏ cấm làm \u2013 Tam vàng coi chừng \u2013 Vuông cam hoá chất \u2013 Chữ nhật chỉ đường.</b>\u201d "
                                        "Câu hỏi Hiểu thường cho một biển báo/tình huống và hỏi ý nghĩa hoặc cách xử lí đúng \u2014 cứ bám vào hình + màu là không nhầm."],
                     bg=BG_PURPLE, accent=PURPLE))
    s.append(callout("\u2726 Ví dụ mẫu",
                     ["<b>Đề:</b> Một bạn cầm tay trần vào đoạn dây điện bị sờn vỏ rồi cắm vào ổ điện. Nguy cơ trực tiếp nhất là gì và thao tác đúng là gì?",
                      "<b>Lời giải:</b> Nguy cơ: bị <b>điện giật</b> do tiếp xúc với phần dẫn điện hở. Thao tác đúng: <b>không sử dụng</b> dây đã sờn/hỏng, báo giáo viên, tắt nguồn trước khi cắm/tháo và chỉ dùng thiết bị còn nguyên vẹn, đúng điện áp định mức."],
                     bg=BG_GREEN, accent=GREEN))

    # ---------------------------------------------------------------- A3
    s.append(h2("A3 \u00b7 1.3 SAI SỐ TRONG PHÉP ĐO. GHI KẾT QUẢ ĐO \u2014 <i>Ma trận: Phần I, 1 câu Biết (nhưng đặc tả có cả Hiểu + Vận dụng)</i>"))
    s.append(callout("NHỚ NHANH (30 giây)",
                     ["<b>Trực tiếp</b> = đọc ngay trên dụng cụ (thước, đồng hồ). <b>Gián tiếp</b> = tính qua công thức (v = s/t).",
                      "<b>Chuỗi 4 công thức không được quên:</b> giá trị trung bình \u2192 sai số từng lần \u2192 sai số tuyệt đối \u2192 sai số tỉ đối. Ghi kết quả: <b>A = \u0100 \u00b1 \u0394A</b>."],
                     bg=BG_TEAL, accent=TEAL))
    s.append(formula(
        "\u0100 = (A\u2081 + A\u2082 + \u2026 + A\u2099) / n &nbsp;&nbsp;|&nbsp;&nbsp; "
        "\u0394A\u1d62 = |\u0100 \u2212 A\u1d62| &nbsp;&nbsp;|&nbsp;&nbsp; "
        "\u0394A = \u0394\u0100 + \u0394A<sub>dc</sub> &nbsp;&nbsp;|&nbsp;&nbsp; "
        "\u03b4A = (\u0394A / \u0100) \u00d7 100%",
        "Trong đó \u0394\u0100 là trung bình cộng các \u0394A\u1d62; \u0394A<sub>dc</sub> là sai số dụng cụ (thường lấy bằng nửa độ chia nhỏ nhất \u2013 ĐCNN); \u03b4A càng nhỏ, phép đo càng chính xác."))
    s.append(h3("1. Các loại sai số và nguyên nhân"))
    s.extend(bullets([
        "<b>Sai số hệ thống:</b> do dụng cụ (điểm 0 lệch, ĐCNN) hoặc lí thuyết/mô hình chưa hoàn thiện \u2014 lặp lại giống nhau, có thể hiệu chỉnh.",
        "<b>Sai số ngẫu nhiên:</b> do thao tác, phản xạ người đo, điều kiện môi trường thay đổi \u2014 mỗi lần đo lệch khác nhau; đo nhiều lần rồi lấy trung bình sẽ giảm ảnh hưởng.",
        "<b>Nguyên nhân thường gặp:</b> đặt mắt/vạch chia lệch, bấm đồng hồ chưa khớp thời điểm, dụng cụ chưa hiệu chuẩn, gió/rung động, đọc số vội.",
        "<b>Sai số tuyệt đối</b> cho biết kết quả lệch tối đa bao nhiêu <i>đơn vị</i>; <b>sai số tỉ đối</b> cho biết độ chính xác <i>so với độ lớn</i> của đại lượng (tính theo %).",
    ]))
    s.append(h3("2. Sai số của phép đo gián tiếp \u2014 \u201cTổng/hiệu cộng tuyệt đối, tích/thương cộng tỉ đối\u201d"))
    s.append(styled_table([
        ["Dạng công thức", "Quy tắc", "Ví dụ"],
        ["A = B + C hoặc A = B \u2212 C", "\u0394A = \u0394B + \u0394C (cộng sai số <b>tuyệt đối</b>)", "Chu vi, tổng độ dài"],
        ["A = B \u00b7 C hoặc A = B / C", "\u03b4A = \u03b4B + \u03b4C (cộng sai số <b>tỉ đối</b>); sau đó \u0394A = \u03b4A \u00b7 \u0100", "v = s/t \u2192 \u03b4v = \u03b4s + \u03b4t"],
    ], [52 * mm, 62 * mm, 42 * mm]))
    s.append(h3("3. Cách ghi kết quả đo (điểm Hiểu rất hay mất oan)"))
    s.extend(bullets([
        "Ghi dạng khoảng giá trị: <b>A = \u0100 \u00b1 \u0394A</b>, nghĩa là \u0100 \u2212 \u0394A \u2264 A \u2264 \u0100 + \u0394A.",
        "<b>\u0394A</b> viết đến chữ số có nghĩa tương ứng với ĐCNN của dụng cụ; <b>\u0100</b> viết đến <b>cùng bậc thập phân</b> với \u0394A.",
        "Làm tròn: chữ số bỏ đi &lt; 5 thì giữ nguyên chữ số trước; \u2265 5 thì tăng chữ số trước lên 1.",
    ]))
    s.append(callout("\u26a0 Bẫy hay gặp",
                     ["Quên cộng <b>sai số dụng cụ</b> vào sai số tuyệt đối; nhầm \u03b4A (có %) với \u0394A (có đơn vị).",
                      "Ghi \u0100 và \u0394A lệch bậc thập phân, ví dụ 25,30 \u00b1 0,1 \u2014 phải ghi 25,3 \u00b1 0,1 hoặc 25,30 \u00b1 0,10 cho khớp."],
                     bg=BG_RED, accent=RED))
    s.append(callout("\u2726 Ví dụ mẫu (làm đúng 5 bước)",
                     ["<b>Đề:</b> Đo chiều dài 5 lần được: 25,2; 25,4; 25,3; 25,2; 25,4 (cm). Thước có ĐCNN 0,2 cm. Tính sai số và ghi kết quả.",
                      "<b>Bước 1 \u2013 Trung bình:</b> \u0100 = (25,2+25,4+25,3+25,2+25,4)/5 = 25,30 cm.",
                      "<b>Bước 2 \u2013 Sai số từng lần:</b> |25,30\u221225,2| = 0,10; 0,10; 0,00; 0,10; 0,10 (cm).",
                      "<b>Bước 3 \u2013 Sai số ngẫu nhiên trung bình:</b> \u0394\u0100 = (0,10+0,10+0+0,10+0,10)/5 = 0,08 cm.",
                      "<b>Bước 4 \u2013 Sai số tuyệt đối:</b> \u0394A<sub>dc</sub> = ĐCNN/2 = 0,10 cm \u2192 \u0394A = 0,08 + 0,10 = 0,18 cm. Sai số tỉ đối \u03b4A = 0,18/25,30 \u00d7 100% \u2248 0,71%.",
                      "<b>Bước 5 \u2013 Ghi kết quả:</b> A = (25,30 \u00b1 0,18) cm."],
                     bg=BG_GREEN, accent=GREEN))

    # ---------------------------------------------------------------- A4
    s.append(h2("A4 \u00b7 2.1 ĐỘ DỊCH CHUYỂN VÀ QUÃNG ĐƯỜNG ĐI ĐƯỢC \u2014 <i>Ma trận: Phần I, 1 Biết + 2 Hiểu (tỉ trọng cao)</i>"))
    s.append(callout("NHỚ NHANH (30 giây)",
                     ["<b>Quãng đường s:</b> độ dài quỹ đạo \u2014 đại lượng <b>vô hướng, luôn \u2265 0</b>, cộng dồn dù đổi chiều.",
                      "<b>Độ dịch chuyển d:</b> vectơ từ <b>vị trí đầu \u2192 vị trí cuối</b> \u2014 có hướng, <b>có thể dương, âm hoặc bằng 0</b>. "
                      "Chỉ khi đi thẳng một chiều không đổi hướng thì |d| = s."],
                     bg=BG_TEAL, accent=TEAL))
    s.append(make_path_diagram())
    s.append(P("<i>Hình A4.</i> Đi 30 m về phía Đông rồi 40 m về phía Bắc: quãng đường 70 m nhưng độ dịch chuyển chỉ 50 m. "
               "Đây là mô hình \u201c3\u20134\u20135\u201d sẽ gặp lại ở cộng vận tốc và rơi tự do.", "Caption"))
    s.append(styled_table([
        ["Tiêu chí", "Quãng đường (s)", "Độ dịch chuyển (d)"],
        ["Bản chất", "Vô hướng", "Vectơ (điểm đặt, phương, chiều, độ lớn)"],
        ["Dấu", "Luôn dương (bằng 0 khi đứng yên)", "Dương / âm / 0 tuỳ chiều dương đã chọn"],
        ["Phụ thuộc", "Toàn bộ đường đi thực tế", "Chỉ vị trí đầu và cuối"],
        ["Khi quay lại điểm xuất phát", "s &gt; 0", "d = 0"],
    ], [38 * mm, 59 * mm, 59 * mm]))
    s.append(P("Trên trục toạ độ: <b>d = x<sub>cuối</sub> \u2212 x<sub>đầu</sub></b>. Chọn chiều dương trước, rồi mới gán dấu: "
               "đi theo chiều dương thì d &gt; 0, ngược chiều dương thì d &lt; 0 \u2014 nhưng s vẫn cộng dương. "
               " Với đường gấp khúc vuông góc, độ lớn của d tính bằng định lí Pythagore."))
    s.append(callout("\u2605 Mẹo nhớ", ["\u201c<b>Quãng đường nhớ đường đi \u2013 Độ dịch chuyển nhớ đích đến.</b>\u201d "
                                        "Thấy chữ \u201cquay lại\u201d, \u201cvòng tròn khép kín\u201d, \u201cvề vị trí ban đầu\u201d \u2192 nghĩ ngay d = 0."],
                     bg=BG_PURPLE, accent=PURPLE))
    s.append(callout("\u2726 Ví dụ mẫu",
                     ["<b>Đề:</b> Một người đi 30 m về phía Đông, sau đó 40 m về phía Bắc. Tính quãng đường và độ lớn độ dịch chuyển.",
                      "<b>Lời giải:</b> s = 30 + 40 = 70 m. Hai đoạn vuông góc nên |d| = \u221a(30\u00b2 + 40\u00b2) = \u221a2500 = 50 m, hướng Đông \u2013 Bắc (hợp với hướng Đông một góc có tan = 40/30)."],
                     bg=BG_GREEN, accent=GREEN))

    # ---------------------------------------------------------------- A5
    s.append(h2("A5 \u00b7 2.2 TỐC ĐỘ VÀ VẬN TỐC (+ THỰC HÀNH ĐO TỐC ĐỘ) \u2014 <i>Ma trận: dàn trải cả 4 phần \u2014 bài \u201cxương sống\u201d</i>"))
    s.append(callout("NHỚ NHANH (30 giây)",
                     ["<b>Tốc độ trung bình</b> (vô hướng): v = s/t. &nbsp; <b>Vận tốc trung bình</b> (vectơ): v = d/t. &nbsp; <b>1 m/s = 3,6 km/h</b>.",
                      "<b>Cộng vận tốc:</b> vectơ v<sub>1,3</sub> = vectơ v<sub>1,2</sub> + vectơ v<sub>2,3</sub> (1 = vật, 2 = hệ quy chiếu chuyển động, 3 = hệ quy chiếu đứng yên). "
                      "Cùng phương: cộng/trừ độ lớn. Vuông góc: Pythagore."],
                     bg=BG_TEAL, accent=TEAL))
    s.append(formula("v<sub>tb</sub> (tốc độ) = s / t &nbsp;&nbsp;|&nbsp;&nbsp; "
                     "v<sub>tb</sub> (vận tốc) = \u0394d / \u0394t &nbsp;&nbsp;|&nbsp;&nbsp; "
                     "v<sub>tức thời</sub> = \u0394d/\u0394t với \u0394t rất nhỏ",
                     "Tốc độ tức thời: số chỉ tốc kế tại một thời điểm. Vận tốc tức thời: có cả độ lớn và hướng tại thời điểm đó."))
    s.append(styled_table([
        ["", "Tốc độ", "Vận tốc"],
        ["Loại đại lượng", "Vô hướng, \u2265 0", "Vectơ: gốc đặt trên vật, hướng trùng hướng của d, độ dài tỉ lệ với độ lớn"],
        ["Dùng đại lượng nào", "Quãng đường s", "Độ dịch chuyển d"],
        ["Khi đi thẳng một chiều", "Độ lớn bằng nhau: tốc độ = |vận tốc|", ""],
        ["Khi đổi chiều / quay lại", "Vẫn lớn", "Có thể nhỏ, âm hoặc bằng 0"],
    ], [34 * mm, 61 * mm, 61 * mm]))
    s.append(h3("Tổng hợp vận tốc \u2014 2 trường hợp phải thuộc"))
    s.append(styled_table([
        ["Trường hợp", "Độ lớn", "Ví dụ nhớ"],
        ["Cùng phương, cùng chiều", "v<sub>1,3</sub> = v<sub>1,2</sub> + v<sub>2,3</sub>", "Người đi cùng chiều tàu: cộng"],
        ["Cùng phương, ngược chiều", "v<sub>1,3</sub> = |v<sub>1,2</sub> \u2212 v<sub>2,3</sub>|", "Người đi ngược chiều tàu: trừ"],
        ["Vuông góc với nhau", "v<sub>1,3</sub> = \u221a(v<sub>1,2</sub>\u00b2 + v<sub>2,3</sub>\u00b2); hướng bằng tỉ số tan", "Thuyền qua sông: 3\u20134\u20135"],
    ], [42 * mm, 62 * mm, 52 * mm]))
    s.append(make_vector_diagram())
    s.append(P("<i>Hình A5.</i> Cộng hai vận tốc vuông góc: vẽ hai vectơ nối đuôi nhau, vectơ tổng là cạnh huyền.", "Caption"))
    s.append(h3("Thực hành đo tốc độ (đặc tả mục 6 \u2014 gộp vào 2.2 trong ma trận, không được bỏ)"))
    s.extend(bullets([
        "<b>Trong đời sống:</b> tốc kế trên xe, súng bắn tốc độ, đồng hồ bấm giây + thước đo. <b>Trong phòng thí nghiệm:</b> đồng hồ đo thời gian hiện số + cổng quang điện, thiết bị cần rung.",
        "<b>Đồng hồ hiện số + cổng quang điện:</b> ưu điểm \u2014 chính xác tới phần nghìn giây (0,001 s), sai số nhỏ; nhược điểm \u2014 thiết bị cồng kềnh, chi phí cao, lắp đặt cần chính xác.",
        "<b>Vì sao dùng hai cổng quang điện?</b> Cổng thứ nhất \u201cbật\u201d đồng hồ, cổng thứ hai \u201ctắt\u201d đồng hồ (chế độ A\u2194B): đo được <b>khoảng thời gian</b> đi giữa hai vị trí, loại bỏ sai số phản xạ bấm tay. Khoảng cách hai cổng chính là quãng đường s, rồi dùng v = s/t.",
        "<b>Đo tốc độ tức thời tại một cổng:</b> dùng thời gian vật chắn cổng và kích thước vật chắn (ví dụ đường kính viên bi): v \u2248 d<sub>vật</sub>/t<sub>chắn</sub> vì khoảng thời gian rất ngắn.",
        "Quy trình đo tốc độ trung bình: đo khoảng cách hai cổng \u2192 RESET đồng hồ về 0.000 \u2192 thả vật \u2192 đọc thời gian \u2192 lặp lại ít nhất 3\u20135 lần \u2192 tính v từng lần và giá trị trung bình.",
    ]))
    s.append(callout("\u26a0 Bẫy hay gặp",
                     ["Lấy <b>trung bình cộng hai tốc độ</b> khi hai đoạn đường/thời gian không bằng nhau \u2014 bắt buộc dùng tổng quãng đường / tổng thời gian.",
                      "Quên đổi đơn vị: km/h \u2194 m/s phải chia/nhân 3,6 <i>trước</i> khi thay vào công thức có gia tốc."],
                     bg=BG_RED, accent=RED))
    s.append(callout("\u2726 Ví dụ mẫu",
                     ["<b>Đề:</b> Thuyền có vận tốc 4 m/s so với nước, hướng về phía Bắc. Nước chảy 3 m/s so với bờ, hướng về phía Đông. Tìm vận tốc của thuyền so với bờ.",
                      "<b>Lời giải:</b> Hai vận tốc vuông góc: v = \u221a(4\u00b2 + 3\u00b2) = 5 m/s. Hướng hợp với hướng Bắc về phía Đông một góc \u03b1 với tan\u03b1 = 3/4 \u2192 \u03b1 \u2248 37\u00b0."],
                     bg=BG_GREEN, accent=GREEN))

    # ---------------------------------------------------------------- A6
    s.append(h2("A6 \u00b7 2.3 ĐỒ THỊ ĐỘ DỊCH CHUYỂN \u2013 THỜI GIAN (d\u2013t) \u2014 <i>Ma trận: Phần I 1B+1H, Phần II Câu 1 (2 ý)</i>"))
    s.append(callout("NHỚ NHANH (30 giây)",
                     ["<b>Độ dốc = vận tốc:</b> v = \u0394d/\u0394t. Dốc càng dốc \u2192 vận tốc càng lớn; dốc lên \u2192 chiều dương; dốc xuống \u2192 ngược chiều dương; <b>nằm ngang \u2192 đứng yên (v = 0)</b>.",
                      "Phương trình đoạn thẳng: <b>d = d\u2080 + v\u00b7t</b> (d\u2080 là vị trí tại t = 0, đọc ở giao điểm với trục d)."],
                     bg=BG_TEAL, accent=TEAL))
    s.append(make_dt_graph([(0, 0), (10, 40), (15, 40)], x_ticks=[(10, "10"), (15, "15")], y_ticks=[(40, "40")]))
    s.append(P("<i>Hình A6.</i> 0\u201310 s: đi theo chiều dương với v = 40/10 = 4 m/s. 10\u201315 s: đồ thị nằm ngang, vật đứng yên tại d = 40 m.", "Caption"))
    s.append(styled_table([
        ["Dáng đồ thị d\u2013t", "Chuyển động tương ứng", "Vận tốc"],
        ["Đoạn thẳng dốc lên", "Thẳng đều theo chiều dương", "v &gt; 0, bằng độ dốc"],
        ["Đoạn thẳng dốc xuống", "Thẳng đều ngược chiều dương", "v &lt; 0"],
        ["Đoạn nằm ngang", "Đứng yên", "v = 0"],
        ["Đường cong", "Chuyển động không đều (vận tốc thay đổi)", "Vận tốc tức thời = độ dốc tiếp tuyến"],
        ["Hai đồ thị cắt nhau", "Hai vật ở cùng vị trí tại thời điểm đó", "Đọc toạ độ giao điểm \u2192 vị trí + thời điểm gặp nhau"],
    ], [42 * mm, 62 * mm, 52 * mm]))
    s.append(callout("\u2605 Mẹo nhớ", ["\u201c<b>Đọc đồ thị d\u2013t bằng 3 câu: Bắt đầu ở đâu (d\u2080)? Dốc về phía nào? Dốc bao nhiêu (v)?</b>\u201d "
                                        "Trả lời đủ 3 câu là giải xong hầu hết câu hỏi đồ thị. Đừng nhầm với đồ thị v\u2013t (ở A8, diện tích mới là độ dịch chuyển)."],
                     bg=BG_PURPLE, accent=PURPLE))
    s.append(callout("\u2726 Ví dụ mẫu",
                     ["<b>Đề:</b> Đồ thị d\u2013t đi qua hai điểm (10 s; 20 m) và (25 s; 50 m). Tính vận tốc.",
                      "<b>Lời giải:</b> v = \u0394d/\u0394t = (50 \u2212 20)/(25 \u2212 10) = 30/15 = 2 m/s. Dấu dương \u2192 vật chuyển động theo chiều dương."],
                     bg=BG_GREEN, accent=GREEN))

    # ---------------------------------------------------------------- A7
    s.append(h2("A7 \u00b7 2.4 CHUYỂN ĐỘNG BIẾN ĐỔI. GIA TỐC \u2014 <i>Ma trận: Phần I, 1 Biết + 1 Hiểu</i>"))
    s.append(callout("NHỚ NHANH (30 giây)",
                     ["Chuyển động có <b>vận tốc thay đổi</b> = chuyển động biến đổi. Gia tốc cho biết vận tốc thay đổi <b>nhanh hay chậm</b>: <b>a = \u0394v/\u0394t</b>, đơn vị <b>m/s\u00b2</b>, là đại lượng <b>vectơ</b>.",
                      "<b>a\u00b7v &gt; 0</b> (cùng dấu/cùng chiều) \u2192 <b>nhanh dần</b>; <b>a\u00b7v &lt; 0</b> (ngược dấu) \u2192 <b>chậm dần</b>. Nhanh/chậm nhìn vào <i>độ lớn</i> của vận tốc, không nhìn dấu của a đơn độc."],
                     bg=BG_TEAL, accent=TEAL))
    s.append(formula("a = \u0394v / \u0394t = (v<sub>t</sub> \u2212 v\u2080) / (t \u2212 t\u2080)",
                     "\u0394v là độ biến thiên vận tốc (m/s), \u0394t là khoảng thời gian biến thiên (s). Gia tốc tức thời lấy \u0394t rất nhỏ."))
    s.extend(bullets([
        "<b>Phương của gia tốc:</b> vectơ gia tốc cùng phương với vectơ độ biến thiên vận tốc \u0394v. Trong chuyển động thẳng, a cùng chiều chuyển động khi nhanh dần, ngược chiều khi chậm dần.",
        "Ví dụ đời sống: xe xuất phát / tăng ga \u2192 nhanh dần; phanh \u2192 chậm dần; xe chạy thẳng đều \u2192 a = 0 dù vận tốc khác 0.",
        "<b>Phân biệt \u0394v và a:</b> \u0394v có đơn vị m/s, a có đơn vị m/s\u00b2 \u2014 kiểm tra đơn vị là cách tự soát nhanh nhất.",
    ]))
    s.append(callout("\u26a0 Bẫy hay gặp",
                     ["\u201ca &lt; 0 nên chuyển động chậm dần\u201d là <b>chưa đủ</b>: nếu v cũng âm (đang đi ngược chiều dương) mà |v| tăng thì vẫn là nhanh dần. Phải xét dấu của <b>cả a và v</b> (hoặc xét |v| tăng/giảm).",
                      "Gia tốc lớn không có nghĩa là vận tốc lớn \u2014 chỉ có nghĩa là vận tốc <i>thay đổi nhanh</i>."],
                     bg=BG_RED, accent=RED))
    s.append(callout("\u2726 Ví dụ mẫu",
                     ["<b>Đề:</b> Xe tăng vận tốc từ 5 m/s lên 15 m/s trong 5 s. Tính gia tốc và cho biết tính chất chuyển động.",
                      "<b>Lời giải:</b> \u0394v = 15 \u2212 5 = 10 m/s; a = 10/5 = 2 m/s\u00b2. Vận tốc tăng \u2192 chuyển động nhanh dần, a cùng chiều vận tốc."],
                     bg=BG_GREEN, accent=GREEN))

    # ---------------------------------------------------------------- A8
    s.append(h2("A8 \u00b7 2.5 CHUYỂN ĐỘNG THẲNG BIẾN ĐỔI ĐỀU (CĐTBĐĐ) \u2014 <i>Ma trận: 9/31 mục chấm \u2014 TRỌNG TÂM SỐ 1, phải học kĩ nhất</i>"))
    s.append(callout("NHỚ NHANH (30 giây) \u2014 thuộc 4 công thức này là có điểm cả Phần I, II và IV",
                     ["<b>(1) v = v\u2080 + a\u00b7t</b> &nbsp; <b>(2) d = v\u2080t + \u00bda\u00b7t\u00b2</b> &nbsp; <b>(3) v\u00b2 \u2212 v\u2080\u00b2 = 2a\u00b7d</b> &nbsp; <b>(4) d = (v\u2080+v)/2 \u00b7 t</b>",
                      "Định nghĩa: chuyển động <b>thẳng</b>, <b>gia tốc không đổi</b> theo thời gian. Nhanh dần đều: |v| tăng đều; chậm dần đều: |v| giảm đều tới 0 (rồi có thể đổi chiều nếu vẫn còn gia tốc)."],
                     bg=BG_TEAL, accent=TEAL))
    s.append(styled_table([
        ["Công thức", "Dùng khi", "Thiếu / thừa ẩn nào"],
        ["v = v\u2080 + at", "Tìm vận tốc tại thời điểm t", "Chưa biết d"],
        ["d = v\u2080t + \u00bdat\u00b2", "Tìm độ dịch chuyển / quãng đường (đi một chiều) theo thời gian", "Chưa biết v cuối"],
        ["v\u00b2 \u2212 v\u2080\u00b2 = 2ad", "\u201cCông thức không chứa t\u201d \u2013 tìm v, a hoặc d khi không cho/không hỏi thời gian", "Không có t"],
        ["d = (v\u2080 + v)/2 \u00b7 t", "Tìm nhanh d khi biết hai đầu vận tốc (vận tốc trung bình của CĐTBĐĐ)", "Tiện khi đã có v"],
    ], [48 * mm, 58 * mm, 50 * mm]))
    s.append(P("Phương trình toạ độ: <b>x = x\u2080 + v\u2080t + \u00bdat\u00b2</b>. Đồ thị <b>v\u2013t</b> của CĐTBĐĐ là đoạn thẳng: "
               "<b>độ dốc của v\u2013t = gia tốc</b>, <b>diện tích dưới v\u2013t = độ dịch chuyển</b> (hình thang / tam giác / chữ nhật tuỳ trường hợp)."))
    s.append(make_vt_graph(5, 13, 4))
    s.append(P("<i>Hình A8.</i> Đồ thị v\u2013t với v\u2080 = 5 m/s, v = 13 m/s sau 4 s: độ dốc a = (13\u22125)/4 = 2 m/s\u00b2; "
               "diện tích hình thang = (5+13)/2 \u00d7 4 = 36 m = độ dịch chuyển.", "Caption"))
    s.append(h3("Quy trình 4 bước giải mọi bài CĐTBĐĐ (dán lên bàn học)"))
    s.extend(numbered([
        "<b>Chọn chiều dương</b> (thường là chiều chuyển động ban đầu) và gốc thời gian; ghi rõ v\u2080, a kèm <b>dấu</b>.",
        "<b>Đổi đơn vị</b> về m, s, m/s (km/h \u00f7 3,6) <i>trước</i> khi tính.",
        "<b>Chọn công thức theo ẩn thiếu:</b> thiếu d dùng (1); thiếu v dùng (2); thiếu t dùng (3).",
        "<b>Kiểm tra hợp lí:</b> chậm dần thì v phải giảm; đã dừng (v = 0) thì không \u201cđi tiếp\u201d với cùng công thức nếu bài chỉ xét tới lúc dừng; quãng đường khi đổi chiều phải tách giai đoạn.",
    ]))
    s.append(callout("\u26a0 Bẫy hay gặp (mất điểm nhiều nhất ở bài này)",
                     ["<b>Quãng đường \u2260 độ dịch chuyển</b> khi vật đổi chiều trong CĐTBĐĐ \u2014 phải tách tại thời điểm v = 0.",
                      "Chậm dần đều tới khi dừng: dùng v = 0 để tìm thời gian dừng t = \u2212v\u2080/a, đừng để t âm hoặc v âm \u201csống sót\u201d vô lí.",
                      "Nhầm \u00bdat\u00b2 thành at\u00b2 (thiếu \u00bd) \u2014 đây là ý Sai kinh điển trong Phần II."],
                     bg=BG_RED, accent=RED))
    s.append(callout("\u2726 Ví dụ mẫu",
                     ["<b>Đề:</b> Vật có v\u2080 = 5 m/s, gia tốc a = 2 m/s\u00b2. Sau 4 s, tìm vận tốc và độ dịch chuyển.",
                      "<b>Lời giải:</b> v = 5 + 2\u00b74 = 13 m/s. d = 5\u00b74 + \u00bd\u00b72\u00b74\u00b2 = 20 + 16 = 36 m. Kiểm tra bằng (4): d = (5+13)/2 \u00d7 4 = 36 m \u2713."],
                     bg=BG_GREEN, accent=GREEN))

    # ---------------------------------------------------------------- A9
    s.append(h2("A9 \u00b7 2.6 SỰ RƠI TỰ DO \u2014 <i>Ma trận: Phần I 1B+2H, Phần III 1 câu Hiểu</i>"))
    s.append(callout("NHỚ NHANH (30 giây)",
                     ["<b>Rơi tự do = rơi chỉ dưới tác dụng của trọng lực</b> (bỏ qua sức cản không khí). Là CĐTBĐĐ đặc biệt: <b>v\u2080 = 0, a = g \u2248 9,8 m/s\u00b2</b> (bài tập thường cho g = 10 m/s\u00b2 \u2014 đọc kĩ đề), chiều hướng xuống.",
                      "<b>3 công thức:</b> v = g\u00b7t &nbsp;|&nbsp; s = \u00bdg\u00b7t\u00b2 &nbsp;|&nbsp; v\u00b2 = 2g\u00b7s. Từ độ cao h: thời gian chạm đất t = \u221a(2h/g), vận tốc chạm đất v = \u221a(2gh)."],
                     bg=BG_TEAL, accent=TEAL))
    s.extend(bullets([
        "<b>Rơi trong không khí:</b> vật còn chịu sức cản. Lông chim, lá, dù rơi chậm không phải rơi tự do; viên bi thép, hòn đá nhỏ rơi trong ống chân không (thí nghiệm ống Newton) mới gần đúng là rơi tự do. Cùng một nơi, mọi vật rơi tự do với <b>cùng gia tốc g</b> \u2014 không phụ thuộc khối lượng.",
        "g phụ thuộc vĩ độ và độ cao; gần mặt đất lấy g \u2248 9,8 m/s\u00b2. Đề cho g = 10 m/s\u00b2 thì phải dùng 10 cho cả bài, không trộn 9,8.",
        "<b>Quãng đường trong giây thứ n:</b> \u0394s<sub>n</sub> = s(n) \u2212 s(n\u22121) = \u00bdg(2n \u2212 1). Với g = 10: các giây liên tiếp đi được 5 \u2013 15 \u2013 25 \u2013 35 m\u2026 (lẻ tăng dần) \u2014 mẹo kiểm tra đáp án cực nhanh.",
        "Rơi tự do là nhanh dần đều: trong mỗi giây, vận tốc tăng thêm đúng g (khoảng 9,8 m/s).",
    ]))
    s.append(callout("\u26a0 Bẫy hay gặp",
                     ["Vật <b>ném xuống</b> có v\u2080 \u2260 0 thì không dùng v = gt / s = \u00bdgt\u00b2 nguyên dạng \u2014 phải dùng công thức CĐTBĐĐ đầy đủ với v\u2080 đó và a = g.",
                      "\u201cVật nặng rơi nhanh hơn vật nhẹ\u201d là <b>sai</b> trong rơi tự do (chỉ đúng khi sức cản đáng kể trong không khí)."],
                     bg=BG_RED, accent=RED))
    s.append(callout("\u2726 Ví dụ mẫu",
                     ["<b>Đề:</b> Thả rơi tự do một vật từ độ cao 80 m, lấy g = 10 m/s\u00b2. Tìm thời gian rơi và vận tốc khi chạm đất.",
                      "<b>Lời giải:</b> t = \u221a(2h/g) = \u221a(160/10) = \u221a16 = 4 s. v = g\u00b7t = 10\u00b74 = 40 m/s (kiểm tra: v = \u221a(2\u00b710\u00b780) = \u221a1600 = 40 m/s \u2713)."],
                     bg=BG_GREEN, accent=GREEN))
    s.append(sp(2))
    s.append(callout("\u2713 Tự kiểm tra cuối Phần A (che đáp án ở Phần B\u2013C, tự trả lời miệng)",
                     ["1) Nói được đối tượng nghiên cứu của Vật lí và thứ tự \u201cHơi \u2013 Điện \u2013 Tự động \u2013 Thông minh\u201d chưa?",
                      "2) Phân biệt được s và d, tốc độ và vận tốc trong trường hợp vật quay đầu chưa?",
                      "3) Thuộc 4 công thức CĐTBĐĐ và 3 công thức rơi tự do, biết chọn công thức theo \u201cẩn thiếu\u201d chưa?",
                      "Nếu còn \u201cchưa\u201d ở câu nào, quay lại đúng bài A đó đọc lại hộp NHỚ NHANH rồi mới sang Phần B."],
                     bg=BG_YELLOW, accent=ORANGE))
    return s

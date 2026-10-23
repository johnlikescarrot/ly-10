# -*- coding: utf-8 -*-
"""PHẦN C – Ngân hàng luyện thêm theo đơn vị; PHẦN D – Tổng ôn; Phụ lục đối chiếu."""
from helpers import (P, h1, h2, h3, sp, callout, styled_table, question,
                     BG_TEAL, BG_GREEN, BG_YELLOW, BG_PURPLE, TEAL, GREEN, ORANGE, PURPLE)
from reportlab.lib.units import mm


def _unit_bank(title, questions, answers):
    """questions: list of (stem, options). answers: list of (key, explain)."""
    out = [h3(title)]
    for i, (stem, opts) in enumerate(questions, 1):
        out.append(question(f"LT{i}", stem, opts))
        out.append(sp(1))
    keys = " \u00b7 ".join([f"LT{i}: <b>{a[0]}</b>" for i, a in enumerate(answers, 1)])
    out.append(callout("Đáp án nhanh", [keys] + [f"<b>LT{i}.</b> {a[1]}" for i, a in enumerate(answers, 1)],
                       bg=BG_GREEN, accent=GREEN))
    out.append(sp(3))
    return out


def get_story():
    s = []
    s.append(h1("PHẦN C \u00b7 NGÂN HÀNG CÂU HỎI LUYỆN THÊM THEO ĐƠN VỊ (CÓ ĐÁP ÁN)"))
    s.append(P("Phần C không lặp lại đề mẫu: mỗi đơn vị có thêm 3\u20134 câu \u201cđổi vỏ\u201d để kiểm tra em hiểu bản chất hay chỉ nhớ đáp án. "
               "Hãy làm hết một đơn vị rồi mới mở hộp <b>Đáp án nhanh</b> ngay dưới đơn vị đó. Kí hiệu LT = luyện thêm."))
    s.append(sp(2))

    s.extend(_unit_bank("C1 \u00b7 1.1 Làm quen với Vật lí", [
        ("Bước thứ ba của phương pháp thực nghiệm là", ["xác định vấn đề cần nghiên cứu.", "quan sát, thu thập thông tin.",
         "đưa ra dự đoán.", "kết luận."]),
        ("Việc coi một ô tô chạy trên đường dài là một chất điểm thuộc loại mô hình nào?",
         ["Mô hình vật chất.", "Mô hình lí thuyết.", "Mô hình toán học.", "Không phải mô hình."]),
        ("Đặc trưng của cuộc cách mạng công nghiệp lần thứ ba là",
         ["sử dụng máy hơi nước.", "sử dụng rộng rãi thiết bị dùng điện.",
          "tự động hoá nhờ điện tử, chất bán dẫn và vi mạch.", "sử dụng trí tuệ nhân tạo và robot."]),
    ], [
        ("C", "Thứ tự 5 bước: vấn đề \u2192 quan sát \u2192 <b>dự đoán</b> \u2192 thí nghiệm kiểm tra \u2192 kết luận."),
        ("B", "Chất điểm, tia sáng là mô hình <b>lí thuyết</b>; quả địa cầu là vật chất; công thức/đồ thị là toán học."),
        ("C", "Lần 3 (thập niên 1970): tự động hoá. Lần 1 hơi nước, lần 2 điện, lần 4 AI/robot/nano."),
    ]))

    s.extend(_unit_bank("C2 \u00b7 1.2 An toàn trong phòng thực hành", [
        ("Hành động nào sau đây <b>không</b> đúng quy tắc an toàn?",
         ["Kiểm tra thiết bị trước khi sử dụng.", "Chỉ tiến hành thí nghiệm khi được giáo viên cho phép.",
          "Để nước và dung dịch dễ cháy gần thiết bị điện cho tiện thao tác.", "Tắt nguồn trước khi cắm hoặc tháo thiết bị điện."]),
        ("Kí hiệu hình vuông, viền đen, nền đỏ cam cảnh báo điều gì?",
         ["Máy hơi nước.", "Nguy hại do hoá chất gây ra.", "Lối thoát hiểm.", "Khu vực cấm lửa."]),
        ("Để tránh làm hỏng thiết bị đo điện, người làm thí nghiệm cần",
         ["chọn bất kì thang đo nào rồi điều chỉnh sau.", "dùng điện áp cao hơn định mức để đo cho rõ.",
          "quan sát kí hiệu, thông số và chọn đúng thang đo, đúng chức năng.", "cắm lỏng lẻo để dễ rút ra."]),
    ], [
        ("C", "Nước/dung dịch dẫn điện và chất dễ cháy phải <b>tránh xa</b> thiết bị điện \u2014 đây là nguy cơ chập cháy."),
        ("B", "\u201cVuông cam hoá chất\u201d. Tam giác vàng = khu vực nguy hiểm; tròn đỏ = cấm; chữ nhật = chỉ dẫn."),
        ("C", "Sai thang đo/sai chức năng/quá điện áp là nguyên nhân chính gây hỏng thiết bị đo điện."),
    ]))

    s.extend(_unit_bank("C3 \u00b7 1.3 Sai số trong phép đo", [
        ("Phép đo nào sau đây là phép đo <b>trực tiếp</b>?",
         ["Dùng thước đo chiều dài của bàn.", "Tính tốc độ bằng v = s/t.", "Tính diện tích bằng dài \u00d7 rộng.", "Tính gia tốc bằng a = \u0394v/\u0394t."]),
        ("Nguyên nhân nào gây ra chủ yếu <b>sai số ngẫu nhiên</b>?",
         ["Thước bị lệch điểm 0.", "Độ chia nhỏ nhất của dụng cụ.", "Người đo bấm đồng hồ chưa khớp với thời điểm vật bắt đầu chuyển động.", "Công thức lí thuyết chưa chính xác."]),
        ("Đo một đại lượng 4 lần được 10,0; 10,2; 10,1; 10,1 (đơn vị). Giá trị trung bình là",
         ["10,0.", "10,1.", "10,2.", "10,4."]),
        ("Kết quả đo được tính là \u0100 = 25,30 cm và \u0394A = 0,18 cm. Cách ghi đúng là",
         ["A = (25,3 \u00b1 0,18) cm.", "A = (25,30 \u00b1 0,2) cm.", "A = (25,30 \u00b1 0,18) cm.", "A = (25 \u00b1 0,18) cm."]),
    ], [
        ("A", "Đọc kết quả ngay trên dụng cụ = trực tiếp; phải qua công thức = gián tiếp."),
        ("C", "Bấm chưa khớp do phản xạ/thao tác \u2192 mỗi lần lệch khác nhau \u2192 ngẫu nhiên. Lệch điểm 0 và ĐCNN thuộc về dụng cụ/hệ thống."),
        ("B", "(10,0+10,2+10,1+10,1)/4 = 40,4/4 = 10,1."),
        ("C", "\u0100 và \u0394A phải <b>cùng bậc thập phân</b>: 25,30 \u00b1 0,18."),
    ]))

    s.extend(_unit_bank("C4 \u00b7 2.1 Độ dịch chuyển và quãng đường", [
        ("Một bạn đi một vòng quanh sân hình vuông cạnh 10 m rồi về đúng chỗ xuất phát. Quãng đường và độ lớn độ dịch chuyển là",
         ["s = 40 m; |d| = 40 m.", "s = 40 m; |d| = 0.", "s = 0; |d| = 40 m.", "s = 10 m; |d| = 0."]),
        ("Quãng đường bằng độ lớn độ dịch chuyển khi vật",
         ["đi theo đường cong.", "đi thẳng và đổi chiều nhiều lần.", "đi thẳng theo một chiều, không đổi chiều chuyển động.", "quay về điểm xuất phát."]),
        ("Một vật ở toạ độ x\u2081 = 7 m, chuyển động đến toạ độ x\u2082 = 2 m trên trục Ox. Độ dịch chuyển của vật là",
         ["9 m.", "5 m.", "\u22125 m.", "\u22129 m."]),
    ], [
        ("B", "Đi hết chu vi 4\u00d710 = 40 m nhưng đầu = cuối nên d = 0."),
        ("C", "Chỉ khi không đổi chiều thì đường đi \u201cgập\u201d trùng với đoạn đầu\u2013cuối."),
        ("C", "d = x\u2082 \u2212 x\u2081 = 2 \u2212 7 = \u22125 m; dấu âm vì đi ngược chiều dương."),
    ]))

    s.extend(_unit_bank("C5 \u00b7 2.2 Tốc độ, vận tốc và đo tốc độ", [
        ("Đổi 72 km/h ra m/s được", ["10 m/s.", "15 m/s.", "20 m/s.", "25 m/s."]),
        ("Một xe đi 30 km trong 1 h, sau đó đi tiếp 30 km trong 0,5 h. Tốc độ trung bình trên cả hành trình là",
         ["45 km/h.", "40 km/h.", "50 km/h.", "60 km/h."]),
        ("Một người đi trên tàu với vận tốc 2 m/s <b>ngược</b> chiều tàu chạy. Tàu có vận tốc 10 m/s so với mặt đất. "
         "Vận tốc của người so với mặt đất là", ["12 m/s.", "10 m/s.", "8 m/s.", "2 m/s."]),
        ("Khi dùng đồng hồ đo thời gian hiện số với hai cổng quang điện (chế độ A\u2194B), hai cổng có vai trò là",
         ["cả hai cổng cùng bật đồng hồ để đo hai lần.",
          "cổng thứ nhất bật đồng hồ, cổng thứ hai tắt đồng hồ, đo khoảng thời gian đi giữa hai cổng.",
          "một cổng đo quãng đường, một cổng đo vận tốc.",
          "hai cổng chỉ để giữ máng thí nghiệm cố định."]),
    ], [
        ("C", "72 \u00f7 3,6 = 20 m/s."),
        ("B", "v = tổng s / tổng t = 60/1,5 = 40 km/h. Trung bình cộng (30+60)/2 = 45 là bẫy vì hai đoạn khác thời gian."),
        ("C", "Ngược chiều nên trừ: 10 \u2212 2 = 8 m/s (cùng chiều chuyển động của tàu)."),
        ("B", "Đó là ý nghĩa của hai cổng: loại bỏ sai số bấm tay, thời gian đo chính xác tới 0,001 s."),
    ]))

    s.extend(_unit_bank("C6 \u00b7 2.3 Đồ thị độ dịch chuyển \u2013 thời gian", [
        ("Đồ thị d\u2013t là đoạn thẳng dốc <b>xuống</b>. Vật đang",
         ["chuyển động theo chiều dương.", "chuyển động ngược chiều dương.", "đứng yên.", "chuyển động nhanh dần đều."]),
        ("Đồ thị d\u2013t đi qua (0 s; 60 m) và (6 s; 0 m). Vận tốc của vật là",
         ["10 m/s.", "6 m/s.", "\u22126 m/s.", "\u221210 m/s."]),
        ("Hai đồ thị d\u2013t của hai vật cắt nhau tại một điểm. Điểm cắt cho biết hai vật",
         ["có cùng vận tốc.", "ở cùng một vị trí tại cùng một thời điểm.", "đi được cùng quãng đường từ lúc xuất phát.", "cùng đứng yên."]),
    ], [
        ("B", "Dốc xuống: d giảm theo t \u2192 ngược chiều dương (v &lt; 0)."),
        ("D", "v = (0 \u2212 60)/(6 \u2212 0) = \u221210 m/s."),
        ("B", "Cùng d tại cùng t = gặp nhau ở cùng vị trí; vận tốc (độ dốc) của hai đồ thị có thể khác nhau."),
    ]))

    s.extend(_unit_bank("C7 \u00b7 2.4 Chuyển động biến đổi. Gia tốc", [
        ("Một vật giảm vận tốc từ 20 m/s xuống 8 m/s trong 3 s. Gia tốc và tính chất chuyển động là",
         ["a = 4 m/s\u00b2; nhanh dần.", "a = \u22124 m/s\u00b2; chậm dần.", "a = \u22124 m/s\u00b2; nhanh dần.", "a = 12 m/s\u00b2; chậm dần."]),
        ("Chuyển động thẳng là <b>nhanh dần</b> khi",
         ["a &gt; 0.", "a &lt; 0.", "vectơ gia tốc cùng chiều với vectơ vận tốc (a\u00b7v &gt; 0).", "vận tốc có giá trị âm."]),
        ("Một xe chuyển động thẳng đều với vận tốc 12 m/s không đổi. Gia tốc của xe bằng",
         ["12 m/s\u00b2.", "6 m/s\u00b2.", "0.", "không xác định được."]),
    ], [
        ("B", "a = (8 \u2212 20)/3 = \u22124 m/s\u00b2; |v| giảm nên chậm dần (a ngược chiều v)."),
        ("C", "Tiêu chuẩn đúng là a cùng chiều v. Chỉ nhìn dấu của a mà không nhìn dấu của v sẽ sai."),
        ("C", "\u0394v = 0 nên a = 0 \u2014 có vận tốc không có nghĩa là có gia tốc."),
    ]))

    s.extend(_unit_bank("C8 \u00b7 2.5 Chuyển động thẳng biến đổi đều", [
        ("Một vật xuất phát từ trạng thái nghỉ, chuyển động nhanh dần đều với a = 3 m/s\u00b2. Vận tốc sau 4 s là",
         ["7 m/s.", "12 m/s.", "16 m/s.", "24 m/s."]),
        ("Một xe đang đi 15 m/s thì phanh với gia tốc \u22123 m/s\u00b2 (chiều dương là chiều chuyển động). Quãng đường xe đi đến khi dừng là",
         ["25 m.", "37,5 m.", "45 m.", "75 m."]),
        ("Một vật có v\u2080 = 2 m/s, a = 4 m/s\u00b2. Độ dịch chuyển sau 2 s là",
         ["8 m.", "10 m.", "12 m.", "16 m."]),
        ("Trên đồ thị vận tốc \u2013 thời gian của CĐTBĐĐ, độ dốc của đồ thị cho biết",
         ["độ dịch chuyển.", "gia tốc.", "quãng đường.", "thời gian."]),
    ], [
        ("B", "v = 0 + 3\u00b74 = 12 m/s."),
        ("B", "Dùng công thức không chứa t: d = (0 \u2212 15\u00b2)/(2\u00b7(\u22123)) = 225/6 = 37,5 m."),
        ("C", "d = 2\u00b72 + \u00bd\u00b74\u00b72\u00b2 = 4 + 8 = 12 m."),
        ("B", "Độ dốc v\u2013t = \u0394v/\u0394t = a. (Còn <i>diện tích</i> dưới v\u2013t mới là độ dịch chuyển.)"),
    ]))

    s.extend(_unit_bank("C9 \u00b7 2.6 Sự rơi tự do", [
        ("Trường hợp nào sau đây <b>gần đúng</b> là rơi tự do nhất?",
         ["Chiếc lá rơi trong không khí.", "Viên bi thép rơi trong ống đã hút hết không khí.",
          "Chiếc dù đang mở rơi chậm.", "Hạt mưa rơi qua lớp không khí dày."]),
        ("Thả rơi tự do, lấy g = 10 m/s\u00b2. Quãng đường vật đi được trong giây thứ ba (từ t = 2 s đến t = 3 s) là",
         ["15 m.", "20 m.", "25 m.", "45 m."]),
        ("Thả rơi tự do một vật từ độ cao 20 m, lấy g = 10 m/s\u00b2. Vận tốc khi chạm đất là",
         ["10 m/s.", "14 m/s.", "20 m/s.", "40 m/s."]),
    ], [
        ("B", "Ống chân không loại bỏ sức cản \u2192 chỉ còn trọng lực. Lá/dù/mưa chịu sức cản đáng kể."),
        ("C", "s(3) \u2212 s(2) = \u00bd\u00b710\u00b79 \u2212 \u00bd\u00b710\u00b74 = 45 \u2212 20 = 25 m. Nhớ dãy 5\u201315\u201325 với g = 10."),
        ("C", "v = \u221a(2gh) = \u221a(2\u00b710\u00b720) = \u221a400 = 20 m/s."),
    ]))

    # ---------------------------------------------------------- PHẦN D
    s.append(h1("PHẦN D \u00b7 TỔNG ÔN TRƯỚC NGÀY THI"))
    s.append(h2("D1. Phiếu công thức 1 trang \u2014 học thuộc trước, hiểu sau cũng được"))
    s.append(styled_table([
        ["Chủ đề", "Công thức phải thuộc", "Điều kiện / lưu ý"],
        ["Tốc độ \u2013 vận tốc", "v = s/t; v = \u0394d/\u0394t; 1 m/s = 3,6 km/h", "Tốc độ dùng s (vô hướng); vận tốc dùng d (vectơ)"],
        ["Cộng vận tốc", "vectơ v<sub>1,3</sub> = vectơ v<sub>1,2</sub> + vectơ v<sub>2,3</sub>", "Cùng chiều: cộng; ngược chiều: trừ; vuông góc: \u221a(tổng bình phương)"],
        ["Đồ thị d\u2013t", "v = \u0394d/\u0394t (độ dốc); d = d\u2080 + vt", "Nằm ngang \u2192 v = 0; dốc xuống \u2192 v &lt; 0"],
        ["Gia tốc", "a = \u0394v/\u0394t [m/s\u00b2]", "a\u00b7v &gt; 0 nhanh dần; a\u00b7v &lt; 0 chậm dần"],
        ["CĐTBĐĐ", "v = v\u2080 + at; d = v\u2080t + \u00bdat\u00b2; v\u00b2 \u2212 v\u2080\u00b2 = 2ad; d = (v\u2080+v)t/2", "Chọn công thức theo ẩn thiếu; chú ý dấu của a"],
        ["Rơi tự do", "v = gt; s = \u00bdgt\u00b2; v\u00b2 = 2gs; t<sub>chạm đất</sub> = \u221a(2h/g)", "v\u2080 = 0, a = g \u2248 9,8 (đề cho 10 thì dùng 10)"],
        ["Sai số", "\u0100 = \u03a3A\u1d62/n; \u0394A = \u0394\u0100 + \u0394A<sub>dc</sub>; \u03b4A = \u0394A/\u0100\u00d7100%; A = \u0100 \u00b1 \u0394A", "Tổng/hiệu: cộng \u0394; tích/thương: cộng \u03b4"],
    ], [32 * mm, 62 * mm, 62 * mm]))
    s.append(sp(3))
    s.append(h2("D2. Năm \u201ccặp sinh đôi\u201d hay bị nhầm nhất"))
    s.append(styled_table([
        ["Cặp hay nhầm", "Phân biệt trong 1 câu", "Dấu hiệu nhận biết trên đề"],
        ["s \u2014 d", "s nhớ đường đi, d nhớ đích đến", "\u201cquay lại / vòng kín\u201d \u2192 d = 0"],
        ["Tốc độ \u2014 vận tốc", "Tốc độ vô hướng, vận tốc vectơ", "Hỏi \u201chướng\u201d \u2192 phải là vận tốc"],
        ["Đồ thị d\u2013t \u2014 v\u2013t", "d\u2013t: độ dốc = v; v\u2013t: độ dốc = a, diện tích = d", "Nhìn tên trục tung trước khi tính"],
        ["\u0394A \u2014 \u03b4A", "\u0394A có đơn vị, \u03b4A có %", "Thấy % \u2192 sai số tỉ đối"],
        ["Nhanh dần \u2014 a dương", "Nhanh dần \u2194 |v| tăng \u2194 a cùng chiều v", "Phải biết dấu/chiều của cả v"],
    ], [34 * mm, 61 * mm, 61 * mm]))
    s.append(sp(2))
    s.append(h2("D3. Lộ trình ôn tập gợi ý"))
    s.append(styled_table([
        ["Thời gian", "Việc cần làm", "Mục tiêu đạt được"],
        ["7 \u2192 4 ngày trước", "Học Phần A theo thứ tự A1\u2192A9; làm ví dụ mẫu bằng cách che lời giải", "Thuộc công thức + hiểu bẫy của từng bài"],
        ["3 \u2192 2 ngày trước", "Làm Phần C theo đơn vị; sửa lỗi theo mã đơn vị", "Lấp lỗ hổng theo từng đơn vị"],
        ["1 ngày trước", "Làm Phần B bấm giờ 50 phút; chấm và đọc toàn bộ lời giải B2\u2013B3", "Quen áp lực thời gian và cấu trúc 4 phần"],
        ["Tối trước ngày thi", "Chỉ đọc D1 (phiếu công thức), D2 (cặp sinh đôi) và các \u2717 đã đánh dấu", "Không học bài mới; ngủ đủ giấc"],
        ["Trong phòng thi", "Nhận biết làm trước \u2192 Hiểu \u2192 Vận dụng; câu tính toán ghi đơn vị và kiểm tra dấu", "Không bỏ trống câu trắc nghiệm nào"],
    ], [32 * mm, 62 * mm, 62 * mm]))
    s.append(sp(2))
    s.append(callout("\u2605 Checklist tự chấm \u201ctôi đã sẵn sàng chưa?\u201d",
                     ["\u2610 Tôi nói lại được toàn bộ phiếu công thức D1 mà không nhìn tài liệu.",
                      "\u2610 Tôi phân biệt được 5 cặp sinh đôi ở D2 bằng ví dụ tự nghĩ.",
                      "\u2610 Tôi đã làm Phần B trong 50 phút và sửa hết lỗi theo mã đơn vị.",
                      "\u2610 Tôi biết 2.5 là trọng tâm (9/31 mục) nên đã dành cho nó thời gian ôn nhiều nhất."],
                     bg=BG_PURPLE, accent=PURPLE))

    # ---------------------------------------------------------- PHỤ LỤC
    s.append(h1("PHỤ LỤC \u00b7 ĐỐI CHIẾU 100% MA TRẬN \u00d7 ĐẶC TẢ \u00d7 ĐỀ CƯƠNG"))
    s.append(P("Bảng này là \u201cbản đồ kiểm chứng\u201d: mỗi yêu cầu trong bản <b>đặc tả</b> đều có đúng một nơi để <b>học</b> (Phần A) "
               "và ít nhất một nơi để <b>luyện có đáp án</b> (Phần B/C). Nếu một hàng nào trong bảng này bị trống, đề cương sẽ bị coi là chưa đầy đủ \u2014 "
               "và bảng dưới đây cho thấy không hàng nào trống. Chữ viết tắt: PI/PII/PIII/PIV = Phần I/II/III/IV của đề mẫu; LT = câu luyện thêm."))
    rows = [
        ["1 \u00b7 Làm quen với Vật lí", "Nêu đối tượng nghiên cứu; thành tựu ứng với các CMCN; quá trình phát triển; phương pháp nghiên cứu (NB). Hiểu quá trình nghiên cứu (TH)", "A1", "PI Câu 1; C1"],
        ["2 \u00b7 An toàn phòng thực hành", "Nêu nguy cơ mất an toàn; nêu quy tắc an toàn (NB). Hiểu/sử dụng thiết bị và biển báo (TH)", "A2", "PI Câu 2\u20133; C2"],
        ["3 \u00b7 Sai số phép đo", "Nêu đo trực tiếp/gián tiếp, các loại sai số, nguyên nhân, công thức \u0100/\u0394A/\u03b4A (NB). Ghi kết quả, tính \u0394A & \u03b4A (TH). Tính giá trị đo và sai số (VD)", "A3", "PI Câu 4; C3"],
        ["4 \u00b7 Độ dịch chuyển & quãng đường", "Nêu định nghĩa d, so sánh d\u2013s (NB). Xác định d và s (TH). Tính d (VD) và trong bài toán (VDC)", "A4", "PI Câu 5\u20137; C4"],
        ["5 \u00b7 Tốc độ và vận tốc", "Ý nghĩa/công thức tốc độ TB; tốc độ tức thời; cách đo tốc độ; định nghĩa/công thức vận tốc; cộng vận tốc (NB). Tính tốc độ TB, phân biệt tốc độ\u2013vận tốc, xác định vectơ vận tốc (TH). Tổng hợp 2 vận tốc cùng phương/vuông góc (VD)", "A5", "PI Câu 8; PII Câu 1a\u2013b; PIII Câu 1; PIV Câu 1; C5"],
        ["6 \u00b7 Thực hành đo tốc độ", "Ưu/nhược điểm đồng hồ hiện số + cổng quang điện; cách sử dụng; ý nghĩa hai cổng (NB). Đo tốc độ bằng dụng cụ (TH)", "A5 (mục Thực hành)", "C5 LT4; A5 ví dụ quy trình"],
        ["7 \u00b7 Đồ thị d\u2013t", "Mô tả chuyển động từ đồ thị (NB). Tính tốc độ từ độ dốc; xác định vị trí/vận tốc từ đồ thị (TH). Vẽ đồ thị; xác định s và d (VD)", "A6", "PI Câu 9\u201310; PII Câu 1c\u2013d; C6"],
        ["8 \u00b7 Gia tốc", "Chuyển động biến đổi; quan hệ phương/chiều a\u2013v; khái niệm/công thức/đơn vị gia tốc (NB). Tính \u0394v, a; phân biệt nhanh/chậm dần (TH)", "A7", "PI Câu 11\u201312; C7"],
        ["9 \u00b7 CĐTBĐĐ", "Định nghĩa CĐTBĐĐ, nhanh/chậm dần đều, các công thức (NB). Dùng công thức tính v, a, d (TH). Giải bài cơ bản (VD) và nâng cao (VDC)", "A8", "PI Câu 13\u201315; PII Câu 2; PIV Câu 2\u20133; C8"],
        ["10 \u00b7 Rơi tự do", "Định nghĩa; đặc điểm rơi trong không khí; các công thức (NB). Phân biệt rơi gần đúng tự do; tính toán đơn giản (TH). Giải bài toán rơi tự do (VD)", "A9", "PI Câu 16\u201318; PIII Câu 2; C9"],
    ]
    s.append(styled_table([["Đơn vị (đặc tả)", "Yêu cầu cần kiểm tra (tóm tắt đầy đủ)", "Học ở", "Luyện ở (có đáp án)"]] + rows,
                          [30 * mm, 72 * mm, 24 * mm, 30 * mm]))
    s.append(sp(3))
    s.append(h2("Nguồn tài liệu và căn cứ biên soạn"))
    s.extend([
        P("1. <b>Tài liệu gốc trong kho lưu trữ:</b> \u201cMA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx\u201d (ma trận phân bổ câu hỏi + bản đặc tả 10 đơn vị kiến thức) \u2014 căn cứ duy nhất quyết định phạm vi và tỉ trọng của đề cương này.", "BodySmall"),
        P("2. <b>Chương trình/SGK đối chiếu:</b> Vật lí 10 \u2013 Kết nối tri thức, Chương I (Bài 1\u20133) và Chương II (Bài 4\u201310). Thứ tự đơn vị 1.1\u20132.6 trong ma trận khớp với thứ tự Bài 1\u201310 của SGK (riêng Bài 6 \u2013 Thực hành đo tốc độ \u2013 được đặc tả tách riêng nhưng ma trận gộp vào 2.2; đề cương đã học gộp ở A5 và đối chiếu riêng ở Phụ lục để không sót).", "BodySmall"),
        P("3. Tài liệu tham khảo lí thuyết và dạng bài (đã kiểm chứng chéo khi biên soạn): tóm tắt lí thuyết và bài tập Vật lí 10 Kết nối tri thức Bài 1\u201310 trên VietJack, Loigiaihay, VnDoc, Hoc247. Mọi công thức và số liệu trong đề mẫu/luyện thêm đều được tính lại độc lập trước khi chốt đáp án.", "BodySmall"),
        P("4. <b>Giới hạn trung thực:</b> vì tài liệu gốc không chứa đề thi cụ thể, không một tài liệu nào có thể khẳng định \u201cđây là câu hỏi sẽ ra y hệt\u201d. Cam kết của đề cương này là: phủ 100% ô ma trận và 100% yêu cầu đặc tả (xem bảng đối chiếu trên), kèm một đề mẫu đúng cấu trúc và ngân hàng câu hỏi đổi dạng \u2014 để bất kì câu hỏi thật nào thuộc phạm vi trên đều đã được học và luyện ít nhất một lần.", "BodySmall"),
    ])
    return s

# -*- coding: utf-8 -*-
"""PHẦN A – Lý thuyết chuyên đề 6 → 10."""

from reportlab.lib.units import cm
from doc_kit import *  # noqa
from figures import fig_dt, fig_vt


def build(d: Doc):
    # ================================================================= BÀI 6
    d.h1("THỰC HÀNH: ĐO TỐC ĐỘ CỦA VẬT CHUYỂN ĐỘNG", kicker="Chuyên đề 06 · Bài 6 SGK · Nội dung đặc tả (không có câu riêng)")

    d.h2("6.1 · Dụng cụ và nguyên lí đo")
    d.table(
        ["Dụng cụ", "Công dụng"],
        [
            ["Đồng hồ đo thời gian hiện số", "Đo khoảng thời gian giữa hai tín hiệu, hiển thị bằng số"],
            ["Cổng quang điện (2 chiếc)", "Phát hiện vật đi qua, gửi tín hiệu mở/đóng đồng hồ"],
            ["Thước thẳng (hoặc thước có gắn cổng)", "Đo quãng đường giữa hai cổng"],
            ["Giá đỡ, máng nghiêng", "Tạo quỹ đạo chuyển động thẳng, giữ cổng cố định"],
            ["Xe lăn / viên bi / tấm chắn sáng", "Vật chuyển động cần đo tốc độ"],
        ],
        widths=[5.4 * cm, 11.7 * cm], font_size=8.4)
    d.p("<b>Nguyên lí:</b> mỗi cổng quang điện gồm một bộ phát tia hồng ngoại và một bộ thu. Bình thường chùm tia "
        "chiếu thẳng vào bộ thu. Khi vật chuyển động đi qua, nó <b>che chùm tia</b> → bộ thu mất tín hiệu → đồng hồ "
        "ghi nhận thời điểm. Đo quãng đường s giữa hai cổng và khoảng thời gian Δt, ta tính <b>v = s/Δt</b>.")

    d.box("remember",
          "• <b>Dùng hai cổng (chế độ A↔B):</b> đo thời gian vật đi từ cổng A đến cổng B → tính được "
          "<b>tốc độ trung bình</b> trên đoạn AB.\n\n"
          "• <b>Dùng một cổng:</b> gắn <b>tấm chắn sáng</b> có bề rộng Δs đã biết lên vật; đo thời gian Δt tấm chắn "
          "che chùm tia → tính <b>tốc độ tức thời</b> tại vị trí cổng: v ≈ Δs/Δt.\n\n"
          "• Ý nghĩa của việc dùng <b>hai cổng</b>: xác định được thời gian chuyển động trên một đoạn đường xác định, "
          "nhờ đó tính được tốc độ trung bình mà không cần người bấm đồng hồ.",
          title="CẦN NHỚ")

    d.h2("6.2 · Ưu điểm và nhược điểm của đồng hồ hiện số + cổng quang điện")
    d.table(
        ["Ưu điểm", "Nhược điểm"],
        [
            ["Độ chính xác cao (có thể tới 0,001 s), đo được khoảng thời gian rất ngắn",
             "Giá thành cao hơn đồng hồ bấm giây thông thường"],
            ["Tự động hoá: không phụ thuộc phản xạ bấm giây của người đo",
             "Cần nguồn điện, dễ hỏng nếu va đập hoặc ẩm"],
            ["Hiển thị số trực tiếp, dễ đọc, hạn chế sai số thị sai",
             "Dễ bị nhiễu bởi ánh sáng mạnh hoặc vật cản khác che chùm tia"],
            ["Lặp lại nhiều lần nhanh, thuận tiện xử lí số liệu",
             "Vật đo phải che được chùm tia; khó đo vật quá nhỏ hoặc trong suốt"],
        ],
        widths=[8.55 * cm, 8.55 * cm], font_size=8.3)

    d.h2("6.3 · Quy trình thực hành 6 bước")
    d.nums([
        "Bố trí máng nghiêng, gắn cố định hai cổng quang điện cách nhau một đoạn s; dùng thước đo chính xác s.",
        "Nối cổng quang với đồng hồ đo thời gian hiện số; cắm điện và bật công tắc.",
        "Chọn chế độ đo (MODE) phù hợp: đo thời gian giữa hai cổng (A↔B).",
        "Nhấn RESET để đưa đồng hồ về 0, kiểm tra đèn báo của hai cổng.",
        "Cho vật chuyển động qua cổng A rồi cổng B; đọc và ghi thời gian Δt trên màn hình.",
        "Lặp lại 3 – 5 lần, tính giá trị trung bình của Δt rồi tính v = s/Δt, ghi kết quả kèm sai số.",
    ])

    d.box("example",
          "<b>Ví dụ.</b> Hai cổng quang cách nhau s = 0,500 m. Đồng hồ hiện số đo được Δt = 0,312 s (chế độ ms). "
          "Tính tốc độ của vật và ghi kết quả, biết sai số của thước là 0,001 m và của đồng hồ là 0,001 s.\n\n"
          "<b>Giải.</b>\n"
          "• v = s/Δt = 0,500/0,312 ≈ <b>1,60 m/s</b>.\n"
          "• Sai số tỉ đối: δ(s) = 0,001/0,500 = 0,2%; δ(t) = 0,001/0,312 ≈ 0,32%.\n"
          "• δ(v) = 0,2% + 0,32% ≈ 0,52% → Δv = 0,52% × 1,60 ≈ 0,008 m/s.\n"
          "• Kết quả: <b>v = 1,600 ± 0,008 m/s</b> (làm tròn: 1,60 ± 0,01 m/s).",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• Quên <b>RESET</b> về 0 trước mỗi lần đo → kết quả bị cộng dồn thời gian lần trước.\n"
          "• Đọc nhầm đơn vị: đồng hồ ở chế độ ms, 312 ms = 0,312 s (không phải 3,12 s).\n"
          "• Dùng một cổng mà không có tấm chắn sáng thì chỉ đo được “thời điểm”, không đo được tốc độ.\n"
          "• Đặt hai cổng quá gần nhau → thời gian quá nhỏ, sai số tương đối lớn.",
          title="BẪY THƯỜNG GẶP")
    d.box("tip", "<b>“HAI cổng → tốc độ trung bình; MỘT cổng + tấm chắn → tốc độ tức thời.”</b> "
                "Nhớ theo số cổng là nhớ được toàn bộ ý nghĩa thí nghiệm.", title="MẸO NHỚ")

    # ================================================================= BÀI 7
    d.h1("ĐỒ THỊ ĐỘ DỊCH CHUYỂN – THỜI GIAN", kicker="Chuyên đề 07 · Bài 7 SGK · 4 đơn vị hỏi (1 Biết + 1 Hiểu ở P.I, 2 ý P.II)")

    d.h2("7.1 · Cách dựng đồ thị")
    d.p("Trục hoành biểu diễn <b>thời gian t</b> (s), trục tung biểu diễn <b>độ dịch chuyển d</b> (m). "
        "Quy trình: lập bảng số liệu (t, d) → chọn tỉ lệ xích phù hợp → xác định các điểm → nối các điểm bằng đường "
        "thẳng (nếu chuyển động đều) hoặc đường cong (nếu vận tốc thay đổi).")
    d.story.append(fig_dt())
    d.p("<i>Hình 1. Ba dạng đồ thị độ dịch chuyển – thời gian thường gặp.</i>", "Caption")

    d.h2("7.2 · Đọc đồ thị: độ dốc chính là vận tốc")
    d.box("remember",
          "Trên đồ thị d – t, <b>độ dốc của đường biểu diễn bằng vận tốc</b>:\n\n"
          "&nbsp;&nbsp;&nbsp;&nbsp;<b>v = Δd/Δt = (d₂ − d₁)/(t₂ − t₁)</b>\n\n"
          "• Đường <b>nằm ngang</b> (độ dốc 0): vật đứng yên, d không đổi.\n"
          "• Đường <b>dốc lên</b>: vật chuyển động theo chiều dương, v &gt; 0.\n"
          "• Đường <b>dốc xuống</b>: vật chuyển động ngược chiều dương, v &lt; 0.\n"
          "• Đường <b>càng dốc</b> thì tốc độ càng lớn (đi được nhiều mét trong cùng một giây).\n"
          "• Đường <b>cong</b>: chuyển động biến đổi (vận tốc thay đổi), độ dốc thay đổi theo thời gian.",
          title="CẦN NHỚ")

    d.h2("7.3 · Bốn việc có thể làm chỉ bằng cách “nhìn” đồ thị")
    d.table(
        ["Cần tìm", "Cách làm trên đồ thị"],
        [
            ["Vị trí của vật tại thời điểm t", "Từ t kẻ đường thẳng đứng cắt đồ thị, đọc tung độ tại giao điểm"],
            ["Vận tốc (tốc độ)", "Tính độ dốc: chọn 2 điểm bất kì trên đường, v = Δd/Δt"],
            ["Thời điểm và vị trí hai vật gặp nhau", "Tìm <b>giao điểm</b> của hai đồ thị; hoành độ là thời điểm, tung độ là vị trí"],
            ["Quãng đường đã đi", "Cộng <b>trị tuyệt đối</b> độ biến thiên độ dịch chuyển của từng đoạn: s = Σ|Δd|"],
        ],
        widths=[5.2 * cm, 11.9 * cm], font_size=8.4)
    d.p("<b>Chú ý:</b> khi vật không đổi chiều thì s = |d(cuối) − d(đầu)|. Khi vật đổi chiều, "
        "phải chia đồ thị thành từng đoạn và cộng trị tuyệt đối – đây là dạng bẫy phổ biến ở câu hỏi Phần II.")

    d.h2("7.4 · Ví dụ đọc – vẽ – tính")
    d.table(
        ["t (s)", "0", "1", "2", "3", "4"],
        [["d (m)", "0", "15", "30", "45", "60"]],
        widths=[2.6 * cm] + [2.9 * cm] * 5, aligns=["L", "C", "C", "C", "C", "C"], font_size=8.6)

    d.box("example",
          "<b>Ví dụ.</b> Một vật chuyển động thẳng, có số liệu như bảng trên.\n"
          "a) Vẽ đồ thị d – t. b) Tính vận tốc. c) Xác định vị trí vật sau 6 s.\n\n"
          "<b>Giải.</b>\n"
          "a) Các điểm (0;0), (1;15), (2;30), (3;45), (4;60) nằm trên một đường thẳng đi qua gốc toạ độ.\n"
          "b) v = Δd/Δt = (60 − 0)/(4 − 0) = <b>15 m/s</b>. Đường thẳng càng dốc thì vận tốc càng lớn.\n"
          "c) Vật chuyển động thẳng đều nên d = 15t → tại t = 6 s: d = <b>90 m</b>.",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• Nhầm <b>đồ thị d – t</b> với <b>đồ thị v – t</b>: ở đồ thị d – t, đường nằm ngang là <b>đứng yên</b>; "
          "ở đồ thị v – t, đường nằm ngang là <b>chuyển động đều</b>.\n"
          "• Thấy đường dốc xuống liền kết luận “chậm dần đều” – sai; dốc xuống chỉ cho biết vật đi ngược chiều dương.\n"
          "• Tính quãng đường bằng |d(cuối) − d(đầu)| khi vật đã đổi chiều → thiếu quãng đường.\n"
          "• Quên ghi đơn vị của độ dốc (m/s).",
          title="BẪY THƯỜNG GẶP")
    d.box("tip", "<b>“Ngang – đứng yên; Lên – xuôi chiều; Xuống – ngược chiều; Cong – biến đổi.”</b><br/>"
                "Và luôn nhớ: <b>độ dốc = vận tốc</b>.", title="MẸO NHỚ")

    # ================================================================= BÀI 8
    d.h1("CHUYỂN ĐỘNG BIẾN ĐỔI. GIA TỐC", kicker="Chuyên đề 08 · Bài 8 SGK · 2 đơn vị hỏi (1 Biết + 1 Hiểu)")

    d.h2("8.1 · Chuyển động biến đổi")
    d.p("<b>Chuyển động biến đổi</b> là chuyển động có <b>vận tốc thay đổi</b> theo thời gian (thay đổi về độ lớn, "
        "về phương, chiều hoặc cả ba). Xe khởi hành, xe phanh, vật rơi, ô tô vào cua… đều là chuyển động biến đổi.")
    d.p("Đại lượng đặc trưng cho mức độ thay đổi nhanh hay chậm của vận tốc là <b>gia tốc</b>.")

    d.h2("8.2 · Gia tốc")
    d.box("remember",
          "<b>Gia tốc trung bình</b> là đại lượng vectơ, bằng thương số của độ biến thiên vận tốc và thời gian "
          "biến thiên:\n\n"
          "&nbsp;&nbsp;&nbsp;&nbsp;<b>a = Δv/Δt = (v₂ − v₁)/(t₂ − t₁)</b>&nbsp;&nbsp;&nbsp;(a và v là vectơ)\n\n"
          "• Trong chuyển động thẳng: a = (v₂ − v₁)/(t₂ − t₁) – giá trị <b>đại số</b>, có thể âm hoặc dương.\n"
          "• Đơn vị: <b>m/s²</b>.\n"
          "• Ý nghĩa: a cho biết vận tốc biến thiên nhanh hay chậm; |a| càng lớn thì vận tốc đổi càng nhanh.\n"
          "• <b>Gia tốc tức thời</b> là gia tốc tại một thời điểm: a = Δv/Δt với Δt rất nhỏ.",
          title="CẦN NHỚ")

    d.h2("8.3 · Quan hệ giữa gia tốc và vận tốc")
    d.table(
        ["Trường hợp", "Quan hệ a và v", "Đặc điểm chuyển động", "Ví dụ"],
        [
            ["<b>Nhanh dần</b>", "a cùng chiều với v (a·v &gt; 0)", "Độ lớn vận tốc tăng dần", "Xe khởi hành, vật rơi"],
            ["<b>Chậm dần</b>", "a ngược chiều với v (a·v &lt; 0)", "Độ lớn vận tốc giảm dần", "Xe hãm phanh, ném vật lên"],
            ["Chuyển động đều", "a = 0", "Độ lớn vận tốc không đổi", "Xe chạy đều trên đường thẳng"],
        ],
        widths=[3.0 * cm, 4.6 * cm, 4.6 * cm, 4.9 * cm], font_size=8.3)
    d.p("Khi đã chọn chiều dương, dấu của a <b>một mình không đủ</b> để kết luận nhanh dần hay chậm dần. "
        "Phải so sánh dấu của a với dấu của v. Ví dụ: xe đang đi ngược chiều dương (v &lt; 0) và hãm phanh thì "
        "a &gt; 0 → a và v trái dấu → chuyển động chậm dần.")

    d.box("example",
          "<b>Ví dụ 1.</b> Xe tăng tốc từ 10 m/s lên 20 m/s trong 5 s. Tính gia tốc.\n"
          "a = (20 − 10)/5 = <b>2 m/s²</b> (cùng chiều dương → nhanh dần).\n\n"
          "<b>Ví dụ 2.</b> Xe đang chạy 20 m/s thì hãm phanh, sau 4 s dừng lại.\n"
          "a = (0 − 20)/4 = <b>−5 m/s²</b>. Dấu “−” cho biết gia tốc ngược chiều dương; vì v &gt; 0 nên a và v "
          "trái dấu → chuyển động chậm dần.\n\n"
          "<b>Ví dụ 3.</b> Xe đang chạy ngược chiều dương với v = −10 m/s, hãm phanh và dừng sau 2 s.\n"
          "a = (0 − (−10))/2 = <b>+5 m/s²</b>. a dương nhưng vẫn là chuyển động <b>chậm dần</b> vì a trái dấu với v.",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• Cho rằng <b>a &gt; 0 là nhanh dần, a &lt; 0 là chậm dần</b> – sai khi chiều dương ngược chiều chuyển động.\n"
          "• Nhầm đơn vị gia tốc (m/s²) với đơn vị vận tốc (m/s).\n"
          "• Tính Δv = v₁ − v₂ (ngược thứ tự) → sai dấu.\n"
          "• Nghĩ rằng vật chuyển động chậm dần thì a phải âm – không nhất thiết.",
          title="BẪY THƯỜNG GẶP")
    d.box("tip", "<b>“CÙNG dấu → NHANH, TRÁI dấu → CHẬM.”</b> Nhìn a và v như hai người đẩy cùng chiều hay "
                "ngược chiều một xe hàng: cùng chiều thì xe chạy nhanh lên.", title="MẸO NHỚ")

    # ================================================================= BÀI 9
    d.h1("CHUYỂN ĐỘNG THẲNG BIẾN ĐỔI ĐỀU", kicker="Chuyên đề 09 · Bài 9 SGK · 7 đơn vị hỏi · “Xương sống” của đề thi")

    d.h2("9.1 · Định nghĩa")
    d.box("remember",
          "<b>Chuyển động thẳng biến đổi đều</b> là chuyển động có quỹ đạo là đường thẳng và có <b>độ lớn vận tốc "
          "tăng đều</b> (nhanh dần đều) hoặc <b>giảm đều</b> (chậm dần đều) theo thời gian – nghĩa là "
          "<b>gia tốc không đổi</b> (a = const).\n\n"
          "• <b>Nhanh dần đều:</b> a cùng dấu với v.\n"
          "• <b>Chậm dần đều:</b> a ngược dấu với v.",
          title="CẦN NHỚ")

    d.h2("9.2 · Bốn công thức cốt lõi")
    d.p("Chọn chiều dương là chiều chuyển động, gốc thời gian lúc bắt đầu khảo sát (t = 0), v₀ là vận tốc ban đầu.")
    d.f("v = v_0 + at", "vận tốc tại thời điểm t")
    d.f("d = v_0 t + ½at²", "độ dịch chuyển (khi không đổi chiều: s = d)")
    d.f("v² − v_0² = 2ad", "hệ thức độc lập với thời gian")
    d.f("d = (v_0 + v)t / 2", "độ dịch chuyển theo vận tốc trung bình")
    d.table(
        ["Kí hiệu", "Ý nghĩa", "Đơn vị"],
        [
            ["v₀", "Vận tốc ban đầu (t = 0)", "m/s"],
            ["v", "Vận tốc tại thời điểm t", "m/s"],
            ["a", "Gia tốc (không đổi)", "m/s²"],
            ["d", "Độ dịch chuyển", "m"],
            ["t", "Thời gian chuyển động", "s"],
        ],
        widths=[2.4 * cm, 9.4 * cm, 4.0 * cm], aligns=["C", "L", "C"], font_size=8.4)

    d.h2("9.3 · Đồ thị vận tốc – thời gian")
    d.story.append(fig_vt())
    d.p("<i>Hình 2. Đồ thị v – t của chuyển động nhanh dần đều.</i>", "Caption")
    d.bullets([
        "Đồ thị v – t của chuyển động thẳng biến đổi đều là một <b>đường thẳng</b>.",
        "<b>Hệ số góc</b> của đường thẳng bằng <b>gia tốc</b>: a = (v₂ − v₁)/(t₂ − t₁).",
        "<b>Diện tích</b> giữa đồ thị và trục thời gian bằng <b>độ dịch chuyển</b> (hình thang ABCD).",
    ])

    d.h2("9.4 · Quy trình giải một bài toán CĐTBĐĐ (5 bước)")
    d.nums([
        "<b>Chọn chiều dương</b> và gốc thời gian; ghi rõ đơn vị đã đổi (km/h → m/s).",
        "<b>Liệt kê</b> các đại lượng đã biết: v₀, v, a, t, d – chú ý dấu theo chiều dương.",
        "<b>Chọn công thức</b> chỉ chứa đại lượng cần tìm và đã biết (bảng 4 công thức).",
        "<b>Thay số và giải</b>; nếu bài có hãm phanh/đổi chiều, kiểm tra vật đã dừng chưa.",
        "<b>Kết luận</b> kèm đơn vị và nhận xét tính chất chuyển động (nhanh dần / chậm dần).",
    ])

    d.h2("9.5 · Năm dạng bài bắt buộc phải biết")
    d.table(
        ["Dạng", "Dấu hiệu nhận biết", "Công thức then chốt"],
        [
            ["1. Từ trạng thái nghỉ", "“bắt đầu chuyển động”, v₀ = 0", "v = at; d = ½at²; v² = 2ad"],
            ["2. Hãm phanh đến khi dừng", "“hãm phanh”, v = 0", "a = −v₀²/(2d); t(dừng) = −v₀/a"],
            ["3. Quãng đường trong giây thứ n", "“trong giây thứ n”, “giây cuối”", "Δs = s(n) − s(n−1) = v₀ + a(n − 0,5)"],
            ["4. Hai vật gặp nhau", "“gặp nhau”, “đuổi kịp”, cách nhau một đoạn", "Lập x₁(t), x₂(t), cho x₁ = x₂"],
            ["5. Đọc/viết phương trình từ đồ thị v–t", "Cho đồ thị v – t", "a = độ dốc; d = diện tích"],
        ],
        widths=[4.6 * cm, 5.6 * cm, 6.9 * cm], font_size=8.3)

    d.box("example",
          "<b>Ví dụ 1 (cơ bản).</b> Xe bắt đầu chuyển động nhanh dần đều với a = 2 m/s². Tính vận tốc và quãng đường "
          "sau 5 s.\n"
          "• v = v₀ + at = 0 + 2·5 = <b>10 m/s</b>.\n"
          "• d = ½at² = ½·2·5² = <b>25 m</b>.\n\n"
          "<b>Ví dụ 2 (hãm phanh).</b> Ô tô đang chạy 72 km/h thì hãm phanh, chuyển động chậm dần đều với "
          "a = −5 m/s². Tính thời gian đến khi dừng và quãng đường đi được từ lúc hãm phanh.\n"
          "• Đổi: 72 km/h = <b>20 m/s</b>.\n"
          "• Thời gian dừng: t = (0 − 20)/(−5) = <b>4 s</b>.\n"
          "• Quãng đường: d = (20 + 0)·4/2 = <b>40 m</b> (hoặc d = 20·4 − ½·5·16 = 40 m).\n"
          "• Quãng đường trong giây thứ 4: s(4) − s(3) = 40 − (20·3 − 2,5·9) = 40 − 37,5 = <b>2,5 m</b>.\n\n"
          "<b>Ví dụ 3 (hai vật gặp nhau).</b> Xe A khởi hành từ O, nhanh dần đều a = 1 m/s². Cùng lúc đó xe B đi qua "
          "điểm cách O 200 m, chuyển động thẳng đều cùng chiều với v = 15 m/s. Tìm thời điểm và vị trí gặp nhau.\n"
          "• Phương trình: x(A) = 0,5t²; x(B) = 200 + 15t.\n"
          "• Gặp nhau: 0,5t² = 200 + 15t → t² − 30t − 400 = 0 → t = <b>40 s</b> (loại t = −10 s).\n"
          "• Vị trí: x = 0,5·40² = <b>800 m</b> cách O.",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• <b>Áp dụng công thức khi vật đã dừng</b>: nếu thời gian hỏi lớn hơn thời gian dừng, quãng đường không "
          "tăng thêm. Luôn kiểm tra t(dừng) trước.\n"
          "• Quên đổi km/h → m/s (chia 3,6) – lỗi mất điểm phổ biến nhất.\n"
          "• Nhầm <b>“trong n giây”</b> (s = v₀n + ½an²) với <b>“trong giây thứ n”</b> (Δs = v₀ + a(n − 0,5)).\n"
          "• Đặt sai dấu a khi vật chuyển động chậm dần.\n"
          "• Với bài có đổi chiều, quãng đường ≠ |độ dịch chuyển|; phải cộng quãng đường từng chặng.\n"
          "• Hai vật gặp nhau: nhớ cộng vị trí ban đầu vào phương trình toạ độ.",
          title="BẪY THƯỜNG GẶP")
    d.box("tip",
          "<b>Bốn công thức = “V – S – H – T”:</b> Vận tốc (v = v₀ + at), Quãng đường (d = v₀t + ½at²), "
          "Hệ thức (v² − v₀² = 2ad), Trung bình (d = (v₀+v)t/2).\n"
          "<b>“Phanh thì tính thời gian dừng trước”</b> – câu thần chú cứu điểm cho mọi bài hãm phanh.",
          title="MẸO NHỚ")

    # ================================================================= BÀI 10
    d.h1("SỰ RƠI TỰ DO", kicker="Chuyên đề 10 · Bài 10 SGK · 4 đơn vị hỏi (1 Biết + 2 Hiểu + 1 câu tự luận)")

    d.h2("10.1 · Định nghĩa và đặc điểm")
    d.box("remember",
          "<b>Sự rơi tự do</b> là sự rơi của một vật <b>chỉ dưới tác dụng của trọng lực</b>.\n\n"
          "Đặc điểm của chuyển động rơi tự do:\n"
          "• Quỹ đạo là <b>đường thẳng đứng</b>.\n"
          "• Chiều chuyển động <b>từ trên xuống</b>.\n"
          "• Là chuyển động <b>thẳng nhanh dần đều</b> với gia tốc rơi tự do <b>g</b>.\n"
          "• Tại cùng một nơi trên Trái Đất, <b>mọi vật rơi với cùng một gia tốc g</b> (nếu bỏ qua lực cản không khí).\n"
          "• g ≈ <b>9,8 m/s²</b>; trong nhiều bài tập lấy g = <b>10 m/s²</b>. g phụ thuộc vĩ độ và độ cao.",
          title="CẦN NHỚ")

    d.h2("10.2 · Sự rơi trong không khí và “rơi gần đúng tự do”")
    d.p("Trong không khí, vật còn chịu <b>lực cản</b> phụ thuộc hình dạng, kích thước và vận tốc của vật. Vì vậy "
        "chiếc lá, tờ giấy, lông chim rơi chậm và không đều – <b>không phải</b> rơi tự do.")
    d.p("Thí nghiệm ống Newton: hút hết không khí ra khỏi ống thuỷ tinh rồi lật ngược, viên bi chì và chiếc lông chim "
        "<b>chạm đáy cùng một lúc</b>. Điều đó chứng tỏ khi không có lực cản của không khí, mọi vật rơi như nhau.")
    d.p("<b>Rơi gần đúng tự do:</b> vật rơi được coi là tự do khi lực cản không khí rất nhỏ so với trọng lực "
        "(hòn đá, viên bi, quả táo rơi từ độ cao nhỏ).")

    d.h2("10.3 · Các công thức")
    d.p("Chọn chiều dương hướng xuống, gốc thời gian lúc bắt đầu rơi, v₀ = 0:")
    d.f("v = gt", "vận tốc tại thời điểm t")
    d.f("h = s = ½gt²", "quãng đường = độ cao đã rơi")
    d.f("v² = 2gh", "hệ thức độc lập thời gian")
    d.f("t = √(2h/g)", "thời gian rơi từ độ cao h")
    d.p("Nếu vật được ném thẳng đứng <b>xuống</b> với vận tốc đầu v₀: <b>v = v₀ + gt</b>; "
        "<b>h = v₀t + ½gt²</b>; <b>v² − v₀² = 2gh</b>.")
    d.p("Nếu vật được ném thẳng đứng <b>lên</b> với v₀ (chiều dương hướng lên): chuyển động chậm dần đều với a = −g; "
        "độ cao cực đại <b>H = v₀²/(2g)</b>; thời gian lên <b>t = v₀/g</b>; tổng thời gian bay (lên + xuống) "
        "<b>2v₀/g</b>.")

    d.h2("10.4 · Quy luật quãng đường – “dãy số lẻ”")
    d.box("remember",
          "Vật rơi tự do (v₀ = 0): quãng đường đi được trong các khoảng thời gian bằng nhau liên tiếp tỉ lệ với "
          "<b>1 : 3 : 5 : 7 : …</b>\n\n"
          "• Quãng đường trong giây thứ n: <b>Δs = ½g(2n − 1)</b>.\n"
          "• Quãng đường trong n giây đầu: <b>sₙ = ½gn²</b>.\n"
          "• Suy ra quãng đường trong giây cuối (khi biết tổng thời gian T): <b>Δs = ½g(2T − 1)</b>.",
          title="CẦN NHỚ")

    d.box("example",
          "<b>Ví dụ 1.</b> Thả một vật rơi tự do từ độ cao 45 m, lấy g = 10 m/s². Tính thời gian rơi và vận tốc "
          "khi chạm đất.\n"
          "• t = √(2h/g) = √(2·45/10) = √9 = <b>3 s</b>.\n"
          "• v = gt = 10·3 = <b>30 m/s</b> (hoặc v = √(2gh) = √900 = 30 m/s).\n\n"
          "<b>Ví dụ 2.</b> Vật rơi tự do trong 5 s (g = 10 m/s²). Tính quãng đường và quãng đường trong giây thứ 5.\n"
          "• h = ½·10·5² = <b>125 m</b>.\n"
          "• Giây thứ 5: Δs = ½·10·(2·5 − 1) = <b>45 m</b> (kiểm tra: 125 − 80 = 45 m).\n\n"
          "<b>Ví dụ 3.</b> Ném thẳng đứng lên với v₀ = 20 m/s, g = 10 m/s². Tính độ cao cực đại và thời gian bay.\n"
          "• H = v₀²/(2g) = 400/20 = <b>20 m</b>.\n"
          "• Thời gian lên: t = 20/10 = 2 s → tổng thời gian bay = <b>4 s</b>.",
          title="VÍ DỤ MẪU")

    d.box("trap",
          "• Lẫn giữa <b>quãng đường trong n giây</b> và <b>trong giây thứ n</b> – hai công thức khác nhau.\n"
          "• Quên rằng khi vật đã chạm đất thì công thức không còn áp dụng cho thời gian sau đó.\n"
          "• Dùng g = 9,8 trong khi đề cho g = 10 (hoặc ngược lại) → lệch đáp án.\n"
          "• Cho rằng vật nặng luôn rơi nhanh hơn – chỉ đúng khi có lực cản không khí đáng kể.\n"
          "• Ném lên: quên rằng gia tốc vẫn là g hướng xuống trong suốt quá trình bay.",
          title="BẪY THƯỜNG GẶP")
    d.box("tip",
          "<b>“Rơi không v₀: v = gt – s = ½gt² – v² = 2gh.”</b><br/>"
          "<b>“1 – 3 – 5 – 7”</b> cho quãng đường từng giây; muốn giây thứ n thì lấy ½g(2n − 1).",
          title="MẸO NHỚ")

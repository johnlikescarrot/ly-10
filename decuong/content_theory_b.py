# -*- coding: utf-8 -*-
"""PHẦN 1 – Lý thuyết trọng tâm: Bài 7 → Bài 10."""
from style import *


def story():
    s = []
    s.append(H1B("CHỦ ĐỀ 2 · ĐỘNG HỌC CHẤT ĐIỂM"))

    # ================================================================= BÀI 7
    s.append(H2("Bài 7. Đồ thị độ dịch chuyển – thời gian"))
    s.append(H3("1. Cách dựng và đọc đồ thị"))
    s.append(P("Trục hoành biểu diễn <b>thời gian t</b> (s), trục tung biểu diễn <b>độ dịch chuyển x</b> (m). "
               "Mỗi điểm trên đồ thị cho biết vật ở đâu vào thời điểm nào."))
    s.append(formula("v = Δx / Δt = (x₂ − x₁)/(t₂ − t₁) = <b>độ dốc (hệ số góc)</b> của đồ thị"))
    s.append(SP(2))
    s.append(fig_st())
    s.append(Paragraph("<i>Hình 1.</i> Một chuyển động gồm 3 giai đoạn: (1) đi theo chiều dương đều; "
                       "(2) đứng yên; (3) đi ngược chiều dương đều.", S["small"]))
    s.append(SP(5))
    s.append(table([
        ["Dạng đồ thị", "Ý nghĩa chuyển động", "Vận tốc"],
        ["Đường <b>nằm ngang</b> (song song trục Ot)", "Vật <b>đứng yên</b>", "v = 0"],
        ["Đường thẳng <b>dốc lên</b>", "Chuyển động thẳng đều theo <b>chiều dương</b>", "v &gt; 0, "
         "dốc càng lớn v càng lớn"],
        ["Đường thẳng <b>dốc xuống</b>", "Chuyển động thẳng đều theo <b>chiều âm</b>", "v &lt; 0"],
        ["Đường <b>cong</b>", "Chuyển động <b>không đều</b> (nhanh dần hoặc chậm dần)", "v thay đổi"],
        ["Hai đồ thị <b>cắt nhau</b>", "Hai vật <b>gặp nhau</b> tại thời điểm và vị trí ứng với giao điểm",
         "—"],
        ["Đồ thị <b>cắt trục Ox</b>", "Vật <b>đổi chiều</b> chuyển động", "v đổi dấu"],
    ], [126, 230, CONTENT_W - 356], font=8.0))
    s.append(SP(4))
    s.append(box("Muốn tính <b>quãng đường</b> từ đồ thị: cộng <b>giá trị tuyệt đối</b> độ dịch chuyển của "
                 "từng đoạn. Muốn tính <b>độ dịch chuyển</b>: chỉ lấy <b>x<sub>cuối</sub> − x<sub>đầu</sub></b>.",
                 "thi"))
    s.append(H3("2. Ví dụ mẫu"))
    s.append(P("Dựa vào Hình 1: giai đoạn 1 (0 → 4 s) vật đi từ 0 đến 8 m; giai đoạn 2 (4 → 6 s) vật đứng yên "
               "tại 8 m; giai đoạn 3 (6 → 10 s) vật đi từ 8 m về 0."))
    s.extend(BULL([
        "Vận tốc mỗi đoạn: v₁ = 8/4 = <b>+2 m/s</b>; v₂ = <b>0</b>; v₃ = (0 − 8)/(10 − 6) = <b>−2 m/s</b>.",
        "Quãng đường: s = 8 + 0 + 8 = <b>16 m</b>.",
        "Độ dịch chuyển cả quá trình: Δx = 0 − 0 = <b>0</b> (vật về đúng chỗ cũ).",
        "Tốc độ trung bình: v<sub>tb</sub> = 16/10 = <b>1,6 m/s</b>; vận tốc trung bình = 0/10 = <b>0</b>.",
    ]))

    # ================================================================= BÀI 8
    s.append(CondPageBreak(150))
    s.append(H2("Bài 8. Chuyển động biến đổi. Gia tốc"))
    s.append(H3("1. Chuyển động biến đổi"))
    s.append(P("<b>Chuyển động biến đổi</b> là chuyển động có <b>vận tốc thay đổi</b> (về độ lớn hoặc về hướng "
               "hoặc cả hai) theo thời gian. Đại lượng đặc trưng cho mức độ thay đổi nhanh hay chậm của "
               "vận tốc là <b>gia tốc</b>."))
    s.append(formula("a̅ = Δv̅ / Δt = (v̅<sub>2</sub> − v̅<sub>1</sub>) / (t₂ − t₁)", "Đơn vị: m/s² (mét trên giây bình phương)"))
    s.append(P("Gia tốc là <b>đại lượng vectơ</b>; trong chuyển động thẳng, vectơ gia tốc nằm trên "
               "đường thẳng quỹ đạo. <b>Độ lớn</b> gia tốc cho biết vận tốc biến thiên nhanh hay chậm; "
               "<b>chiều</b> gia tốc cho biết vận tốc tăng hay giảm."))

    s.append(H3("2. Quan hệ về phương, chiều giữa gia tốc và vận tốc"))
    s.append(table([
        ["Quan hệ a̅ và v̅", "Tính chất chuyển động", "Ví dụ"],
        ["<b>Cùng phương, cùng chiều</b>", "Chuyển động <b>nhanh dần</b> (v tăng)", "Xe khởi hành, tăng tốc"],
        ["<b>Cùng phương, ngược chiều</b>", "Chuyển động <b>chậm dần</b> (v giảm)", "Xe hãm phanh"],
        ["<b>Vuông góc</b>", "Vận tốc <b>đổi hướng</b>, độ lớn không đổi", "Chuyển động tròn đều"],
        ["a = 0", "Vận tốc <b>không đổi</b>", "Chuyển động thẳng đều"],
    ], [120, 180, CONTENT_W - 300], font=8.2))
    s.append(SP(4))
    s.append(box("<b>“Cùng chiều thì nhanh, ngược chiều thì chậm.”</b> Câu này đúng cho <b>vectơ</b> a và v, "
                 "không phải cho <b>dấu</b> của a. a âm vẫn có thể là nhanh dần nếu vật đang chuyển động "
                 "theo chiều âm (khi đó v cũng âm: a và v cùng dấu).", "meo"))
    s.append(box("Sai lầm phổ biến: “a &gt; 0 là nhanh dần, a &lt; 0 là chậm dần”. <b>Sai!</b> Phải xét "
                 "<b>dấu tương đối</b> giữa a và v: <b>a·v &gt; 0 → nhanh dần; a·v &lt; 0 → chậm dần</b>.",
                 "bay"))

    s.append(H3("3. Ví dụ mẫu"))
    s.append(P("<b>Ví dụ 1.</b> Một xe đang chạy 10 m/s, sau 5 s đạt 20 m/s. Tính gia tốc."))
    s.append(P("<b>Giải.</b> a = (20 − 10)/5 = <b>2 m/s²</b>; a cùng chiều v → xe nhanh dần."))
    s.append(P("<b>Ví dụ 2.</b> Xe đang chạy 20 m/s thì hãm phanh, sau 4 s còn 8 m/s. Tính gia tốc."))
    s.append(P("<b>Giải.</b> a = (8 − 20)/4 = <b>−3 m/s²</b>; a ngược chiều v → xe chậm dần."))
    s.append(P("<b>Ví dụ 3.</b> Một vật chuyển động với vận tốc 6 m/s theo chiều âm rồi tăng tốc đến "
               "12 m/s (cũng theo chiều âm) sau 3 s. Tính gia tốc."))
    s.append(P("<b>Giải.</b> a = (−12 − (−6))/3 = −2 m/s² → a và v <b>cùng dấu âm</b> nên vật vẫn "
               "<b>nhanh dần</b>. Đây chính là cái bẫy “a âm”. "))

    # ================================================================= BÀI 9
    s.append(CondPageBreak(150))
    s.append(H2("Bài 9. Chuyển động thẳng biến đổi đều"))
    s.append(P("Đây là chuyên đề <b>nặng ký nhất</b> của đề thi: 3 câu trắc nghiệm, 4 ý đúng/sai và "
               "2 ý tự luận vận dụng.", "lead"))
    s.append(H3("1. Định nghĩa và phân loại"))
    s.extend(BULL([
        "<b>Chuyển động thẳng biến đổi đều</b> là chuyển động có quỹ đạo là đường thẳng và có "
        "<b>gia tốc không đổi</b> (vận tốc biến thiên những lượng bằng nhau trong những khoảng thời gian "
        "bằng nhau).",
        "<b>Nhanh dần đều:</b> a cùng chiều với v, độ lớn vận tốc <b>tăng đều</b>.",
        "<b>Chậm dần đều:</b> a ngược chiều với v, độ lớn vận tốc <b>giảm đều</b>.",
    ]))

    s.append(H3("2. Ba công thức vàng"))
    s.append(formula("(1)  v = v₀ + a·t", "Vận tốc tại thời điểm t"))
    s.append(formula("(2)  d = v₀·t + ½·a·t²", "Độ dịch chuyển trong thời gian t"))
    s.append(formula("(3)  v² − v₀² = 2·a·d", "Hệ thức liên hệ, <b>không chứa t</b>"))
    s.append(SP(2))
    s.append(P("Trong đó: v₀ – vận tốc ban đầu (m/s); v – vận tốc ở thời điểm t; a – gia tốc (m/s²); "
               "t – thời gian (s); d – độ dịch chuyển (m). Nếu vật <b>không đổi chiều</b> thì quãng đường "
               "<b>s = |d|</b>."))
    s.append(fig_vt())
    s.append(Paragraph("<i>Hình 2.</i> Đồ thị vận tốc – thời gian của chuyển động nhanh dần đều: "
                       "độ dốc của đường thẳng bằng gia tốc, <b>diện tích hình thang</b> bằng độ dịch chuyển.",
                       S["small"]))
    s.append(SP(5))
    s.append(box("<b>Ba công thức – ba tình huống:</b> thiếu t → dùng (3); thiếu v → dùng (2); "
                 "thiếu d → dùng (1).<br/>"
                 "Mẹo nhớ: <b>“Vận tốc cộng dồn – Quãng đường bình phương – Liên hệ không thời gian.”</b>",
                 "meo"))

    s.append(H3("3. Quy ước dấu – bước không được bỏ"))
    s.append(P("Chọn một chiều dương (thường là chiều chuyển động ban đầu). Khi đó:"))
    s.append(table([
        ["Đại lượng", "Dấu +", "Dấu −"],
        ["v₀", "Vật chuyển động theo chiều dương", "Vật chuyển động ngược chiều dương"],
        ["a", "a hướng theo chiều dương", "a hướng ngược chiều dương"],
        ["Tính chất", "a và v₀ <b>cùng dấu</b> → nhanh dần đều", "a và v₀ <b>trái dấu</b> → chậm dần đều"],
    ], [70, 200, CONTENT_W - 270], font=8.2))
    s.append(SP(4))
    s.append(box("Nếu chọn chiều dương là chiều chuyển động ban đầu thì: nhanh dần đều → <b>a &gt; 0</b>; "
                 "chậm dần đều → <b>a &lt; 0</b>. Đây là quy ước dùng trong 90% bài tập.", "thi"))

    s.append(H3("4. Năm dạng bài và ví dụ mẫu"))

    s.append(P("<b>Dạng 1. Tính v, a, d bằng công thức cơ bản.</b>"))
    s.append(P("<i>Đề:</i> Xe đang chạy 10 m/s thì tăng tốc đều với a = 2 m/s². Tính vận tốc và quãng đường "
               "sau 5 s.<br/><i>Giải:</i> v = 10 + 2·5 = <b>20 m/s</b>; "
               "d = 10·5 + ½·2·5² = 50 + 25 = <b>75 m</b>."))

    s.append(P("<b>Dạng 2. Quãng đường đi trong giây thứ n.</b>"))
    s.append(formula("Δs<sub>giây thứ n</sub> = s(n) − s(n−1) = v₀ + a·(n − 0,5)"))
    s.append(P("<i>Đề:</i> Vật bắt đầu chuyển động nhanh dần đều với a = 2 m/s², v₀ = 0. Tính quãng đường "
               "đi trong giây thứ 4.<br/><i>Giải:</i> s(4) = ½·2·16 = 16 m; s(3) = ½·2·9 = 9 m → "
               "Δs = 16 − 9 = <b>7 m</b> (đúng bằng 0 + 2·3,5)."))
    s.append(box("Phân biệt: <b>“trong giây thứ 4”</b> = từ t = 3 s đến t = 4 s (1 giây); "
                 "<b>“sau 4 giây”</b> = từ t = 0 đến t = 4 s. Hai kết quả khác nhau hoàn toàn.", "bay"))

    s.append(P("<b>Dạng 3. Vật chuyển động chậm dần đều rồi dừng lại.</b>"))
    s.append(formula("t<sub>dừng</sub> = v₀ / |a| ;   s<sub>dừng</sub> = v₀² / (2|a|)"))
    s.append(P("<i>Đề:</i> Xe đang chạy 20 m/s thì hãm phanh, chuyển động chậm dần đều với gia tốc có độ lớn "
               "2 m/s². Tính thời gian và quãng đường từ lúc hãm đến khi dừng.<br/>"
               "<i>Giải:</i> t = 20/2 = <b>10 s</b>; s = 20²/(2·2) = <b>100 m</b>."))

    s.append(P("<b>Dạng 4. Hai vật gặp nhau.</b> Viết phương trình chuyển động của mỗi vật "
               "(chọn gốc toạ độ, gốc thời gian), cho <b>x₁ = x₂</b> để tìm t, rồi thay t vào một phương trình "
               "để tìm vị trí gặp."))
    s.append(P("<i>Đề:</i> Vật 1 xuất phát từ O, nhanh dần đều với a = 2 m/s², v₀ = 0. Cùng lúc đó, vật 2 "
               "ở cách O 200 m, chuyển động đều <b>ngược về phía O</b> với tốc độ 10 m/s. Tìm thời điểm và "
               "vị trí gặp nhau.<br/><i>Giải:</i> x₁ = t²; x₂ = 200 − 10t. Cho x₁ = x₂: "
               "t² + 10t − 200 = 0 → (t − 10)(t + 20) = 0 → <b>t = 10 s</b>, vị trí <b>x = 100 m</b> "
               "(cách O 100 m)."))

    s.append(P("<b>Dạng 5. Vật đổi chiều chuyển động.</b>"))
    s.append(P("<i>Đề:</i> Vật chuyển động theo chiều dương với v₀ = 10 m/s, a = −2 m/s². Tính quãng đường "
               "và độ dịch chuyển sau 8 s.<br/><i>Giải:</i> Vật dừng ở t = 5 s, đi được 25 m; "
               "từ 5 s đến 8 s vật quay lại. Độ dịch chuyển d = 10·8 − ½·2·64 = <b>16 m</b>; "
               "quãng đường s = 25 + (25 − 16) = <b>34 m</b>. Như vậy <b>s ≠ |d|</b> khi vật đổi chiều."))
    s.append(box("Trong mọi bài có thể đổi chiều: <b>tính thời điểm dừng trước</b> (v = 0), rồi mới chia "
                 "chặng. Đây là lỗi mất điểm nhiều nhất của dạng 5.", "bay"))

    s.append(H3("5. Bảng tra nhanh theo yêu cầu đề"))
    s.append(table([
        ["Đề cho", "Đề hỏi", "Dùng công thức"],
        ["v₀, a, t", "v", "v = v₀ + at"],
        ["v₀, a, t", "d (hoặc s)", "d = v₀t + ½at²"],
        ["v₀, v, a", "d", "d = (v² − v₀²)/(2a)"],
        ["v₀, a, d", "v", "v = √(v₀² + 2ad)"],
        ["v₀, a", "quãng đường đến khi dừng", "s = v₀²/(2|a|)"],
        ["v₀, a, n", "quãng đường trong giây thứ n", "s(n) − s(n−1)"],
        ["a, quãng đường", "vận tốc cuối", "v = √(2ad) khi v₀ = 0"],
    ], [120, 150, CONTENT_W - 270], font=8.2))

    # ================================================================= BÀI 10
    s.append(CondPageBreak(150))
    s.append(H2("Bài 10. Sự rơi tự do"))
    s.append(H3("1. Định nghĩa và đặc điểm"))
    s.append(P("<b>Rơi tự do</b> là sự rơi của một vật <b>chỉ dưới tác dụng của trọng lực</b>. "
               "Trong thực tế, khi <b>sức cản của không khí không đáng kể</b> so với trọng lượng, "
               "ta coi vật rơi gần đúng là rơi tự do."))
    s.extend(BULL([
        "Phương: <b>thẳng đứng</b>. Chiều: <b>từ trên xuống</b>.",
        "Chuyển động: <b>thẳng nhanh dần đều</b> với gia tốc rơi tự do <b>g</b>.",
        "g phụ thuộc vị trí địa lí và độ cao; thường lấy <b>g ≈ 9,8 m/s²</b> (hoặc <b>10 m/s²</b> khi đề cho).",
        "Trong <b>chân không</b>, mọi vật rơi như nhau, không phụ thuộc khối lượng.",
    ]))
    s.append(table([
        ["Trường hợp", "Kết luận", "Ví dụ"],
        ["Rơi <b>gần đúng tự do</b>", "Bỏ qua được sức cản không khí",
         "Hòn sỏi, chìa khoá, quả bóng sắt rơi từ độ cao vài mét"],
        ["<b>Không phải</b> rơi tự do", "Sức cản không khí đáng kể",
         "Chiếc lá, tờ giấy phẳng, lông chim, giọt mưa nhỏ rơi"],
    ], [110, 160, CONTENT_W - 270], font=8.2))
    s.append(SP(4))
    s.append(formula("v = g·t       h = ½·g·t²       v² = 2·g·h       t = √(2h/g)",
                     "Bốn công thức của rơi tự do (gốc thời gian lúc thả, chiều dương hướng xuống)"))

    s.append(H3("2. Ví dụ mẫu"))
    s.append(P("<b>Ví dụ 1.</b> Thả một vật từ độ cao 45 m, lấy g = 10 m/s². Tính thời gian rơi và vận tốc "
               "khi chạm đất.<br/><i>Giải:</i> t = √(2·45/10) = <b>3 s</b>; v = 10·3 = <b>30 m/s</b>."))
    s.append(P("<b>Ví dụ 2.</b> Cũng bài trên, tính quãng đường vật rơi trong <b>giây cuối cùng</b>."))
    s.append(P("<i>Giải:</i> Quãng đường sau 2 s: h₂ = ½·10·4 = 20 m. Quãng đường trong giây cuối = "
               "45 − 20 = <b>25 m</b>. (Công thức nhanh: Δh = g·(t − 0,5) = 10·2,5 = 25 m.)"))
    s.append(P("<b>Ví dụ 3.</b> Hai vật được thả từ cùng một độ cao, vật 1 thả trước vật 2 đúng 1 s. "
               "Sau khi vật 1 rơi được 3 s, hai vật cách nhau bao xa? (g = 10 m/s²)"))
    s.append(P("<i>Giải:</i> h₁ = ½·10·9 = 45 m; h₂ = ½·10·4 = 20 m → cách nhau <b>25 m</b>. "
               "Nhận xét: khoảng cách tăng dần theo thời gian vì vật 1 luôn nhanh hơn."))
    s.append(box("• Đừng dùng <b>h = v·t</b> cho rơi tự do (v thay đổi liên tục).<br/>"
                 "• “Giây cuối” = h(t) − h(t−1), không phải h(1).<br/>"
                 "• Nếu đề không cho g, hãy dùng <b>g = 9,8 m/s²</b>; nếu đề cho g = 10 thì dùng 10 để "
                 "tính cho gọn.", "bay"))

    s.append(H3("3. So sánh ba loại chuyển động của chương"))
    s.append(table([
        ["Tiêu chí", "Thẳng đều", "Thẳng biến đổi đều", "Rơi tự do"],
        ["Gia tốc", "a = 0", "a = const (a ≠ 0)", "a = g ≈ 9,8 m/s²"],
        ["Vận tốc", "v = const", "v = v₀ + at", "v = g·t"],
        ["Quãng đường", "s = v·t", "s = v₀t + ½at²", "h = ½gt²"],
        ["Đồ thị v–t", "Đường nằm ngang", "Đường thẳng dốc", "Đường thẳng dốc, đi qua gốc"],
    ], [76, 110, 150, CONTENT_W - 336], font=8.1))
    s.append(PageBreak())
    return s

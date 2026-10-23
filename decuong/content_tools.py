# -*- coding: utf-8 -*-
"""PHẦN 2 – Sổ tay công thức & cây quyết định."""
from style import *


def story():
    s = []
    s.append(H1("PHẦN 2 · SỔ TAY CÔNG THỨC & CÂY QUYẾT ĐỊNH"))
    s.append(P("Đây là phần “tra cứu nhanh” – in riêng 2 trang này dán vào bìa vở là đủ dùng cho cả kì.",
               "lead"))
    s.append(SP(3))

    s.append(H2("2.1. Toàn bộ công thức của chương trình giữa kì I"))
    rows = [
        ["Bài", "Đại lượng", "Công thức", "Đơn vị", "Ghi chú"],
        ["3", "Giá trị trung bình", "Ā = (A₁ + … + Aₙ)/n", "theo A", "n ≥ 3 lần đo"],
        ["3", "Sai số ngẫu nhiên TB", "Δ̄A = (ΔA₁ + … + ΔAₙ)/n", "theo A", "ΔAᵢ = |Ā − Aᵢ|"],
        ["3", "Sai số tuyệt đối", "ΔA = Δ̄A + ΔA<sub>đc</sub>", "theo A", "ΔA<sub>đc</sub> = ½ ĐCNN"],
        ["3", "Sai số tỉ đối", "δA = (ΔA/Ā)·100%", "%", "Càng nhỏ càng chính xác"],
        ["3", "Tổng – hiệu", "ΔA = ΔB + ΔC", "theo A", "Cộng sai số tuyệt đối"],
        ["3", "Tích – thương", "δA = δB + δC", "%", "Cộng sai số tỉ đối"],
        ["3", "Ghi kết quả", "A = Ā ± ΔA", "theo A", "Cùng bậc thập phân"],
        ["4", "Độ dịch chuyển (1D)", "Δx = x₂ − x₁", "m", "Vectơ, có dấu"],
        ["5", "Tốc độ trung bình", "v<sub>tb</sub> = s/Δt", "m/s", "Vô hướng"],
        ["5", "Tốc độ tức thời", "v = Δs/Δt (Δt rất nhỏ)", "m/s", "Độ lớn vận tốc tức thời"],
        ["5", "Vận tốc trung bình", "v<sub>tb</sub> = Δd/Δt", "m/s", "Vectơ"],
        ["5", "Chuyển động thẳng đều", "s = v·t", "m", "v không đổi"],
        ["5", "Cộng vận tốc", "v̅<sub>13</sub> = v̅<sub>12</sub> + v̅<sub>23</sub>", "m/s", "Cùng chiều: +; ngược: −; vuông: √"],
        ["5", "Đổi đơn vị", "1 m/s = 3,6 km/h", "—", "km/h → m/s: chia 3,6"],
        ["7", "Vận tốc từ đồ thị", "v = (x₂ − x₁)/(t₂ − t₁)", "m/s", "Độ dốc đồ thị s–t"],
        ["8", "Gia tốc", "a = Δv/Δt = (v₂ − v₁)/(t₂ − t₁)", "m/s²", "Vectơ"],
        ["9", "Vận tốc", "v = v₀ + a·t", "m/s", "Thiếu d → dùng"],
        ["9", "Độ dịch chuyển", "d = v₀t + ½at²", "m", "Thiếu v → dùng"],
        ["9", "Hệ thức liên hệ", "v² − v₀² = 2ad", "—", "Thiếu t → dùng"],
        ["9", "Quãng đường dừng", "s = v₀²/(2|a|) ; t = v₀/|a|", "m ; s", "Chậm dần đến dừng"],
        ["9", "Giây thứ n", "Δs = s(n) − s(n−1) = v₀ + a(n − 0,5)", "m", "Không dùng s(n)/n"],
        ["10", "Vận tốc rơi", "v = g·t", "m/s", "g ≈ 9,8 hoặc 10"],
        ["10", "Quãng đường rơi", "h = ½gt²", "m", "Tính từ lúc thả"],
        ["10", "Liên hệ", "v² = 2gh ; t = √(2h/g)", "—", "Không chứa t / không chứa v"],
    ]
    s.append(table(rows, [26, 96, 150, 46, CONTENT_W - 318], font=7.9,
                   align=["c", "l", "l", "c", "l"]))
    s.append(SP(5))

    s.append(H2("2.2. Hằng số và đổi đơn vị"))
    s.append(table([
        ["Đại lượng", "Đơn vị hợp pháp", "Đổi thường gặp"],
        ["Độ dài", "mét (m)", "1 km = 1000 m; 1 cm = 0,01 m; 1 mm = 0,001 m"],
        ["Thời gian", "giây (s)", "1 phút = 60 s; 1 h = 3600 s"],
        ["Vận tốc", "m/s", "1 km/h = 1/3,6 m/s; 1 m/s = 3,6 km/h"],
        ["Gia tốc", "m/s²", "1 km/h² ≈ 7,7×10⁻⁵ m/s² (rất ít dùng)"],
        ["Gia tốc rơi tự do", "m/s²", "g ≈ 9,8 m/s²; nhiều đề lấy g = 10 m/s²"],
    ], [108, 100, CONTENT_W - 208], font=8.2))
    s.append(SP(4))
    s.append(box("Đổi <b>km/h → m/s</b>: chia 3,6 (54 km/h = 15 m/s; 36 km/h = 10 m/s; 72 km/h = 20 m/s). "
                 "Đổi <b>m/s → km/h</b>: nhân 3,6. Hãy ghi ngay 3 cặp số này ra lề đề trước khi làm bài.",
                 "meo"))

    s.append(H2("2.3. Cây quyết định khi gặp một bài toán động học"))
    s.append(table([
        ["Bước", "Câu hỏi tự đặt", "Việc phải làm"],
        ["1", "Đề cho những đại lượng nào? Cần tìm gì?", "Tóm tắt bằng kí hiệu: v₀, v, a, t, s/d, g…"],
        ["2", "Chuyển động thuộc loại nào?",
         "v không đổi → thẳng đều (s = vt). a không đổi → biến đổi đều. Chỉ có trọng lực → rơi tự do."],
        ["3", "Chọn chiều dương ở đâu?", "Thường chọn chiều chuyển động ban đầu; ghi rõ vào bài làm"],
        ["4", "Công thức nào chứa đủ 3 đại lượng đã biết + 1 đại lượng cần tìm?",
         "Thiếu t → dùng v² − v₀² = 2ad; thiếu v → dùng d = v₀t + ½at²; thiếu d → dùng v = v₀ + at"],
        ["5", "Có lúc nào vật dừng/đổi chiều không?", "Nếu có: tính t<sub>dừng</sub> = v₀/|a| rồi chia chặng"],
        ["6", "Đơn vị đã đồng nhất chưa?", "Đổi km/h → m/s, cm → m <b>trước</b> khi thay số"],
        ["7", "Kết quả có hợp lí không?", "Kiểm tra bậc độ lớn, dấu, đơn vị; ghi đáp số kèm đơn vị"],
    ], [38, 170, CONTENT_W - 208], font=8.0, align=["c", "l", "l"]))
    s.append(SP(5))

    s.append(H2("2.4. Từ khoá trong đề → công thức cần dùng"))
    s.append(table([
        ["Cụm từ trong đề", "Công thức / cách xử lí"],
        ["“bắt đầu chuyển động”, “thả nhẹ”, “khởi hành”", "v₀ = 0"],
        ["“dừng lại”, “hãm phanh đến khi dừng”", "v = 0; dùng s = v₀²/(2|a|)"],
        ["“chuyển động đều”, “vận tốc không đổi”", "a = 0; s = v·t"],
        ["“nhanh dần đều”", "a cùng dấu v₀ (chọn chiều dương theo chuyển động thì a &gt; 0)"],
        ["“chậm dần đều”", "a trái dấu v₀ (thường a &lt; 0)"],
        ["“trong giây thứ n”", "Δs = s(n) − s(n−1)"],
        ["“sau n giây”", "s(n) = v₀n + ½a·n²"],
        ["“quãng đường trong giây cuối” (rơi)", "Δh = h(t) − h(t−1) = g(t − 0,5)"],
        ["“vận tốc chạm đất”", "v = √(2gh) hoặc v = g·t"],
        ["“độ dịch chuyển” khác “quãng đường”", "Δx = x₂ − x₁; s = tổng |Δx| từng đoạn"],
        ["“tốc độ trung bình trên cả quãng đường”", "v<sub>tb</sub> = tổng s / tổng t (không lấy trung bình cộng)"],
        ["“thuyền, ca nô, máy bay, người đi trên thang cuốn”", "cộng vận tốc v₁₃ = v₁₂ + v₂₃"],
        ["“đồ thị là đường thẳng dốc”", "v = độ dốc; a = 0 nếu s–t, a = độ dốc nếu v–t"],
        ["“hai vật gặp nhau”", "viết x₁(t), x₂(t); giải x₁ = x₂"],
    ], [CONTENT_W * 0.46, CONTENT_W * 0.54], font=8.0))
    s.append(SP(5))
    s.append(box("<b>Quy tắc 3 giây:</b> trước khi bấm máy tính, hãy viết ra giấy <b>công thức chữ</b> → "
                 "<b>thay số có đơn vị</b> → <b>ra kết quả có đơn vị</b>. Ba dòng này chính là ba điểm "
                 "trình bày mà giám khảo chấm.", "thi"))
    s.append(PageBreak())
    return s

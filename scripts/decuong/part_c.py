# -*- coding: utf-8 -*-
"""Phần C – Sổ tay công thức và kỹ năng."""
from __future__ import annotations

from .style import CONTENT_W, P, SPC, box, data_table, formula


def part_c():
    f = []
    f.append(P("PHẦN C · SỔ TAY CÔNG THỨC & KỸ NĂNG", "h1"))
    f.append(P("Trang này là “phao cứu sinh” trước giờ thi: học thuộc bảng dưới đây là em đã giữ chắc phần lớn "
               "số điểm của đề.", "body"))

    f.append(P("C1. Toàn bộ công thức trong học kì I", "h2"))
    f.append(data_table(
        ["Bài", "Đại lượng – công thức", "Ghi nhớ nhanh"],
        [
            ["3", "Ā = (A₁+…+A<sub>n</sub>)/n ; ΔA<sub>i</sub> = |Ā − A<sub>i</sub>| ; ΔĀ = ΣΔA<sub>i</sub>/n<br/>"
                  "ΔA = ΔĀ + ΔA<sub>dc</sub> ; δA = (ΔA/Ā)·100% ; <b>A = Ā ± ΔA</b>",
             "ΔA<sub>dc</sub> = nửa ĐCNN; ΔA và Ā cùng bậc thập phân"],
            ["4", "Δd = d₂ − d₁ ; |Δd| ≤ s", "Thẳng, không đổi chiều thì |Δd| = s"],
            ["5", "v<sub>tb</sub> = s/Δt ; <b>v</b><sub>tb</sub> = Δ<b>d</b>/Δt<br/>"
                  "v₁₃ = v₁₂ + v₂₃ (cùng chiều: +; ngược chiều: −; vuông góc: √(v₁₂²+v₂₃²))",
             "1 km/h = 1/3,6 m/s"],
            ["7", "v = Δd/Δt = độ dốc của đồ thị d – t", "Đường ngang → v = 0"],
            ["8", "a = Δv/Δt = (v − v₀)/t ; đơn vị m/s²", "a cùng chiều v → nhanh dần"],
            ["9", "v = v₀ + at ; s = v₀t + ½at² ; v² − v₀² = 2as ; x = x₀ + v₀t + ½at²<br/>"
                  "v₀ = 0: s = ½at², v = at ; dừng lại: t = v₀/|a|, s = v₀²/(2|a|)",
             "Không có t → dùng v² − v₀² = 2as"],
            ["10", "v = gt ; s = ½gt² ; v² = 2gs ; t = √(2s/g)", "Quãng đường 1 s – 2 s – 3 s: 1 : 4 : 9"],
        ],
        [28, 330, 153], align=["CENTER", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(6))

    f.append(P("C2. Đổi đơn vị – bảng cần thuộc", "h2"))
    f.append(data_table(
        ["Đại lượng", "Đổi", "Ví dụ"],
        [
            ["Vận tốc", "1 km/h = 1/3,6 m/s ≈ 0,278 m/s; 1 m/s = 3,6 km/h", "36 km/h = 10 m/s; 54 km/h = 15 m/s; 72 km/h = 20 m/s"],
            ["Độ dài", "1 cm = 0,01 m; 1 mm = 0,001 m; 1 km = 1000 m", "45 cm = 0,45 m"],
            ["Thời gian", "1 phút = 60 s; 1 h = 3600 s", "0,5 phút = 30 s"],
            ["Diện tích", "1 cm² = 10⁻⁴ m²", "20 cm² = 2·10⁻³ m²"],
        ],
        [68, 226, 217], align=["LEFT", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(6))

    f.append(P("C3. Quy tắc ghi kết quả và làm tròn", "h2"))
    f.append(box("Ba quy tắc bắt buộc", [
        P("<b>1.</b> Sai số tuyệt đối ΔA viết đến <b>1 hoặc 2 chữ số có nghĩa</b>, cùng bậc với ĐCNN.", "box_item"),
        P("<b>2.</b> Giá trị trung bình Ā viết đến <b>cùng bậc thập phân</b> với ΔA.", "box_item"),
        P("<b>3.</b> Làm tròn: chữ số bỏ đi ≥ 5 thì tăng chữ số bên trái 1 đơn vị; < 5 thì giữ nguyên.", "box_item"),
    ], "def"))

    f.append(P("C4. Kỹ năng đọc – vẽ đồ thị", "h2"))
    f.append(data_table(
        ["Câu hỏi của đề", "Cách làm"],
        [
            ["Vận tốc từ đồ thị d – t", "Lấy hai điểm bất kì: v = (d₂ − d₁)/(t₂ − t₁) = độ dốc"],
            ["Vật đứng yên?", "Đồ thị là đoạn nằm ngang"],
            ["Vật đi ngược chiều dương?", "Đồ thị dốc xuống (d giảm theo t)"],
            ["Vị trí tại thời điểm t", "Đọc tung độ tại hoành độ t"],
            ["Quãng đường trong khoảng thời gian", "Nếu không đổi chiều: |Δd|; nếu đổi chiều: cộng |Δd| từng đoạn"],
            ["Gia tốc từ đồ thị v – t", "Độ dốc của đường v – t"],
            ["Độ dịch chuyển từ đồ thị v – t", "Diện tích hình giới hạn bởi đồ thị và trục Ot"],
        ],
        [176, 335], align=["LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(6))

    f.append(P("C5. Những cặp khái niệm dễ nhầm", "h2"))
    f.append(data_table(
        ["Cặp khái niệm", "Phân biệt trong một dòng"],
        [
            ["Quãng đường – Độ dịch chuyển", "Quãng đường: vô hướng, phụ thuộc đường đi. Độ dịch chuyển: vectơ, chỉ phụ thuộc điểm đầu – cuối"],
            ["Tốc độ – Vận tốc", "Tốc độ: vô hướng, s/Δt. Vận tốc: vectơ, Δd/Δt"],
            ["Vận tốc – Gia tốc", "Vận tốc: vị trí thay đổi nhanh hay chậm. Gia tốc: vận tốc thay đổi nhanh hay chậm"],
            ["Nhanh dần – Chậm dần", "So <b>chiều</b>: a cùng chiều v → nhanh dần; a ngược chiều v → chậm dần"],
            ["Sai số hệ thống – Sai số ngẫu nhiên", "Hệ thống: lặp lại, do dụng cụ, hiệu chỉnh được. Ngẫu nhiên: thay đổi mỗi lần, giảm bằng đo nhiều lần"],
            ["Sai số tuyệt đối – Sai số tỉ đối", "Tuyệt đối: cùng đơn vị với đại lượng. Tỉ đối: %, cho biết độ chính xác"],
            ["Rơi tự do – Rơi trong không khí", "Rơi tự do: chỉ có trọng lực. Rơi trong không khí: thêm lực cản, có thể không đều"],
        ],
        [150, 361], align=["LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(6))

    f.append(box("Bốn công thức “cứu điểm” khi quên bài", [
        P("Không có thời gian → <b>v² − v₀² = 2as</b>.", "box_item"),
        P("Không có gia tốc → <b>s = (v₀ + v)·t/2</b>.", "box_item"),
        P("Vật dừng lại → <b>s = v₀²/(2|a|)</b> và <b>t = v₀/|a|</b>.", "box_item"),
        P("Rơi tự do → <b>t = √(2h/g)</b>, <b>v = √(2gh)</b>.", "box_item"),
    ], "tip"))
    return f


# =========================================================================== #
def part_c2():
    """C6 – C7: các dạng bài vận dụng và bộ câu đúng/sai hay gặp."""
    f = []
    f.append(P("C6. Sáu dạng bài vận dụng phải làm được", "h2"))
    f.append(data_table(
        ["Dạng bài", "Nhận diện", "Đường đi ngắn nhất"],
        [
            ["1. Cộng vận tốc", "Có “so với nước / so với bờ”, thuyền, ca nô, máy bay",
             "Cùng chiều: cộng · Ngược chiều: trừ · Vuông góc: Py-ta-go"],
            ["2. Tăng tốc đều", "“tăng tốc đều”, cho v₀, v, t",
             "a = (v − v₀)/t rồi s = v₀t + ½at²"],
            ["3. Hãm phanh – dừng lại", "“hãm phanh”, “dừng lại sau …”, cho v₀ và s hoặc t",
             "v = 0 → v₀² = 2|a|s ; t = v₀/|a|"],
            ["4. Quãng đường trong giây thứ n", "“giây thứ n”, “giây cuối”",
             "Δs = s(n) − s(n − 1)"],
            ["5. Rơi tự do", "“rơi tự do”, “thả rơi”, cho độ cao h",
             "t = √(2h/g) → v = gt hoặc v = √(2gh)"],
            ["6. Đọc đồ thị", "Cho hình vẽ d – t hoặc v – t",
             "d – t: độ dốc = v · v – t: độ dốc = a, diện tích = s"],
        ],
        [124, 176, 211], align=["LEFT", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(6))

    f.append(P("C7. 12 câu đúng – sai “kinh điển” (tự trả lời trước khi xem đáp án)", "h2"))
    f.append(data_table(
        ["#", "Phát biểu", "Đ/S"],
        [
            ["1", "Quãng đường là đại lượng vectơ.", "<b>S</b>"],
            ["2", "Độ lớn độ dịch chuyển không lớn hơn quãng đường.", "<b>Đ</b>"],
            ["3", "Tốc độ trung bình luôn bằng độ lớn vận tốc trung bình.", "<b>S</b>"],
            ["4", "Trên đồ thị d – t, đoạn nằm ngang ứng với vật đứng yên.", "<b>Đ</b>"],
            ["5", "Độ dốc của đồ thị d – t là vận tốc của vật.", "<b>Đ</b>"],
            ["6", "Gia tốc đặc trưng cho mức độ thay đổi của vận tốc.", "<b>Đ</b>"],
            ["7", "Gia tốc âm thì vật luôn chuyển động chậm dần.", "<b>S</b>"],
            ["8", "Trong chuyển động thẳng nhanh dần đều, a cùng chiều với v.", "<b>Đ</b>"],
            ["9", "Công thức v² − v₀² = 2as dùng được khi vật đổi chiều.", "<b>Đ</b>"],
            ["10", "Hai vật khác khối lượng rơi tự do từ cùng độ cao thì chạm đất cùng lúc.", "<b>Đ</b>"],
            ["11", "Trong không khí, tờ giấy vo tròn rơi nhanh hơn tờ giấy để phẳng.", "<b>Đ</b>"],
            ["12", "Sai số dụng cụ thường được lấy bằng một độ chia nhỏ nhất.", "<b>S</b> (nửa ĐCNN)"],
        ],
        [22, 380, 109], align=["CENTER", "LEFT", "LEFT"], font="tbl_small",
    ))
    return f

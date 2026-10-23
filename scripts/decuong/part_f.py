# -*- coding: utf-8 -*-
"""Phần F – Checklist thuộc bài, lỗi thường gặp và trang ghi chú."""
from __future__ import annotations

from .style import CONTENT_W, P, SPC, box, data_table

CHECK = [
    ("Bài 1", [
        "Nêu được đối tượng nghiên cứu của Vật lí",
        "Kể tên 4 cuộc cách mạng công nghiệp và thành tựu tương ứng",
        "Phân biệt phương pháp thực nghiệm và phương pháp lí thuyết",
    ]),
    ("Bài 2", [
        "Liệt kê được 5 nguy cơ mất an toàn trong phòng thực hành",
        "Nêu 5 quy tắc an toàn cơ bản",
        "Nhận ra biển cấm – biển cảnh báo – biển chỉ dẫn theo màu sắc",
    ]),
    ("Bài 3", [
        "Phân biệt phép đo trực tiếp và gián tiếp",
        "Viết đúng 5 công thức: Ā, ΔA<sub>i</sub>, ΔĀ, ΔA, δA",
        "Biết ΔA<sub>dc</sub> = nửa ĐCNN và cách ghi A = Ā ± ΔA",
    ]),
    ("Bài 4", [
        "Phát biểu được định nghĩa độ dịch chuyển (vectơ) và quãng đường",
        "So sánh được hai đại lượng, nêu khi nào |Δd| = s",
        "Tính được độ dịch chuyển tổng hợp khi hai đoạn vuông góc",
    ]),
    ("Bài 5", [
        "Viết công thức tốc độ trung bình và vận tốc trung bình",
        "Phân biệt tốc độ – vận tốc, tốc độ trung bình – tốc độ tức thời",
        "Áp dụng thành thạo 3 trường hợp cộng vận tốc",
    ]),
    ("Bài 6", [
        "Nêu nguyên tắc đo tốc độ bằng cổng quang điện",
        "Phân biệt MODE A, B, A + B, A ↔ B",
        "Nêu 2 ưu điểm và 2 nhược điểm của đồng hồ hiện số",
    ]),
    ("Bài 7", [
        "Đọc được độ dốc của đồ thị d – t thành vận tốc",
        "Nhận ra vật đứng yên / đi ngược chiều qua đồ thị",
        "Tính được quãng đường và độ dịch chuyển từ đồ thị",
    ]),
    ("Bài 8", [
        "Nêu định nghĩa và đơn vị của gia tốc",
        "Viết công thức a = Δv/Δt và tính đúng dấu",
        "Xác định nhanh dần / chậm dần dựa vào chiều của a và v",
    ]),
    ("Bài 9", [
        "Thuộc 4 công thức: v, s, v² − v₀², x",
        "Giải được bài toán tăng tốc và hãm phanh",
        "Biết quãng đường trong giây thứ n và đồ thị v – t",
    ]),
    ("Bài 10", [
        "Nêu định nghĩa, phương, chiều, tính chất chuyển động khi rơi tự do",
        "Thuộc 4 công thức: v, s, v² = 2gs, t = √(2s/g)",
        "Giải thích được vì sao giấy phẳng rơi chậm hơn giấy vo tròn",
    ]),
]


def part_f():
    f = []
    f.append(P("PHẦN F · CHECKLIST “ĐÃ THUỘC BÀI” & LỖI CẦN TRÁNH", "h1"))
    f.append(P("Hãy đánh dấu □ vào từng dòng chỉ khi em có thể <b>nói lại mà không cần mở vở</b>. "
               "Còn ô trống nào là còn điểm có thể mất.", "body"))

    f.append(P("F1. Checklist 30 mục", "h2"))
    for lesson, items in CHECK:
        f.append(P(f"<b>{lesson}</b>", "h3"))
        for it in items:
            f.append(P(f"□  {it}", "opt"))
        f.append(SPC(2))

    f.append(SPC(4))
    f.append(P("F2. Mười lỗi làm mất điểm oan nhất", "h2"))
    f.append(data_table(
        ["#", "Lỗi", "Cách tránh"],
        [
            ["1", "Không đổi km/h → m/s", "Nhìn thấy km/h là chia ngay 3,6"],
            ["2", "Bỏ đơn vị ở kết quả", "Mọi con số phải có đơn vị"],
            ["3", "Nhầm tốc độ với vận tốc", "Vận tốc phải có chiều (dấu)"],
            ["4", "Quên cộng sai số dụng cụ", "ΔA = ΔĀ + ΔA<sub>dc</sub>"],
            ["5", "Viết kết quả đo lệch bậc", "Ā cùng bậc thập phân với ΔA"],
            ["6", "Nhầm “giây thứ n” với “n giây”", "Giây thứ n: từ t = n − 1 đến t = n"],
            ["7", "Cho rằng a âm là chậm dần", "So sánh chiều a với v"],
            ["8", "Đọc độ dốc đồ thị bằng độ cao", "v = Δd/Δt, không phải d/t"],
            ["9", "Không chọn chiều dương", "Ghi chiều dương ngay đầu bài"],
            ["10", "Bỏ trống câu khó", "Đoán cũng có xác suất, đừng để trống"],
        ],
        [24, 216, 271], align=["CENTER", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(8))

    f.append(box("Ba câu thần chú trước khi vào phòng thi", [
        P("<b>1.</b> “Đơn vị – Chiều dương – Dấu.”", "box_item"),
        P("<b>2.</b> “Câu dễ làm trước, câu khó quay lại.”", "box_item"),
        P("<b>3.</b> “Đã viết công thức là có điểm.”", "box_item"),
    ], "tip"))
    f.append(SPC(10))

    f.append(P("F3. Trang ghi chú của em", "h2"))
    f.append(P("Ghi lại những lỗi em từng mắc, công thức hay quên, hoặc câu hỏi cần hỏi lại thầy cô.", "small"))
    f.append(SPC(4))
    return f

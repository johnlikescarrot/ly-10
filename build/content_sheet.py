# -*- coding: utf-8 -*-
"""PHẦN B – Sổ tay công thức, đổi đơn vị và bảng bẫy."""

from reportlab.lib.units import cm
from doc_kit import *  # noqa


def build(d: Doc):
    d.pb()
    d.h1("SỔ TAY CÔNG THỨC & BẢNG BẪY", kicker="Phần B · In riêng 3 trang này để ôn nhanh")
    d.lead("Toàn bộ công thức của học kì I trên một trang – kèm đơn vị và điều kiện áp dụng.")

    d.h2("B.1 · Đại lượng – công thức – đơn vị")
    d.table(
        ["Đại lượng", "Công thức", "Đơn vị", "Điều kiện / ghi chú"],
        [
            ["Giá trị trung bình", "Ā = (A₁ + … + Aₙ)/n", "theo đại lượng", "n ≥ 3 lần đo"],
            ["Sai số tuyệt đối", "ΔA = ΔĀ + ΔA(dc)", "theo đại lượng", "ΔĀ là sai số ngẫu nhiên trung bình"],
            ["Sai số tỉ đối", "δA = (ΔA/Ā)·100%", "%", "Đánh giá độ chính xác tương đối"],
            ["Sai số gián tiếp", "Δ(x±y) = Δx + Δy; δ(x·y) = δx + δy", "—", "Luỹ thừa n: δ = n·δx"],
            ["Độ dịch chuyển", "Δd = d₂ − d₁ (vectơ)", "m", "Nối điểm đầu → điểm cuối"],
            ["Quãng đường", "s = Σ|Δdᵢ|", "m", "Luôn ≥ 0, không giảm"],
            ["Tốc độ trung bình", "v = s/Δt", "m/s", "Dùng quãng đường"],
            ["Vận tốc trung bình", "v = Δd/Δt (vectơ)", "m/s", "Dùng độ dịch chuyển"],
            ["Cộng vận tốc", "v₁₃ = v₁₂ + v₂₃ (vectơ)", "m/s", "Xuôi cộng – ngược trừ – vuông Pythagore"],
            ["Gia tốc", "a = Δv/Δt = (v₂ − v₁)/(t₂ − t₁)", "m/s²", "Đại lượng vectơ"],
            ["Vận tốc (CĐTBĐĐ)", "v = v₀ + at", "m/s", "a không đổi"],
            ["Độ dịch chuyển", "d = v₀t + ½at²", "m", "Không đổi chiều thì d = s"],
            ["Hệ thức độc lập", "v² − v₀² = 2ad", "—", "Không cần biết thời gian"],
            ["Quãng đường giây thứ n", "Δs = v₀ + a(n − 0,5)", "m", "Chỉ khi không đổi chiều"],
            ["Rơi tự do", "v = gt; h = ½gt²; v² = 2gh", "m/s; m", "v₀ = 0, bỏ qua lực cản"],
            ["Thời gian rơi", "t = √(2h/g)", "s", "Suy từ h = ½gt²"],
            ["Rơi – giây thứ n", "Δs = ½g(2n − 1)", "m", "Quãng đường tỉ lệ 1 : 3 : 5 : 7"],
            ["Ném lên – độ cao cực đại", "H = v₀²/(2g)", "m", "Tại đỉnh v = 0"],
        ],
        widths=[3.6 * cm, 6.1 * cm, 2.3 * cm, 5.1 * cm], font_size=8.0)

    d.h2("B.2 · Đổi đơn vị – bảng “chia 3,6”")
    d.table(
        ["Từ", "Sang", "Cách đổi", "Ví dụ"],
        [
            ["km/h", "m/s", "chia 3,6", "72 km/h = 20 m/s; 36 km/h = 10 m/s; 54 km/h = 15 m/s"],
            ["m/s", "km/h", "nhân 3,6", "10 m/s = 36 km/h"],
            ["cm/s", "m/s", "chia 100", "50 cm/s = 0,5 m/s"],
            ["km", "m", "nhân 1000", "1,5 km = 1500 m"],
            ["phút", "giây", "nhân 60", "0,5 phút = 30 s"],
        ],
        widths=[2.2 * cm, 2.0 * cm, 2.8 * cm, 10.1 * cm], font_size=8.2)

    d.h2("B.3 · Sơ đồ chọn công thức – “đề cho gì, dùng nấy”")
    d.table(
        ["Đề cho", "Đề hỏi", "Dùng"],
        [
            ["v₀; a; t", "v", "v = v₀ + at"],
            ["v₀; a; t", "d (hoặc s)", "d = v₀t + ½at²"],
            ["v₀; v; d", "a", "a = (v² − v₀²)/(2d)"],
            ["v₀; a; d", "v", "v = √(v₀² + 2ad)"],
            ["v₀; v; t", "d", "d = (v₀ + v)t/2"],
            ["h (rơi tự do)", "t", "t = √(2h/g)"],
            ["h (rơi tự do)", "v chạm đất", "v = √(2gh)"],
            ["tổng thời gian T", "quãng đường giây cuối", "Δs = ½g(2T − 1)"],
        ],
        widths=[4.4 * cm, 5.0 * cm, 7.7 * cm], font_size=8.2)

    d.h2("B.4 · 14 lỗi mất điểm – đọc trước khi vào phòng thi")
    d.table(
        ["#", "Lỗi", "Cách phòng"],
        [
            ["1", "Không đổi km/h sang m/s", "Thấy km/h là đổi ngay ở dòng đầu bài làm"],
            ["2", "Nhầm quãng đường với độ dịch chuyển", "Hỏi “đi bao xa” → s; hỏi “dịch chuyển” → vectơ Δd"],
            ["3", "Tính tốc độ trung bình bằng trung bình cộng", "Luôn dùng s/Δt"],
            ["4", "Quên sai số dụng cụ", "ΔA = ΔĀ + ΔA(dc)"],
            ["5", "Cộng sai số tuyệt đối khi nhân/chia", "Nhân chia → cộng sai số tỉ đối"],
            ["6", "Kết luận nhanh/chậm dần chỉ dựa vào dấu của a", "So sánh dấu a với dấu v"],
            ["7", "Áp dụng công thức sau khi vật đã dừng", "Kiểm tra t(dừng) = −v₀/a"],
            ["8", "Nhầm “trong n giây” với “trong giây thứ n”", "Gạch chân cụm từ khoá trong đề"],
            ["9", "Nhầm đồ thị d–t và v–t", "Nhìn tên trục tung trước khi đọc đồ thị"],
            ["10", "Tính quãng đường bằng |d cuối − d đầu| khi đổi chiều", "Chia đoạn, cộng trị tuyệt đối"],
            ["11", "Dùng g = 9,8 khi đề cho g = 10", "Ghi g ngay dưới đề bài"],
            ["12", "Quên đơn vị ở kết quả", "Mỗi con số phải kèm đơn vị"],
            ["13", "Làm tròn sai số quá nhiều chữ số", "Sai số 1–2 chữ số có nghĩa"],
            ["14", "Tô đáp án lệch dòng ở phiếu trả lời", "Tô theo câu, kiểm tra 3 phút cuối"],
        ],
        widths=[0.9 * cm, 7.4 * cm, 8.8 * cm], font_size=8.1, aligns=["C", "L", "L"])

    d.box("tip",
          "<b>Quy tắc 30 giây cuối mỗi bài tự luận:</b> đọc lại đề → kiểm tra đơn vị → kiểm tra dấu của a → "
          "kiểm tra xem câu hỏi có yêu cầu “tính quãng đường” hay “độ dịch chuyển”. Bốn bước này thường “cứu” "
          "được 0,5 – 1 điểm.",
          title="MẸO PHÒNG THI")
    d.pb()

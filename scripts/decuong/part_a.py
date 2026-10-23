# -*- coding: utf-8 -*-
"""Phần A – Phân tích đề, ma trận và chiến lược ôn thi."""
from __future__ import annotations

from reportlab.platypus import Spacer

from .style import (
    BG_SOFT, CONTENT_W, LINE, P, S, SPC, bullets, box, data_table, formula,
    numbered, rule,
)


def part_a():
    f = []
    f.append(P("PHẦN A · HIỂU ĐỀ ĐỂ ÔN ĐÚNG TRỌNG TÂM", "h1"))

    f.append(P(
        "Đề kiểm tra giữa kì I môn Vật lí 10 gồm <b>bốn phần</b>, thời gian <b>50 phút</b>, cấu trúc "
        "<b>70% trắc nghiệm – 30% tự luận</b>. Điều quan trọng nhất: đề <b>không dàn đều</b> cho 10 bài. "
        "Bài 5, 7, 9, 10 chiếm phần lớn số câu, trong đó <b>Bài 9 (chuyển động thẳng biến đổi đều)</b> "
        "xuất hiện ở <b>cả bốn phần</b> – đây là “trọng tâm của trọng tâm”.", "body"))

    f.append(SPC(2))
    f.append(box("Tài liệu gốc là ma trận – không phải đề bài", [
        P("Tệp thầy cô gửi là <b>ma trận đề + bản đặc tả</b>: nó quy định <b>cấu trúc, số câu, mức độ và nội dung</b> "
          "của đề kiểm tra, nhưng <b>không kèm nội dung từng câu hỏi</b>.", "box_item"),
        P("Vì vậy tài liệu này <b>không in lại “đề thật”</b>. Thay vào đó, <b>Phần D</b> là đề mô phỏng được biên soạn "
          "<b>đúng từng ô của ma trận</b> – đủ 18 câu phần I, 2 câu × 4 ý phần II, 2 câu phần III, 3 ý phần IV, phân bổ "
          "theo đúng 9 đơn vị kiến thức – kèm <b>đáp án và lời giải chi tiết</b>.", "box_item"),
        P("Nếu có thêm <b>đề minh hoạ hoặc đề chính thức</b>, chỉ cần thay bộ câu hỏi ở Phần D bằng đề đó; toàn bộ "
          "phần lý thuyết, công thức và kỹ năng phía trước giữ nguyên giá trị.", "box_item"),
    ], "note"))

    # ------------------------------------------------------------------ A1
    f.append(P("A1. Cấu trúc đề kiểm tra", "h2"))
    f.append(data_table(
        ["Phần", "Hình thức", "Số câu / số ý", "Mức độ", "Điểm (gợi ý)", "Thời gian"],
        [
            ["<b>I</b>", "Trắc nghiệm nhiều lựa chọn", "18 câu", "10 Biết + 8 Hiểu", "4,5", "≈ 20 phút"],
            ["<b>II</b>", "Trắc nghiệm đúng – sai", "2 câu × 4 ý = 8 ý", "6 ý Biết + 2 ý Hiểu", "2,0", "≈ 10 phút"],
            ["<b>III</b>", "Tự luận ngắn", "2 câu", "1 Biết + 1 Hiểu", "0,5", "≈ 7 phút"],
            ["<b>IV</b>", "Tự luận vận dụng", "3 ý", "1 Hiểu + 2 Vận dụng", "3,0", "≈ 13 phút"],
            ["<b>Tổng</b>", "70% TN – 30% TL", "18 câu + 8 ý + 5 ý", "—", "<b>10,0</b>", "<b>50 phút</b>"],
        ],
        [38, 132, 106, 108, 66, 61],
        align=["CENTER", "LEFT", "LEFT", "LEFT", "CENTER", "CENTER"], font="tbl_small",
    ))
    f.append(P("Ghi chú: ma trận gốc chỉ nêu tỉ lệ <b>70% trắc nghiệm – 30% tự luận</b>; thang điểm chi tiết do giáo viên "
               "quy định. Cách chia ở trên là phương án tham khảo thường dùng (trắc nghiệm 6,5 điểm – tự luận 3,5 điểm, "
               "tổng 10,0). Hãy hỏi lại thầy cô nếu lớp có thang điểm riêng.", "small"))
    f.append(SPC(4))

    f.append(box("Cách tính điểm phần II (đúng – sai) mà em cần biết", [
        P("Mỗi câu có 4 ý a), b), c), d). Điểm của cả câu <b>không</b> chia đều cho 4 ý mà tính theo số ý đúng:", "box_item"),
        P("<b>1 ý đúng → 0,1 · 2 ý đúng → 0,25 · 3 ý đúng → 0,5 · 4 ý đúng → 1,0 điểm</b> (trên thang 1 điểm/câu).", "box_item"),
        P("Vì vậy <b>đừng bỏ trống</b> một ý nào: chỉ cần thêm 1 ý đúng có thể nhảy từ 0,5 lên 1,0 điểm.", "box_item"),
    ], "tip"))

    # ------------------------------------------------------------------ A2
    from reportlab.platypus import KeepTogether
    f.append(KeepTogether([
        P("A2. Ma trận phân bổ câu hỏi theo từng bài", "h2"),
        P("Bảng dưới đây là bản rút gọn trung thành với ma trận gốc – <b>số câu của em nằm ở đây</b>:", "body"),
        data_table(
        ["Đơn vị kiến thức", "P.I<br/>Biết", "P.I<br/>Hiểu", "P.II<br/>(ý)", "P.III", "P.IV", "Tổng"],
        [
            ["1.1. Làm quen với Vật lí", "1", "–", "–", "–", "–", "1"],
            ["1.2. Quy tắc an toàn phòng thực hành", "1", "1", "–", "–", "–", "2"],
            ["1.3. Sai số trong phép đo. Ghi kết quả", "1", "–", "–", "–", "–", "1"],
            ["2.1. Độ dịch chuyển và quãng đường", "1", "2", "–", "–", "–", "3"],
            ["2.2. Tốc độ và vận tốc", "1", "–", "2 (câu 1)", "1 Biết", "1 Hiểu", "<b>5</b>"],
            ["2.3. Đồ thị độ dịch chuyển – thời gian", "1", "1", "2 (câu 1)", "–", "–", "<b>4</b>"],
            ["2.4. Chuyển động biến đổi. Gia tốc", "1", "1", "–", "–", "–", "2"],
            ["2.5. Chuyển động thẳng biến đổi đều", "2", "1", "2B + 2H (câu 2)", "–", "2 Vận dụng", "<b>9</b>"],
            ["2.6. Sự rơi tự do", "1", "2", "–", "1 Hiểu", "–", "<b>4</b>"],
            ["<b>Tổng</b>", "<b>10</b>", "<b>8</b>", "<b>6 Biết + 2 Hiểu</b>", "<b>1 Biết + 1 Hiểu</b>", "<b>1 Hiểu + 2 Vận dụng</b>", "<b>18 câu + 13 ý</b>"],
        ],
        [201, 38, 38, 78, 56, 62, 38],
        align=["LEFT", "CENTER", "CENTER", "CENTER", "CENTER", "CENTER", "CENTER"], font="tbl_small",
    )]))
    f.append(SPC(3))
    from .figures import fig_matrix_bars
    f.append(fig_matrix_bars())
    f.append(P("Cột càng dài thì phần đó càng “nặng điểm”: Bài 9 chiếm gần một phần ba tổng số câu/ý của đề.", "cap"))
    f.append(SPC(5))
    f.append(box("Đọc ra điều gì?", [
        P("<b>Bài 9 (chuyển động thẳng biến đổi đều)</b> là bài “nặng” nhất: 3 câu phần I + 4 ý đúng/sai + 2 câu vận dụng.", "box_item"),
        P("<b>Bài 10 (rơi tự do)</b> có 3 câu phần I + 1 câu tự luận ngắn → học kĩ công thức và đặc điểm rơi.", "box_item"),
        P("<b>Bài 5 và Bài 7</b> xuất hiện ở phần đúng/sai và tự luận → nắm chắc khái niệm và đồ thị.", "box_item"),
        P("<b>Bài 1, 2, 3, 4, 8</b> chủ yếu ra ở mức Biết – Hiểu: học thuộc định nghĩa, quy tắc, công thức là đủ điểm.", "box_item"),
        P("Bài 6 (thực hành đo tốc độ) <b>không có câu trong ma trận</b> nhưng nằm trong đặc tả → đọc để phòng câu hỏi thực hành.", "box_item"),
    ], "def"))

    # ------------------------------------------------------------------ A3
    f.append(P("A3. Ba tầng kiến thức phải học", "h2"))
    f.append(data_table(
        ["Tầng", "Chiếm bao nhiêu", "Em cần làm gì"],
        [
            ["<b>Biết</b> – nhận ra, phát biểu lại", "10 câu P.I + 6 ý P.II + 1 câu P.III", "Học thuộc định nghĩa, công thức, đơn vị, quy tắc an toàn, kí hiệu"],
            ["<b>Hiểu</b> – giải thích, phân biệt", "8 câu P.I + 2 ý P.II + 1 câu P.III + 1 ý P.IV", "Lập bảng so sánh, tự hỏi “vì sao”, làm ví dụ mẫu"],
            ["<b>Vận dụng</b> – tính toán", "2 câu P.IV", "Luyện 8 dạng bài ở Phần D – E, viết đủ bước và đơn vị"],
        ],
        [122, 168, 221], align=["LEFT", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(6))

    # ------------------------------------------------------------------ A4
    f.append(P("A4. Phân bổ 50 phút trong phòng thi", "h2"))
    f.append(data_table(
        ["Chặng", "Thời gian", "Việc cần làm"],
        [
            ["1", "0 – 18 phút", "Làm 18 câu trắc nghiệm: câu biết làm trước, câu tính toán sau"],
            ["2", "18 – 27 phút", "Làm 2 câu đúng/sai: đọc kĩ từng ý, đánh dấu Đ/S ngay vào đề"],
            ["3", "27 – 35 phút", "Viết 2 câu tự luận ngắn – trình bày gọn, đủ ý"],
            ["4", "35 – 47 phút", "Làm 3 ý tự luận vận dụng – ghi công thức trước, thay số sau"],
            ["5", "47 – 50 phút", "Rà soát: đơn vị, dấu, tô đáp án, kiểm tra không bỏ trống"],
        ],
        [40, 78, 393], align=["CENTER", "CENTER", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(6))

    # ------------------------------------------------------------------ A5
    f.append(P("A5. Bảy nguyên tắc “không mất điểm oan”", "h2"))
    f += numbered([
        "<b>Đọc kĩ từ phủ định</b>: “không đúng”, “sai”, “ngoại trừ” – gạch chân ngay trên đề.",
        "<b>Đổi đơn vị trước khi tính</b>: km/h → m/s (chia 3,6); cm → m (chia 100); phút → s (nhân 60).",
        "<b>Chọn chiều dương</b> rồi ghi rõ vào bài; mọi đại lượng mang dấu theo chiều dương đó.",
        "<b>Với câu đúng/sai</b>: mỗi ý phải được xét độc lập, đừng để ý a “dính” sang ý b.",
        "<b>Với câu tự luận</b>: viết công thức – thay số – kết quả có đơn vị. Có công thức đúng vẫn được điểm.",
        "<b>Không bỏ trống</b>: câu trắc nghiệm đoán có cơ hội, câu đúng/sai cũng được 0,1 điểm/ý đúng.",
        "<b>Ưu tiên điểm dễ</b>: làm hết câu biết trước, đánh dấu câu khó để quay lại.",
    ])

    # ------------------------------------------------------------------ A6
    f.append(P("A6. Lộ trình ôn 7 ngày (mỗi ngày 60 – 90 phút)", "h2"))
    f.append(data_table(
        ["Ngày", "Nội dung", "Sản phẩm cần đạt"],
        [
            ["1", "Bài 1 – 2 – 3 (lý thuyết + ví dụ sai số)", "Thuộc 4 cuộc CMCN, quy tắc an toàn, 5 bước tính sai số"],
            ["2", "Bài 4 – 5 (độ dịch chuyển, tốc độ – vận tốc)", "Phân biệt được 2 cặp khái niệm, làm 6 câu TN"],
            ["3", "Bài 6 – 7 (thực hành, đồ thị d – t)", "Đọc được đồ thị, nêu ưu – nhược điểm cổng quang"],
            ["4", "Bài 8 – 9 (gia tốc, chuyển động thẳng BĐĐ)", "Thuộc 4 công thức, giải 4 bài mẫu"],
            ["5", "Bài 10 (rơi tự do) + ôn công thức", "Giải 5 bài rơi tự do, thuộc sổ tay công thức"],
            ["6", "Làm trọn đề mô phỏng (Phần D) trong 50 phút", "Có bài làm đầy đủ, tự chấm điểm"],
            ["7", "Chữa đề + checklist + đọc lại bẫy thường gặp", "Sửa hết lỗi sai, đạt ≥ 8 điểm đề mô phỏng"],
        ],
        [36, 230, 245], align=["CENTER", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(6))

    # ------------------------------------------------------------------ A7
    f.append(P("A7. Năm điều tuyệt đối tránh khi ôn thi", "h2"))
    f.append(data_table(
        ["Điều nên tránh", "Vì sao", "Thay bằng"],
        [
            ["Học thuộc lòng mà không làm bài", "Đề 30% là vận dụng, học thuộc không đủ điểm",
             "Mỗi bài: 1 ví dụ mẫu + 3 câu tự luyện"],
            ["Đọc lời giải rồi gật đầu", "Cảm giác “hiểu” không phải là “làm được”",
             "Gấp lời giải, tự làm lại từ đầu"],
            ["Học dàn trải 10 bài như nhau", "Bài 9, 10, 5, 7 chiếm phần lớn số câu",
             "Ưu tiên theo bảng A2"],
            ["Chỉ học công thức, bỏ đơn vị", "Mất điểm oan ở gần như mọi bài toán",
             "Viết đơn vị ở mọi bước thay số"],
            ["Thức trắng đêm trước hôm thi", "Giảm khả năng đọc kĩ đề, tăng lỗi cẩu thả",
             "Ôn nhẹ 30 phút, ngủ đủ 7 – 8 giờ"],
        ],
        [150, 196, 165], align=["LEFT", "LEFT", "LEFT"], font="tbl_small",
    ))
    f.append(SPC(4))
    return f

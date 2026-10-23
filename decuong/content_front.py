# -*- coding: utf-8 -*-
"""PHẦN 0 – Đọc vị đề thi & cách dùng tài liệu."""
from style import *


def story():
    s = []
    s.append(H1("PHẦN 0 · ĐỌC VỊ ĐỀ THI TRƯỚC KHI HỌC"))
    s.append(P("Một đề cương chỉ thật sự hiệu quả khi người học biết <b>cái gì sẽ được hỏi, "
               "hỏi ở mức nào, chiếm bao nhiêu điểm</b>. Phần này “giải mã” ma trận – đặc tả "
               "đề kiểm tra giữa kì I để bạn phân bổ sức học đúng chỗ ngay từ hôm nay.", "lead"))
    s.append(SP(2))
    s.append(box("Tài liệu gồm <b>6 phần</b>: (0) đọc vị đề thi – (1) lý thuyết 10 bài – "
                 "(2) sổ tay công thức – (3) đề mô phỏng + lời giải – (4) 70 thẻ nhớ – "
                 "(5) chống mất điểm – (6) trang bỏ túi + phụ lục đặc tả.", "thi", "TỔNG QUAN NHANH"))
    s.append(SP(4))

    s.append(H2("0.1. Cấu trúc đề kiểm tra"))
    rows = [
        ["Phần", "Hình thức", "Số câu / số ý", "Mức độ nhận thức", "Nội dung rơi vào"],
        ["<b>I</b>", "Trắc nghiệm 4 lựa chọn (A, B, C, D)",
         "18 câu", "10 câu <b>Biết</b> + 8 câu <b>Hiểu</b>",
         "Bài 1, 2, 3 và toàn bộ Bài 4 → 10 (trừ Bài 6 – Thực hành đo tốc độ)"],
        ["<b>II</b>", "Trắc nghiệm <b>Đúng / Sai</b>, mỗi câu 4 ý",
         "2 câu = <b>8 ý</b>", "6 ý <b>Biết</b> + 2 ý <b>Hiểu</b>",
         "Câu 1: Tốc độ – vận tốc (2.2) + Đồ thị s–t (2.3)<br/>Câu 2: Chuyển động thẳng biến đổi đều (2.5)"],
        ["<b>III</b>", "Tự luận ngắn (trình bày – giải thích)",
         "2 câu", "1 câu <b>Biết</b> + 1 câu <b>Hiểu</b>",
         "Câu 1: Tốc độ và vận tốc (2.2)<br/>Câu 2: Sự rơi tự do (2.6)"],
        ["<b>IV</b>", "Tự luận – bài toán",
         "3 ý", "1 ý <b>Hiểu</b> + 2 ý <b>Vận dụng</b>",
         "Ý 1: Tốc độ – vận tốc (2.2)<br/>Ý 2–3: Chuyển động thẳng biến đổi đều (2.5)"],
    ]
    s.append(table(rows, [34, 94, 62, 106, CONTENT_W - 296], font=8.0))
    s.append(SP(5))
    s.append(P("<b>Tỉ lệ điểm:</b> 70% trắc nghiệm (Phần I + II) – 30% tự luận (Phần III + IV). "
               "<b>Thời gian:</b> 50 phút. Trong đó, phần “Biết” chiếm tới <b>17/31 ý</b> – nghĩa là "
               "chỉ cần học thuộc kỹ lý thuyết và công thức là đã có khoảng 55–60% số điểm.", "body"))

    s.append(H2("0.2. Ma trận phân bổ câu hỏi"))
    m = [
        ["Đơn vị kiến thức", "TN<br/>Biết", "TN<br/>Hiểu", "Đ/S<br/>Biết", "Đ/S<br/>Hiểu",
         "TL<br/>Biết", "TL<br/>Hiểu", "TL<br/>Hiểu (P.IV)", "TL<br/>Vận dụng"],
        ["1.1. Làm quen với Vật lí", "1", "", "", "", "", "", "", ""],
        ["1.2. Các quy tắc an toàn trong phòng thực hành", "1", "1", "", "", "", "", "", ""],
        ["1.3. Thực hành tính sai số trong phép đo", "1", "", "", "", "", "", "", ""],
        ["2.1. Độ dịch chuyển và quãng đường đi được", "1", "2", "", "", "", "", "", ""],
        ["2.2. Tốc độ và vận tốc", "1", "", "2 ý (câu I)", "", "1", "", "1", ""],
        ["2.3. Đồ thị độ dịch chuyển – thời gian", "1", "1", "2 ý (câu I)", "", "", "", "", ""],
        ["2.4. Chuyển động biến đổi. Gia tốc", "1", "1", "", "", "", "", "", ""],
        ["2.5. Chuyển động thẳng biến đổi đều", "2", "1", "2 ý (câu II)", "2 ý (câu II)", "", "", "", "2"],
        ["2.6. Sự rơi tự do", "1", "2", "", "", "", "1", "", ""],
        ["<b>TỔNG</b>", "<b>10</b>", "<b>8</b>", "<b>6</b>", "<b>2</b>", "<b>1</b>", "<b>1</b>", "<b>1</b>", "<b>2</b>"],
    ]
    s.append(table(m, [CONTENT_W - 8 * 44] + [44] * 8, font=7.9, align=["l"] + ["c"] * 8))
    s.append(SP(4))
    s.append(P("Đọc bảng theo hàng ngang: ví dụ dòng <b>2.5</b> cho biết chuyên đề chuyển động thẳng "
               "biến đổi đều xuất hiện ở <b>3 câu trắc nghiệm</b> (2 Biết + 1 Hiểu), <b>4 ý đúng/sai</b> "
               "và <b>2 ý tự luận vận dụng</b> – đây là “mỏ điểm” lớn nhất của đề.", "body"))

    s.append(H2("0.3. Ba túi điểm và cách đầu tư thời gian"))
    t = [
        ["Túi điểm", "Chuyên đề", "Số ý", "Bản chất câu hỏi", "Cách học"],
        ["<b>Dễ – phải lấy trọn</b>", "1.1, 1.2, 1.3, 2.4",
         "7 ý", "Hỏi khái niệm, đơn vị, quy tắc, phân loại sai số",
         "Học thuộc bảng + thẻ nhớ. Không cần làm bài tập."],
        ["<b>Trung bình – lấy 80%</b>", "2.1, 2.3, 2.6",
         "8 ý", "Tính s, d, v từ đồ thị; tính thời gian/quãng đường rơi",
         "Nắm 2–3 công thức + luyện 5 bài mẫu mỗi dạng."],
        ["<b>Nặng – quyết định điểm 9–10</b>", "2.2, 2.5",
         "16 ý + cả bài vận dụng", "Bài toán cộng vận tốc, nhanh dần đều, chậm dần đều, đổi chiều",
         "Học theo 5 dạng bài ở Mục 2.5 + làm lại đề mô phỏng 2 lần."],
    ]
    s.append(table(t, [78, 78, 56, 122, CONTENT_W - 334], font=8.0))
    s.append(SP(4))
    s.append(box("<b>2.5 + 2.2 chiếm gần 2/3 số ý của đề.</b> Nếu chỉ còn ít thời gian, hãy học "
                 "chắc hai chuyên đề này trước, rồi mới quay lại Bài 1–2–3 (4 câu, dễ nhưng ít điểm).",
                 "meo", "CHIẾN LƯỢC"))

    s.append(H2("0.4. Phân bổ 50 phút trong phòng thi"))
    t2 = [
        ["Việc làm", "Thời gian", "Ghi chú"],
        ["Đọc lướt toàn đề, đánh dấu câu “chắc chắn làm được”", "2 phút", "Đừng sa vào câu khó ngay"],
        ["Phần I – 18 câu trắc nghiệm", "14 phút", "≈ 45 giây/câu; câu nào quá 90 giây thì bỏ qua, đánh dấu"],
        ["Phần II – 8 ý đúng/sai", "8 phút", "Mỗi ý phải chỉ rõ <b>sai ở đâu</b>, không đoán"],
        ["Phần III – 2 câu tự luận ngắn", "7 phút", "Viết đúng công thức trước, thay số sau"],
        ["Phần IV – bài toán vận dụng", "14 phút", "Tóm tắt → chọn chiều dương → công thức → thay số → đơn vị"],
        ["Rà soát, tô lại phiếu, kiểm tra đơn vị", "5 phút", "Ưu tiên kiểm tra các câu đã đánh dấu"],
    ]
    s.append(table(t2, [CONTENT_W - 160, 60, 100], font=8.0, align=["l", "c", "l"]))
    s.append(SP(5))

    s.append(H2("0.5. Cách dùng tài liệu này để nhớ lâu"))
    s.extend(BULL([
        "<b>Lần 1 (hiểu):</b> đọc Phần 1 theo đúng thứ tự bài học, gạch chân mọi công thức. "
        "Đừng học thuộc ngay – hãy tự hỏi “vì sao có công thức này?”.",
        "<b>Lần 2 (nhớ):</b> che phần lý thuyết, chỉ nhìn các hộp <b>MẸO NHỚ</b> và bảng công thức "
        "ở Phần 2 rồi tự phát biểu lại.",
        "<b>Lần 3 (luyện):</b> làm <b>Đề mô phỏng</b> ở Phần 3 trong đúng 50 phút, không mở đáp án. "
        "Chấm theo thang điểm ở cuối đề, ghi lại các câu sai vào “sổ lỗi”.",
        "<b>Lần 4 (vá lỗi):</b> chỉ học lại những mục tương ứng với câu sai + đọc bảng “12 lỗi mất điểm” "
        "ở Phần 5.",
        "<b>Lần 5 (trước giờ thi 15 phút):</b> chỉ đọc <b>Trang bỏ túi</b> ở cuối tài liệu.",
    ]))
    s.append(box("Trong toàn bộ tài liệu: <b>chữ đậm</b> = ý buộc phải nhớ; hộp "
                 "<b>MẸO NHỚ</b> = câu chốt để nhớ nhanh; hộp <b>BẪY ĐỀ</b> = lỗi học sinh hay mất điểm; "
                 "hộp <b>GHI NHỚ</b> = kết luận cốt lõi.", "thi", "QUY ƯỚC TRÌNH BÀY"))
    s.append(PageBreak())
    return s

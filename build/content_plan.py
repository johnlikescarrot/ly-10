# -*- coding: utf-8 -*-
"""PHẦN E – Chiến lược làm bài, kế hoạch ôn và checklist."""

from reportlab.lib.units import cm
from doc_kit import *  # noqa


def build(d: Doc):
    d.h1("CHIẾN LƯỢC & KẾ HOẠCH ÔN TẬP", kicker="Phần E · Biến kiến thức thành điểm số")

    d.h2("E.1 · Dòng thời gian 50 phút trong phòng thi")
    d.table(
        ["Thời gian", "Việc cần làm", "Lưu ý"],
        [
            ["0 – 2 phút", "Đọc lướt toàn đề, ghi g = 10 hay 9,8; đánh dấu câu dễ", "Không làm ngay câu khó"],
            ["2 – 22 phút", "Làm 18 câu Phần I", "Câu nào quá 60 giây → đánh dấu, bỏ qua"],
            ["22 – 32 phút", "Phần II – 2 câu đúng/sai", "Đọc từng ý, tính lại bằng số"],
            ["32 – 38 phút", "Phần III – 2 câu tự luận ngắn", "Viết công thức trước, thay số sau"],
            ["38 – 47 phút", "Phần IV – 3 câu vận dụng", "Làm câu dễ trước (tổng hợp vận tốc)"],
            ["47 – 50 phút", "Soát bài: đơn vị, dấu của a, phiếu trả lời", "Không đổi đáp án nếu không chắc"],
        ],
        widths=[3.0 * cm, 9.0 * cm, 5.1 * cm], font_size=8.3)

    d.box("tip",
          "Câu dễ “ăn điểm” nhất trong 5 phút đầu: <b>định nghĩa</b> (Phần I câu 1, 5, 8, 11, 16) và "
          "<b>công thức</b> (câu 13). Hãy làm hết nhóm này trước để tạo đà và “khoá” 1,5 điểm chắc chắn.",
          title="CHIẾN THUẬT MỞ MÀN")

    d.h2("E.2 · Thang điểm tham khảo và cách phân bổ điểm")
    d.table(
        ["Phần", "Điểm", "Cách tính điểm khi tự chấm"],
        [
            ["I – 18 câu trắc nghiệm", "4,5 đ", "Mỗi câu đúng 0,25 điểm"],
            ["II – 2 câu đúng/sai", "2,5 đ", "Mỗi câu 1,25 điểm; mỗi ý đúng ≈ 0,31 điểm"],
            ["III – 2 câu tự luận ngắn", "1,0 đ", "Mỗi câu 0,5 điểm (định nghĩa + công thức + đơn vị)"],
            ["IV – 3 câu vận dụng", "2,0 đ", "Câu 1: 0,5 đ; câu 2: 0,75 đ; câu 3: 0,75 đ"],
            ["<b>Tổng</b>", "<b>10 đ</b>", "Luôn trừ điểm trình bày nếu thiếu đơn vị hoặc không ghi công thức"],
        ],
        widths=[4.8 * cm, 2.2 * cm, 10.0 * cm], aligns=["L", "C", "L"], font_size=8.3)

    d.h2("E.3 · Kế hoạch ôn 7 ngày (mỗi ngày 60 – 90 phút)")
    d.table(
        ["Ngày", "Nội dung", "Sản phẩm cần có"],
        [
            ["<b>Ngày 1</b>", "Chuyên đề 09 – Chuyển động thẳng biến đổi đều (4 công thức + dạng hãm phanh)",
             "Viết lại 4 công thức không nhìn tài liệu; làm 5 bài hãm phanh"],
            ["<b>Ngày 2</b>", "Chuyên đề 10 – Sự rơi tự do + chuyên đề 08 – Gia tốc",
             "Bảng phân biệt nhanh dần/chậm dần; 6 bài rơi tự do"],
            ["<b>Ngày 3</b>", "Chuyên đề 05 – Tốc độ, vận tốc, cộng vận tốc + chuyên đề 06 – Thực hành",
             "Vẽ sơ đồ 3 trường hợp cộng vận tốc; 4 bài ca nô/thuyền"],
            ["<b>Ngày 4</b>", "Chuyên đề 07 – Đồ thị + chuyên đề 04 – Độ dịch chuyển",
             "Tự vẽ 3 đồ thị d–t; 5 bài có đổi chiều"],
            ["<b>Ngày 5</b>", "Chuyên đề 01, 02, 03 – phần mở đầu và sai số",
             "Bảng 4 loại biển báo; 3 bài tính sai số đầy đủ"],
            ["<b>Ngày 6</b>", "Làm trọn đề luyện tập số 01 trong 50 phút (Phần C)",
             "Bài làm + bảng điểm theo từng phần"],
            ["<b>Ngày 7</b>", "Chữa đề, đọc Phần B.4, học lại đúng những câu sai",
             "Danh sách 5 lỗi cá nhân và cách tránh"],
        ],
        widths=[1.8 * cm, 8.6 * cm, 6.7 * cm], font_size=8.2)

    d.h2("E.4 · Ba cách học để nhớ thật, không học vẹt")
    d.nums([
        "<b>Viết lại từ trí nhớ (active recall).</b> Gấp tài liệu, viết công thức ra giấy trắng, rồi mở ra đối chiếu. "
        "Sai ở đâu, đánh dấu đỏ ở đó – lần sau chỉ ôn phần đỏ.",
        "<b>Giải thích cho người khác (Feynman).</b> Giảng lại “vì sao a ngược chiều v thì chậm dần” cho bạn cùng bàn "
        "bằng lời của mình. Nếu không giảng được nghĩa là chưa hiểu.",
        "<b>Làm bài theo dạng, không theo đề.</b> Mỗi dạng (hãm phanh, rơi tự do, hai xe gặp nhau) làm 5 bài liên tiếp "
        "để não nhận ra “mẫu”. Khi vào thi, chỉ cần nhận dạng là biết dùng công thức nào.",
    ])

    d.h2("E.5 · Checklist “Tôi đã sẵn sàng”")
    d.table(
        ["✓", "Việc cần kiểm tra", "Trang"],
        [
            ["□", "Phát biểu được định nghĩa độ dịch chuyển và phân biệt với quãng đường", "Chuyên đề 04"],
            ["□", "Viết đúng công thức tốc độ trung bình và vận tốc trung bình", "Chuyên đề 05"],
            ["□", "Áp dụng thành thạo 3 trường hợp cộng vận tốc", "Chuyên đề 05"],
            ["□", "Đọc được vận tốc từ độ dốc của đồ thị d – t", "Chuyên đề 07"],
            ["□", "Phân biệt nhanh dần – chậm dần bằng dấu của a và v", "Chuyên đề 08"],
            ["□", "Thuộc và vận dụng 4 công thức của chuyển động thẳng biến đổi đều", "Chuyên đề 09"],
            ["□", "Giải bài hãm phanh có kiểm tra thời gian dừng", "Chuyên đề 09"],
            ["□", "Tính được quãng đường trong giây thứ n", "Chuyên đề 09 – 10"],
            ["□", "Thuộc 3 công thức rơi tự do và quy luật 1 : 3 : 5", "Chuyên đề 10"],
            ["□", "Tính đúng sai số tuyệt đối, sai số tỉ đối và ghi kết quả đo", "Chuyên đề 03"],
            ["□", "Nhận diện 4 nhóm biển báo an toàn", "Chuyên đề 02"],
            ["□", "Đổi km/h ↔ m/s không cần máy tính", "Sổ tay B.2"],
        ],
        widths=[0.9 * cm, 12.2 * cm, 4.0 * cm], aligns=["C", "L", "C"], font_size=8.4)
    d.p("<i>Chỉ khi đánh dấu được 12/12 ô này, bạn mới nên bước vào phòng thi với tâm thế “mình đã chuẩn bị xong”.</i>", "Small")

    d.h2("E.6 · Ba câu hỏi tự kiểm tra cuối cùng")
    d.box("remember",
          "<b>1.</b> Một xe đi nửa quãng đường đầu với 40 km/h, nửa sau với 60 km/h. Tốc độ trung bình là bao nhiêu?\n"
          "→ <i>Không phải 50 km/h.</i> Gọi mỗi nửa là s: v = 2s/(s/40 + s/60) = 48 km/h.\n\n"
          "<b>2.</b> Vật rơi tự do trong giây cuối đi được 25 m. Thời gian rơi là bao nhiêu?\n"
          "→ Δs = ½g(2T − 1) = 25 → 5(2T − 1) = 25 → T = 3 s.\n\n"
          "<b>3.</b> Xe đang chạy ngược chiều dương với v = −10 m/s và tăng tốc theo chiều dương. Chuyển động là "
          "nhanh dần hay chậm dần?\n"
          "→ a &gt; 0, v &lt; 0 → trái dấu → <b>chậm dần</b> (xe đang đi về phía gốc toạ độ và giảm tốc).",
          title="TỰ KIỂM TRA")

    d.gap(8)
    d.callout("<b>Lời kết.</b> Đề giữa kì I Vật lí 10 không khó – nó chỉ rộng. Chỉ cần 4 công thức của chuyển động "
              "thẳng biến đổi đều, 3 công thức rơi tự do và một chút cẩn thận với đơn vị, bạn đã nắm trong tay "
              "phần lớn số điểm. Hãy học theo ma trận, luyện theo dạng và giữ thói quen kiểm tra lại bài – "
              "đó là khác biệt giữa 8 điểm và 10 điểm.")

    d.h2("E.7 · Sổ tay lỗi của tôi")
    d.p("Đây là phần quan trọng nhất của cả tài liệu – và chỉ <b>bạn</b> mới điền được. Mỗi lần làm sai một câu, "
        "ghi lại: <b>câu nào → sai vì đâu → lần sau làm gì khác</b>. Trước ngày thi, chỉ cần đọc trang này.",
        "Body")
    rows = []
    for i in range(1, 7):
        rows.append([str(i), "", "", ""])
    d.table(
        ["#", "Dạng bài / câu đã sai", "Nguyên nhân (đơn vị? dấu? công thức? đọc đề?)", "Cách khắc phục lần sau"],
        rows,
        widths=[0.9 * cm, 4.6 * cm, 6.0 * cm, 5.6 * cm],
        aligns=["C", "L", "L", "L"], font_size=8.4, zebra=False)
    d.p("<i>Gợi ý dùng: viết bằng bút màu cho phần “nguyên nhân” để lần sau nhìn là nhớ.</i>", "Small")

    d.gap(6)
    d.callout("<b>Cam kết 7 ngày.</b> Tôi sẽ dành 60 – 90 phút mỗi ngày cho đúng kế hoạch ở mục E.3, "
              "làm trọn đề luyện tập trong 50 phút mà không mở tài liệu, và ghi lại mọi lỗi sai vào sổ tay này.\n"
              "Ký tên: ……………………………………  Ngày: ……… / ……… / 20……")

    d.gap(10)
    d.p("<b>Tài liệu tham chiếu:</b> Ma trận và Đặc tả đề kiểm tra giữa kì I – môn Vật lí lớp 10, năm học 2026 – 2027 "
        "(văn bản gốc do giáo viên cung cấp); Sách giáo khoa Vật lí 10 – Chương trình GDPT 2018, các bài 1 – 10.", "Small")

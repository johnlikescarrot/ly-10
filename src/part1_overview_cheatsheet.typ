#import "template.typ": *

// ============================================================================
// COVER & EXECUTIVE DASHBOARD
// ============================================================================

#block(
  width: 100%,
  fill: c-navy,
  radius: 10pt,
  inset: (x: 20pt, y: 18pt),
)[
  #align(center)[
    #box(
      fill: rgb("#1E3A8A"),
      stroke: 0.8pt + rgb("#60A5FA"),
      radius: 20pt,
      inset: (x: 12pt, y: 4pt),
    )[
      #text(fill: rgb("#93C5FD"), weight: "bold", size: 8.8pt, tracking: 0.6pt)[TÀI LIỆU ÔN TẬP TRỌNG TÂM CHUẨN MA TRẬN ĐẶC TẢ 2026–2027]
    ]
    #v(8pt)
    #text(fill: white, weight: "extrabold", size: 20pt)[ĐỀ CƯƠNG ÔN TẬP KIỂM TRA GIỮA HỌC KÌ I]
    #v(4pt)
    #text(fill: rgb("#FACC15"), weight: "extrabold", size: 15pt)[MÔN VẬT LÍ LỚP 10 — CHƯƠNG TRÌNH GDPT 2018]
    #v(5pt)
    #text(fill: rgb("#E2E8F0"), size: 9.8pt)[Biên soạn chuyên sâu bám sát 100% file _“MA TRẬN ĐẶC TẢ KTGK I L10 - 2026”_ (Bộ sách Kết nối tri thức với cuộc sống)]
    #v(12pt)
    #grid(
      columns: (1fr, 1fr, 1fr, 1fr),
      column-gutter: 8pt,
      box(fill: rgb("#1E293B"), stroke: 0.6pt + rgb("#334155"), radius: 6pt, inset: 8pt, width: 100%)[
        #text(fill: rgb("#93C5FD"), size: 8pt, weight: "bold")[THỜI GIAN LÀM BÀI]\
        #v(2pt)
        #text(fill: white, size: 12pt, weight: "extrabold")[50 Phút]
      ],
      box(fill: rgb("#1E293B"), stroke: 0.6pt + rgb("#334155"), radius: 6pt, inset: 8pt, width: 100%)[
        #text(fill: rgb("#6EE7B7"), size: 8pt, weight: "bold")[CẤU TRÚC ĐỀ THI]\
        #v(2pt)
        #text(fill: white, size: 11pt, weight: "extrabold")[70% TN + 30% TL]
      ],
      box(fill: rgb("#1E293B"), stroke: 0.6pt + rgb("#334155"), radius: 6pt, inset: 8pt, width: 100%)[
        #text(fill: rgb("#FCD34D"), size: 8pt, weight: "bold")[PHẠM VI KIẾN THỨC]\
        #v(2pt)
        #text(fill: white, size: 11pt, weight: "extrabold")[Bài 1 → Bài 10]
      ],
      box(fill: rgb("#1E293B"), stroke: 0.6pt + rgb("#334155"), radius: 6pt, inset: 8pt, width: 100%)[
        #text(fill: rgb("#FCA5A5"), size: 8pt, weight: "bold")[NGÂN HÀNG & ĐỀ THI]\
        #v(2pt)
        #text(fill: white, size: 11pt, weight: "extrabold")[130+ Câu & Giải]
      ],
    )
  ]
]

#v(8pt)

#block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: 0.8pt + c-border,
  radius: 8pt,
  inset: (x: 14pt, y: 10pt),
)[
  #text(weight: "extrabold", size: 10.5pt, fill: c-navy)[LỘ TRÌNH SỬ DỤNG ĐỀ CƯƠNG HIỆU QUẢ NHẤT (5 PHẦN KHÉP KÍN)]
  #v(4pt)
  #grid(
    columns: (1fr, 1fr),
    column-gutter: 14pt,
    row-gutter: 5pt,
    [• *Phần A — Giải mã Ma trận & Chiến thuật 50 phút:* Nắm rõ từng ô câu hỏi, điểm số từng bài và cách tránh mất điểm oan.],
    [• *Phần D — Ngân hàng Câu hỏi & Tự luận kèm Đáp án:* Quét sạch mọi dạng câu hỏi Phần I, II (`2-I`, `2-II`), III, IV xuất hiện trong đề thi.],
    [• *Phần B — Tờ Công Thức Vàng & 10 Khẩu Quyết:* Học thuộc lòng toàn bộ công thức và mẹo phản xạ nhanh chỉ trong 15 phút.],
    [• *Phần E — 02 Đề Thi Chuẩn Hóa 100% Ma Trận 2026:* Luyện đề thực chiến 50 phút kèm bảng chấm điểm chi tiết từng 0,25 điểm.],
    [• *Phần C — Lý thuyết Trọng tâm 10 Bài & Sơ đồ:* Cô đọng đúng các chỉ báo Nhận biết – Thông hiểu – Vận dụng trong Bản đặc tả.],
    [• *Cam kết độ phủ:* Bao quát *100% đơn vị kiến thức, dạng câu hỏi và bài toán* có trong bài Kiểm tra Giữa kì I năm học 2026–2027.]
  )
]

#v(4pt)
#outline(
  title: [MỤC LỤC TRA CỨU NHANH],
  indent: 12pt,
  depth: 2,
)

#pagebreak()

// ============================================================================
// PHẦN A: GIẢI MÃ MA TRẬN ĐẶC TẢ & CHIẾN THUẬT PHÒNG THI
// ============================================================================

= PHẦN A. GIẢI MÃ MA TRẬN ĐẶC TẢ KTGK I (2026–2027) & CHIẾN THUẬT 50 PHÚT

== A.1. Bảng Ma trận Đề kiểm tra Giữa kì I & Quy đổi Trọng số Điểm chi tiết

Đề kiểm tra Giữa học kì I môn Vật lí 10 năm học 2026–2027 được thiết kế theo cấu trúc định dạng mới (*70% Trắc nghiệm khách quan = 7,0 điểm; 30% Tự luận = 3,0 điểm; thời gian 50 phút*). Bảng dưới đây trình bày nguyên bản Ma trận chính thức đồng thời quy đổi ra *tỉ trọng điểm số thực tế* của từng bài học để học sinh phân bổ sức học thông minh nhất:

#v(3pt)
#set text(size: 8.3pt)
#table(
  columns: (2.3fr, 0.55fr, 0.55fr, 0.65fr, 0.65fr, 0.55fr, 0.55fr, 0.55fr, 0.65fr, 0.85fr),
  align: (left + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
  stroke: 0.55pt + c-border,
  fill: (x, y) => if y < 3 { rgb("#1E3A8A") } else if y == 12 { rgb("#DBEAFE") } else if calc.odd(y) { rgb("#F8FAFC") } else { white },
  inset: (x: 4pt, y: 4.5pt),

  table.cell(rowspan: 3)[#text(fill: white, weight: "bold")[Đơn vị kiến thức\ (SGK Kết nối tri thức)]],
  table.cell(colspan: 6)[#text(fill: white, weight: "bold")[TRẮC NGHIỆM KHÁCH QUAN (7,0 điểm)]],
  table.cell(colspan: 2)[#text(fill: white, weight: "bold")[TỰ LUẬN (3,0 đ)]],
  table.cell(rowspan: 3)[#text(fill: rgb("#FACC15"), weight: "bold")[Tổng\ điểm\ ước tính]],

  table.cell(colspan: 2)[#text(fill: rgb("#BAE6FD"), weight: "bold")[Phần I (18 câu)\ 4,50 điểm]],
  table.cell(colspan: 2)[#text(fill: rgb("#BAE6FD"), weight: "bold")[Phần II (2 câu)\ 2,00 điểm]],
  table.cell(colspan: 2)[#text(fill: rgb("#BAE6FD"), weight: "bold")[Phần III (2 câu)\ 0,50 điểm]],
  table.cell(colspan: 2)[#text(fill: rgb("#FDE68A"), weight: "bold")[Phần IV (3 câu)\ 3,00 điểm]],

  [#text(fill: white, weight: "bold")[Biết]],
  [#text(fill: white, weight: "bold")[Hiểu]],
  [#text(fill: white, weight: "bold")[Biết]],
  [#text(fill: white, weight: "bold")[Hiểu]],
  [#text(fill: white, weight: "bold")[Biết]],
  [#text(fill: white, weight: "bold")[Hiểu]],
  [#text(fill: white, weight: "bold")[Hiểu]],
  [#text(fill: white, weight: "bold")[V.Dụng]],

  [*1.1.* Làm quen với Vật lí (Bài 1)], [1], [–], [–], [–], [–], [–], [–], [–], [*0,25 đ*],
  [*1.2.* Quy tắc an toàn phòng TH (Bài 2)], [1], [1], [–], [–], [–], [–], [–], [–], [*0,50 đ*],
  [*1.3.* Sai số & ghi kết quả đo (Bài 3)], [1], [–], [–], [–], [–], [–], [–], [–], [*0,25 đ*],
  [*2.1.* Độ dịch chuyển & quãng đường (Bài 4)], [1], [2], [–], [–], [–], [–], [–], [–], [*0,75 đ*],
  [*2.2.* Tốc độ & vận tốc + TH đo tốc độ (Bài 5, 6)], [1], [–], [2–I], [–], [1], [–], [1], [–], [*2,00 đ*],
  [*2.3.* Đồ thị độ dịch chuyển – thời gian (Bài 7)], [1], [1], [2–I], [–], [–], [–], [–], [–], [*1,00 đ*],
  [*2.4.* Chuyển động biến đổi. Gia tốc (Bài 8)], [1], [1], [–], [–], [–], [–], [–], [–], [*0,50 đ*],
  [*2.5.* Chuyển động thẳng biến đổi đều (Bài 9)], [2], [1], [2–II], [2–II], [–], [–], [–], [2], [*3,75 đ*],
  [*2.6.* Sự rơi tự do (Bài 10)], [1], [2], [–], [–], [–], [1], [–], [–], [*1,00 đ*],

  [*TỔNG SỐ CÂU / Ý TOÀN ĐỀ*], [*10*], [*8*], [*6 ý*], [*2 ý*], [*1*], [*1*], [*1*], [*2*], [*10,0 đ*],
)
#set text(size: 9.8pt)

#v(4pt)
#grid(
  columns: (1fr, 1fr),
  column-gutter: 10pt,
  mnemonic-box("Giải mã ký hiệu 2–I và 2–II ở Phần II", [
    • *Câu 1 Phần II (ký hiệu `–I`, 1,0 điểm):* Là bài toán tích hợp *Đồ thị độ dịch chuyển – thời gian ($d - t$)* (2 ý Nhận biết) kết hợp với *Tốc độ và vận tốc* (2 ý Nhận biết).\
    • *Câu 2 Phần II (ký hiệu `–II`, 1,0 điểm):* Là bài toán trọng tâm về *Chuyển động thẳng biến đổi đều* gồm *2 ý Nhận biết* + *2 ý Thông hiểu*.
  ]),
  trap-box("Phát hiện Chiến lược từ Ma trận", [
    • *Chương I (Bài 1, 2, 3)* chỉ có đúng *4 câu trắc nghiệm Phần I = 1,0 điểm* (không có Đúng/Sai, không có Tự luận).\
    • *Chương II (Bài 4 → 10)* chiếm tới *9,0 điểm (90% đề thi)*! Đặc biệt riêng *Bài 9 (CĐTBĐĐ)* chiếm *3,75 điểm* và *Bài 5–6 (Tốc độ, vận tốc)* chiếm *2,00 điểm*!
  ])
)

#pagebreak()

== A.2. Quy tắc tính điểm 4 Phần & Chiến thuật phân bổ 50 Phút Vàng

#table(
  columns: (1.1fr, 1.3fr, 2.1fr, 0.9fr),
  align: (left + horizon, left + horizon, left + horizon, center + horizon),
  stroke: 0.55pt + c-border,
  fill: (x, y) => if y == 0 { rgb("#F1F5F9") } else { white },
  inset: (x: 7pt, y: 5pt),
  [*Phần thi*], [*Cấu trúc & Thang điểm*], [*Bí quyết ăn trọn điểm & Tránh mất điểm oan*], [*Thời gian*],
  [*PHẦN I*\ Nhiều lựa chọn], [18 câu $times$ 0,25 đ\ = *4,50 điểm*], [Đọc kỹ từ khóa phủ định (*không phải*, *sai*). Dùng loại trừ nhanh cho 10 câu Nhận biết trong 4 phút đầu, dành 8 phút cho 8 câu Thông hiểu.], [*12 phút*\ (Phút 0–12)],
  [*PHẦN II*\ Đúng / Sai], [2 câu $times$ 4 ý = *2,00 điểm*\ 1 ý: 0,1đ | 2 ý: 0,25đ\ 3 ý: 0,5đ | *4 ý: 1,00đ*], [*Cực kỳ cẩn thận ở ý thứ 4!* Sai 1 ý mất ngay *0,50 điểm* (bằng 2 câu Phần I). Luôn kiểm tra đơn vị (phút $arrow.r$ giây, km/h $arrow.r$ m/s) và dấu của vận tốc $v$, gia tốc $a$.], [*8 phút*\ (Phút 12–20)],
  [*PHẦN III*\ Trả lời ngắn], [2 câu $times$ 0,25 đ\ = *0,50 điểm*], [Câu 1 thuộc *Tốc độ – Vận tốc* (Biết), Câu 2 thuộc *Rơi tự do* (Hiểu). Đọc kỹ đề hỏi theo đơn vị nào (`m/s` hay `km/h`, `m` hay `cm`) và làm tròn đúng hàng thập phân.], [*5 phút*\ (Phút 20–25)],
  [*PHẦN IV*\ Tự luận], [3 câu (1 Hiểu + 2 VD)\ = *3,00 điểm*], [Trình bày đủ *4 bước ăn điểm thành phần*: (1) Tóm tắt + đổi đơn vị SI + chọn chiều dương; (2) Viết công thức gốc; (3) Thay số đúng dấu; (4) Kết luận kèm đơn vị.], [*20 phút*\ (Phút 25–45)],
  [*RÀ SOÁT*], [Kiểm tra toàn bài], [Soát lại 8 ý Đúng/Sai, dấu âm/dương trong Tự luận, đơn vị kết quả và tô phiếu trả lời.], [*5 phút*\ (Phút 45–50)],
)

#v(6pt)
#formula-box("Bảng Quy Đổi Đơn Vị Chuẩn SI Bắt Buộc Thuộc Lòng Trước Khi Vào Phòng Thi", [
  #grid(
    columns: (1fr, 1fr),
    column-gutter: 14pt,
    row-gutter: 4pt,
    [• *Độ dài – Quãng đường:* $1 "km" = 1000 "m"$; $1 "cm" = "0,01" "m"$; $1 "mm" = "0,001" "m" = 10^(-3) "m"$.],
    [• *Thời gian:* $1 "h" = 60 "phút" = 3600 "s"$; $1 "phút" = 60 "s"$; $1 "ms" = "0,001" "s"$.],
    [• *Tốc độ – Vận tốc:* *$1 "m/s" = "3,6" "km/h"$*.\ Đổi $"km/h" arrow.r "m/s"$: *chia cho $"3,6"$* (VD: $36 "km/h" = 10 "m/s"$; $54 "km/h" = 15 "m/s"$; $72 "km/h" = 20 "m/s"$).],
    [• *Gia tốc:* Đơn vị chuẩn SI là *$"m/s"^2$*.\ _Cấm kỵ tuyệt đối:_ Không bao giờ thay lẫn lộn $v$ tính bằng $"km/h"$ với $t$ tính bằng $"s"$ và $a$ tính bằng $"m/s"^2$!]
  )
])

#v(5pt)
#mnemonic-box("Checklist 5 Bước Tự Kiểm Tra Trước Khi Nộp Bài (Giữ Trọn Từng 0,25 Điểm)", [
  *1.* Đã khoanh đủ *18 câu Phần I* và tô đủ *8 ý Đúng/Sai* (4 ý Câu 1 + 4 ý Câu 2) chưa? _(Tuyệt đối không bỏ trống ô nào!)_\
  *2.* Ở *2 câu Trả lời ngắn Phần III*: Đã đổi đúng đơn vị đề yêu cầu (`m/s` hay `km/h`, `s` hay `h`) và làm tròn đúng chữ số thập phân chưa?\
  *3.* Ở *Câu 1 Tự luận*: Đã phân biệt rõ *Tốc độ TB* ($v_("tb") = s/t$) với *Vận tốc TB* ($v = d/t$) khi vật đổi chiều chuyển động chưa?\
  *4.* Ở *Câu 2 & Câu 3 Tự luận*: Đã ghi câu *“Chọn gốc tọa độ, gốc thời gian, chiều dương là chiều chuyển động”* trước khi thay dấu của $v_0, a$ chưa?\
  *5.* Mọi đáp số cuối cùng trong Phần Tự luận đã ghi đầy đủ *đơn vị chuẩn* (`m`, `s`, `m/s`, `m/s²`) chưa?
])

#pagebreak()

// ============================================================================
// PHẦN B: TỜ CÔNG THỨC VÀNG 1 TRANG & 10 KHẨU QUYẾT SIÊU TRÍ NHỚ
// ============================================================================

= PHẦN B. “TỜ CÔNG THỨC VÀNG 1 TRANG” & 10 KHẨU QUYẾT SIÊU TRÍ NHỚ

== B.1. Bảng Tổng Hợp 100% Công Thức Vật Lí 10 Giữa Kì I (Tra Cứu Thần Tốc)

#set text(size: 8.25pt)
#table(
  columns: (1.22fr, 1.85fr, 2.13fr),
  align: (left + horizon, center + horizon, left + horizon),
  stroke: 0.55pt + c-border,
  fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { rgb("#F8FAFC") } else { white },
  inset: (x: 5.5pt, y: 3.3pt),
  [#text(fill: white, weight: "bold")[Chủ đề / Đại lượng]],
  [#text(fill: rgb("#FACC15"), weight: "bold")[Công thức chuẩn SGK Kết nối tri thức]],
  [#text(fill: white, weight: "bold")[Giải thích ký hiệu & Lưu ý vàng khi làm bài]],

  [*1. Giá trị trung bình*\ & *Sai số tuyệt đối*\ _(Bài 3)_],
  [$ overline(A) = (A_1 + A_2 + dots + A_n) / n $\ $ overline(Delta A) = (|overline(A) - A_1| + dots + |overline(A) - A_n|) / n $\ $ Delta A = overline(Delta A) + Delta A_("dc") $],
  [• $Delta A_("dc")$: sai số dụng cụ (thường lấy bằng *1 ĐCNN* hoặc *nửa ĐCNN* tùy đề bài nêu).\ • Ghi kết quả đo: $A = overline(A) plus.minus Delta A$.\ • $Delta A$ giữ tối đa 1–2 chữ số có nghĩa (tới bậc ĐCNN); $overline(A)$ làm tròn *cùng bậc thập phân* với $Delta A$.],

  [*2. Sai số tỉ đối &*\ *Sai số gián tiếp*\ _(Bài 3)_],
  [$ delta A = (Delta A) / overline(A) dot 100% $\ $F = X plus.minus Y arrow.r.double Delta F = Delta X + Delta Y$\ $F = X^m dot Y^n / Z^k arrow.r.double delta F = m delta X + n delta Y + k delta Z$],
  [• Sai số tỉ đối $delta A$ càng *nhỏ* thì phép đo càng *chính xác*.\ • Đo tốc độ gián tiếp $v = s/t$: $delta v = delta s + delta t = (Delta s)/overline(s) + (Delta t)/overline(t)$, suy ra $Delta v = delta v dot overline(v)$.],

  [*3. Độ dịch chuyển*\ & *Quãng đường*\ _(Bài 4)_],
  [Trên trục $O x$: $d = Delta x = x_2 - x_1$\ Cùng chiều: $d = d_1 + d_2$ | Ngược chiều: $d = |d_1 - d_2|$\ Vuông góc ($arrow(d)_1 perp arrow(d)_2$): $d = sqrt(d_1^2 + d_2^2)$],
  [• Quãng đường $s >= 0$ (vô hướng, luôn không âm).\ • Độ dịch chuyển $arrow(d)$ là *vectơ*; giá trị đại số $d$ có thể $> 0, < 0, = 0$. Luôn có $s >= |d|$; chỉ $s = |d|$ khi đi *thẳng, không đổi chiều*.],

  [*4. Tốc độ &*\ *Vận tốc*\ _(Bài 5)_],
  [Tốc độ TB: $v_("tb") = s / t = (s_1 + s_2 + dots) / (t_1 + t_2)$\ Vận tốc TB: $arrow(v) = arrow(d) / t arrow.r.double v = (Delta d) / (Delta t) = (x_2 - x_1) / (t_2 - t_1)$],
  [• Đổi đơn vị: *$1 "m/s" = "3,6" "km/h"$* ($"km/h" div "3,6" arrow.r "m/s"$).\ • *Cảnh báo:* Tốc độ TB *KHÔNG* bằng $(v_1 + v_2)/2$ (chỉ bằng khi $t_1 = t_2$). Nếu đi 2 nửa quãng đường đầu–cuối: $v_("tb") = (2 v_1 v_2)/(v_1 + v_2)$.],

  [*5. Đo tốc độ bằng*\ *cổng quang điện*\ _(Bài 6)_],
  [Tốc độ TB giữa 2 cổng $E, F$: $v_("tb") = s_(E F) / t_(A arrow.l.r B)$\ Tốc độ tức thời tại cổng $E$: $v_t = d_("bi") / t_A$],
  [• $d_("bi")$: đường kính viên bi thép (hoặc chiều rộng tấm chắn sáng); $t_A$: thời gian chắn tia sáng ở 1 cổng (`MODE A` hoặc `B`).\ • Đồng hồ cần rung $f = 50 "Hz"$: khoảng thời gian 2 chấm liên tiếp $Delta t = "0,02" "s"$.],

  [*6. Công thức*\ *cộng vận tốc*\ _(Bài 5)_],
  [$ arrow(v)_("1,3") = arrow(v)_("1,2") + arrow(v)_("2,3") $\ • $arrow(v)_("1,2") arrow.t arrow.t arrow(v)_("2,3") arrow.r.double v_("1,3") = v_("1,2") + v_("2,3")$ (xuôi dòng)\ • $arrow(v)_("1,2") arrow.t arrow.b arrow(v)_("2,3") arrow.r.double v_("1,3") = |v_("1,2") - v_("2,3")|$ (ngược dòng)\ • $arrow(v)_("1,2") perp arrow(v)_("2,3") arrow.r.double v_("1,3") = sqrt(v_("1,2")^2 + v_("2,3")^2)$],
  [• Số *1*: Vật chuyển động (thuyền, người); Số *2*: Hệ quy chiếu chuyển động (nước, tàu); Số *3*: Hệ quy chiếu đứng yên (bờ, mặt đất).\ • Ca nô hướng mũi vuông góc bờ sông rộng $L$: thời gian qua sông $t = L / v_("1,2")$, độ trôi xuôi dòng $x = v_("2,3") dot t$.],

  [*7. Đồ thị $(d - t)$*\ _(Bài 7)_],
  [Vận tốc = Độ dốc (hệ số góc):\ $ v = (Delta d) / (Delta t) = (d_2 - d_1) / (t_2 - t_1) $\ Phương trình CĐT đều: $d = v t$ (hoặc $x = x_0 + v t$)],
  [• Đoạn thẳng đi lên: $v > 0$ (cùng chiều dương).\ • Đoạn thẳng nằm ngang: $v = 0$ (*vật đứng yên*).\ • Đoạn thẳng đi xuống: $v < 0$ (*vật đi ngược chiều dương*).\ • Tổng quãng đường: $s = |Delta d_1| + |Delta d_2| + dots$ (cộng trị tuyệt đối từng đoạn!).],

  [*8. Gia tốc*\ _(Bài 8)_],
  [$ arrow(a) = (Delta arrow(v)) / (Delta t) = (arrow(v)_t - arrow(v)_0) / (t - t_0) arrow.r.double a = (v_t - v_0) / (Delta t) $],
  [• Đơn vị chuẩn SI: $"m/s"^2$ (hoặc $"m" dot "s"^(-2)$).\ • *Nhanh dần:* $arrow(a) arrow.t arrow.t arrow(v) arrow.l.r.double a dot v > 0$ ($a, v$ cùng dấu).\ • *Chậm dần:* $arrow(a) arrow.t arrow.b arrow(v) arrow.l.r.double a dot v < 0$ ($a, v$ trái dấu).],

  [*9. Chuyển động*\ *thẳng biến đổi đều*\ _(Bài 9 — 3,75 điểm!)_],
  [(1) $v_t = v_0 + a t$\ (2) $d = v_0 t + 1/2 a t^2$  _(tọa độ: $x = x_0 + v_0 t + 1/2 a t^2$)_\ (3) $v_t^2 - v_0^2 = 2 a d$  _(độc lập thời gian)_\ (4) $d = (v_0 + v_t) / 2 dot t$],
  [• Nếu vật đi thẳng *không đổi chiều* theo chiều dương: $s = d$.\ • Vật xuất phát từ nghỉ: $v_0 = 0$. Vật hãm phanh dừng lại: $v_t = 0$.\ • Quãng đường đi trong *giây thứ $n$*: $Delta s_n = s(n) - s(n - 1) = v_0 + a(n - "0,5")$.\ • Quãng đường trong *$k$ giây cuối* trước khi dừng hẳn: $s_("cuối") = 1/2 |a| k^2$.],

  [*10. Sự rơi tự do*\ _(Bài 10)_],
  [$v_t = g t$ #h(12pt) $h = s = d = 1/2 g t^2$\ $v_t = sqrt(2 g h)$ #h(12pt) $t = sqrt((2 h) / g)$],
  [• Là CĐT *nhanh dần đều* theo phương thẳng đứng, chiều từ trên xuống với $v_0 = 0, a = g approx "9,8" "m/s"^2$ (hoặc $10 "m/s"^2$ theo đề).\ • Quãng đường rơi trong giây thứ $n$: $Delta h_n = 1/2 g (2n - 1)$.],
)
#set text(size: 9.8pt)

#pagebreak()

== B.2. 10 Khẩu Quyết Siêu Trí Nhớ — Đọc 1 Lần Thuộc Ngay Toàn Bộ Đề Cương

#grid(
  columns: (1fr, 1fr),
  column-gutter: 10pt,
  row-gutter: 6.5pt,
  mnemonic-box("1. Bốn cuộc Cách mạng Công nghiệp (Bài 1)", [
    *“1 HƠI – 2 ĐIỆN – 3 TỰ – 4 TRÍ”*\
    • CMCN 1 (TK XVIII – 1765): Máy *hơi* nước (James Watt – Nhiệt học).\
    • CMCN 2 (Cuối TK XIX – 1831): *Điện* năng, cảm ứng điện từ (Faraday).\
    • CMCN 3 (1970s – TK XX): *Tự* động hóa, bán dẫn, vi mạch IC.\
    • CMCN 4 (Đầu TK XXI): *Trí* tuệ nhân tạo (AI), IoT, Robot, Nano.
  ]),
  mnemonic-box("2. Quy trình Nghiên cứu Vật lí (Bài 1)", [
    • *Thực nghiệm (5 bước):* *“Xác – Quan – Dự – Thử – Kết”*\
      (Xác định vấn đề $arrow.r$ Quan sát $arrow.r$ Dự đoán $arrow.r$ Thí nghiệm $arrow.r$ Kết luận).\
    • *Mô hình (4 bước):* *“Đối – Xây – Kiểm – Kết”*\
      (Đối tượng $arrow.r$ Xây dựng mô hình $arrow.r$ Kiểm tra phù hợp $arrow.r$ Kết luận).
  ]),
  mnemonic-box("3. Nhận diện 4 Biển báo An toàn (Bài 2)", [
    *“Tròn Đỏ CẤM – Tròn Xanh BẮT BUỘC – Tam Vàng CẢNH BÁO – Vuông Cam HÓA CHẤT”*\
    • Cháy thiết bị điện: *Ngắt cầu dao điện ngay*, tuyệt đối *KHÔNG tạt nước*!
  ]),
  mnemonic-box("4. Quy tắc Sai số Gián tiếp (Bài 3)", [
    *“Cộng Trừ CỘNG TUYỆT ĐỐI ($Delta$) — Nhân Chia CỘNG TỈ ĐỐI ($delta$)”*\
    • Số mũ hạ xuống làm hệ số nhân: $A = R^2 arrow.r.double delta A = 2 delta R$.\
    • Hằng số chính xác (như số $2$, $1/2$) có sai số bằng $0$!
  ]),
  mnemonic-box("5. Vô hướng vs Vectơ (Bài 4 & Bài 5)", [
    *“Quãng – Tốc luôn DƯƠNG vô hướng; Dịch – Vận có HƯỚNG âm dương”*\
    • Đi 1 vòng khép kín (bơi đi rồi bơi về chỗ cũ): $s > 0$ nhưng *$d = 0, arrow(v)_("tb") = arrow(0)$*!\
    • Đồng hồ tốc kế xe máy đo *tốc độ tức thời*.
  ]),
  mnemonic-box("6. Cộng Vận tốc — Nối Đuôi Số 2 (Bài 5)", [
    Viết đúng thứ tự chỉ số: *$arrow(v)_("1,3") = arrow(v)_("1,2") + arrow(v)_("2,3")$* (số *2* kẹp ở giữa!).\
    • Cùng chiều: *Cộng* | Ngược chiều: *Trừ* | Vuông góc: *Pythagore*.\
    • Muốn tìm $arrow(v)_("1,2")$ của xe A so với xe B: $arrow(v)_(A,B) = arrow(v)_(A,"đất") - arrow(v)_(B,"đất")$.
  ]),
  mnemonic-box("7. Đọc Đồ thị (d – t) trong 3 giây (Bài 7)", [
    *“Dốc LÊN tiến dương – NGANG đứng nghỉ – Dốc XUỐNG quay đầu – Càng DỐC càng NHANH”*\
    • Bẫy hay gặp nhất: Đường nằm ngang ở $(d - t)$ là *ĐỨNG YÊN*, còn ở $(v - t)$ mới là *chuyển động thẳng đều*!
  ]),
  mnemonic-box("8. Dấu của Gia tốc & Tính chất CĐ (Bài 8, 9)", [
    *“Cùng dấu NHANH DẦN ($a dot v > 0$) — Trái dấu CHẬM DẦN ($a dot v < 0$)”*\
    • Đừng thấy $a < 0$ mà vội khoanh chậm dần! Nếu vật đi theo chiều âm ($v < 0$) và $a < 0$ thì $a dot v > 0 arrow.r$ *nhanh dần*!
  ]),
  mnemonic-box("9. Chọn đúng 1 trong Bộ Tứ CĐTBĐĐ (Bài 9)", [
    Đề *không hỏi & không cho* đại lượng nào thì chọn công thức *vắng* nó:\
    • Vắng $d$: $v_t = v_0 + a t$ #h(10pt) • Vắng $v_t$: $d = v_0 t + 1/2 a t^2$\
    • Vắng $t$: $v_t^2 - v_0^2 = 2 a d$ #h(10pt) • Vắng $a$: $d = (v_0 + v_t)/2 dot t$.
  ]),
  mnemonic-box("10. Sự Rơi Tự Do & Mẹo Tỉ Lệ (Bài 10)", [
    *“Cùng nơi rơi NHƯ NHAU — Độ cao tỉ lệ BÌNH PHƯƠNG thời gian”*\
    • $h_1 / h_2 = (t_1 / t_2)^2$: Thời gian rơi gấp *2 lần* $arrow.r$ độ cao gấp *4 lần*!\
    • Tỉ lệ quãng đường rơi trong các giây liên tiếp: *$1 : 3 : 5 : 7 : dots$*
  ]),
)

#pagebreak()

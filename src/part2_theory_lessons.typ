#import "template.typ": *

// ============================================================================
// PHẦN C: LÝ THUYẾT TRỌNG TÂM 10 BÀI HỌC (BÁM SÁT 100% BẢN ĐẶC TẢ)
// ============================================================================

= PHẦN C. HỆ THỐNG KIẾN THỨC TRỌNG TÂM, SƠ ĐỒ & BẪY HAY SAI (BÀI 1 → BÀI 10)

// ----------------------------------------------------------------------------
// BÀI 1
// ----------------------------------------------------------------------------
#lesson-header("1 (Mục 1.1)", "BÀI 1. LÀM QUEN VỚI VẬT LÍ", "Phần I: 1 câu Nhận biết", "0,25 điểm")

*1. Đối tượng nghiên cứu & Mục tiêu của môn Vật lí*
- *Đối tượng nghiên cứu chủ yếu:* Các dạng *vận động của vật chất* (gồm *chất* và *trường*) và *năng lượng*.
- *Các lĩnh vực chính:* Cơ học, Nhiệt học, Điện học, Điện từ học, Quang học, Âm học, Vật lí nguyên tử & hạt nhân, Vật lí lượng tử, Thuyết tương đối. _(Lưu ý: Cấu tạo & biến đổi chất là Hóa học; quang hợp & tế bào là Sinh học)_.
- *Mục tiêu:* Khám phá ra *quy luật tổng quát nhất* chi phối sự vận động của vật chất và năng lượng, cũng như tương tác giữa chúng ở mọi cấp độ: *vi mô* (hạt nhân, nguyên tử, electron) và *vĩ mô* (hành tinh, thiên hà).
- *Vai trò:* Vật lí được coi là *cơ sở của khoa học tự nhiên và công nghệ*. Tuy nhiên, nếu ứng dụng sai mục đích có thể gây ô nhiễm môi trường, hủy hoại hệ sinh thái, chạy đua vũ khí hạt nhân.

*2. Ba giai đoạn phát triển lịch sử & Bốn cuộc Cách mạng Công nghiệp (CMCN)*

#set text(size: 8.8pt)
#grid(
  columns: (1fr, 1.15fr),
  column-gutter: 8pt,
  table(
    columns: (0.9fr, 1.8fr),
    stroke: 0.5pt + c-border,
    fill: (x, y) => if y == 0 { rgb("#F1F5F9") } else { white },
    inset: 5pt,
    [*Giai đoạn*], [*Đặc trưng phương pháp & Cột mốc*],
    [*1. Tiền Vật lí*\ (350 TCN – TK XVI)], [Các nhà triết học tự nhiên (*Aristotle*) dựa vào *quan sát và suy luận chủ quan*, chưa làm thí nghiệm kiểm chứng.],
    [*2. Vật lí cổ điển*\ (TK XVII – cuối XIX)], [Dùng *phương pháp thực nghiệm* tìm hiểu tự nhiên (*Galilei* thả vật ở tháp Pisa 1600, *Newton* 1687, *Faraday* 1831).],
    [*3. Vật lí hiện đại*\ (Cuối TK XIX – nay)], [Tập trung vào các *mô hình lí thuyết tìm hiểu thế giới vi mô* và dùng thí nghiệm kiểm chứng (*Planck* 1900, *Einstein* 1905).],
  ),
  table(
    columns: (0.8fr, 1.9fr),
    stroke: 0.5pt + c-border,
    fill: (x, y) => if y == 0 { rgb("#F1F5F9") } else { white },
    inset: 5pt,
    [*Cuộc CMCN*], [*Thành tựu Vật lí nền tảng & Đặc trưng*],
    [*Lần 1* (TK XVIII)], [Nghiên cứu *Nhiệt động lực học* $arrow.r$ Máy hơi nước (*James Watt*, 1765). Thay sức cơ bắp bằng sức máy móc.],
    [*Lần 2* (Cuối XIX)], [*Cảm ứng điện từ* (*Faraday*, 1831) $arrow.r$ Máy phát điện, thiết bị dùng điện trong sản xuất & đời sống.],
    [*Lần 3* (1970s XX)], [Nghiên cứu *điện tử, chất bán dẫn, vi mạch IC, laser* $arrow.r$ *Tự động hóa* dây chuyền sản xuất.],
    [*Lần 4* (Đầu XXI)], [Vật lí hiện đại, vật liệu *nano* $arrow.r$ *Trí tuệ nhân tạo (AI), Robot, Internet vạn vật (IoT)*, thiết bị thông minh.],
  )
)
#set text(size: 9.8pt)

#v(4pt)
*3. Hai phương pháp nghiên cứu Vật lí chủ yếu*
- *Phương pháp thực nghiệm* _(có tính quyết định trong kiểm chứng)_ — *5 bước theo đúng thứ tự:*
  *(1)* Xác định vấn đề cần nghiên cứu $arrow.r$ *(2)* Quan sát, thu thập thông tin $arrow.r$ *(3)* Đưa ra dự đoán (giả thuyết) $arrow.r$ *(4)* Thí nghiệm kiểm tra dự đoán $arrow.r$ *(5)* Kết luận (công nhận hoặc điều chỉnh/bác bỏ dự đoán).
- *Phương pháp mô hình* — gồm *3 loại phổ biến*: *Mô hình vật chất* (quả địa cầu, mô hình hệ Mặt Trời), *Mô hình lí thuyết* (chất điểm, tia sáng), *Mô hình toán học* (công thức $d = v t$, vectơ $arrow(v)$, đồ thị). Quy trình *4 bước*: *(1)* Xác định đối tượng cần mô hình hóa $arrow.r$ *(2)* Xây dựng mô hình giả thuyết $arrow.r$ *(3)* Kiểm tra sự phù hợp của mô hình $arrow.r$ *(4)* Kết luận.
- *Lưu ý thêm về Hệ đơn vị SI (7 đơn vị cơ bản):* mét (`m` – chiều dài), kilôgam (`kg` – khối lượng), giây (`s` – thời gian), kelvin (`K` – nhiệt độ), ampe (`A` – cường độ dòng điện), mol (`mol` – lượng chất), candela (`cd` – cường độ sáng). Các đơn vị như Newton (`N`), Joule (`J`), km/h là *đơn vị dẫn xuất* hoặc ngoài SI.

// ----------------------------------------------------------------------------
// BÀI 2
// ----------------------------------------------------------------------------
#lesson-header("2 (Mục 1.2)", "BÀI 2. CÁC QUY TẮC AN TOÀN TRONG PHÒNG THỰC HÀNH VẬT LÍ", "Phần I: 1 NB + 1 TH", "0,50 điểm")

*1. Kí hiệu thiết bị thí nghiệm & Sử dụng thiết bị an toàn*
- *Thiết bị điện (nguy cơ mất an toàn cao nhất):*
  - Kí hiệu nguồn điện: *`DC`* hoặc dấu *`–`* (dòng điện một chiều); *`AC`* hoặc dấu *`~`* (dòng điện xoay chiều); *`Input (I)`* (đầu vào); *`Output`* (đầu ra); *`+` / màu đỏ* (cực dương); *`–` / màu xanh (hoặc đen)* (cực âm).
  - *Máy biến áp:* Chỉ biến đổi điện áp *xoay chiều (AC)* sang mức điện áp khác. Khi bật phải vặn núm điều chỉnh ở *mức điện áp thấp nhất* rồi tăng dần lên. *Bộ chuyển đổi điện áp (Adapter):* Biến đổi AC (220–240 V) sang điện áp thấp (AC hoặc DC cố định, ví dụ 12 V).
  - *Thiết bị đo điện (Ampe kế, Vôn kế, Đồng hồ đa năng):* Phải chọn *đúng chức năng và thang đo phù hợp* (tránh quá tải gây cháy hỏng thiết bị).
- *Thiết bị nhiệt & thủy tinh:* Thủy tinh dễ nứt vỡ (nhiệt kế thủy ngân vỡ rất độc!); không cầm tay trần vào vật đang nung nóng; khi đun ống nghiệm phải kẹp và nghiêng miệng ống về phía không có người; tắt đèn cồn bằng *nắp chụp* (*tuyệt đối không thổi trực tiếp*).
- *Thiết bị quang học & tia laser:* Tuyệt đối *không chiếu hoặc nhìn trực tiếp vào chùm tia laser* (gây tổn thương võng mạc mắt); không chạm tay làm xước thấu kính, gương.

#v(4pt)
#align(center)[#image("assets/safety_signs.svg", width: 98%)]

*2. Các quy tắc an toàn bắt buộc & Xử lí sự cố trong phòng thực hành*
- *Chỉ tiến hành thí nghiệm khi có sự cho phép của giáo viên hướng dẫn*; đọc kĩ hướng dẫn và kiểm tra thiết bị trước khi dùng; bố trí dây điện gọn gàng.
- *Tắt công tắc nguồn thiết bị điện trước khi cắm hoặc tháo thiết bị*; chỉ cắm vào nguồn có hiệu điện thế đúng định mức; cầm vào *phần vỏ nhựa phích cắm* (không kéo dây điện, không chạm phần kim loại hoặc dây sờn hở).
- *Khi xảy ra cháy ở nơi có thiết bị điện:* *(1)* Lập tức *ngắt toàn bộ hệ thống điện*; *(2)* Đưa hóa chất dễ cháy ra vùng an toàn; *(3)* *TUYỆT ĐỐI KHÔNG dùng nước* dập đám cháy có điện (nước dẫn điện gây điện giật chết người) và *không dùng bình $"CO"_2$* dập cháy quần áo trên người (gây bỏng lạnh/ngạt) hoặc cháy kim loại kiềm (Mg, Na...).

// ----------------------------------------------------------------------------
// BÀI 3
// ----------------------------------------------------------------------------
#lesson-header("3 (Mục 1.3)", "BÀI 3. THỰC HÀNH TÍNH SAI SỐ TRONG PHÉP ĐO. GHI KẾT QUẢ ĐO", "Phần I: 1 câu Nhận biết", "0,25 điểm")

*1. Phân biệt Phép đo & Phân loại Sai số*
- *Phép đo trực tiếp:* Đọc trực tiếp kết quả trên dụng cụ đo (VD: dùng thước đo chiều dài, cân đo khối lượng, đồng hồ bấm giây đo thời gian).
- *Phép đo gián tiếp:* Xác định đại lượng thông qua *công thức vật lí* liên hệ với các đại lượng đo trực tiếp (VD: đo quãng đường $s$ và thời gian $t$ rồi tính tốc độ $v = s/t$; đo khối lượng $m$ và thể tích $V$ để tính khối lượng riêng $D = m/V$).
- *Hai loại sai số phép đo:*
  - *Sai số hệ thống (sai số dụng cụ):* Có tính quy luật lặp lại theo một chiều (do đặc điểm cấu tạo độ chia nhỏ nhất của dụng cụ, hoặc chưa hiệu chỉnh kim về vạch số 0). Sai số dụng cụ $Delta A_("dc")$ thường lấy bằng *nửa độ chia nhỏ nhất (0,5 ĐCNN)* hoặc *1 ĐCNN* (tùy quy ước đề bài).
  - *Sai số ngẫu nhiên:* Không rõ nguyên nhân xác định, trị số dao động hỗn loạn qua các lần đo (do thao tác bấm đồng hồ lệch nhịp, đặt mắt xiên, gió/nhiệt độ thay đổi). *Cách khắc phục:* Thao tác chuẩn, *đo lặp lại nhiều lần* rồi lấy giá trị trung bình và tính sai số.

#formula-box("Quy trình 4 bước tính sai số và ghi kết quả đo chuẩn SGK", [
  *Bước 1 — Giá trị trung bình:* $overline(A) = (A_1 + A_2 + dots + A_n) / n$ #h(16pt)
  *Bước 2 — Sai số từng lần:* $Delta A_i = |overline(A) - A_i|$\
  *Bước 3 — Sai số ngẫu nhiên TB & Sai số tuyệt đối:* $overline(Delta A) = (Delta A_1 + Delta A_2 + dots + Delta A_n) / n arrow.r.double Delta A = overline(Delta A) + Delta A_("dc")$\
  *Bước 4 — Sai số tỉ đối & Ghi kết quả:* $delta A = (Delta A) / overline(A) dot 100%$ #h(10pt) và #h(10pt) *$A = overline(A) plus.minus Delta A$*\
  • *Quy tắc làm tròn:* Sai số tuyệt đối $Delta A$ thường chỉ viết đến *1 hoặc 2 chữ số có nghĩa* (tới bậc ĐCNN). Giá trị trung bình $overline(A)$ *bắt buộc làm tròn đến đúng bậc thập phân của $Delta A$*! (VD: $overline(s) = "1,524" "m"$ và $Delta s = "0,01" "m"$ $arrow.r$ ghi *$s = "1,52" plus.minus "0,01" " (m)"$*, không ghi $"1,524" plus.minus "0,01"$!).
])

// ----------------------------------------------------------------------------
// BÀI 4
// ----------------------------------------------------------------------------
#lesson-header("4 (Mục 2.1)", "BÀI 4. ĐỘ DỊCH CHUYỂN VÀ QUÃNG ĐƯỜNG ĐI ĐƯỢC", "Phần I: 1 NB + 2 TH", "0,75 điểm")

*1. Hệ quy chiếu & Khái niệm cơ bản*
- *Chất điểm:* Vật chuyển động được coi là chất điểm khi kích thước của nó *rất nhỏ* so với độ dài đường đi.
- *Hệ quy chiếu* = *Hệ tọa độ gắn với vật làm mốc* (xác định vị trí) + *Mốc thời gian và đồng hồ* (xác định thời điểm $t$ và thời gian trôi $Delta t = t - t_0$).

*2. Bảng phân biệt Quãng đường đi được ($s$) và Độ dịch chuyển ($arrow(d)$)*

#set text(size: 8.9pt)
#table(
  columns: (1.1fr, 1.9fr, 2.0fr),
  stroke: 0.5pt + c-border,
  fill: (x, y) => if y == 0 { rgb("#F1F5F9") } else { white },
  inset: 5.5pt,
  [*Tiêu chí*], [*Quãng đường đi được ($s$)*], [*Độ dịch chuyển ($arrow(d)$)*],
  [*Bản chất*], [*Đại lượng vô hướng* — chỉ cho biết độ dài toàn bộ quỹ đạo vật đã đi qua.], [*Đại lượng vectơ* — vừa cho biết *độ dài*, vừa cho biết *hướng* thay đổi vị trí từ điểm đầu tới điểm cuối.],
  [*Giá trị*], [*Luôn không âm ($s >= 0$)*, chỉ tăng theo thời gian khi vật còn chuyển động.], [Trên trục $O x$: *$d = x_2 - x_1$* có thể *dương ($>0$), âm ($<0$) hoặc bằng $0$* (khi quay về vị trí xuất phát!).],
  [*Mối quan hệ*], table.cell(colspan: 2)[Luôn có *$s >= |d|$*. Độ lớn độ dịch chuyển và quãng đường *CHỈ bằng nhau ($|d| = s$)* khi vật chuyển động *thẳng và không đổi chiều*!],
)
#set text(size: 9.8pt)

*3. Tổng hợp độ dịch chuyển ($arrow(d) = arrow(d)_1 + arrow(d)_2$)*
- *Cùng phương, cùng chiều:* $d = d_1 + d_2$. #h(12pt) *Cùng phương, ngược chiều:* $d = |d_1 - d_2|$ (hướng theo vectơ dài hơn).
- *Hai độ dịch chuyển vuông góc* (VD: đi hướng Bắc $d_1$ rồi rẽ Đông $d_2$): *$d = sqrt(d_1^2 + d_2^2)$*, góc lệch $tan alpha = d_2 / d_1$.

#v(3pt)
#align(center)[#image("assets/displacement_velocity.svg", width: 98%)]

// ----------------------------------------------------------------------------
// BÀI 5
// ----------------------------------------------------------------------------
#lesson-header("5 (Mục 2.2)", "BÀI 5. TỐC ĐỘ VÀ VẬN TỐC — TỔNG HỢP VẬN TỐC", "P.I: 1 NB | P.II: 2 ý | P.III: 1 NB | P.IV: 1 câu TL", "2,00 điểm")

*1. Phân biệt Tốc độ và Vận tốc (Trọng tâm cả Trắc nghiệm & Tự luận!)*
- *Tốc độ trung bình:* $v_("tb") = s / t = (s_1 + s_2 + dots) / (t_1 + t_2 + dots)$ — *đại lượng vô hướng*, luôn $v_("tb") >= 0$, đặc trưng cho mức độ nhanh chậm của chuyển động trên quãng đường $s$.
- *Tốc độ tức thời:* Tốc độ tại một thời điểm xác định (trong khoảng $Delta t$ rất ngắn). *Số chỉ của tốc kế* trên xe máy, ô tô hay súng bắn tốc độ giao thông chính là *tốc độ tức thời*.
- *Vận tốc trung bình:* $arrow(v) = arrow(d) / t = (Delta arrow(d)) / (Delta t)$ — *đại lượng vectơ* (gốc đặt tại vật, hướng trùng với hướng của độ dịch chuyển $arrow(d)$, độ dài tỉ lệ với độ lớn vận tốc), đặc trưng cho sự nhanh chậm *theo một hướng xác định*.
- *Vận tốc tức thời:* $arrow(v)_t = (Delta arrow(d)) / (Delta t)$ với $Delta t$ rất nhỏ. *Độ lớn* của vận tốc tức thời luôn bằng *tốc độ tức thời* tại thời điểm đó!

#trap-box("2 Cái Bẫy Chết Người ở Bài 5 (Rất hay ra trong Tự luận Câu 1!)", [
  *Bẫy 1:* Vật đi từ $A$ đến $B$ rồi quay ngược lại $C$ $arrow.r$ *Tốc độ trung bình* dùng *tổng quãng đường* $s = A B + B C$, còn *Vận tốc trung bình* dùng *độ dịch chuyển* $d = x_C - x_A$! Khi vật quay về đúng vị trí đầu ($C equiv A$): $v_("tb") = (2 A B)/t > 0$, nhưng *vận tốc trung bình bằng $0$*!\
  *Bẫy 2:* Xe đi nửa quãng đường đầu với $v_1$, nửa quãng đường sau với $v_2$: tuyệt đối *KHÔNG* lấy $(v_1 + v_2)/2$! Phải viết: $t_1 = s/(2 v_1), t_2 = s/(2 v_2) arrow.r.double v_("tb") = s / (t_1 + t_2) = (2 v_1 v_2) / (v_1 + v_2)$.
])

*2. Công thức cộng vận tốc: $arrow(v)_("1,3") = arrow(v)_("1,2") + arrow(v)_("2,3")$*
Quy ước chuẩn 3 đối tượng: *(1)* Vật chuyển động (ca nô, hành khách, máy bay) — *(2)* Hệ quy chiếu chuyển động (dòng nước, đoàn tàu, gió) — *(3)* Hệ quy chiếu đứng yên (bờ sông, mặt đường, mặt đất):
- $arrow(v)_("1,3")$: *Vận tốc tuyệt đối* (của vật 1 đối với bờ/đất 3).
- $arrow(v)_("1,2")$: *Vận tốc tương đối* (của vật 1 đối với nước/tàu 2 — cũng là vận tốc ca nô khi nước lặng!).
- $arrow(v)_("2,3")$: *Vận tốc kéo theo* (của nước/tàu 2 đối với bờ/đất 3).
- *3 trường hợp tính độ lớn:*
  1. *Cùng chiều* (ca nô xuôi dòng / người đi về đầu tàu): *$v_("xuôi") = v_("1,3") = v_("1,2") + v_("2,3")$*.
  2. *Ngược chiều* (ca nô ngược dòng / người đi về cuối tàu): *$v_("ngược") = v_("1,3") = |v_("1,2") - v_("2,3")|$*. _(Hệ quả hay: $v_("1,2") = (v_("xuôi") + v_("ngược"))/2$ và $v_("2,3") = (v_("xuôi") - v_("ngược"))/2$)_.
  3. *Vuông góc* ($arrow(v)_("1,2") perp arrow(v)_("2,3")$ — ca nô hướng mũi vuông góc bờ sông rộng $L$):
     *$v_("1,3") = sqrt(v_("1,2")^2 + v_("2,3")^2)$*; thời gian sang sông *$t = L / v_("1,2")$*; khoảng cách bị nước đẩy trôi xuôi bờ bên kia *$Delta x = v_("2,3") dot t$*; tổng quãng đường thực tế ca nô đi so với bờ *$s = v_("1,3") dot t = sqrt(L^2 + Delta x^2)$*.
- *Vận tốc tương đối giữa 2 xe A, B trên cùng đường thẳng:*
  - Hai xe chạy *cùng chiều*: $v_(A,B) = |v_A - v_B|$ (thời gian đuổi kịp: $t = d_0 / abs(v_A - v_B)$).
  - Hai xe chạy *ngược chiều*: $v_(A,B) = v_A + v_B$ (thời gian gặp nhau: $t = d_0 / (v_A + v_B)$).

// ----------------------------------------------------------------------------
// BÀI 6
// ----------------------------------------------------------------------------
#lesson-header("6 (TT 6 Đặc tả)", "BÀI 6. THỰC HÀNH: ĐO TỐC ĐỘ CỦA VẬT CHUYỂN ĐỘNG", "Tích hợp trong Mục 2.2", "Thực hành")

*1. Dụng cụ đo thời gian hiện số MC964 & Cổng quang điện*
- *Ưu điểm:* Cổng quang điện đóng vai trò như công tắc quang tự động đóng/ngắt đồng hồ ngay khi vật chắn tia hồng ngoại $arrow.r$ *sai số rất nhỏ, độ chính xác cao* (đo chính xác tới phần nghìn giây: ĐCNN $"0,001" "s"$ hoặc $"0,01" "s"$).
- *Nhược điểm:* Chi phí mua thiết bị đắt tiền, bộ thí nghiệm cồng kềnh, lắp đặt đòi hỏi cẩn thận (cắm giắc đúng khe định vị ở ổ A, B; không rung lắc chân cắm).
- *Ý nghĩa sử dụng 1 cổng vs 2 cổng quang điện:*
  - *Dùng 2 cổng quang điện E (ổ A) và F (ổ B) — Chế độ `MODE A↔B`:* Đo khoảng thời gian $t$ viên bi chuyển động từ cổng $E$ tới cổng $F$ cách nhau $s_(E F)$ $arrow.r$ xác định *tốc độ trung bình* $v_("tb") = s_(E F) / t$.
  - *Dùng 1 cổng quang điện E (hoặc F) — Chế độ `MODE A` (hoặc `MODE B`):* Đo khoảng thời gian rất ngắn $Delta t$ khi viên bi (đường kính $d$ đo bằng thước cặp) chắn chùm tia tại cổng đó $arrow.r$ xác định *tốc độ tức thời* $v_t = d / (Delta t)$. _(Muốn đo đồng thời tốc độ tức thời tại cả 2 cổng E và F trong cùng 1 lần thả, cần dùng 2 đồng hồ hiện số)_.
  - *Các nút khác:* `MODE A+B` (tổng thời gian chắn cổng A và chắn cổng B); `MODE T` (chu kì dao động); `RESET` (đưa chỉ số đồng hồ về `0.000`).
- *Đồng hồ cần rung:* Cần rung gõ đều đặn $50$ lần/giây ($f = 50 "Hz"$) lên băng giấy gắn vào xe $arrow.r$ khoảng thời gian giữa 2 chấm liên tiếp trên băng giấy là *$Delta t = 1/50 = "0,02" "s"$*.

#v(3pt)
#align(center)[#image("assets/photogate_setup.svg", width: 98%)]

// ----------------------------------------------------------------------------
// BÀI 7
// ----------------------------------------------------------------------------
#lesson-header("7 (Mục 2.3)", "BÀI 7. ĐỒ THỊ ĐỘ DỊCH CHUYỂN – THỜI GIAN (d – t)", "P.I: 1 NB + 1 TH | P.II: 2 ý (2–I)", "1,00 điểm")

*1. Cách đọc và khai thác mọi thông tin từ đồ thị $(d - t)$ trong chuyển động thẳng*
- Trong chuyển động thẳng đều, $d = v t$ (hoặc $d = d_0 + v t$ khi xuất phát cách gốc $d_0$) có dạng hàm bậc nhất $y = a x + b$ nên đồ thị $(d - t)$ là *một đoạn thẳng*.
- *Hệ số góc (độ dốc) của đường thẳng chính là VẬN TỐC $v$:*
  $ v = (Delta d) / (Delta t) = (d_2 - d_1) / (t_2 - t_1) $
- *4 dạng đường biểu diễn trên đồ thị $(d - t)$ cần thuộc nằm lòng:*
  1. *Đoạn thẳng đi lên từ trái sang phải (độ dốc dương):* Vật chuyển động thẳng đều *theo chiều dương* ($v > 0$). Đường nào *dốc hơn* thì tốc độ *lớn hơn*.
  2. *Đoạn thẳng nằm ngang song song trục $O t$ (độ dốc $= 0$):* Độ dịch chuyển $d$ không đổi $arrow.r$ *Vật đang ĐỨNG YÊN ($v = 0$)*!
  3. *Đoạn thẳng đi xuống từ trái sang phải (độ dốc âm):* Vật chuyển động thẳng đều *ngược chiều dương* ($v < 0$, nhưng tốc độ vẫn dương $|v| > 0$!). Đỉnh nhọn chuyển từ đi lên sang đi xuống là *thời điểm vật đổi chiều chuyển động*.
  4. *Đường cong (nhánh parabol):* Độ dốc thay đổi liên tục $arrow.r$ vật *chuyển động biến đổi* (tốc độ thay đổi).
- *Cách tính Độ dịch chuyển $d$ vs Quãng đường $s$ trên đồ thị nhiều giai đoạn:*
  - *Độ dịch chuyển tổng cộng* từ $t_("đầu")$ đến $t_("cuối")$: chỉ lấy *$d = d_("cuối") - d_("đầu")$*.
  - *Quãng đường tổng cộng* $s$: phải cộng *độ lớn từng đoạn*: *$s = |d_A - d_O| + |d_B - d_A| + |d_C - d_B|$*!

#v(3pt)
#align(center)[#image("assets/dt_vs_vt_graphs.svg", width: 98%)]

// ----------------------------------------------------------------------------
// BÀI 8
// ----------------------------------------------------------------------------
#lesson-header("8 (Mục 2.4)", "BÀI 8. CHUYỂN ĐỘNG BIẾN ĐỔI. GIA TỐC", "Phần I: 1 NB + 1 TH", "0,50 điểm")

*1. Khái niệm, Công thức & Ý nghĩa của Gia tốc*
- *Chuyển động biến đổi:* Là chuyển động có *vận tốc thay đổi* (về độ lớn, về hướng, hoặc cả hai) theo thời gian.
- *Gia tốc ($arrow(a)$):* Là đại lượng *vectơ* đặc trưng cho độ *biến thiên nhanh hay chậm của vận tốc* theo thời gian:
  $ arrow(a) = (Delta arrow(v)) / (Delta t) = (arrow(v)_t - arrow(v)_0) / (t - t_0) quad arrow.r.double quad "Giá trị đại số trên trục Ox:" quad a = (v_t - v_0) / (t - t_0) $
- *Đơn vị của gia tốc trong hệ SI:* *$ "m/s"^2 $* (hay $"m" dot "s"^(-2)$). _(Lưu ý bẫy đơn vị: `cm/s²`, `km/h²` vẫn là đơn vị gia tốc hợp lệ, còn `m/s` hay `km/phút` là đơn vị vận tốc, KHÔNG phải gia tốc!)_.

*2. Quan hệ về hướng giữa $arrow(a)$ và $arrow(v)$ — Quy tắc xét tính chất chuyển động thẳng*
- Vì $Delta t > 0$ nên $arrow(a)$ luôn *cùng phương, cùng chiều với vectơ độ biến thiên vận tốc $Delta arrow(v) = arrow(v)_t - arrow(v)_0$*.
- Trong chuyển động thẳng:
  - *Chuyển động nhanh dần* (độ lớn vận tốc $|v|$ tăng): *$arrow(a)$ cùng chiều $arrow(v)$ ($arrow(a) arrow.t arrow.t arrow(v)$) $arrow.l.r.double a dot v > 0$* (gồm cả 2 TH: $v > 0, a > 0$ hoặc $v < 0, a < 0$).
  - *Chuyển động chậm dần* (độ lớn vận tốc $|v|$ giảm): *$arrow(a)$ ngược chiều $arrow(v)$ ($arrow(a) arrow.t arrow.b arrow(v)$) $arrow.l.r.double a dot v < 0$* (gồm cả 2 TH: $v > 0, a < 0$ hoặc $v < 0, a > 0$).
  - *Chuyển động thẳng đều* ($arrow(v)$ không đổi): *$a = 0$*.

// ----------------------------------------------------------------------------
// BÀI 9
// ----------------------------------------------------------------------------
#lesson-header("9 (Mục 2.5)", "BÀI 9. CHUYỂN ĐỘNG THẲNG BIẾN ĐỔI ĐỀU (CHỦ ĐỀ TRỌNG TÂM SỐ 1)", "P.I: 3 câu | P.II: 1 câu (2–II) | P.IV: 2 câu TL", "3,75 điểm")

*1. Định nghĩa & Đặc điểm nhận dạng*
- *Chuyển động thẳng biến đổi đều (CĐTBĐĐ):* Quỹ đạo là *đường thẳng* và độ lớn vận tốc *tăng đều hoặc giảm đều* theo thời gian:
  - Độ lớn vận tốc tăng đều ($a dot v > 0$): *Chuyển động thẳng nhanh dần đều*.
  - Độ lớn vận tốc giảm đều ($a dot v < 0$): *Chuyển động thẳng chậm dần đều*.
- *Đặc điểm cốt lõi của gia tốc:* Trong CĐTBĐĐ, *vectơ gia tốc $arrow(a)$ hoàn toàn không đổi theo thời gian* (không đổi cả phương, chiều lẫn độ lớn: $a = (Delta v)/(Delta t) = "hằng số"$).

*2. Đồ thị trong Chuyển động thẳng biến đổi đều*
- *Đồ thị vận tốc – thời gian $(v - t)$:* Vì $v_t = v_0 + a t$ là hàm bậc nhất nên đồ thị $(v - t)$ là *một đường thẳng xiên góc*:
  - Hệ số góc (độ dốc) của đường thẳng bằng *gia tốc*: $a = (v_2 - v_1)/(t_2 - t_1)$.
  - *Diện tích hình phẳng* (tam giác / hình thang) giới hạn bởi đồ thị $v(t)$ và trục $O t$ từ $t_1$ đến $t_2$ bằng *độ dịch chuyển $d$* trong khoảng thời gian đó!
- *Đồ thị độ dịch chuyển – thời gian $(d - t)$:* Vì $d = v_0 t + 1/2 a t^2$ là hàm bậc hai theo $t$ nên đồ thị $(d - t)$ là *một nhánh parabol*.

#formula-box("Hệ 4 Công Thức Gốc & 3 Công Thức Giải Nhanh Tự Luận Vận Dụng Cao (Bài 9)", [
  Chọn gốc thời gian $t_0 = 0$, chiều dương là chiều chuyển động ban đầu ($v_0 >= 0$):
  #grid(
    columns: (1fr, 1.15fr),
    column-gutter: 12pt,
    [
      *Bộ Tứ Công Thức Chuẩn SGK:*\
      *(1) Vận tốc tức thời:* $v_t = v_0 + a t$\
      *(2) Độ dịch chuyển:* $d = v_0 t + 1/2 a t^2$\
      *(3) Phương trình tọa độ:* $x = x_0 + v_0 t + 1/2 a t^2$\
      *(4) Độc lập thời gian:* $v_t^2 - v_0^2 = 2 a d$\
      *(5) Vận tốc trung bình:* $v_("tb") = (v_0 + v_t) / 2 = d / t$
    ],
    [
      *3 Công Thức Vận Dụng / VDC Hay Ra Tự Luận:*\
      • *Nhận dạng từ phương trình đề cho:* Nếu đề cho $d = A t + B t^2$ (hoặc $x = x_0 + A t + B t^2$) thì đối chiếu với $d = v_0 t + 1/2 a t^2$ suy ra ngay: *$v_0 = A$* và *$1/2 a = B arrow.r.double a = 2 B$*! _(Rất nhiều bạn quên nhân 2 nên lấy nhầm $a = B$!)_\
      • *Quãng đường đi trong giây thứ $n$* (từ $t = n - 1$ đến $t = n$, không đổi chiều): *$Delta s_n = s(n) - s(n - 1) = v_0 + a(n - "0,5")$*.\
      • *Quãng đường đi trong $k$ giây cuối trước khi dừng hẳn* ($v_("cuối") = 0$): Đảo ngược thời gian coi như xuất phát từ nghỉ: *$s_(k "giây cuối") = 1/2 |a| k^2$*!
    ]
  )
])

// ----------------------------------------------------------------------------
// BÀI 10
// ----------------------------------------------------------------------------
#lesson-header("10 (Mục 2.6)", "BÀI 10. SỰ RƠI TỰ DO", "P.I: 1 NB + 2 TH | P.III: 1 câu TH", "1,00 điểm")

*1. Sự rơi trong không khí vs Sự rơi tự do*
- *Sự rơi trong không khí:* Trong không khí, các vật rơi nhanh chậm khác nhau *KHÔNG PHẢI vì nặng nhẹ khác nhau*, mà do *lực cản của không khí* tác dụng lên chúng khác nhau! Lực cản không khí càng nhỏ so với trọng lực thì vật rơi càng nhanh (thí nghiệm ống Newton hút chân không: viên bi chì và cái lông chim rơi nhanh *như nhau*).
- *Định nghĩa rơi tự do:* Sự rơi của các vật *chỉ dưới tác dụng của trọng lực* gọi là sự rơi tự do. Trong không khí, nếu lực cản của không khí *không đáng kể* so với trọng lực (như thả viên bi sắt, hòn sỏi, quả tạ ở độ cao không lớn) thì chuyển động của vật được coi gần đúng là *rơi tự do*. Ngược lại, chiếc lá rụng, tờ giấy phẳng, hạt bụi, vận động viên đang mở dù *không phải* rơi tự do.

*2. Bốn đặc điểm cốt lõi của chuyển động rơi tự do*
1. *Phương:* Thẳng đứng (phương của dây dọi). #h(16pt) 2. *Chiều:* Từ trên xuống dưới.
3. *Tính chất chuyển động:* Là *chuyển động thẳng nhanh dần đều* không vận tốc ban đầu ($v_0 = 0$).
4. *Gia tốc rơi tự do ($g$):* Tại *cùng một nơi* trên Trái Đất và ở gần mặt đất, *mọi vật đều rơi tự do với cùng một gia tốc $g$* (không phụ thuộc khối lượng hay kích thước vật!). Giá trị $g$ *phụ thuộc vào vĩ độ địa lí và độ cao* (tăng dần từ Xích đạo $g approx "9,78" "m/s"^2$ về hai Địa cực $g approx "9,83" "m/s"^2$; càng lên cao $g$ càng giảm; thường lấy $g = "9,8" "m/s"^2$ hoặc $g = 10 "m/s"^2$).

#formula-box("Hệ Công Thức Rơi Tự Do (Thả từ độ cao h, chọn chiều dương hướng xuống, v₀ = 0)", [
  #grid(
    columns: (1fr, 1fr, 1fr, 1fr),
    column-gutter: 8pt,
    [*Vận tốc tại thời điểm $t$:*\ $ v_t = g t $],
    [*Quãng đường / Độ dịch chuyển:*\ $ s = d = 1/2 g t^2 $],
    [*Thời gian chạm đất:*\ $ t = sqrt((2 h) / g) $],
    [*Vận tốc ngay khi chạm đất:*\ $ v_("đất") = g t = sqrt(2 g h) $],
  )
  #v(4pt)
  • *Quãng đường rơi trong giây thứ $n$:* $Delta s_n = s(n) - s(n - 1) = 1/2 g n^2 - 1/2 g (n - 1)^2 = 1/2 g (2 n - 1)$.\
  • *Quãng đường rơi trong $k$ giây cuối trước khi chạm đất (tổng thời gian rơi là $t$):* $Delta s_("cuối") = 1/2 g t^2 - 1/2 g (t - k)^2 = g k (t - k/2)$.
])

#pagebreak()

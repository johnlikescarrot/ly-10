#import "template.typ": *

// ============================================================================
// PHẦN E: BỘ 02 ĐỀ THI CHÍNH THỨC CHUẨN HÓA 100% MA TRẬN KTGK I L10 (2026–2027)
// ============================================================================

= PHẦN E. BỘ 02 ĐỀ THI CHUẨN HÓA 100% MA TRẬN KTGK I L10 (2026–2027)

// ============================================================================
// ĐỀ THI SỐ 01
// ============================================================================

== E.1. Đề Thi Chuẩn Ma Trận Số 01 (Thời gian làm bài: 50 phút)

#block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: 1pt + c-navy,
  radius: 6pt,
  inset: (x: 12pt, y: 8pt),
)[
  #grid(
    columns: (1fr, 1.2fr),
    align: (center + horizon, center + horizon),
    [
      *SỞ GIÁO DỤC VÀ ĐÀO TẠO*\
      *ĐỀ KIỂM TRA GIỮA HỌC KÌ I*\
      _(Đề gồm 04 phần — Chuẩn Ma trận 2026)_
    ],
    [
      *MÔN: VẬT LÍ — LỚP 10 (NĂM HỌC 2026–2027)*\
      *Thời gian làm bài: 50 phút* _(không kể thời gian phát đề)_\
      *Hình thức: 70% Trắc nghiệm (7,0 đ) + 30% Tự luận (3,0 đ)*
    ]
  )
]

#section-heading("PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (4,5 điểm — từ Câu 1 đến Câu 18)")
_Mỗi câu hỏi thí sinh chỉ chọn một phương án đúng (0,25 điểm/câu)._

#mcq(1, badge("1.1-NB"), [Đặc trưng nổi bật của cuộc Cách mạng công nghiệp lần thứ tư (bắt đầu từ đầu thế kỉ XXI) dựa trên thành tựu Vật lí hiện đại là:],
  [Thay thế sức lực cơ bắp bằng máy hơi nước.],
  [Xuất hiện các thiết bị dùng điện trong sản xuất và đời sống.],
  [Tự động hóa sản xuất nhờ linh kiện bán dẫn và vi mạch.],
  [Sử dụng trí tuệ nhân tạo (AI), robot, Internet toàn cầu và công nghệ nano.], cols: 1)

#mcq(2, badge("1.2-NB"), [Trên một bộ nguồn điện thí nghiệm có ghi kí hiệu *DC* (hoặc dấu *–*). Kí hiệu này cho biết đó là:],
  [Đầu ra dòng điện một chiều.], [Đầu ra dòng điện xoay chiều.],
  [Cảnh báo khu vực có tia laser.], [Thiết bị dễ vỡ khi va chạm.], cols: 2)

#mcq(3, badge("1.2-TH"), [Khi tiến hành thí nghiệm đun nước bằng đèn cồn trong phòng thực hành Vật lí, thao tác nào sau đây là *đúng quy tắc an toàn*?],
  [Dùng miệng thổi mạnh trực tiếp vào ngọn lửa để tắt đèn cồn.],
  [Dùng nắp chụp đèn cồn đậy lên bấc đèn để tắt lửa và không cầm tay trần vào bình đang nóng.],
  [Rót thêm cồn vào đèn khi đèn cồn vẫn đang cháy.],
  [Đặt đèn cồn sát cạnh nguồn điện xoay chiều 220 V.], cols: 1)

#mcq(4, badge("1.3-NB"), [Gọi $overline(Delta A)$ là sai số ngẫu nhiên tuyệt đối trung bình của $n$ lần đo và $Delta A_("dc")$ là sai số dụng cụ. Sai số tuyệt đối $Delta A$ của phép đo được tính theo công thức:],
  [$Delta A = overline(Delta A) - Delta A_("dc")$], [$Delta A = overline(Delta A) + Delta A_("dc")$],
  [$Delta A = (overline(Delta A)) / (Delta A_("dc"))$], [$Delta A = overline(Delta A) dot Delta A_("dc")$], cols: 2)

#mcq(5, badge("2.1-NB"), [Đại lượng vật lí vừa cho biết *độ dài*, vừa cho biết *hướng* của sự thay đổi vị trí của vật từ điểm đầu đến điểm cuối chuyển động là:],
  [Quãng đường đi được.], [Tốc độ trung bình.], [Độ dịch chuyển.], [Thời gian chuyển động.], cols: 2)

#mcq(6, badge("2.1-TH"), [Một học sinh đi bộ thẳng theo hướng Đông $300 "m"$, sau đó quay đầu đi thẳng ngược lại theo hướng Tây $100 "m"$. Quãng đường đi được $s$ và độ lớn độ dịch chuyển $d$ của học sinh là:],
  [$s = 400 "m"; d = 200 "m"$.], [$s = 200 "m"; d = 400 "m"$.],
  [$s = 400 "m"; d = 400 "m"$.], [$s = 300 "m"; d = 200 "m"$.], cols: 2)

#mcq(7, badge("2.1-TH"), [Một người bơi ngang qua con sông rộng $30 "m"$ theo hướng Bắc, nhưng do nước chảy sang hướng Đông nên khi sang đến bờ bên kia người đó đã bị trôi xuôi dòng một đoạn $40 "m"$. Độ lớn độ dịch chuyển tổng hợp của người đó là:],
  [$70 "m"$.], [$10 "m"$.], [$50 "m"$.], [$35 "m"$.], cols: 4)

#mcq(8, badge("2.2-NB"), [Biểu thức định nghĩa vectơ vận tốc trung bình của một vật thực hiện độ dịch chuyển $arrow(d)$ trong khoảng thời gian $t$ là:],
  [$arrow(v) = s / t$], [$arrow(v) = arrow(d) / t$], [$arrow(v) = arrow(d) dot t$], [$arrow(v) = t / arrow(d)$], cols: 4)

#mcq(9, badge("2.3-NB"), [Trên đồ thị độ dịch chuyển – thời gian $(d - t)$ của chuyển động thẳng, hệ số góc (độ dốc) của đường thẳng biểu diễn cho biết giá trị của đại lượng nào?],
  [Quãng đường đi được.], [Gia tốc của vật.], [Vận tốc của vật.], [Thời gian chuyển động.], cols: 2)

#mcq(10, badge("2.3-TH"), [Đồ thị độ dịch chuyển – thời gian $(d - t)$ của một vật chuyển động thẳng đều là đường thẳng đi qua hai điểm $M(t_1 = 1 "s"; d_1 = 5 "m")$ và $N(t_2 = 6 "s"; d_2 = 25 "m")$. Vận tốc của vật là:],
  [$5 "m/s"$.], [$4 "m/s"$.], [$"3,6" "m/s"$.], [$6 "m/s"$.], cols: 4)

#mcq(11, badge("2.4-NB"), [Trong hệ đơn vị đo lường quốc tế SI, đơn vị chuẩn của gia tốc là:],
  [$"m/s"$.], [$"km/h"$.], [$"m/s"^2$.], [$"m" dot "s"$.], cols: 4)

#mcq(12, badge("2.4-TH"), [Một xe máy đang chạy thẳng với tốc độ $36 "km/h"$ thì tăng ga, sau $5 "s"$ đạt tốc độ $54 "km/h"$. Chọn chiều dương cùng chiều chuyển động, gia tốc trung bình của xe máy trong $5 "s"$ đó là:],
  [$"3,6" "m/s"^2$.], [$"1,0" "m/s"^2$.], [$"2,0" "m/s"^2$.], [$"0,5" "m/s"^2$.], cols: 4)

#mcq(13, badge("2.5-NB"), [Chuyển động thẳng biến đổi đều là chuyển động có quỹ đạo là đường thẳng và có:],
  [Vận tốc không đổi theo thời gian.],
  [Độ lớn vận tốc tăng đều hoặc giảm đều theo thời gian.],
  [Quãng đường đi được tỉ lệ thuận bậc nhất với thời gian.],
  [Gia tốc tăng đều theo thời gian.], cols: 2)

#mcq(14, badge("2.5-NB"), [Một vật chuyển động thẳng biến đổi đều với vận tốc đầu $v_0$ và gia tốc $a$. Vận tốc tức thời $v_t$ tại thời điểm $t$ (với $t_0 = 0$) được xác định bởi công thức:],
  [$v_t = v_0 + 1/2 a t^2$], [$v_t = v_0 + a t$], [$v_t = v_0 - a t^2$], [$v_t = a / t$], cols: 4)

#mcq(15, badge("2.5-TH"), [Một đoàn tàu đang chạy với vận tốc $15 "m/s"$ thì hãm phanh chuyển động thẳng chậm dần đều với gia tốc $a = -"0,5" "m/s"^2$. Quãng đường tàu đi được trong $10 "s"$ đầu kể từ lúc hãm phanh là:],
  [$150 "m"$.], [$125 "m"$.], [$100 "m"$.], [$175 "m"$.], cols: 4)

#mcq(16, badge("2.6-NB"), [Phát biểu nào sau đây *KHÔNG ĐÚNG* khi nói về sự rơi tự do?],
  [Sự rơi tự do là sự rơi chỉ dưới tác dụng của trọng lực.],
  [Phương của chuyển động rơi tự do là phương thẳng đứng, chiều từ trên xuống dưới.],
  [Ở cùng một nơi trên Trái Đất, vật nặng hơn luôn rơi tự do với gia tốc lớn hơn vật nhẹ.],
  [Chuyển động rơi tự do là chuyển động thẳng nhanh dần đều.], cols: 1)

#mcq(17, badge("2.6-TH"), [Một hòn bi sắt được thả rơi tự do từ độ cao $h = 45 "m"$ xuống đất tại nơi có $g = 10 "m/s"^2$. Thời gian rơi của hòn bi cho tới khi chạm đất là:],
  [$"3,0" "s"$.], [$"4,5" "s"$.], [$"9,0" "s"$.], [$"2,1" "s"$.], cols: 4)

#mcq(18, badge("2.6-TH"), [Thả một vật rơi tự do không vận tốc đầu tại nơi có $g = "9,8" "m/s"^2$. Quãng đường vật rơi được trong $2 "s"$ đầu tiên là:],
  [$"9,8" "m"$.], [$"19,6" "m"$.], [$"39,2" "m"$.], [$"4,9" "m"$.], cols: 4)

#section-heading("PHẦN II. Câu trắc nghiệm đúng sai (2,0 điểm — Câu 1 và Câu 2)")
_Trong mỗi ý *a), b), c), d)* ở mỗi câu, thí sinh chọn *Đúng* hoặc *Sai*. (Đúng 1 ý: 0,1đ; 2 ý: 0,25đ; 3 ý: 0,5đ; 4 ý: 1,0đ)._

#tf-question(
  "1",
  "Ma trận 2–I: Đồ thị (d – t) & Tốc độ, vận tốc",
  [Một xe khách xuất phát từ bến $O$ chuyển động trên một tuyến quốc lộ thẳng có đồ thị độ dịch chuyển – thời gian $(d - t)$ như hình vẽ bên dưới.],
  image("assets/exam1_dt_graph.svg", width: 58%),
  [Trong $2$ giờ đầu tiên (đoạn $O A$), xe khách chuyển động thẳng đều theo chiều dương.],
  [Tốc độ của xe khách trong $2$ giờ đầu tiên bằng $40 "km/h"$.],
  [Từ $t = 2 "h"$ đến $t = 3 "h"$ (đoạn $A B$), xe khách chuyển động thẳng đều với tốc độ $80 "km/h"$.],
  [Từ $t = 3 "h"$ đến $t = 5 "h"$ (đoạn $B C$), xe khách quay đầu đi ngược chiều dương với vận tốc $-40 "km/h"$.],
)

#tf-question(
  "2",
  "Ma trận 2–II: Chuyển động thẳng biến đổi đều",
  [Một xe máy đang chạy thẳng đều với tốc độ $36 "km/h"$ thì người lái xe tăng ga cho xe chuyển động thẳng nhanh dần đều với gia tốc có độ lớn $"1,5" "m/s"^2$. Chọn chiều dương là chiều chuyển động của xe, gốc thời gian lúc bắt đầu tăng ga.],
  none,
  [Trong quá trình tăng ga, gia tốc của xe máy là một hằng số dương $a = "1,5" "m/s"^2$.],
  [Đổi sang hệ đơn vị chuẩn SI, vận tốc ban đầu của xe lúc bắt đầu tăng ga là $v_0 = 36 "m/s"$.],
  [Sau $4 "s"$ kể từ lúc tăng ga, vận tốc của xe máy đạt $16 "m/s"$.],
  [Quãng đường xe máy đi được trong $6 "s"$ đầu kể từ lúc bắt đầu tăng ga bằng $87 "m"$.],
)

#section-heading("PHẦN III. Câu trắc nghiệm trả lời ngắn (0,5 điểm — Câu 1 và Câu 2)")
_Mỗi câu trả lời đúng được 0,25 điểm._

- *Câu 1* #badge("2.2-NB")*:* Một học sinh đạp xe đều trên đoạn đường thẳng dài $"3,6" "km"$ hết thời gian $10$ phút. Tốc độ trung bình của học sinh đó bằng bao nhiêu $"m/s"$?
- *Câu 2* #badge("2.6-TH")*:* Một hòn sỏi được thả rơi tự do từ một vách đá cao $80 "m"$ xuống mặt đất. Bỏ qua sức cản của không khí, lấy $g = 10 "m/s"^2$. Tốc độ của hòn sỏi ngay trước khi chạm đất bằng bao nhiêu $"m/s"$?

#section-heading("PHẦN IV. Tự luận (3,0 điểm — Câu 1, Câu 2 và Câu 3)")

- *Câu 1 (1,0 điểm — Mục 2.2 Thông hiểu):* Một ca nô có vận tốc đối với mặt nước khi nước yên lặng là $18 "km/h"$. Ca nô chạy xuôi dòng từ bến $A$ đến bến $B$ cách nhau $"1,2" "km"$ trên một đoạn sông thẳng rồi lập tức quay đầu chạy ngược dòng trở về bến $A$. Biết dòng nước chảy đều từ $A$ về $B$ với vận tốc $"3,6" "km/h"$ so với bờ sông.\
  *a)* Tính thời gian ca nô đi xuôi dòng từ $A$ đến $B$ và thời gian đi ngược dòng từ $B$ về $A$ (theo đơn vị giây).\
  *b)* Tính *tốc độ trung bình* và *vận tốc trung bình* của ca nô trên cả chuyến đi khứ hồi $A arrow.r B arrow.r A$.
- *Câu 2 (1,0 điểm — Mục 2.5 Vận dụng):* Một ô tô đang chạy thẳng với tốc độ $72 "km/h"$ thì hãm phanh chuyển động thẳng chậm dần đều. Sau $5 "s"$ kể từ lúc bắt đầu hãm phanh, tốc độ của ô tô giảm còn $36 "km/h"$. Chọn chiều dương cùng chiều chuyển động của ô tô.\
  *a)* Tính gia tốc của ô tô và quãng đường ô tô đi được trong $5 "s"$ đầu đó.\
  *b)* Tính tổng quãng đường ô tô đi được kể từ lúc bắt đầu hãm phanh cho đến khi dừng hẳn.
- *Câu 3 (1,0 điểm — Mục 2.5 Vận dụng cao):* Một chất điểm bắt đầu chuyển động thẳng nhanh dần đều từ trạng thái đứng yên ($v_0 = 0$). Biết riêng trong *giây thứ 5* (từ $t = 4 "s"$ đến $t = 5 "s"$), chất điểm đi được quãng đường là $18 "m"$.\
  *a)* Tính gia tốc $a$ của chất điểm.\
  *b)* Tính quãng đường chất điểm đi được trong khoảng thời gian từ cuối giây thứ $3$ đến cuối giây thứ $6$.

#v(5pt)
#solution-card("ĐÁP ÁN & BIỂU ĐIỂM CHẤM CHI TIẾT — ĐỀ THI CHUẨN MA TRẬN SỐ 01", [
  *1. PHẦN I (4,50 điểm — 0,25 đ/câu):*\
  #set text(size: 8.5pt)
  #table(
    columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt + c-border,
    fill: (x, y) => if calc.even(y) { rgb("#EFF6FF") } else { white },
    inset: 3.5pt,
    [*1. D*], [*2. A*], [*3. B*], [*4. B*], [*5. C*], [*6. A*], [*7. C*], [*8. B*], [*9. C*],
    [*10. B*], [*11. C*], [*12. B*], [*13. B*], [*14. B*], [*15. B*], [*16. C*], [*17. A*], [*18. B*],
  )
  #set text(size: 9.0pt)
  _Giải nhanh các câu tính toán Phần I:_ *Câu 6:* $s = 300 + 100 = 400 "m", d = 300 - 100 = 200 "m"$. *Câu 7:* $d = sqrt(30^2 + 40^2) = 50 "m"$. *Câu 10:* $v = (25 - 5)/(6 - 1) = 4 "m/s"$. *Câu 12:* $a = (15 - 10)/5 = "1,0" "m/s"^2$. *Câu 15:* $d = 15 dot 10 + 1/2(-"0,5") dot 10^2 = 125 "m"$. *Câu 17:* $t = sqrt(2 dot 45 / 10) = "3,0" "s"$. *Câu 18:* $s = 1/2 dot "9,8" dot 2^2 = "19,6" "m"$.

  #v(3pt)
  *2. PHẦN II (2,00 điểm):*\
  • *Câu 1:* *a) Đúng | b) Đúng | c) Sai | d) Đúng.* _(Ý c sai vì trên $A B$ tọa độ $d = 80 "km"$ không đổi nên xe đang dừng nghỉ, $v = 0$; ý d đúng vì $v_(B C) = (0 - 80)/(5 - 3) = -40 "km/h"$)_. \
  • *Câu 2:* *a) Đúng | b) Sai | c) Đúng | d) Đúng.* _(Ý b sai vì $36 "km/h" = 10 "m/s"$; ý c: $v = 10 + "1,5" dot 4 = 16 "m/s"$; ý d: $s = 10 dot 6 + 1/2 dot "1,5" dot 6^2 = 60 + 27 = 87 "m"$)_.

  #v(3pt)
  *3. PHẦN III (0,50 điểm — 0,25 đ/câu):*\
  • *Câu 1:* Điền *`6`* _($s = 3600 "m", t = 600 "s" arrow.r v = 3600 / 600 = 6 "m/s"$)_. #h(12pt)
  • *Câu 2:* Điền *`40`* _($v = sqrt(2 dot 10 dot 80) = 40 "m/s"$)_.

  #v(3pt)
  *4. PHẦN IV – TỰ LUẬN (3,00 điểm):*\
  • *Câu 1 (1,00 đ):* Đổi $v_("1,2") = 18 "km/h" = 5 "m/s"$; $v_("2,3") = "3,6" "km/h" = 1 "m/s"$; $A B = 1200 "m"$. *(0,25 đ)*\
    – a) Xuôi dòng: $v_x = v_("1,2") + v_("2,3") = 6 "m/s" arrow.r t_1 = 1200 / 6 = #strong[$200 "s"$]$. Ngược dòng: $v_n = v_("1,2") - v_("2,3") = 4 "m/s" arrow.r t_2 = 1200 / 4 = #strong[$300 "s"$]$. *(0,25 đ)*\
    – b) Cả chuyến đi khứ hồi: tổng quãng đường $s = 1200 + 1200 = 2400 "m"$, tổng thời gian $t = 200 + 300 = 500 "s" arrow.r$ *Tốc độ trung bình:* $v_("tb") = 2400 / 500 = #strong[$"4,8" "m/s"$]$ ($= "17,28" "km/h"$). *(0,25 đ)* Vì ca nô quay về đúng bến xuất phát $A$ nên độ dịch chuyển $d = 0 arrow.r$ *Vận tốc trung bình:* $v = 0 / 500 = #strong[$0 "m/s"$]$. *(0,25 đ)*\
  • *Câu 2 (1,00 đ):* Đổi $v_0 = 72 "km/h" = 20 "m/s"$; $v_1 = 36 "km/h" = 10 "m/s"$. *(0,25 đ)*\
    – a) Gia tốc: $a = (v_1 - v_0)/t_1 = (10 - 20)/5 = #strong[$-2 "m/s"^2$]$. Quãng đường đi trong $5 "s"$ đầu: $s_1 = 20 dot 5 + 1/2(-2) dot 5^2 = #strong[$75 "m"$]$. *(0,50 đ)*\
    – b) Khi dừng hẳn $v = 0$: áp dụng $v^2 - v_0^2 = 2 a s_("dừng") arrow.r s_("dừng") = (0 - 20^2)/(2 dot (-2)) = #strong[$100 "m"$]$. *(0,25 đ)*\
  • *Câu 3 (1,00 đ):* Vì $v_0 = 0$ nên quãng đường đi sau thời gian $t$ là $s(t) = 1/2 a t^2$. *(0,25 đ)*\
    – a) Quãng đường đi trong giây thứ 5: $Delta s_5 = s(5) - s(4) = 1/2 a (5^2 - 4^2) = "4,5" a = 18 arrow.r.double #strong[$a = 4 "m/s"^2$]$. *(0,50 đ)*\
    – b) Quãng đường đi từ $t = 3 "s"$ đến $t = 6 "s"$: $Delta s_(3 arrow.r 6) = s(6) - s(3) = 1/2 dot 4 dot (6^2 - 3^2) = 2 dot 27 = #strong[$54 "m"$]$. *(0,25 đ)*
])

#pagebreak()

// ============================================================================
// ĐỀ THI SỐ 02
// ============================================================================

== E.2. Đề Thi Chuẩn Ma Trận Số 02 (Thời gian làm bài: 50 phút)

#block(
  width: 100%,
  fill: rgb("#F8FAFC"),
  stroke: 1pt + c-navy,
  radius: 6pt,
  inset: (x: 12pt, y: 8pt),
)[
  #grid(
    columns: (1fr, 1.2fr),
    align: (center + horizon, center + horizon),
    [
      *SỞ GIÁO DỤC VÀ ĐÀO TẠO*\
      *ĐỀ KIỂM TRA GIỮA HỌC KÌ I*\
      _(Đề số 02 — Quét phủ toàn diện Ma trận 2026)_
    ],
    [
      *MÔN: VẬT LÍ — LỚP 10 (NĂM HỌC 2026–2027)*\
      *Thời gian làm bài: 50 phút* _(không kể thời gian phát đề)_\
      *Hình thức: 70% Trắc nghiệm (7,0 đ) + 30% Tự luận (3,0 đ)*
    ]
  )
]

#section-heading("PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (4,5 điểm — từ Câu 1 đến Câu 18)")

#mcq(1, badge("1.1-NB"), [Trong lịch sử phát triển của Vật lí, thí nghiệm thả rơi hai vật tại tháp nghiêng Pisa của Galilei (khoảng năm 1600) đã đánh dấu bước ngoặt mở đầu cho:],
  [Giai đoạn tiền Vật lí dựa trên suy luận chủ quan.],
  [Phương pháp thực nghiệm trong nghiên cứu Vật lí cổ điển.],
  [Sự ra đời của thuyết tương đối và vật lí lượng tử.],
  [Cuộc cách mạng công nghiệp lần thứ tư.], cols: 2)

#mcq(2, badge("1.2-NB"), [Biển báo an toàn trong phòng thí nghiệm có dạng *hình tròn, nền trắng, viền đỏ và có vạch gạch chéo màu đỏ* thuộc nhóm:],
  [Biển báo cấm thực hiện.], [Biển báo bắt buộc thực hiện.],
  [Biển cảnh báo hóa chất độc hại.], [Biển chỉ dẫn nơi để bình chữa cháy.], cols: 2)

#mcq(3, badge("1.2-TH"), [Một học sinh dùng tay nắm chặt phần dây dẫn điện rồi giật mạnh để rút phích cắm khỏi ổ điện 220 V. Hành động này gây nguy cơ mất an toàn trực tiếp nào?],
  [Làm tăng điện áp định mức của nguồn điện.],
  [Làm đứt ngầm lõi dây hoặc tuột vỏ cách điện gây hở mạch và điện giật.],
  [Làm đổi chiều dòng điện xoay chiều thành một chiều.],
  [Làm giảm độ chia nhỏ nhất của thiết bị đo.], cols: 1)

#mcq(4, badge("1.3-NB"), [Để khắc phục và làm giảm *sai số ngẫu nhiên* khi tiến hành một phép đo trực tiếp trong phòng thực hành Vật lí, biện pháp hiệu quả nhất là:],
  [Chỉ đo đúng 1 lần duy nhất thật nhanh.],
  [Thực hiện thao tác chuẩn xác, tiến hành đo lặp lại nhiều lần rồi lấy giá trị trung bình.],
  [Không cần hiệu chỉnh dụng cụ đo về vạch số 0.],
  [Thay đổi công thức tính đại lượng cần đo.], cols: 1)

#mcq(5, badge("2.1-NB"), [Trên một trục tọa độ $O x$, một vật chuyển động từ vị trí có tọa độ $x_1$ đến vị trí có tọa độ $x_2$. Giá trị đại số của độ dịch chuyển $d$ của vật được xác định bởi:],
  [$d = x_1 + x_2$], [$d = x_2 - x_1$], [$d = (x_1 + x_2) / 2$], [$d = x_1 dot x_2$], cols: 4)

#mcq(6, badge("2.1-TH"), [Một vận động viên chạy trọn 1 vòng trên đường chạy hình tròn có bán kính $R = 50 "m"$ rồi dừng lại ở đúng vạch xuất phát. Độ lớn độ dịch chuyển $d$ của vận động viên bằng:],
  [$50 "m"$.], [$100 "m"$.], [$100 pi "m"$.], [$0 "m"$.], cols: 4)

#mcq(7, badge("2.1-TH"), [Một học sinh đi bộ từ ngã tư đi thẳng $80 "m"$ về hướng Nam, sau đó rẽ vuông góc đi thẳng $60 "m"$ về hướng Tây. Độ lớn độ dịch chuyển tổng hợp của học sinh so với ngã tư là:],
  [$140 "m"$.], [$20 "m"$.], [$100 "m"$.], [$70 "m"$.], cols: 4)

#mcq(8, badge("2.2-NB"), [Trong bộ thí nghiệm đo tốc độ chuyển động bằng đồng hồ đo thời gian hiện số MC964, nút *RESET* trên mặt đồng hồ có chức năng:],
  [Đổi đơn vị đo từ giây sang phút.],
  [Đặt lại chỉ số hiển thị của đồng hồ về giá trị `0.000`.],
  [Bật hoặc tắt nam châm điện giữ viên bi thép.],
  [Đo đường kính của viên bi thép.], cols: 2)

#mcq(9, badge("2.3-NB"), [Trên đồ thị độ dịch chuyển – thời gian $(d - t)$, nếu đường biểu diễn là một đoạn thẳng *xiên xuống từ trái sang phải* (hệ số góc âm) thì vật đang:],
  [Chuyển động thẳng nhanh dần đều.],
  [Đứng yên tại gốc tọa độ.],
  [Chuyển động thẳng đều theo chiều dương.],
  [Chuyển động thẳng đều ngược chiều dương.], cols: 2)

#mcq(10, badge("2.3-TH"), [Một vật chuyển động thẳng đều có đồ thị $(d - t)$ là đoạn thẳng nối từ điểm $P(t_1 = 0 "s"; d_1 = 30 "m")$ đến điểm $Q(t_2 = 5 "s"; d_2 = 10 "m")$. Vận tốc của vật bằng:],
  [$4 "m/s"$.], [$-4 "m/s"$.], [$6 "m/s"$.], [$-2 "m/s"$.], cols: 4)

#mcq(11, badge("2.4-NB"), [Một chất điểm chuyển động thẳng theo một chiều xác định. Nếu chất điểm chuyển động *nhanh dần* thì:],
  [$arrow(a)$ luôn ngược chiều với $arrow(v)$ ($a dot v < 0$).],
  [$arrow(a)$ luôn cùng chiều với $arrow(v)$ ($a dot v > 0$).],
  [Gia tốc $a$ bắt buộc phải bằng $0$.],
  [Gia tốc $a$ bắt buộc phải mang dấu âm.], cols: 2)

#mcq(12, badge("2.4-TH"), [Một ô tô đang chuyển động thẳng theo chiều dương với vận tốc $22 "m/s"$ thì giảm ga, sau $4 "s"$ vận tốc giảm xuống còn $10 "m/s"$. Gia tốc trung bình của ô tô trong $4 "s"$ đó là:],
  [$3 "m/s"^2$.], [$-3 "m/s"^2$.], [$-"5,5" "m/s"^2$.], [$8 "m/s"^2$.], cols: 4)

#mcq(13, badge("2.5-NB"), [Đồ thị vận tốc – thời gian $(v - t)$ của một vật chuyển động thẳng biến đổi đều có dạng là:],
  [Một đường thẳng song song với trục thời gian $O t$.],
  [Một đoạn thẳng xiên góc với trục thời gian $O t$.],
  [Một đường tròn tâm $O$.],
  [Một đường hypebol.], cols: 2)

#mcq(14, badge("2.5-NB"), [Trong các phương trình dưới đây ($x$ tính bằng mét, $t$ tính bằng giây), phương trình nào biểu diễn tọa độ của một vật *chuyển động thẳng biến đổi đều*?],
  [$x = 5 + 4 t$], [$x = 12$], [$x = 2 + 6 t - 2 t^2$], [$x = 3 / t$], cols: 4)

#mcq(15, badge("2.5-TH"), [Một xe đua xuất phát từ trạng thái đứng yên, chuyển động thẳng nhanh dần đều với gia tốc $3 "m/s"^2$. Quãng đường xe đua đi được cho tới khi đạt vận tốc $12 "m/s"$ là:],
  [$24 "m"$.], [$48 "m"$.], [$18 "m"$.], [$36 "m"$.], cols: 4)

#mcq(16, badge("2.6-NB"), [Gia tốc rơi tự do $g$ của các vật ở gần bề mặt Trái Đất có đặc điểm nào sau đây?],
  [Phụ thuộc vào khối lượng của vật được thả rơi.],
  [Phụ thuộc vào vĩ độ địa lí và độ cao của nơi thả vật.],
  [Bằng $0$ tại xích đạo và cực đại tại hai địa cực.],
  [Tăng đều theo thời gian trong quá trình vật rơi.], cols: 2)

#mcq(17, badge("2.6-TH"), [Thả một hòn đá rơi tự do từ đỉnh một tòa tháp xuống đất, sau $"4,0" "s"$ hòn đá chạm đất. Lấy $g = 10 "m/s"^2$, bỏ qua sức cản không khí. Chiều cao của tòa tháp là:],
  [$40 "m"$.], [$80 "m"$.], [$160 "m"$.], [$20 "m"$.], cols: 4)

#mcq(18, badge("2.6-TH"), [Một vật rơi tự do từ độ cao đủ lớn tại nơi có $g = 10 "m/s"^2$. Quãng đường vật rơi được *chỉ tính riêng trong giây thứ 3* (từ $t = 2 "s"$ đến $t = 3 "s"$) là:],
  [$45 "m"$.], [$15 "m"$.], [$25 "m"$.], [$30 "m"$.], cols: 4)

#section-heading("PHẦN II. Câu trắc nghiệm đúng sai (2,0 điểm — Câu 1 và Câu 2)")

#tf-question(
  "1",
  "Ma trận 2–I: Đồ thị (d – t) & Tốc độ, vận tốc",
  [Một người đi xe đạp trên một đoạn đường thẳng có đồ thị độ dịch chuyển – thời gian $(d - t)$ gồm ba đoạn $A B$, $B C$, $C D$ như hình vẽ.],
  image("assets/exam2_dt_graph.svg", width: 58%),
  [Tại thời điểm $t = 0$, người đi xe đạp xuất phát ở vị trí cách gốc tọa độ $20 "m"$ về phía dương.],
  [Trong $10 "s"$ đầu tiên (đoạn $A B$), người đó chuyển động thẳng đều với tốc độ $4 "m/s"$.],
  [Từ $t = 10 "s"$ đến $t = 20 "s"$ (đoạn $B C$), người đi xe đạp dừng lại nghỉ bên đường.],
  [Từ $t = 20 "s"$ đến $t = 35 "s"$ (đoạn $C D$), vận tốc của người đi xe đạp có giá trị là $+4 "m/s"$.],
)

#tf-question(
  "2",
  "Ma trận 2–II: Chuyển động thẳng biến đổi đều",
  [Một chất điểm chuyển động thẳng trên trục $O x$ có phương trình tọa độ theo thời gian là: $x = 10 + 12 t - "1,5" t^2$ (với $x$ tính bằng mét, $t$ tính bằng giây, kể từ $t = 0$).],
  none,
  [Tại thời điểm ban đầu $t = 0$, chất điểm ở tọa độ $x_0 = 10 "m"$ và có vận tốc đầu $v_0 = 12 "m/s"$.],
  [Gia tốc của chất điểm có giá trị là $a = -"1,5" "m/s"^2$.],
  [Trong giai đoạn đầu chuyển động, chất điểm chuyển động thẳng chậm dần đều và dừng lại tạm thời ở thời điểm $t = 4 "s"$.],
  [Quãng đường chất điểm đi được từ lúc $t = 0$ cho đến lúc dừng lại ở $t = 4 "s"$ bằng $24 "m"$.],
)

#section-heading("PHẦN III. Câu trắc nghiệm trả lời ngắn (0,5 điểm — Câu 1 và Câu 2)")

- *Câu 1* #badge("2.2-NB")*:* Trong thí nghiệm đo tốc độ tức thời bằng cổng quang điện (`MODE A`), viên bi thép có đường kính $d = 18 "mm"$ lăn qua chắn chùm tia sáng tại cổng quang điện trong khoảng thời gian $"0,03" "s"$. Tốc độ tức thời của viên bi tại cổng đó bằng bao nhiêu $"m/s"$?
- *Câu 2* #badge("2.6-TH")*:* Một quả cầu nhỏ được thả rơi tự do từ độ cao $h = "44,1" "m"$ xuống mặt đất tại nơi có gia tốc rơi tự do $g = "9,8" "m/s"^2$. Thời gian từ lúc thả đến lúc quả cầu chạm đất bằng bao nhiêu giây?

#section-heading("PHẦN IV. Tự luận (3,0 điểm — Câu 1, Câu 2 và Câu 3)")

- *Câu 1 (1,0 điểm — Mục 2.2 Thông hiểu):* Một con sông thẳng rộng $180 "m"$ có dòng nước chảy đều với tốc độ $"1,5" "m/s"$ so với bờ. Một chiếc xuồng máy hướng mũi vuông góc với bờ sông và chạy đều với tốc độ $"2,0" "m/s"$ đối với mặt nước.\
  *a)* Tính độ lớn vận tốc của xuồng máy đối với bờ sông.\
  *b)* Tính thời gian xuồng đi sang đến bờ bên kia và khoảng cách xuồng bị nước đẩy trôi xuôi dòng theo phương dọc bờ sông.
- *Câu 2 (1,0 điểm — Mục 2.5 Vận dụng):* Một ô tô đi qua điểm $A$ với tốc độ $36 "km/h"$ và tăng tốc chuyển động thẳng nhanh dần đều về phía điểm $B$ cách $A$ một đoạn $75 "m"$. Khi đi qua điểm $B$, ô tô đạt tốc độ $72 "km/h"$. Chọn chiều dương từ $A$ đến $B$.\
  *a)* Tính gia tốc của ô tô trên đoạn đường $A B$.\
  *b)* Tính thời gian ô tô đi từ $A$ đến $B$.
- *Câu 3 (1,0 điểm — Mục 2.5 Vận dụng cao):* Cùng một lúc tại điểm $A$ trên một đường thẳng, xe thứ nhất đi qua $A$ và chuyển động thẳng đều với vận tốc $v_1 = 12 "m/s"$; đồng thời xe thứ hai bắt đầu khởi hành từ $A$ ($v_(0 2) = 0$) chuyển động thẳng nhanh dần đều đuổi theo xe thứ nhất với gia tốc $a_2 = "1,5" "m/s"^2$.\
  *a)* Xác định thời điểm và vị trí (cách $A$ bao xa) khi xe thứ hai đuổi kịp xe thứ nhất.\
  *b)* Tính vận tốc của xe thứ hai lúc đuổi kịp xe thứ nhất và khoảng cách xa nhất giữa hai xe trước khi xe thứ hai đuổi kịp.

#v(5pt)
#solution-card("ĐÁP ÁN & BIỂU ĐIỂM CHẤM CHI TIẾT — ĐỀ THI CHUẨN MA TRẬN SỐ 02", [
  *1. PHẦN I (4,50 điểm — 0,25 đ/câu):*\
  #set text(size: 8.5pt)
  #table(
    columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: center + horizon,
    stroke: 0.5pt + c-border,
    fill: (x, y) => if calc.even(y) { rgb("#EFF6FF") } else { white },
    inset: 3.5pt,
    [*1. B*], [*2. A*], [*3. B*], [*4. B*], [*5. B*], [*6. D*], [*7. C*], [*8. B*], [*9. D*],
    [*10. B*], [*11. B*], [*12. B*], [*13. B*], [*14. C*], [*15. A*], [*16. B*], [*17. B*], [*18. C*],
  )
  #set text(size: 9.0pt)
  _Giải nhanh các câu tính toán Phần I:_ *Câu 6:* Quay về vạch xuất phát $arrow.r d = 0$. *Câu 7:* $d = sqrt(80^2 + 60^2) = 100 "m"$. *Câu 10:* $v = (10 - 30)/(5 - 0) = -4 "m/s"$. *Câu 12:* $a = (10 - 22)/4 = -3 "m/s"^2$. *Câu 15:* $s = (12^2 - 0)/(2 dot 3) = 24 "m"$. *Câu 17:* $h = 1/2 dot 10 dot 4^2 = 80 "m"$. *Câu 18:* $Delta s_3 = 1/2 dot 10 dot (3^2 - 2^2) = 25 "m"$.

  #v(3pt)
  *2. PHẦN II (2,00 điểm):*\
  • *Câu 1:* *a) Đúng | b) Đúng | c) Đúng | d) Sai.* _(Ý b: $v_(A B) = (60 - 20)/10 = 4 "m/s"$; ý d sai vì trên $C D$, $v_(C D) = (0 - 60)/(35 - 20) = -4 "m/s" < 0$, dấu âm!)_.\
  • *Câu 2:* *a) Đúng | b) Sai | c) Đúng | d) Đúng.* _(Ý b sai vì $1/2 a = -"1,5" arrow.r.double a = -3 "m/s"^2$; ý c: $v = 12 - 3 t = 0 arrow.r t = 4 "s"$; ý d: $s = 12 dot 4 - "1,5" dot 4^2 = 24 "m"$)_.

  #v(3pt)
  *3. PHẦN III (0,50 điểm — 0,25 đ/câu):*\
  • *Câu 1:* Điền *`0,6`* _(Đổi $d = 18 "mm" = "0,018" "m" arrow.r v_t = "0,018" / "0,03" = "0,6" "m/s"$)_. #h(10pt)
  • *Câu 2:* Điền *`3`* _($t = sqrt((2 dot "44,1") / "9,8") = sqrt(9) = 3 "s"$)_.

  #v(3pt)
  *4. PHẦN IV – TỰ LUẬN (3,00 điểm):*\
  • *Câu 1 (1,00 đ):* Gọi (1) xuồng, (2) nước, (3) bờ: $arrow(v)_("1,3") = arrow(v)_("1,2") + arrow(v)_("2,3")$. *(0,25 đ)*\
    – a) Vì $arrow(v)_("1,2") perp arrow(v)_("2,3")$ nên độ lớn vận tốc xuồng so với bờ: $v_("1,3") = sqrt("2,0"^2 + "1,5"^2) = #strong[$"2,5" "m/s"$]$. *(0,25 đ)*\
    – b) Thời gian qua sông: $t = L / v_("1,2") = 180 / "2,0" = #strong[$90 "s"$]$. Độ trôi xuôi dòng: $Delta x = v_("2,3") dot t = "1,5" dot 90 = #strong[$135 "m"$]$. *(0,50 đ)*\
  • *Câu 2 (1,00 đ):* Đổi $v_A = 36 "km/h" = 10 "m/s"$; $v_B = 72 "km/h" = 20 "m/s"$; $d = 75 "m"$. *(0,25 đ)*\
    – a) Áp dụng $v_B^2 - v_A^2 = 2 a d arrow.r a = (20^2 - 10^2)/(2 dot 75) = 300 / 150 = #strong[$2 "m/s"^2$]$. *(0,50 đ)*\
    – b) Thời gian đi từ $A$ đến $B$: $t = (v_B - v_A)/a = (20 - 10)/2 = #strong[$5 "s"$]$. *(0,25 đ)*\
  • *Câu 3 (1,00 đ):* Chọn gốc tọa độ tại $A$, chiều dương là chiều hai xe chạy, gốc thời gian lúc xuất phát: $d_1 = 12 t$ _(m)_; $d_2 = 1/2 dot "1,5" t^2 = "0,75" t^2$ _(m)_. *(0,25 đ)*\
    – a) Khi xe (2) đuổi kịp xe (1) ($t > 0$): $d_1 = d_2 arrow.l.r.double "0,75" t^2 = 12 t arrow.r.double #strong[$t = 16 "s"$]$. Vị trí gặp nhau cách $A$: $d = 12 dot 16 = #strong[$192 "m"$]$. *(0,40 đ)*\
    – b) Vận tốc xe (2) lúc đuổi kịp: $v_2 = a_2 t = "1,5" dot 16 = #strong[$24 "m/s"$]$. Trước khi đuổi kịp ($0 < t < 16$), khoảng cách giữa hai xe là $Delta d = 12 t - "0,75" t^2 = 48 - "0,75"(t - 8)^2 <= 48 "m"$ $arrow.r$ xa nhất là *$Delta d_("max") = 48 "m"$* tại $t = 8 "s"$ (khi $v_2 = v_1 = 12 "m/s"$). *(0,35 đ)*
])

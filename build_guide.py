from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from xml.sax.saxutils import escape

TITLE='ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I – VẬT LÍ 10'
SUB='Năm học 2026–2027 | Hệ thống kiến thức, công thức và câu hỏi – đáp án'
sections=[
('0. ĐỌC MA TRẬN ĐỂ ÔN ĐÚNG TRỌNG TÂM',[
('Nguồn này cho biết những gì?','Tệp “MA TRẬN ĐẶC TẢ KTGK I L10- 2026.docx” là ma trận và đặc tả, không phải đề thi hoàn chỉnh: không có nguyên văn đề, lựa chọn A–D, dữ kiện từng câu hay đáp án chính thức. Vì vậy, phần hỏi–đáp dưới đây là bộ câu hỏi ôn tập tự biên soạn bám sát toàn bộ yêu cầu nêu trong ma trận; không thể khẳng định đó là toàn văn các câu sẽ xuất hiện trong đề.'),
('Phạm vi và cấu trúc dự kiến?','Phạm vi nêu trong tài liệu gồm: làm quen với Vật lí; an toàn thực hành; phép đo và sai số; độ dịch chuyển/quãng đường; tốc độ/vận tốc; thực hành đo tốc độ; đồ thị độ dịch chuyển–thời gian; gia tốc; chuyển động thẳng biến đổi đều; rơi tự do. Đề dự kiến làm trong 50 phút, 70% trắc nghiệm và 30% tự luận. Ma trận thể hiện Phần I 18 câu; Phần II 2 câu, mỗi câu 4 ý; Phần III 2 câu; Phần IV có các ý vận dụng. Số câu/ý giữa cách trình bày và dòng tổng trong bảng không hoàn toàn rõ, nên hãy theo thông báo chính thức của giáo viên.'),
('Ôn tập thế nào cho nhanh?','Nhớ định nghĩa và đơn vị trước; luyện đổi đơn vị; chọn chiều dương rồi ghi dấu đại lượng; với mỗi bài toán hãy viết dữ kiện, công thức, thay số, đơn vị và kết luận. Tự che đáp án để làm trước, sau đó mới đối chiếu.')]),
('1. LÀM QUEN VỚI VẬT LÍ',[
('Vật lí nghiên cứu điều gì?','Vật lí nghiên cứu các dạng vận động của vật chất, năng lượng và những quy luật tương tác, biến đổi của chúng trong tự nhiên; từ vi mô đến vĩ mô.'),
('Nêu một số thành tựu vật lí gắn với các cuộc cách mạng công nghiệp.','Cách mạng công nghiệp lần thứ nhất gắn với cơ học, máy hơi nước; lần hai với điện từ học, động cơ điện và truyền thông; lần ba với điện tử, bán dẫn, máy tính và công nghệ số; lần bốn với hệ thống thông minh, cảm biến, dữ liệu lớn, trí tuệ nhân tạo và vật liệu/công nghệ mới. Đây là các ví dụ tiêu biểu, không phải danh sách duy nhất.'),
('Các giai đoạn phát triển của vật lí có thể khái quát ra sao?','Từ quan sát và mô tả tự nhiên thời cổ đại; đến vật lí cổ điển với cơ học, nhiệt học, điện từ học; rồi vật lí hiện đại với thuyết tương đối và lượng tử; ngày nay các lĩnh vực tiếp tục mở rộng và liên ngành. Ranh giới giai đoạn là cách khái quát lịch sử.'),
('Phương pháp nghiên cứu vật lí gồm những cách nào?','Phương pháp thực nghiệm (quan sát, đặt câu hỏi/giả thuyết, thiết kế phép đo, thu thập và xử lí dữ liệu, rút kết luận) và phương pháp lí thuyết (xây dựng mô hình, lập luận/toán học, dự đoán rồi đối chiếu thực nghiệm). Hai phương pháp thường bổ sung cho nhau.'),
('Trình bày quy trình nghiên cứu vật lí cơ bản.','Nêu vấn đề → hình thành giả thuyết/mô hình → thiết kế và tiến hành nghiên cứu (thí nghiệm hoặc lí thuyết) → xử lí, đánh giá dữ liệu → kết luận, công bố/kiểm chứng và điều chỉnh giả thuyết nếu cần. Kết luận khoa học cần có bằng chứng và có thể được kiểm tra lại.')]),
('2. AN TOÀN TRONG PHÒNG THỰC HÀNH',[
('Nêu các nguy cơ thường gặp khi làm thí nghiệm Vật lí.','Điện giật/chập điện; bỏng do nguồn nóng; vỡ thủy tinh, vật sắc gây đứt tay; vật rơi hoặc chuyển động va đập; tia sáng mạnh/laser gây tổn thương mắt; hóa chất (nếu có) bắn/đổ; dây dẫn vướng hoặc thiết bị đặt không vững.'),
('Nêu các nguyên tắc an toàn cơ bản.','Đọc hướng dẫn và nhận biết cảnh báo trước khi làm; chỉ dùng thiết bị theo chỉ dẫn của giáo viên; kiểm tra dây, nguồn và lắp mạch khi nguồn đã ngắt; không chạm phần dẫn điện trần; giữ bàn gọn, khô; dùng kính/dụng cụ bảo hộ phù hợp; không tự ý bật nguồn hay thay đổi bố trí; báo ngay sự cố, không tự xử lí nguy hiểm; tắt nguồn và thu dọn sau thí nghiệm.'),
('Khi thấy dây điện hở hoặc có người bị điện giật, xử trí thế nào?','Không chạm trực tiếp vào người hoặc dây điện. Báo giáo viên/người lớn, ngắt nguồn điện an toàn nếu có thể; gọi hỗ trợ khẩn cấp. Chỉ sơ cứu khi đã bảo đảm nguồn điện được cách ly và theo hướng dẫn được đào tạo.'),
('Biển báo an toàn có tác dụng gì?','Cảnh báo nguy cơ, cấm hành vi nguy hiểm, yêu cầu biện pháp bảo hộ hoặc chỉ dẫn lối thoát/thiết bị khẩn cấp. Đọc hình dạng, màu sắc và biểu tượng, sau đó tuân theo hướng dẫn tại phòng thực hành; không suy đoán chỉ từ màu nếu chưa hiểu kí hiệu.'),
('Dùng dụng cụ đo đúng cách cần lưu ý gì?','Chọn thang đo và giới hạn đo phù hợp; đặt mắt vuông góc với vạch chia để giảm sai số đọc; kiểm tra điểm 0/hiệu chỉnh nếu cần; không vượt quá giới hạn dụng cụ; đọc đúng đơn vị; thao tác nhẹ nhàng và tắt/hoàn nguyên thiết bị sau khi đo.')]),
('3. PHÉP ĐO VÀ SAI SỐ',[
('Phân biệt phép đo trực tiếp và gián tiếp.','Đo trực tiếp: đọc đại lượng cần đo ngay trên dụng cụ (ví dụ đo thời gian bằng đồng hồ). Đo gián tiếp: tính đại lượng cần tìm từ các đại lượng đo trực tiếp và quan hệ vật lí (ví dụ vận tốc trung bình v=s/t).'),
('Sai số ngẫu nhiên và sai số hệ thống khác nhau thế nào?','Sai số ngẫu nhiên biến đổi khó dự đoán giữa các lần đo, do dao động thao tác/môi trường; đo lặp và lấy trung bình giúp giảm ảnh hưởng. Sai số hệ thống làm kết quả lệch theo một hướng tương đối ổn định, thường do dụng cụ lệch chuẩn, phương pháp hoặc cách đặt; cần hiệu chỉnh và loại nguyên nhân.'),
('Nêu một số nguyên nhân gây sai số.','Độ chia/độ chính xác hữu hạn của dụng cụ; điểm 0 lệch; mắt nhìn lệch; phản xạ khi bấm giờ; điều kiện môi trường; vật/dụng cụ rung; thao tác chưa nhất quán; mô hình tính toán đã bỏ qua một số ảnh hưởng.'),
('Viết công thức giá trị trung bình và sai số tuyệt đối trung bình.','Với n phép đo x₁,…,xₙ: x̄=(x₁+x₂+…+xₙ)/n. Sai số tuyệt đối mỗi lần: Δxᵢ=|xᵢ−x̄|; sai số ngẫu nhiên tuyệt đối trung bình: Δx_tb=(ΣΔxᵢ)/n. Sai số dụng cụ được xét thêm theo quy ước của dụng cụ và hướng dẫn lớp học.'),
('Cách ghi kết quả đo và sai số tỉ đối?','Sai số tỉ đối δ=(Δx/x̄)×100%. Ghi x=x̄±Δx (kèm đơn vị), làm tròn sai số và giá trị đo đến hàng thập phân tương ứng; không ghi quá nhiều chữ số có nghĩa. Nếu đề cho sai số dụng cụ, tổng sai số tuyệt đối thường được xác định theo hướng dẫn bài học (thường cộng thành phần ngẫu nhiên và dụng cụ).'),
('Ví dụ tính trung bình, sai số và sai số tỉ đối: đo 1,20; 1,24; 1,22 m.','x̄=(1,20+1,24+1,22)/3=1,22 m. Các độ lệch là 0,02; 0,02; 0,00 m nên Δx_tb=0,013… m. δ≈(0,0133/1,22)×100%≈1,1%. Có thể ghi x≈(1,22±0,01) m nếu làm tròn theo độ chính xác phù hợp; nếu tính cả sai số dụng cụ, phải cộng/đánh giá thành phần đó theo quy ước được dạy.')]),
('4. ĐỘ DỊCH CHUYỂN VÀ QUÃNG ĐƯỜNG',[
('Quãng đường và độ dịch chuyển là gì?','Quãng đường s là độ dài toàn bộ quỹ đạo vật đã đi, là đại lượng vô hướng và không âm. Độ dịch chuyển Δx=x₂−x₁ (trong một chiều) hoặc vectơ từ vị trí đầu đến vị trí cuối; cho biết sự thay đổi vị trí, có phương chiều và có thể bằng 0.'),
('So sánh quãng đường với độ lớn độ dịch chuyển.','Luôn có s≥|Δx|. Hai đại lượng bằng nhau khi vật đi thẳng một chiều, không đổi hướng; nếu quay lại hoặc đi theo đường vòng thì quãng đường lớn hơn độ lớn độ dịch chuyển.'),
('Một người đi 3 m về phía đông rồi 4 m về phía tây. Tính quãng đường và độ dịch chuyển.','Chọn chiều đông dương: s=3+4=7 m; Δx=+3−4=−1 m, tức độ dịch chuyển 1 m về phía tây. Độ lớn độ dịch chuyển 1 m nhỏ hơn quãng đường 7 m.'),
('Vật ở x₁=−2 m rồi đến x₂=5 m trên trục thẳng.','Δx=x₂−x₁=5−(−2)=+7 m. Quãng đường bằng 7 m nếu chuyển động chỉ theo một chiều từ vị trí đầu đến cuối; nếu có đường đi vòng/đổi hướng thì cần biết hành trình mới tính được quãng đường.')]),
('5. TỐC ĐỘ, VẬN TỐC VÀ ĐO TỐC ĐỘ',[
('Tốc độ trung bình là gì? Công thức và đơn vị?','Tốc độ trung bình bằng tổng quãng đường chia tổng thời gian: v_tb=s/t. Là đại lượng vô hướng, đơn vị SI là m/s; cũng thường dùng km/h. Đổi: 1 m/s=3,6 km/h.'),
('Phân biệt tốc độ tức thời với tốc độ trung bình.','Tốc độ trung bình mô tả toàn hành trình trong khoảng thời gian xét. Tốc độ tức thời cho biết mức nhanh/chậm tại một thời điểm, như số chỉ tốc kế; trong mô hình chuyển động liên tục, là giới hạn của tốc độ trung bình khi khoảng thời gian rất nhỏ.'),
('Vận tốc khác tốc độ ở điểm nào?','Vận tốc gắn với độ dịch chuyển và có hướng: trong một chiều v_tb=Δx/Δt. Tốc độ gắn với quãng đường và không có hướng. Độ lớn vận tốc trung bình không vượt tốc độ trung bình; khi vật đổi chiều, chúng thường khác nhau.'),
('Tính tốc độ trung bình: đi 120 m trong 20 s.','v_tb=120/20=6 m/s. Đổi ra km/h: 6×3,6=21,6 km/h.'),
('Một vật đi 60 m trong 10 s rồi 40 m trong 20 s. Tính tốc độ trung bình toàn hành trình.','Không lấy trung bình cộng hai tốc độ nếu thời gian khác nhau. v_tb=(60+40)/(10+20)=100/30≈3,33 m/s.'),
('Vận tốc trung bình của vật đi 60 m sang phải trong 10 s rồi 40 m sang trái trong 20 s?','Chọn phải dương: Δx=60−40=20 m; tổng thời gian 30 s. v_tb=20/30≈+0,67 m/s, nghĩa là hướng sang phải. Quãng đường 100 m nên tốc độ trung bình 100/30≈3,33 m/s.'),
('Cộng vận tốc cùng phương như thế nào?','Dùng quy ước dấu theo chiều dương: v_A/C=v_A/B+v_B/C. Cùng chiều thì cộng độ lớn; ngược chiều thì trừ đại số, hướng của kết quả theo dấu. Ví dụ 5 m/s sang đông và 2 m/s sang tây cho vận tốc hợp 3 m/s sang đông.'),
('Hai vận tốc vuông góc 3 m/s và 4 m/s, độ lớn vận tốc hợp bằng bao nhiêu?','Với hai vectơ vuông góc: v=√(v₁²+v₂²)=√(9+16)=5 m/s. Hướng hợp với vectơ 3 m/s một góc θ thỏa tanθ=4/3.'),
('Đo tốc độ bằng cổng quang điện: cách làm và vai trò hai cổng?','Vật gắn bản chắn sáng có chiều dài đã biết L đi qua cổng; cổng đo thời gian chắn sáng Δt, suy ra tốc độ tức thời gần đúng v=L/Δt. Hai cổng giúp đo thời gian vật đi giữa hai vị trí, khảo sát chuyển động/biến thiên vận tốc hoặc loại ảnh hưởng thao tác bấm tay tùy chế độ thiết bị. Cần chọn đúng chế độ, nối đúng cổng và kiểm tra đơn vị.'),
('Ưu, nhược điểm của đồng hồ hiện số và cổng quang điện?','Ưu điểm: tự động đo thời gian với độ phân giải tốt, giảm sai số phản xạ người bấm; hai cổng cho phép xác định thời gian giữa hai vị trí. Hạn chế: cần lắp đặt/đấu nối và chọn chế độ đúng, phải căn thẳng vật và biết chiều dài bản chắn sáng; thiết bị có giới hạn độ phân giải và có thể bị ảnh hưởng bởi lắp đặt sai. Đồng hồ bấm tay đơn giản nhưng phản xạ người đo làm tăng sai số.')]),
('6. ĐỒ THỊ ĐỘ DỊCH CHUYỂN – THỜI GIAN',[
('Đồ thị d–t cho biết điều gì?','Trục ngang biểu diễn thời gian t, trục đứng biểu diễn độ dịch chuyển d (hoặc tọa độ theo quy ước). Độ dốc thể hiện vận tốc: v=Δd/Δt. Đường nằm ngang: vật đứng yên; dốc dương/âm: vận tốc dương/âm; độ dốc càng lớn về độ lớn thì tốc độ càng lớn.'),
('Trên đồ thị d–t, vật đi từ d=2 m lúc t=0 đến d=14 m lúc t=4 s. Tính vận tốc.','v=(14−2)/(4−0)=3 m/s. Đồ thị là đoạn thẳng nên vận tốc không đổi trong khoảng này.'),
('Đồ thị có đoạn d không đổi từ 3 s đến 5 s. Diễn giải?','Độ dịch chuyển/vị trí không đổi theo thời gian nên vật đứng yên trong khoảng 3–5 s; vận tốc bằng 0.'),
('Đồ thị d–t có độ dốc âm có nghĩa gì?','Theo chiều dương đã chọn, tọa độ/độ dịch chuyển giảm theo thời gian; vận tốc âm, vật chuyển động theo chiều âm. Điều này không nhất thiết có nghĩa là vật chậm lại.'),
('Làm sao tìm vị trí và vận tốc tại một thời điểm trên đồ thị?','Đọc tung độ tại thời điểm cần tìm để lấy d (hoặc tọa độ). Tính độ dốc của đoạn đồ thị chứa thời điểm đó để có vận tốc; tại điểm gấp khúc, xét độ dốc bên trái/phải riêng, vận tốc tức thời có thể không xác định ngay tại điểm đổi đoạn.'),
('Vật đi từ 0 đến 10 m, rồi quay về 4 m. Tính quãng đường và độ dịch chuyển.','Quãng đường=10+(10−4)=16 m. Độ dịch chuyển=4−0=+4 m. Trên đồ thị d–t, quãng đường là tổng độ biến thiên tuyệt đối của d qua từng đoạn; độ dịch chuyển chỉ là vị trí cuối trừ vị trí đầu.'),
('Cách phác họa đồ thị d–t khi biết chuyển động?','Lập trục t và d, chọn tỉ lệ; xác định các điểm (t,d) từ điều kiện ban đầu và vận tốc/độ dịch chuyển; nối theo từng giai đoạn. Chuyển động đều là đoạn thẳng có độ dốc v; vật đứng yên là đoạn ngang. Ghi đơn vị, chiều dương và các điểm đổi trạng thái.')]),
('7. CHUYỂN ĐỘNG BIẾN ĐỔI VÀ GIA TỐC',[
('Chuyển động biến đổi là gì?','Chuyển động có vận tốc thay đổi theo thời gian về độ lớn, hướng hoặc cả hai. Chuyển động thẳng có thể biến đổi độ lớn vận tốc; chuyển động cong có thể đổi hướng dù tốc độ không đổi.'),
('Định nghĩa, công thức và đơn vị gia tốc?','Gia tốc đặc trưng cho tốc độ biến thiên của vận tốc: a=Δv/Δt=(v−v₀)/t nếu xét khoảng từ 0 đến t. Là vectơ cùng hướng với Δv; đơn vị SI m/s².'),
('Một vật tăng vận tốc từ 4 lên 16 m/s trong 6 s. Tính gia tốc.','a=(16−4)/6=2 m/s².'),
('Làm thế nào nhận biết nhanh dần hay chậm dần trên đường thẳng?','Chọn trục và xét dấu v, a. Nếu v và a cùng dấu thì tốc độ tăng (nhanh dần); nếu trái dấu thì tốc độ giảm (chậm dần). Không kết luận chỉ bằng “a dương là nhanh dần”: dấu phụ thuộc chiều dương đã chọn.'),
('Vật có v=−8 m/s, a=+2 m/s²: nhanh hay chậm dần?','v và a trái dấu nên tốc độ đang giảm: vật chậm dần. Nếu gia tốc giữ nguyên đủ lâu, vật dừng rồi đổi chiều; sau khi đổi chiều, tốc độ có thể tăng.')]),
('8. CHUYỂN ĐỘNG THẲNG BIẾN ĐỔI ĐỀU',[
('Chuyển động thẳng biến đổi đều là gì?','Chuyển động theo đường thẳng có gia tốc không đổi; vận tốc biến thiên đều theo thời gian. Nhanh dần đều khi tốc độ tăng đều, chậm dần đều khi tốc độ giảm đều.'),
('Nêu các công thức cơ bản (trục thẳng, gia tốc không đổi).','v=v₀+at; Δx=v₀t+(1/2)at²; v²−v₀²=2aΔx; vận tốc trung bình trong khoảng xét v_tb=(v₀+v)/2 nên Δx=[(v₀+v)/2]t. Dùng đại lượng có dấu nhất quán; Δx là độ dịch chuyển, không mặc nhiên là quãng đường.'),
('Một xe xuất phát từ nghỉ, a=2 m/s² trong 5 s. Tính vận tốc cuối và độ dịch chuyển.','v₀=0; v=0+2×5=10 m/s. Δx=0+(1/2)×2×5²=25 m.'),
('Một xe đang đi 20 m/s hãm với gia tốc −4 m/s². Sau bao lâu dừng, quãng đường phanh bao nhiêu?','Chọn chiều chuyển động là dương. Khi dừng v=0: t=(v−v₀)/a=(0−20)/(−4)=5 s. Δx=(v²−v₀²)/(2a)=(0−400)/(−8)=50 m. Vật không đổi chiều trong khoảng phanh nên quãng đường 50 m.'),
('Vật có v₀=3 m/s, a=−1 m/s² trong 4 s. Tính vận tốc cuối và độ dịch chuyển; có thể lấy quãng đường bằng độ dịch chuyển không?','v=3−4=−1 m/s. Δx=3×4+(1/2)(−1)×16=4 m. Vật dừng ở t=3 s rồi đổi chiều trong giây cuối, nên quãng đường= (3×3/2) + (1×1/2)=5 m, không phải 4 m.'),
('Quy trình giải bài toán chuyển động thẳng biến đổi đều?','Vẽ sơ đồ, chọn chiều dương và gốc; ghi v₀, v, a, t, Δx kèm dấu; đổi đơn vị về SI; chọn phương trình có đại lượng cần tìm; thay số và kiểm tra đơn vị, dấu, tính hợp lí. Nếu vật đổi chiều, chia hành trình tại thời điểm v=0 để tính quãng đường.')]),
('9. RƠI TỰ DO',[
('Rơi tự do là gì? Đặc điểm?','Rơi tự do là chuyển động chỉ dưới tác dụng của trọng lực (bỏ qua sức cản không khí). Gần mặt đất, vật rơi theo phương thẳng đứng xuống, nhanh dần đều với gia tốc g≈9,8 m/s² (nhiều bài cho lấy 10 m/s²).'),
('Vật nào gần đúng rơi tự do?','Vật rơi trong không khí khi lực cản nhỏ so với trọng lực, chẳng hạn vật nhỏ, đặc, rơi quãng ngắn với tốc độ chưa quá lớn. Tờ giấy phẳng rơi chậm do cản không khí đáng kể; trong chân không mọi vật rơi với cùng gia tốc g nếu cùng điều kiện vị trí.'),
('Viết công thức rơi tự do từ trạng thái nghỉ.','Chọn chiều xuống dương: v=gt; h=(1/2)gt²; v²=2gh. Nếu có vận tốc ban đầu theo phương thẳng đứng: v=v₀+gt, Δy=v₀t+(1/2)gt² với chiều dương phù hợp. Luôn xác định chiều trước khi gán dấu.'),
('Vật thả rơi từ nghỉ trong 2 s, lấy g=10 m/s². Tìm tốc độ và độ cao đã rơi.','v=gt=10×2=20 m/s; h=(1/2)×10×2²=20 m.'),
('Vật rơi từ độ cao 45 m, bỏ qua cản không khí, g=10 m/s². Thời gian và tốc độ ngay trước đất?','h=(1/2)gt² nên t=√(2h/g)=√(90/10)=3 s. v=gt=30 m/s hướng xuống.'),
('Ném một vật thẳng đứng lên với v₀=20 m/s, g=10 m/s². Thời gian lên cao nhất và độ cao tăng thêm?','Tại đỉnh v=0: t=−v₀/(−g)=v₀/g=2 s. Δh=v₀²/(2g)=400/20=20 m. Nếu bỏ qua cản, tổng thời gian lên rồi về cùng độ cao là 4 s.')]),
('10. TỰ KIỂM TRA NHANH – ĐÁP ÁN',[
('1) Đổi 72 km/h sang m/s.','72/3,6=20 m/s.'),
('2) Vật đi một vòng tròn rồi trở về điểm xuất phát. Độ dịch chuyển?','Bằng 0; quãng đường vẫn lớn hơn 0.'),
('3) Tốc độ 5 m/s trong 12 s, chuyển động thẳng một chiều. Quãng đường?','s=vt=60 m.'),
('4) Đồ thị d–t nằm ngang.','Vật đứng yên, v=0.'),
('5) v=+6 m/s, a=−2 m/s².','Chậm dần; tốc độ giảm tại thời điểm xét.'),
('6) v₀=2 m/s, a=3 m/s², t=4 s. Tìm v và Δx.','v=2+3×4=14 m/s; Δx=2×4+(1/2)×3×16=32 m.'),
('7) Sai số tỉ đối nếu x̄=5,0 cm, Δx=0,1 cm?','δ=(0,1/5,0)×100%=2%.'),
('8) Khi nào tốc độ trung bình bằng độ lớn vận tốc trung bình?','Khi vật đi thẳng và không đổi chiều trong khoảng xét (quãng đường bằng độ lớn độ dịch chuyển).')])]

out='De_cuong_on_tap_Vat_li_10_GK1_2026-2027.pdf'
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DV',font)); pdfmetrics.registerFont(TTFont('DV-Bold',bold))
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Cover',fontName='DV-Bold',fontSize=22,leading=30,textColor=colors.HexColor('#102A43'),alignment=TA_CENTER,spaceAfter=16))
styles.add(ParagraphStyle(name='Sub',fontName='DV',fontSize=11,leading=17,textColor=colors.HexColor('#486581'),alignment=TA_CENTER))
styles.add(ParagraphStyle(name='H1x',fontName='DV-Bold',fontSize=15,leading=20,textColor=colors.HexColor('#0B7285'),spaceBefore=12,spaceAfter=7,keepWithNext=True))
styles.add(ParagraphStyle(name='Q',fontName='DV-Bold',fontSize=9.5,leading=14,textColor=colors.HexColor('#243B53'),spaceBefore=6,spaceAfter=2,keepWithNext=True))
styles.add(ParagraphStyle(name='A',fontName='DV',fontSize=9,leading=13,textColor=colors.HexColor('#334E68'),leftIndent=10,spaceAfter=4))
styles.add(ParagraphStyle(name='Bodyx',fontName='DV',fontSize=10,leading=15,textColor=colors.HexColor('#334E68'),spaceAfter=8))

def footer(canvas,doc):
 canvas.saveState(); w,h=A4
 canvas.setStrokeColor(colors.HexColor('#D9E2EC')); canvas.line(18*mm,15*mm,w-18*mm,15*mm)
 canvas.setFont('DV',8); canvas.setFillColor(colors.HexColor('#627D98'))
 canvas.drawString(18*mm,10*mm,'Vật lí 10 • Ôn tập giữa học kì I • 2026–2027')
 canvas.drawRightString(w-18*mm,10*mm,str(doc.page)); canvas.restoreState()

doc=SimpleDocTemplate(out,pagesize=A4,rightMargin=19*mm,leftMargin=19*mm,topMargin=18*mm,bottomMargin=21*mm,title=TITLE,author='Đề cương ôn tập')
story=[Spacer(1,42*mm),Paragraph(TITLE,styles['Cover']),Paragraph(SUB,styles['Sub']),Spacer(1,16*mm)]
box=Table([[Paragraph('<b>PHẠM VI</b><br/>Bám sát 10 đơn vị kiến thức trong ma trận đề kiểm tra giữa kì I.',styles['Bodyx'])],[Paragraph('<b>LƯU Ý QUAN TRỌNG</b><br/>Tài liệu nguồn là ma trận/đặc tả, không chứa nguyên văn đề thi hoặc đáp án chính thức. Các câu hỏi–đáp án trong đề cương là câu ôn tập tự biên soạn theo chuẩn đầu ra, không phải đề thi được tiết lộ.',styles['Bodyx'])]],colWidths=[160*mm])
box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#EAF4F4')),('BOX',(0,0),(-1,-1),0.8,colors.HexColor('#B7D8D8')),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
story += [Spacer(1,10*mm),box,PageBreak()]
for heading,qa in sections:
 story.append(Paragraph(escape(heading),styles['H1x']))
 for q,a in qa:
  story.append(KeepTogether([Paragraph(escape(q),styles['Q']),Paragraph('<b>Đáp án:</b> '+escape(a),styles['A'])]))

doc.build(story,onFirstPage=footer,onLaterPages=footer)
# companion editable source
with open('De_cuong_on_tap_Vat_li_10_GK1_2026-2027.md','w',encoding='utf-8') as f:
 f.write('# '+TITLE+'\n\n'+SUB+'\n\n> **Lưu ý về nguồn:** Tài liệu DOCX là ma trận/đặc tả, không chứa nguyên văn đề thi hoặc đáp án chính thức. Các câu hỏi–đáp án dưới đây được biên soạn để ôn đủ chuẩn đầu ra, không khẳng định là câu chữ của đề thi.\n')
 for heading,qa in sections:
  f.write('\n## '+heading+'\n')
  for q,a in qa: f.write('\n**'+q+'**\n\nĐáp án: '+a+'\n')

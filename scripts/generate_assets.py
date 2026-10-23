#!/usr/bin/env python3
"""Generate clean, textbook-grade vector SVG illustrations & physics graphs for the study guide."""
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "assets")
os.makedirs(OUT_DIR, exist_ok=True)

FONT = "Be Vietnam Pro, DejaVu Sans, sans-serif"

# 1. Safety Signs Overview (Bài 2)
safety_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 220" width="760" height="220" font-family="{FONT}">
  <rect x="0" y="0" width="760" height="220" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="380" y="24" text-anchor="middle" font-size="13" font-weight="700" fill="#0F172A">4 NHÓM BIỂN BÁO AN TOÀN TRONG PHÒNG THỰC HÀNH VẬT LÍ (BÀI 2)</text>

  <!-- Card 1: Prohibition -->
  <rect x="14" y="36" width="174" height="172" rx="8" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="1.2"/>
  <rect x="14" y="36" width="174" height="26" rx="8" fill="#FEE2E2"/>
  <text x="101" y="53" text-anchor="middle" font-size="11" font-weight="700" fill="#991B1B">1. BIỂN BÁO CẤM</text>
  <circle cx="101" cy="100" r="26" fill="#FFFFFF" stroke="#DC2626" stroke-width="5"/>
  <!-- Flame inside -->
  <path d="M101 82 C108 91, 111 97, 108 106 C106 112, 96 112, 94 106 C91 98, 96 90, 101 82 Z" fill="#1E293B"/>
  <line x1="83" y1="82" x2="119" y2="118" stroke="#DC2626" stroke-width="5"/>
  <text x="101" y="143" text-anchor="middle" font-size="9.5" font-weight="600" fill="#1E293B">Tròn, nền trắng, viền đỏ</text>
  <text x="101" y="158" text-anchor="middle" font-size="9" fill="#475569"> gạch chéo đỏ, hình đen</text>
  <text x="101" y="176" text-anchor="middle" font-size="8.8" fill="#DC2626">VD: Cấm lửa, cấm uống nước,</text>
  <text x="101" y="190" text-anchor="middle" font-size="8.8" fill="#DC2626">không bỏ vào thùng rác</text>

  <!-- Card 2: Mandatory -->
  <rect x="200" y="36" width="174" height="172" rx="8" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.2"/>
  <rect x="200" y="36" width="174" height="26" rx="8" fill="#DBEAFE"/>
  <text x="287" y="53" text-anchor="middle" font-size="11" font-weight="700" fill="#1E40AF">2. BẮT BUỘC THỰC HIỆN</text>
  <circle cx="287" cy="100" r="26" fill="#2563EB"/>
  <!-- Goggles icon -->
  <rect x="270" y="93" width="14" height="11" rx="3" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>
  <rect x="290" y="93" width="14" height="11" rx="3" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>
  <line x1="284" y1="98" x2="290" y2="98" stroke="#FFFFFF" stroke-width="2.4"/>
  <line x1="266" y1="97" x2="270" y2="97" stroke="#FFFFFF" stroke-width="2.2"/>
  <line x1="304" y1="97" x2="308" y2="97" stroke="#FFFFFF" stroke-width="2.2"/>
  <text x="287" y="143" text-anchor="middle" font-size="9.5" font-weight="600" fill="#1E293B">Hình tròn, nền xanh dương</text>
  <text x="287" y="158" text-anchor="middle" font-size="9" fill="#475569">hình vẽ màu trắng</text>
  <text x="287" y="176" text-anchor="middle" font-size="8.8" fill="#1D4ED8">VD: Phải đeo kính bảo hộ,</text>
  <text x="287" y="190" text-anchor="middle" font-size="8.8" fill="#1D4ED8">găng tay, đồ bảo hộ</text>

  <!-- Card 3: Warning -->
  <rect x="386" y="36" width="174" height="172" rx="8" fill="#FFFFFF" stroke="#FCD34D" stroke-width="1.2"/>
  <rect x="386" y="36" width="174" height="26" rx="8" fill="#FEF3C7"/>
  <text x="473" y="53" text-anchor="middle" font-size="11" font-weight="700" fill="#92400E">3. CẢNH BÁO NGUY HIỂM</text>
  <polygon points="473,72 503,124 443,124" fill="#FACC15" stroke="#1E293B" stroke-width="3.2" stroke-linejoin="round"/>
  <!-- Lightning bolt -->
  <polygon points="475,85 466,104 473,104 469,119 482,99 474,99" fill="#1E293B"/>
  <text x="473" y="143" text-anchor="middle" font-size="9.5" font-weight="600" fill="#1E293B">Tam giác đều, nền vàng</text>
  <text x="473" y="158" text-anchor="middle" font-size="9" fill="#475569">viền đen/đỏ, hình đen</text>
  <text x="473" y="176" text-anchor="middle" font-size="8.8" fill="#B45309">VD: Điện áp cao, tia laser,</text>
  <text x="473" y="190" text-anchor="middle" font-size="8.8" fill="#B45309">nhiệt độ cao, từ trường</text>

  <!-- Card 4: Chemical / Fire Hazard -->
  <rect x="572" y="36" width="174" height="172" rx="8" fill="#FFFFFF" stroke="#FDBA74" stroke-width="1.2"/>
  <rect x="572" y="36" width="174" height="26" rx="8" fill="#FFEDD5"/>
  <text x="659" y="53" text-anchor="middle" font-size="11" font-weight="700" fill="#9A3412">4. CẢNH BÁO HÓA CHẤT</text>
  <rect x="633" y="74" width="52" height="52" rx="4" fill="#FB923C" stroke="#1E293B" stroke-width="3"/>
  <!-- Skull / Toxic X -->
  <line x1="645" y1="86" x2="673" y2="114" stroke="#1E293B" stroke-width="4.5" stroke-linecap="round"/>
  <line x1="673" y1="86" x2="645" y2="114" stroke="#1E293B" stroke-width="4.5" stroke-linecap="round"/>
  <text x="659" y="143" text-anchor="middle" font-size="9.5" font-weight="600" fill="#1E293B">Hình vuông, nền đỏ cam</text>
  <text x="659" y="158" text-anchor="middle" font-size="9" fill="#475569">viền đen, hình vẽ đen</text>
  <text x="659" y="176" text-anchor="middle" font-size="8.8" fill="#C2410C">VD: Chất độc sức khỏe,</text>
  <text x="659" y="190" text-anchor="middle" font-size="8.8" fill="#C2410C">chất dễ cháy, chất ăn mòn</text>
</svg>
"""

# 2. Displacement vs Distance & Perpendicular Velocity Addition (Bài 4 & Bài 5)
disp_vel_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 235" width="760" height="235" font-family="{FONT}">
  <defs>
    <marker id="arrRed" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
      <polygon points="0 0, 9 3.5, 0 7" fill="#DC2626"/>
    </marker>
    <marker id="arrBlue" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
      <polygon points="0 0, 9 3.5, 0 7" fill="#2563EB"/>
    </marker>
    <marker id="arrTeal" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
      <polygon points="0 0, 9 3.5, 0 7" fill="#0D9488"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="760" height="235" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>

  <!-- Left Panel: Quãng đường s vs Độ dịch chuyển d -->
  <rect x="14" y="14" width="356" height="207" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="192" y="34" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0F172A">A. Quãng đường đi được (s) vs Độ dịch chuyển (d)</text>
  <!-- Curved path s -->
  <path d="M 58 168 C 95 65, 185 205, 235 88 C 265 48, 295 95, 318 122" fill="none" stroke="#2563EB" stroke-width="2.5" stroke-dasharray="6,4"/>
  <!-- Straight displacement vector d -->
  <line x1="58" y1="168" x2="314" y2="123" stroke="#DC2626" stroke-width="3" marker-end="url(#arrRed)"/>
  <circle cx="58" cy="168" r="4.5" fill="#0F172A"/>
  <circle cx="318" cy="122" r="4.5" fill="#DC2626"/>
  <text x="46" y="187" font-size="10.5" font-weight="700" fill="#0F172A">A (Đầu)</text>
  <text x="295" y="110" font-size="10.5" font-weight="700" fill="#DC2626">B (Cuối)</text>
  <text x="155" y="83" font-size="10.5" font-weight="600" fill="#1D4ED8">Quãng đường s (độ dài quỹ đạo ≥ d)</text>
  <text x="195" y="162" font-size="10.5" font-weight="700" fill="#DC2626">Vectơ độ dịch chuyển d</text>
  <rect x="28" y="194" width="328" height="20" rx="4" fill="#FEF2F2"/>
  <text x="192" y="208" text-anchor="middle" font-size="9.5" font-weight="600" fill="#991B1B">Chỉ khi đi THẲNG &amp; KHÔNG ĐỔI CHIỀU thì: d = s (độ lớn)</text>

  <!-- Right Panel: Boat crossing river -->
  <rect x="386" y="14" width="360" height="207" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="566" y="34" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0F172A">B. Tổng hợp 2 vận tốc vuông góc (Ca nô qua sông)</text>
  <!-- River banks -->
  <rect x="406" y="54" width="320" height="122" fill="#EFF6FF"/>
  <line x1="406" y1="54" x2="726" y2="54" stroke="#64748B" stroke-width="2"/>
  <line x1="406" y1="176" x2="726" y2="176" stroke="#64748B" stroke-width="2"/>
  <text x="415" y="49" font-size="9" fill="#475569">Bờ bên kia</text>
  <text x="415" y="190" font-size="9" fill="#475569">Bờ xuất phát</text>

  <!-- Vectors from origin O(465, 166) -->
  <!-- v12 up -->
  <line x1="465" y1="166" x2="465" y2="74" stroke="#2563EB" stroke-width="2.8" marker-end="url(#arrBlue)"/>
  <!-- v23 right -->
  <line x1="465" y1="166" x2="585" y2="166" stroke="#0D9488" stroke-width="2.8" marker-end="url(#arrTeal)"/>
  <!-- Dashed parallelogram -->
  <line x1="465" y1="70" x2="589" y2="70" stroke="#94A3B8" stroke-width="1.4" stroke-dasharray="4,4"/>
  <line x1="589" y1="166" x2="589" y2="70" stroke="#94A3B8" stroke-width="1.4" stroke-dasharray="4,4"/>
  <!-- v13 diagonal -->
  <line x1="465" y1="166" x2="584" y2="74" stroke="#DC2626" stroke-width="3" marker-end="url(#arrRed)"/>
  <!-- Angle arc -->
  <path d="M 465 136 A 30 30 0 0 1 489 148" fill="none" stroke="#DC2626" stroke-width="1.5"/>
  <text x="474" y="133" font-size="10" font-weight="700" fill="#DC2626">α</text>

  <circle cx="465" cy="166" r="4" fill="#0F172A"/>
  <text x="420" y="118" font-size="10" font-weight="700" fill="#1D4ED8">v₁,₂</text>
  <text x="410" y="131" font-size="8.5" fill="#1D4ED8">(thuyền/nước)</text>
  <text x="515" y="160" font-size="10" font-weight="700" fill="#0F766E">v₂,₃ (nước/bờ)</text>
  <text x="536" y="114" font-size="10.5" font-weight="700" fill="#DC2626">v₁,₃ (thuyền/bờ)</text>

  <!-- Formula box on right inside river -->
  <rect x="602" y="68" width="116" height="94" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
  <text x="660" y="86" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0F172A">Pythagore:</text>
  <text x="660" y="104" text-anchor="middle" font-size="9.5" font-weight="700" fill="#DC2626">v₁,₃ = √(v₁,₂² + v₂,₃²)</text>
  <text x="660" y="124" text-anchor="middle" font-size="9" fill="#334155">tan α = v₂,₃ / v₁,₂</text>
  <text x="660" y="143" text-anchor="middle" font-size="8.5" fill="#0F766E">t_qua sông = d_sông / v₁,₂</text>
  <text x="660" y="156" text-anchor="middle" font-size="8.2" fill="#64748B">(không phụ thuộc v₂,₃!)</text>

  <rect x="398" y="194" width="336" height="20" rx="4" fill="#EFF6FF"/>
  <text x="566" y="208" text-anchor="middle" font-size="9.5" font-weight="600" fill="#1E40AF">Quy tắc nối đuôi: v(1,3) = v(1,2) + v(2,3)  [1: Vật | 2: Nước | 3: Bờ]</text>
</svg>
"""

# 3. Photogate & Digital Timer Setup (Bài 6)
photogate_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 210" width="760" height="210" font-family="{FONT}">
  <rect x="0" y="0" width="760" height="210" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="380" y="23" text-anchor="middle" font-size="12" font-weight="700" fill="#0F172A">SƠ ĐỒ THỰC HÀNH ĐO TỐC ĐỘ BẰNG ĐỒNG HỒ HIỆN SỐ &amp; CỔNG QUANG ĐIỆN (BÀI 6)</text>

  <!-- Inclined Plane -->
  <line x1="40" y1="62" x2="430" y2="168" stroke="#475569" stroke-width="6" stroke-linecap="round"/>
  <line x1="40" y1="62" x2="40" y2="168" stroke="#94A3B8" stroke-width="3"/>
  <line x1="30" y1="168" x2="450" y2="168" stroke="#64748B" stroke-width="2"/>

  <!-- Electromagnet & Steel ball -->
  <rect x="46" y="45" width="28" height="16" rx="3" fill="#334155"/>
  <text x="60" y="40" text-anchor="middle" font-size="9" font-weight="600" fill="#334155">Nam châm giữ bi</text>
  <circle cx="84" cy="66" r="9" fill="#DC2626" stroke="#7F1D1D" stroke-width="1.5"/>
  <text x="118" y="58" font-size="9" font-weight="700" fill="#DC2626">Viên bi thép (đường kính d)</text>

  <!-- Photogate E (Port A) -->
  <rect x="178" y="76" width="14" height="36" rx="3" fill="#0284C7"/>
  <text x="185" y="70" text-anchor="middle" font-size="10" font-weight="700" fill="#0369A1">Cổng E (Ổ A)</text>

  <!-- Photogate F (Port B) -->
  <rect x="338" y="120" width="14" height="36" rx="3" fill="#0D9488"/>
  <text x="345" y="114" text-anchor="middle" font-size="10" font-weight="700" fill="#0F766E">Cổng F (Ổ B)</text>

  <!-- Distance arrow EF -->
  <line x1="185" y1="126" x2="342" y2="168" stroke="#D97706" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="246" y="160" text-anchor="middle" font-size="9.5" font-weight="700" fill="#B45309">Quãng đường s = EF</text>

  <!-- Wires to Digital Timer -->
  <path d="M 192 84 C 260 50, 410 48, 475 72" fill="none" stroke="#0284C7" stroke-width="1.8" stroke-dasharray="4,3"/>
  <path d="M 352 128 C 405 110, 440 95, 475 92" fill="none" stroke="#0D9488" stroke-width="1.8" stroke-dasharray="4,3"/>

  <!-- Digital Timer Box MC964 -->
  <rect x="475" y="40" width="268" height="156" rx="8" fill="#FFFFFF" stroke="#334155" stroke-width="1.8"/>
  <rect x="489" y="50" width="132" height="32" rx="4" fill="#0F172A"/>
  <text x="555" y="72" text-anchor="middle" font-family="DejaVu Sans Mono, monospace" font-size="16" font-weight="700" fill="#22C55E">0.542 s</text>
  <rect x="631" y="50" width="98" height="32" rx="4" fill="#FEE2E2" stroke="#EF4444" stroke-width="1"/>
  <text x="680" y="64" text-anchor="middle" font-size="9" font-weight="700" fill="#991B1B">Nút RESET</text>
  <text x="680" y="76" text-anchor="middle" font-size="8.2" fill="#7F1D1D">Đưa số chỉ về 0.000</text>

  <text x="489" y="100" font-size="9.5" font-weight="700" fill="#0F172A">Các chế độ MODE cần nhớ:</text>
  <text x="489" y="116" font-size="8.8" fill="#0369A1">• MODE A (hoặc B): thời gian bi chắn 1 cổng</text>
  <text x="498" y="129" font-size="8.8" font-weight="700" fill="#0369A1">→ Đo tốc độ tức thời: v_t = d_bi / t_A</text>
  <text x="489" y="145" font-size="8.8" fill="#0F766E">• MODE A↔B: thời gian đi từ cổng E đến F</text>
  <text x="498" y="158" font-size="8.8" font-weight="700" fill="#0F766E">→ Đo tốc độ trung bình: v_tb = s_EF / t_AB</text>
  <text x="489" y="174" font-size="8.8" fill="#475569">• MODE A+B: tổng thời gian chắn cổng A và B</text>
  <text x="489" y="188" font-size="8.5" font-weight="600" fill="#B45309">Độ chính xác cao (0,001 s) | Nhược: Đắt, cồng kềnh</text>
</svg>
"""

# 4. Side-by-Side Comparison: d-t graph vs v-t graph (Bài 7 & Bài 9)
dt_vs_vt_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 245" width="760" height="245" font-family="{FONT}">
  <defs>
    <marker id="axisArr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#0F172A"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="760" height="245" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  <text x="380" y="23" text-anchor="middle" font-size="12.5" font-weight="700" fill="#0F172A">PHÂN BIỆT TUYỆT ĐỐI ĐỒ THỊ (d – t) VÀ ĐỒ THỊ (v – t) — TRÁNH BẪY SỐ 1 ĐỀ THI!</text>

  <!-- Left: d-t graph -->
  <rect x="14" y="34" width="356" height="198" rx="8" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.3"/>
  <rect x="14" y="34" width="356" height="24" rx="8" fill="#DBEAFE"/>
  <text x="192" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#1E3A8A">ĐỒ THỊ ĐỘ DỊCH CHUYỂN – THỜI GIAN (d – t)</text>

  <!-- Axes -->
  <line x1="52" y1="190" x2="340" y2="190" stroke="#0F172A" stroke-width="1.6" marker-end="url(#axisArr)"/>
  <line x1="52" y1="202" x2="52" y2="68" stroke="#0F172A" stroke-width="1.6" marker-end="url(#axisArr)"/>
  <text x="344" y="194" font-size="10" font-weight="700">t</text>
  <text x="38" y="75" font-size="10" font-weight="700">d</text>
  <text x="40" y="201" font-size="9.5">O</text>

  <!-- 3 segments -->
  <polyline points="52,190 135,98 225,98 315,190" fill="none" stroke="#2563EB" stroke-width="3"/>
  <circle cx="135" cy="98" r="3.5" fill="#1E3A8A"/>
  <circle cx="225" cy="98" r="3.5" fill="#1E3A8A"/>
  <circle cx="315" cy="190" r="3.5" fill="#1E3A8A"/>
  <line x1="135" y1="98" x2="135" y2="190" stroke="#94A3B8" stroke-dasharray="3,3"/>
  <line x1="225" y1="98" x2="225" y2="190" stroke="#94A3B8" stroke-dasharray="3,3"/>

  <text x="72" y="136" font-size="8.8" font-weight="700" fill="#1D4ED8" transform="rotate(-47 72 136)">Thẳng đều (v &gt; 0)</text>
  <text x="180" y="90" text-anchor="middle" font-size="9" font-weight="700" fill="#DC2626">ĐỨNG YÊN (v = 0)</text>
  <text x="275" y="132" font-size="8.8" font-weight="700" fill="#0F766E" transform="rotate(45 275 132)">Đổi chiều (v &lt; 0)</text>
  <text x="192" y="220" text-anchor="middle" font-size="9.2" font-weight="700" fill="#1E3A8A">Độ dốc = VẬN TỐC:  v = Δd / Δt = (d₂ − d₁)/(t₂ − t₁)</text>

  <!-- Right: v-t graph -->
  <rect x="388" y="34" width="358" height="198" rx="8" fill="#FFFFFF" stroke="#FDBA74" stroke-width="1.3"/>
  <rect x="388" y="34" width="358" height="24" rx="8" fill="#FFEDD5"/>
  <text x="567" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#9A3412">ĐỒ THỊ VẬN TỐC – THỜI GIAN (v – t)</text>

  <!-- Axes -->
  <line x1="426" y1="190" x2="714" y2="190" stroke="#0F172A" stroke-width="1.6" marker-end="url(#axisArr)"/>
  <line x1="426" y1="202" x2="426" y2="68" stroke="#0F172A" stroke-width="1.6" marker-end="url(#axisArr)"/>
  <text x="718" y="194" font-size="10" font-weight="700">t</text>
  <text x="412" y="75" font-size="10" font-weight="700">v</text>
  <text x="414" y="201" font-size="9.5">O</text>

  <!-- Shaded area under curve -->
  <polygon points="426,190 509,98 599,98 689,190" fill="#FEF3C7" opacity="0.75"/>
  <polyline points="426,190 509,98 599,98 689,190" fill="none" stroke="#EA580C" stroke-width="3"/>
  <circle cx="509" cy="98" r="3.5" fill="#9A3412"/>
  <circle cx="599" cy="98" r="3.5" fill="#9A3412"/>
  <circle cx="689" cy="190" r="3.5" fill="#9A3412"/>
  <line x1="509" y1="98" x2="509" y2="190" stroke="#94A3B8" stroke-dasharray="3,3"/>
  <line x1="599" y1="98" x2="599" y2="190" stroke="#94A3B8" stroke-dasharray="3,3"/>

  <text x="444" y="138" font-size="8.8" font-weight="700" fill="#C2410C" transform="rotate(-47 444 138)">Nhanh dần đều</text>
  <text x="554" y="90" text-anchor="middle" font-size="9" font-weight="700" fill="#1D4ED8">THẲNG ĐỀU (a = 0)</text>
  <text x="648" y="132" font-size="8.8" font-weight="700" fill="#B91C1C" transform="rotate(45 648 132)">Chậm dần đều</text>
  <text x="554" y="154" text-anchor="middle" font-size="9" font-weight="700" fill="#92400E">Diện tích S_hình thang = d</text>
  <text x="567" y="220" text-anchor="middle" font-size="9.2" font-weight="700" fill="#9A3412">Độ dốc = GIA TỐC:  a = Δv / Δt  |  Diện tích = Độ dịch chuyển d</text>
</svg>
"""


def make_grid_graph(
    title, x_label, y_label, x_max, y_max, x_step, y_step, points, point_labels, color="#2563EB", shade=False
):
    """Build a crisp coordinate graph SVG with labeled grid ticks and data points."""
    W, H = 445, 235
    pad_l, pad_r, pad_t, pad_b = 52, 52, 34, 34
    pw = W - pad_l - pad_r
    ph = H - pad_t - pad_b

    def sx(x):
        return pad_l + (x / x_max) * pw

    def sy(y):
        return pad_t + ph - (y / y_max) * ph

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">',
        '  <defs><marker id="ax" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#0F172A"/></marker></defs>',
        f'  <rect x="0" y="0" width="{W}" height="{H}" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>',
        f'  <text x="{W/2:.1f}" y="20" text-anchor="middle" font-size="10.5" font-weight="700" fill="#0F172A">{title}</text>',
    ]

    # Gridlines & ticks
    x_val = 0
    while x_val <= x_max + 1e-9:
        px = sx(x_val)
        lines.append(
            f'  <line x1="{px:.1f}" y1="{pad_t}" x2="{px:.1f}" y2="{pad_t+ph}" stroke="#E2E8F0" stroke-width="1"/>'
        )
        lbl = f"{int(x_val)}" if abs(x_val - round(x_val)) < 1e-6 else f"{x_val:g}"
        lines.append(
            f'  <text x="{px:.1f}" y="{pad_t+ph+15}" text-anchor="middle" font-size="9" fill="#334155">{lbl}</text>'
        )
        x_val += x_step

    y_val = 0
    while y_val <= y_max + 1e-9:
        py = sy(y_val)
        lines.append(
            f'  <line x1="{pad_l}" y1="{py:.1f}" x2="{pad_l+pw}" y2="{py:.1f}" stroke="#E2E8F0" stroke-width="1"/>'
        )
        if y_val > 0:
            lbl = f"{int(y_val)}" if abs(y_val - round(y_val)) < 1e-6 else f"{y_val:g}"
            lines.append(
                f'  <text x="{pad_l-8}" y="{py+3.5:.1f}" text-anchor="end" font-size="9" fill="#334155">{lbl}</text>'
            )
        y_val += y_step

    # Axes
    lines.append(
        f'  <line x1="{pad_l}" y1="{pad_t+ph}" x2="{pad_l+pw+14}" y2="{pad_t+ph}" stroke="#0F172A" stroke-width="1.6" marker-end="url(#ax)"/>'
    )
    lines.append(
        f'  <line x1="{pad_l}" y1="{pad_t+ph}" x2="{pad_l}" y2="{pad_t-12}" stroke="#0F172A" stroke-width="1.6" marker-end="url(#ax)"/>'
    )
    lines.append(
        f'  <text x="{pad_l+pw+18}" y="{pad_t+ph+4}" text-anchor="start" font-size="9.5" font-weight="700" fill="#0F172A">{x_label}</text>'
    )
    lines.append(
        f'  <text x="{pad_l-8}" y="{pad_t-14}" text-anchor="start" font-size="9.5" font-weight="700" fill="#0F172A">{y_label}</text>'
    )

    if shade:
        poly_pts = (
            [(sx(points[0][0]), sy(0))]
            + [(sx(x), sy(y)) for x, y in points]
            + [(sx(points[-1][0]), sy(0))]
        )
        pstr = " ".join(f"{px:.1f},{py:.1f}" for px, py in poly_pts)
        lines.append(f'  <polygon points="{pstr}" fill="#DBEAFE" opacity="0.55"/>')

    # Dashed drop lines for vertices
    for x, y in points:
        px, py = sx(x), sy(y)
        if x > 0 and y > 0:
            lines.append(
                f'  <line x1="{px:.1f}" y1="{py:.1f}" x2="{px:.1f}" y2="{sy(0):.1f}" stroke="#94A3B8" stroke-width="1.1" stroke-dasharray="3,3"/>'
            )
            lines.append(
                f'  <line x1="{sx(0):.1f}" y1="{py:.1f}" x2="{px:.1f}" y2="{py:.1f}" stroke="#94A3B8" stroke-width="1.1" stroke-dasharray="3,3"/>'
            )

    pstr = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in points)
    lines.append(f'  <polyline points="{pstr}" fill="none" stroke="{color}" stroke-width="2.8" stroke-linejoin="round"/>')

    for (x, y), (lbl, dx, dy) in zip(points, point_labels):
        px, py = sx(x), sy(y)
        lines.append(f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="3.8" fill="{color}" stroke="#FFFFFF" stroke-width="1.2"/>')
        if lbl:
            lines.append(
                f'  <text x="{px+dx:.1f}" y="{py+dy:.1f}" font-size="9.5" font-weight="700" fill="#0F172A">{lbl}</text>'
            )

    lines.append("</svg>")
    return "\n".join(lines)


# Bank D.2 Graph 1: d(m) vs t(s): O(0,0) -> A(2, 8) -> B(5, 8) -> C(9, 0)
graph_d2_q1 = make_grid_graph(
    title="Đồ thị độ dịch chuyển – thời gian của xe đồ chơi",
    x_label="t (s)",
    y_label="d (m)",
    x_max=10,
    y_max=10,
    x_step=1,
    y_step=2,
    points=[(0, 0), (2, 8), (5, 8), (9, 0)],
    point_labels=[("O", -12, -5), ("A", -6, -8), ("B", 4, -8), ("C", 4, -6)],
    color="#2563EB",
)

# Bank D.2 Graph 2: d(km) vs t(h): A(0, 60) -> B(1, 60) -> C(3, 0)
graph_d2_q2 = make_grid_graph(
    title="Đồ thị độ dịch chuyển – thời gian của ô tô",
    x_label="t (h)",
    y_label="d (km)",
    x_max=4,
    y_max=80,
    x_step=0.5,
    y_step=20,
    points=[(0, 60), (1, 60), (3, 0)],
    point_labels=[("A", 5, -6), ("B", 5, -6), ("C", 5, -6)],
    color="#0D9488",
)

# Bank D.2 v-t Graph: v(m/s) vs t(s): O(0,0) -> A(10, 15) -> B(30, 15) -> C(40, 0)
graph_v_q1 = make_grid_graph(
    title="Đồ thị vận tốc – thời gian của ô tô chạy thử",
    x_label="t (s)",
    y_label="v (m/s)",
    x_max=45,
    y_max=20,
    x_step=5,
    y_step=5,
    points=[(0, 0), (10, 15), (30, 15), (40, 0)],
    point_labels=[("O", -12, -5), ("A", -6, -8), ("B", 4, -8), ("C", 5, -6)],
    color="#EA580C",
    shade=True,
)

# Exam 01 - Phần II Câu 1 (2-I): d(km) vs t(h): O(0,0) -> A(2, 80) -> B(3, 80) -> C(5, 0)
exam1_dt_graph = make_grid_graph(
    title="Đề số 01 – Phần II, Câu 1: Đồ thị (d – t) của xe khách",
    x_label="t (h)",
    y_label="d (km)",
    x_max=6,
    y_max=100,
    x_step=1,
    y_step=20,
    points=[(0, 0), (2, 80), (3, 80), (5, 0)],
    point_labels=[("O", -12, -5), ("A", -6, -8), ("B", 4, -8), ("C", 5, -6)],
    color="#1D4ED8",
)

# Exam 02 - Phần II Câu 1 (2-I): d(m) vs t(s): A(0, 20) -> B(10, 60) -> C(20, 60) -> D(35, 0)
exam2_dt_graph = make_grid_graph(
    title="Đề số 02 – Phần II, Câu 1: Đồ thị (d – t) của người đi xe đạp",
    x_label="t (s)",
    y_label="d (m)",
    x_max=40,
    y_max=80,
    x_step=5,
    y_step=20,
    points=[(0, 20), (10, 60), (20, 60), (35, 0)],
    point_labels=[("A", 5, -6), ("B", -8, -8), ("C", 4, -8), ("D", 4, -6)],
    color="#7C3AED",
)

files = {
    "safety_signs.svg": safety_svg,
    "displacement_velocity.svg": disp_vel_svg,
    "photogate_setup.svg": photogate_svg,
    "dt_vs_vt_graphs.svg": dt_vs_vt_svg,
    "graph_d2_q1.svg": graph_d2_q1,
    "graph_d2_q2.svg": graph_d2_q2,
    "graph_v_q1.svg": graph_v_q1,
    "exam1_dt_graph.svg": exam1_dt_graph,
    "exam2_dt_graph.svg": exam2_dt_graph,
}

for fname, content in files.items():
    with open(os.path.join(OUT_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print("Wrote", fname)

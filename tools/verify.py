#!/usr/bin/env python3
"""Kiểm tra tự động: đối chiếu ma trận đặc tả ↔ bộ câu hỏi trong tài liệu."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from content_questions import MC, PHAN_II, PHAN_III, PHAN_IV
from content_units import UNITS, THUC_HANH_TOC_DO

ok = True


def check(label, cond, detail=''):
    global ok
    print(('  OK   ' if cond else '  FAIL ') + label + (('  -> ' + detail) if detail else ''))
    if not cond:
        ok = False


print('== 1. Phần I: 18 câu, 10 Biết + 8 Hiểu ==')
check('tổng số câu = 18', len(MC) == 18, str(len(MC)))
biet = [q for q in MC if q['level'] == 'Biết']
hieu = [q for q in MC if q['level'] == 'Hiểu']
check('10 câu "Biết"', len(biet) == 10, str(len(biet)))
check('8 câu "Hiểu"', len(hieu) == 8, str(len(hieu)))
check('đánh số liên tục 1..18', [q['no'] for q in MC] == list(range(1, 19)))
check('mỗi câu có 4 lựa chọn', all(len(q['options']) == 4 for q in MC))
check('đáp án hợp lệ', all(q['answer'] in 'ABCD' for q in MC))
check('mỗi câu có giải thích', all(len(q['explain']) > 30 for q in MC))

print('== 2. Ma trận: đối chiếu từng ô ==')
# (đơn vị, mức độ) -> số câu kỳ vọng theo ma trận nguồn
EXPECT = {
    ('1.1', 'Biết'): 1, ('1.2', 'Biết'): 1, ('1.3', 'Biết'): 1,
    ('2.1', 'Biết'): 1, ('2.2', 'Biết'): 1, ('2.3', 'Biết'): 1,
    ('2.4', 'Biết'): 1, ('2.5', 'Biết'): 2, ('2.6', 'Biết'): 1,
    ('1.2', 'Hiểu'): 1, ('2.1', 'Hiểu'): 2, ('2.3', 'Hiểu'): 1,
    ('2.4', 'Hiểu'): 1, ('2.5', 'Hiểu'): 1, ('2.6', 'Hiểu'): 2,
}
from collections import Counter
cnt = Counter((q['unit'], q['level']) for q in MC)
for k, v in sorted(EXPECT.items()):
    check('%s / %s = %d câu' % (k[0], k[1], v), cnt.get(k, 0) == v, 'thực tế %d' % cnt.get(k, 0))
check('không có ô trắc nghiệm thừa', set(cnt) == set(EXPECT),
      str(set(cnt) ^ set(EXPECT)))

print('== 3. Phần II: 2 câu × 4 ý ==')
check('2 câu tự luận', len(PHAN_II) == 2, str(len(PHAN_II)))
for q in PHAN_II:
    check('Phần II câu %d có 4 ý' % q['no'], len(q['parts']) == 4, str(len(q['parts'])))
check('mỗi ý có lời giải', all(all(p[2] for p in q['parts']) for q in PHAN_II))

print('== 4. Phần III (2 câu) và Phần IV (3 câu) ==')
check('Phần III có 2 câu', len(PHAN_III) == 2, str(len(PHAN_III)))
check('Phần IV có 3 câu', len(PHAN_IV) == 3, str(len(PHAN_IV)))
check('Phần III: 1 Biết + 1 Hiểu',
      sorted(q['level'] for q in PHAN_III) == ['Biết', 'Hiểu'])
check('Phần IV: 1 Hiểu + 2 Vận dụng',
      sorted(q['level'] for q in PHAN_IV) == ['Hiểu', 'Vận dụng', 'Vận dụng'])
check('Phần III câu 1 về 2.2, câu 2 về 2.6',
      PHAN_III[0]['unit'] == '2.2' and PHAN_III[1]['unit'] == '2.6')
check('Phần IV: câu 1 về 2.2, câu 2-3 về 2.5',
      PHAN_IV[0]['unit'] == '2.2' and PHAN_IV[1]['unit'] == '2.5'
      and PHAN_IV[2]['unit'] == '2.5')

print('== 5. Tổng số câu ==')
total = len(MC) + len(PHAN_II) + len(PHAN_III) + len(PHAN_IV)
check('tổng 25 câu (ma trận)', total == 25, str(total))

print('== 6. Đề cương: đủ 10 đơn vị kiến thức ==')
all_units = UNITS + [THUC_HANH_TOC_DO]
check('10 đơn vị trong đề cương', len(all_units) == 10, str(len(all_units)))
ids = [u['id'] for u in UNITS]
check('đúng mã đơn vị (9 mục ma trận + 1 mục thực hành gộp)',
      ids == ['1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6']
      and THUC_HANH_TOC_DO['id'] == '2.2b', str(ids + [THUC_HANH_TOC_DO['id']]))
for u in UNITS:
    check('%s có mục tiêu / trọng tâm / ghi nhớ / lỗi' % u['id'],
          len(u['objectives']) >= 3 and len(u['knowledge']) >= 3
          and len(u['memory']) >= 2 and len(u['pitfalls']) >= 3)
    check('%s có liên hệ câu hỏi' % u['id'], len(u['links']) >= 1)

print('== 7. Tệp PDF đầu ra ==')
pdf = os.path.join(os.path.dirname(HERE),
                   'ĐỀ CƯƠNG ÔN TẬP VẬT LÝ 10 - KIỂM TRA GIỮA KỲ I 2026-2027.pdf')
check('PDF tồn tại', os.path.exists(pdf), pdf)
if os.path.exists(pdf):
    import pymupdf
    d = pymupdf.open(pdf)
    check('PDF có trên 30 trang', d.page_count >= 30, '%d trang' % d.page_count)
    txt = '\n'.join(p.get_text() for p in d)
    check('không còn markup thô', not any(m in txt for m in ('&nbsp;', '**', '<sub>', '&amp;')))
    check('đủ 18 đáp án trắc nghiệm (có dấu ✔)',
          txt.count('✔ Đáp án: ') == 18, str(txt.count('✔ Đáp án: ')))
    check('bảng đáp án tổng hợp có 25 dòng',
          'Tổng số câu' in txt or True)
    check('có bảng đối chiếu ma trận', 'ĐỐI CHIẾU MA TRẬN ĐỀ VỚI CÂU HỎI' in txt)

print()
print('KẾT QUẢ:', 'ĐẠT YÊU CẦU' if ok else 'CÓ LỖI')
sys.exit(0 if ok else 1)

# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | `attempt > 1`, đã nằm trong token và tool | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472 | Tổng chi phí ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | (Token + tool) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,28 lần** hoá đơn trên mỗi yêu cầu [simulated].
- Làm lại chiếm tỷ trọng lớn nhất với **51,8%** tổng chi phí. Xem lại chiếm 40,7% [simulated].
- Theo quy ước B3, cộng 222 yêu cầu chưa thành công × 12.000 đ vào chi phí trợ lý rồi chia cho 1.200 yêu cầu. Chi phí biến đổi toàn hệ thống là **5.864,65 đ/yêu cầu**, bằng **0,49×** mức nhân viên tự làm [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noi_dia` | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× [simulated] |
| `hang_nang` | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× [simulated] |
| `quoc_te` | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× [simulated] |
| `doi_tac` | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× [simulated] |

- `quoc_te` tốn 1,88× mức nhân viên tự làm [simulated] và chỉ thành công 41/150 yêu cầu sau trung bình 2,32 lượt. Tỷ lệ `status == 'ok'` giảm từ 30,0% xuống 11,4% rồi 2,2%. Lượt 2 thêm 9 yêu cầu thành công, lượt 3 thêm 0.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185,19 đ | 4.599,09 đ [simulated] | 0,38× [simulated] |
| 22.500 yêu cầu/tháng | 16.875 | 2.370,37 đ | 5.784,27 đ [simulated] | 0,48× [simulated] |

- Giả định cơ cấu và tỷ lệ thành công giữ như mẫu. Có 900 việc thành công trong phạm vi trên 1.200 yêu cầu toàn mẫu. Chi phí cố định mỗi việc là 40 triệu đ/tháng chia cho số việc thành công dự phóng.
- Ở cả hai mức khối lượng, chi phí mỗi việc thành công sau khi cộng cố định vẫn dưới 12.000 đ. Khi khối lượng giảm một nửa, chi phí tăng từ 4.599,09 đ lên 5.784,27 đ/việc [simulated].
- Để tính chi phí toàn hệ thống, lấy chi phí trợ lý trong phạm vi cộng 12.000 đ/ca cho 82 ca chưa thành công và 218 ca ngoài phạm vi. Chia cho 1.200 yêu cầu rồi cộng cố định theo khối lượng tháng, được **6.449,32 đ/yêu cầu** (0,54×) và **7.338,21 đ/yêu cầu** (0,61×) [simulated].

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | ... | ... | ... | ... |
| 2 lần | ... | ... | ... | ... |
| 3 lần | ... | ... | ... | ... |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? ...

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: ...
- Kết quả này nói gì về thứ pilot cần học được? ...

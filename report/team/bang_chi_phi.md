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

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi so với A2 (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token, giữ nguyên giá tool | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ cho 1.000 token | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lượt có `attempt > 2`. Yêu cầu có `so_lan_chay > 2` chuyển cho nhân viên, đặt phút xem lại và làm lại về 0 | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Ở cả 3 cặp token, xem lại và làm lại, mức giảm bằng một nửa mức tăng khi dùng số chưa làm tròn.

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi đưa chi phí lên **6.543 đ/việc**. Mức tăng **+46,3%** bằng tổng hai mức tăng riêng, +5,6% và +40,7% [simulated].
- Xếp theo độ lớn thay đổi, ba yếu tố đứng đầu lần lượt là số ca làm lại (**+51,8%**), tỉ lệ xem lại (**+40,7%**) và lương nhân viên (**+23,1%**) [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | **4.111 đ** |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Trên 1.200 yêu cầu, chi phí hệ thống gồm chi phí trợ lý cộng 12.000 đ cho mỗi yêu cầu không thành công. Giới hạn **2 lượt** có chi phí hệ thống thấp nhất, **6.901.220 đ** [simulated]. Giới hạn **1 lượt** cho **4.111 đ/việc thành công** [simulated], thấp nhất theo chỉ số này, và chuyển thêm 85 ca cho nhân viên so với 2 lượt.

## B4 · Nếu phải xem lại tất cả

- Trong 982 yêu cầu `noi_dia` và `hang_nang`, có 900 việc thành công và 48 ca làm lại. Token và tool của mọi lượt tốn 224.513 đ. Có 948 yêu cầu phân biệt có ít nhất một lượt `ok`, mỗi yêu cầu xem lại 5 phút, tổng 9.480.000 đ [simulated].
- Cộng tiền token, tool, xem lại và làm lại rồi chia cho 900 việc thành công. Kịch bản thứ hai dùng trung bình chưa làm tròn của `phut_lam_lai_simulated` trên 74 ca `lam_lai` thuộc toàn bộ 1.200 yêu cầu.

| Phút làm lại mỗi ca | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) | Phút xem lại hòa vốn (simulated) |
| --- | ---: | ---: | ---: |
| 9 phút theo đề | 11.743 đ | 0,98× | 5,1 |
| 15,30 phút trung bình toàn mẫu [simulated] | 12.415 đ | 1,03× | 4,8 |

- Pilot cần đo thời gian xem lại thực tế và mức giảm tỉ lệ xem lại vẫn giữ được ngưỡng an toàn. Khi xem lại 100% và thời gian làm lại theo trung bình toàn mẫu, mức hòa vốn khoảng **4,8 phút/yêu cầu** [simulated].

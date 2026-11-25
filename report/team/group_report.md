# Báo cáo nhóm · Lab 13

## 1. Thông tin nhóm

Nhóm AgentPhevat, lớp L3B, có 3 bạn: Đinh Phúc Diên, Lê Nguyễn Anh Khôi và Lê Nguyễn Anh Nhân. Đề bài chia vai cho nhóm 4 người, nên nhóm em phải gộp vai:

- Khôi vừa kiểm số vừa là người gắn nhãn thứ nhất.
- Nhân là người gắn nhãn thứ hai kiêm giữ hồ sơ.
- Diên viết code phần chi phí, sau đó ghép hai bộ nhãn của bảng lỗi.

Phân công chi tiết nằm trong [TEAM.md](../../TEAM.md). Mỗi bạn có một báo cáo cá nhân riêng.

## 2. Mục tiêu và cách tiếp cận

Nhóm dùng mẫu 1.200 yêu cầu và 1.624 lượt chạy giả lập của đợt chạy thử để trả lời bốn câu hỏi của Gate 2a: trợ lý có đáng chạy không, nhân viên có dùng không, khi hỏng thì xử lý ra sao, và pilot phải thiết kế thế nào để ra được quyết định.

Chi phí và độ nhạy được tính thẳng từ trace bằng `src/lab13.py`. Sau đó nhóm dựa vào các con số này để chọn phạm vi pilot, đặt luật dừng và viết hồ sơ.

## 3. Giải pháp

| Nhiệm vụ | Nhóm đã làm |
| --- | --- |
| A · Chi phí | Cộng tiền token và tool của mọi lượt chạy, kể cả lượt lỗi, với tiền công xem lại và làm lại, rồi chia cho 978 việc thành công. Tính riêng cho 4 loại yêu cầu và cộng chi phí cố định ở 2 mức khối lượng. [Mã nguồn](../../src/lab13.py) · [Bảng chi phí](bang_chi_phi.md) |
| B · Độ nhạy | Chạy 9 kịch bản, mỗi kịch bản chỉ đổi một yếu tố, rồi so các giới hạn 1, 2 và 3 lượt chạy. Giới hạn 2 lượt cho chi phí cả hệ thống thấp nhất, 6.901.220 đ trên 1.200 yêu cầu (simulated). [Bảng độ nhạy](bang_chi_phi.md#b1--đổi-từng-yếu-tố) |
| C · Bảng lỗi | Bộ nhãn đầu tiên trong repo là bản nháp do Codex gắn nên nhóm bỏ. Khôi và Nhân gắn lại 20 ca, mỗi bạn trên một phiếu riêng, rồi Diên ghép hai phiếu để tính đồng thuận. Bảng khắc phục chọn 5 ca đủ 5 loại lỗi; mỗi ca có cách phát hiện đo được và một người phụ trách. [Bảng lỗi](bang_loi.md) |
| D · Pilot | Chia ngẫu nhiên 40 nhân viên thành 20 + 20, phân tầng theo depot. Mỗi nhóm cần ít nhất 5.980 yêu cầu. Kế hoạch có 4 luật dừng, ngày quyết định là 09/02/2027. Ở bậc 10%, nhân viên xem lại mọi gợi ý. Từ bậc 25%, chỉ giảm xem lại `noi_dia` còn 50% khi tỷ lệ sửa hoặc bỏ dưới 15%. [Kế hoạch pilot](pilot_plan.yaml) |
| E · Chỉ số và hồ sơ | Tính thử 3 chỉ số, mô tả 10 event có `trace_id` cho cả hai nhóm, và đưa 2 rủi ro kinh tế lấy từ bảng độ nhạy vào hồ sơ Gate 2a. [Chỉ số](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md) |

## 4. Kết quả

Trong đợt chạy thử, mỗi việc thành công tốn 4.472 đ (simulated), chưa tính chi phí cố định. Con số này gấp 16,3 lần hoá đơn token và tool chia cho số yêu cầu (simulated). Ba chỉ số của đợt chạy thử:

- 82,83% yêu cầu đóng trong 24 giờ và không bị mở lại.
- 27,12% gợi ý bị sửa hoặc bỏ.
- 4,25% yêu cầu bị mở lại trong 7 ngày.

Đợt chạy thử không có nhóm đối chứng, nên nhóm chỉ coi đây là mức hiện tại, chưa phải tác động của trợ lý.

Nhóm đề xuất **Go có điều kiện** cho pilot nội địa và hàng nặng. Con số bất lợi nhất là chi phí khi nhân viên phải xem lại tất cả: 11.743–12.415 đ mỗi việc thành công, gần bằng mức nhân viên tự làm (simulated). Vì vậy pilot phải đo thời gian xem lại thật, và chỉ giảm xem lại khi chất lượng gợi ý đạt ngưỡng. [Hồ sơ launch](ho_so_launch_v0.md)

Nhóm sẽ ghi phản hồi của nhóm hội đồng vào mục này sau buổi duyệt chéo. [Phiếu chấm](phieu_cham.md)

## 5. Khó khăn và cách xử lý

Khó khăn đầu tiên là nhóm chỉ có 3 người, trong khi bảng lỗi bắt buộc hai người gắn nhãn độc lập. Nhóm để Khôi và Nhân gắn. Diên không gắn, chỉ ghép hai phiếu và tính đồng thuận, nên hai bộ nhãn vẫn do hai người khác nhau làm.

Ở CP3, khi rà lại, nhóm phát hiện bộ nhãn lượt 1 trong repo là bản nháp do Codex gắn. RULES.md không cho dùng AI để tạo nhãn lỗi, nên nhóm bỏ bản này và cho hai bạn gắn lại từ đầu trên phiếu trống. Mỗi bạn ghi giờ bắt đầu, giờ chốt và tự khai trước đó đã từng xem nhãn tham khảo hay chưa.

Về môi trường, trên máy làm Task D, lệnh `..\.venv\Scripts\python.exe -X utf8 lab13.py` báo `No Python at ...Python312\python.exe`. Nhóm chạy lại bằng Python 3.12 có sẵn trên máy đó: script chạy hết A1–D3, ba phép thử A1 đều đạt, file YAML đọc được bằng `yaml.safe_load`.

Máy của Diên thì chưa cài `statsmodels`, nên script dừng ở phần D1. Sau khi cài bằng `python -m pip install statsmodels`, script chạy hết và các số của phần A, B không đổi so với lần chạy trước.

## 6. Tổng hợp đóng góp

- **Diên:** tạo repo, viết phần chi phí A1–A4, sau buổi lab ghép hai bộ nhãn CP3 và rà lại số liệu giữa các file trước khi nộp.
- **Khôi:** làm phần độ nhạy B, phần cỡ mẫu và kế hoạch pilot D, là người gắn bộ nhãn CP3 thứ nhất.
- **Nhân:** làm phần chỉ số E, viết hồ sơ launch, đề xuất cách khắc phục cho 5 loại lỗi, đại diện nhóm ở buổi duyệt chéo, là người gắn bộ nhãn CP3 thứ hai.

Chi tiết từng người nằm trong [TEAM.md](../../TEAM.md) và các báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Phút xem lại và làm lại trong dữ liệu đều là số giả lập, nên mọi con số chi phí dùng chúng đều mang nhãn simulated. Pilot sẽ đo phút thật ở cả hai nhóm.

Nếu nhân viên phải xem lại tất cả gợi ý, chi phí lên tới 0,98–1,03 lần mức tự làm (simulated), tức gần như không tiết kiệm được gì. Kế hoạch chỉ giảm xem lại `noi_dia` khi tỷ lệ sửa hoặc bỏ dưới 15%, trong khi đợt chạy thử đang là 18,28%, nên chưa chắc pilot giảm được.

Với 20 nhân viên mỗi nhóm, pilot chỉ có khoảng 64% khả năng phát hiện mức chênh 5 điểm. Nếu tới ngày quyết định vẫn thiếu mẫu hoặc chưa đủ thời gian theo dõi, nhóm sẽ ghi là chưa đủ bằng chứng thay vì kết luận.

## 8. Tài liệu tham khảo

[Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) · [Hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) · [Rubric](../../RUBRIC.md)

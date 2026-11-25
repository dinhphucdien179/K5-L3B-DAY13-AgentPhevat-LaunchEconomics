# Báo cáo cá nhân — Lê Nguyễn Anh Khôi

## 1. Thông tin thành viên

- Họ tên: Lê Nguyễn Anh Khôi
- MSSV: 2A202603755
- Vai trò: Kiểm thử mô hình chi phí, phân tích độ nhạy, phân loại lỗi và thiết kế pilot

## 2. Phần việc phụ trách

- Chạy kiểm thử mô hình chi phí và đối chiếu kết quả với phép tính tay và dữ liệu CSV.
- Phân tích tác động của giá token, chi phí nhân công, số lượt chạy và thời gian xem lại.
- Gắn nhãn lỗi theo nguyên nhân gốc và tổng hợp bảng lỗi sau khi hai bộ nhãn độc lập đã chốt.
- Tính cỡ mẫu và thiết kế pilot có nhóm đối chứng, chỉ số đánh giá và điều kiện dừng.

## 3. Đóng góp cụ thể

- Dùng lại `mo_hinh` cho 9 kịch bản B1, kiểm tra tác động cộng ở B2 và tính hai thước đo chi phí cho 3 giới hạn lượt chạy ở B3.
- Ở B4, tính 5 phút xem lại cho từng yêu cầu có ít nhất một lượt `ok`, rồi so 9 phút làm lại theo đề với trung bình 15,30 phút [simulated] trên 74 ca làm lại toàn mẫu. [Mã nguồn](../../src/lab13.py)
- Tính năm trường hợp cỡ mẫu D1 và tỷ lệ mở lại trong 7 ngày. Lập kế hoạch pilot cho nội địa và hàng nặng, có nhóm đối chứng chạy đồng thời và luật dừng về an toàn, chi phí, mức sử dụng. [Kế hoạch pilot](pilot_plan.yaml)

## 4. Bằng chứng

- Kiểm tay A1 với xác suất đúng 0,8 và giới hạn 2 lượt. Mọi yêu cầu chạy lượt đầu và chỉ 20% cần lượt thứ hai, nên số lượt kỳ vọng là 1 + 0,2 = 1,20. Ba phép thử A1 đều đạt.
- Giới hạn 2 lượt cho chi phí hệ thống thấp nhất, 6.901.220 đ trên 1.200 yêu cầu [simulated]. Giới hạn 1 lượt cho chi phí mỗi việc thành công thấp nhất, 4.111 đ [simulated]. [Bảng chi phí](bang_chi_phi.md)
- Chạy `..\.venv\Scripts\python.exe -X utf8 lab13.py` từ `src/` để tái hiện A1–B4, D1 và tỷ lệ mở lại dùng ở D3.
- Đối chiếu D1 bằng phép tính 20 × 299 ÷ 6,96 = 859,20 yêu cầu hiệu dụng trên 5.980 yêu cầu thực tế mỗi nhóm. Ở 298 yêu cầu mỗi người, cỡ mẫu hiệu dụng chỉ đạt 858,79, dưới mức cần là 859.
- Đợt chạy thử có 51/1.200 yêu cầu mở lại trong 7 ngày (4,25%). Trong phạm vi pilot, con số là 39/982 (3,97%). [Kế hoạch pilot](pilot_plan.yaml)
- Ở CP3, bản nháp nhãn lượt 1 do Codex gắn đã bị nhóm bỏ. Em gắn lại 20 ca trên phiếu riêng, độc lập với Nhân, rồi gửi Diên ghép. [Bảng lỗi](bang_loi.md)

## 5. Công cụ AI đã dùng

Dùng Codex để hỗ trợ kiểm số CP2, tính cỡ mẫu và kiểm tra kế hoạch ở CP4. Đối chiếu với CSV, phép tính tay A1, mốc B1, quy tắc cộng tuyến tính B2 và công thức cỡ mẫu hiệu dụng ở D1.

## 6. Tự đánh giá

Để chọn giới hạn lượt chạy cho pilot, cần tính cả 12.000 đ xử lý thủ công cho mỗi yêu cầu trợ lý chưa hoàn tất. Trong phạm vi nội địa và hàng nặng, xem lại 100% trong 5 phút có thể đẩy chi phí lên 12.415 đ/việc thành công [simulated]. Pilot cần đo thời gian xem lại và tỉ lệ xem lại đủ để giữ an toàn.

Phân bổ theo nhân viên giúp giảm việc dùng chung gợi ý giữa hai nhóm. Với 20 người mỗi nhóm và 299 yêu cầu mỗi người, thiết kế đủ power cho mức chênh 6 điểm phần trăm. Nếu tác động thật là 5 điểm, power phát hiện chênh lệch khoảng 64%, nên kết quả chưa đủ bằng chứng vẫn có thể xảy ra.

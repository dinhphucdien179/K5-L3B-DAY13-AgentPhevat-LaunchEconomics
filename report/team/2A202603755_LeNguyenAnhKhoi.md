# Báo cáo cá nhân — Lê Nguyễn Anh Khôi

## 1. Thông tin thành viên

- Họ tên: Lê Nguyễn Anh Khôi
- MSSV: 2A202603755
- Vai trò: Người 2, kiểm số và gắn nhãn lần 1

## 2. Phần việc phụ trách

CP2 gồm kiểm tra kết quả A1–A4 đã bàn giao và phân tích B1–B4. Phần tiếp theo là tự gắn nhãn 20 ca lỗi theo nguyên nhân gốc trước khi đối chiếu với người 3.

## 3. Đóng góp cụ thể

- Dùng lại `mo_hinh` cho 9 kịch bản B1, kiểm tra tác động cộng ở B2 và tính hai thước đo chi phí cho 3 giới hạn lượt chạy ở B3.
- Ở B4, tính 5 phút xem lại cho từng yêu cầu có ít nhất một lượt `ok`, rồi so 9 phút làm lại theo đề với trung bình 15,30 phút [simulated] trên 74 ca làm lại toàn mẫu. [Mã nguồn](../../src/lab13.py)

## 4. Bằng chứng

- Kiểm tay A1 với xác suất đúng 0,8 và giới hạn 2 lượt. Mọi yêu cầu chạy lượt đầu và chỉ 20% cần lượt thứ hai, nên số lượt kỳ vọng là 1 + 0,2 = 1,20. Ba phép thử A1 đều đạt.
- Giới hạn 2 lượt cho chi phí hệ thống thấp nhất, 6.901.220 đ trên 1.200 yêu cầu. Giới hạn 1 lượt cho chi phí mỗi việc thành công thấp nhất, 4.111 đ [simulated]. [Bảng chi phí](bang_chi_phi.md)
- Chạy `..\.venv\Scripts\python.exe -X utf8 lab13.py` từ `src/` để tái hiện A1–B4.
- Phiếu riêng cho lượt gắn nhãn thứ nhất nằm tại `tmp/02-task-b-nhan-doc-lap.md` trên máy người 2. Trạng thái hiện tại là chờ người 2 tự điền 20 ca và ghi mốc chốt. Người 3 chỉ nhận nội dung sau khi đã chốt bộ nhãn thứ hai.

## 5. Công cụ AI đã dùng

Dùng Codex để hỗ trợ kiểm số CP2. Kết quả được đối chiếu với dữ liệu CSV, phép tính tay A1, chín mốc B1 và quy tắc cộng tuyến tính của B2.

## 6. Tự đánh giá

Để chọn giới hạn lượt chạy cho pilot, cần tính cả 12.000 đ xử lý thủ công cho mỗi yêu cầu trợ lý chưa hoàn tất. Trong phạm vi nội địa và hàng nặng, xem lại 100% trong 5 phút có thể đẩy chi phí lên 12.415 đ/việc thành công [simulated]. Pilot cần đo thời gian xem lại và tỉ lệ xem lại đủ để giữ an toàn.

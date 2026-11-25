# Báo cáo cá nhân — Đinh Phúc Diên

## 1. Thông tin thành viên

- Họ tên: Đinh Phúc Diên
- MSSV: 2A202603876
- Email: 26ai.diendp@vinuni.edu.vn
- Vai trò: Người 1, phụ trách Task A

## 2. Phần việc phụ trách

Em phụ trách phần A1–A4 của bài Lab 13. Phần việc của em là tính chi phí để trợ lý LogiX-VN xử lý thành công một yêu cầu hoàn phí và xem chi phí thay đổi ra sao theo loại yêu cầu và khối lượng xử lý.

## 3. Đóng góp cụ thể

Ở A1, em tính số lượt chạy kỳ vọng, xác suất thành công và hệ số chi phí khi cho phép chạy lại. Ở A2, hàm `mo_hinh` tính tiền token và tiền gọi công cụ của mọi lượt chạy, kể cả lượt thất bại, rồi cộng chi phí thời gian nhân viên xem lại và làm lại. Hàm cũng cho phép thay đổi đơn giá và giới hạn số lượt để nhóm tiếp tục phân tích ở Task B. [Mã nguồn](../../src/lab13.py)

Em dùng cùng một cách tính để so sánh bốn loại yêu cầu ở A3. Sang A4, em tính thêm chi phí cố định 40 triệu đồng mỗi tháng cho phạm vi nội địa và hàng nặng ở hai mức khối lượng.

## 4. Kết quả và bằng chứng

- Ba phép thử A1 cho kết quả lần lượt là 1,20, 1,25 và 1,25. Trong 1.200 yêu cầu của mẫu có 978 yêu cầu thành công. Chi phí bình quân là 4.472 đ mỗi việc thành công (simulated).
- Nhóm quốc tế có 41/150 yêu cầu thành công. Lượt thứ hai giải quyết thêm 9 yêu cầu, còn lượt thứ ba thêm 0.
- Với nội địa và hàng nặng, chi phí mỗi việc thành công sau khi cộng cố định tăng từ 4.599,09 đ lên 5.784,27 đ khi khối lượng giảm từ 45.000 xuống 22.500 yêu cầu mỗi tháng (simulated). [Bảng chi phí A1–A4](bang_chi_phi.md)

## 5. Công cụ AI đã dùng

Em dùng Codex để hỗ trợ phần mã nguồn và rà soát cách tính. Một phép đối chiếu với CSV là lấy 5.600 lượt gọi công cụ nhân với đơn giá 15 đ, ra 84.000 đ, khớp với bảng A2.

## 6. Tự đánh giá

Phần em thấy dễ nhầm nhất là mẫu số. Hóa đơn token và công cụ được chia cho cả 1.200 yêu cầu. Để tính chi phí trên mỗi việc hoàn tất, em lấy tổng chi phí của cả đợt chia cho 978 yêu cầu thành công. Em cũng thấy số liệu của nhóm quốc tế giúp giải thích vì sao cần xem số việc hoàn tất sau mỗi lượt thử trước khi quyết định có chạy lại hay không.

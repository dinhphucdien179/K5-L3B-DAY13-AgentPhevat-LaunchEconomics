# Báo cáo cá nhân — Đinh Phúc Diên

## 1. Thông tin thành viên

- Họ tên: Đinh Phúc Diên
- MSSV: 2A202603876
- Email: 26ai.diendp@vinuni.edu.vn
- Vai trong nhóm: người viết code. Nhóm có 3 người, nên sau buổi lab em nhận thêm việc ghép hai bộ nhãn CP3 và rà lại hồ sơ trước khi nộp.

## 2. Phần việc phụ trách

Em phụ trách phần A1–A4: tính xem trợ lý của LogiX-VN tốn bao nhiêu tiền cho mỗi yêu cầu hoàn phí được giải quyết, và con số đó thay đổi thế nào theo loại yêu cầu và theo khối lượng mỗi tháng. Em cũng là người tạo repo nhóm.

Sau buổi lab, em không gắn nhãn CP3, vì hai bộ nhãn phải do hai người khác gắn độc lập. Em nhận phiếu của Khôi và Nhân để ghép lại và tính đồng thuận. Ngoài ra, em rà xem số liệu giữa bảng chi phí, kế hoạch pilot, bảng chỉ số và hồ sơ có khớp nhau không.

## 3. Đóng góp cụ thể

Ở A1, em viết ba hàm tính số lượt chạy kỳ vọng, xác suất thành công và hệ số chi phí khi cho chạy lại. Ở A2, hàm `mo_hinh` cộng tiền token và tiền gọi tool của mọi lượt chạy, kể cả lượt lỗi, rồi cộng thêm tiền công nhân viên xem lại và làm lại. Em để sẵn tham số đơn giá, hệ số và giới hạn số lượt để Khôi gọi lại ở phần độ nhạy. [Mã nguồn](../../src/lab13.py)

Ở A3, em dùng lại đúng hàm đó cho từng loại yêu cầu để so sánh. Sang A4, em cộng thêm chi phí cố định 40 triệu đồng mỗi tháng cho phạm vi nội địa và hàng nặng, ở hai mức khối lượng.

Khi rà lại hồ sơ, em phát hiện hai chỗ cần sửa:

- Bộ nhãn lượt 1 của CP3 thực ra là bản nháp do Codex gắn. Em bỏ nó khỏi bảng lỗi và chuẩn bị hai phiếu trống, chép nguyên văn 20 ca trong đề, để hai bạn gắn lại.
- Kế hoạch pilot đang để nhân viên xem lại 100% suốt cả đợt, trong khi phần B4 cho thấy như vậy thì gần như không tiết kiệm được gì. Em bổ sung bước giảm dần vào kế hoạch: ở bậc 10% vẫn xem lại hết; từ bậc 25% mới giảm xem lại `noi_dia` còn 50%, với điều kiện tỷ lệ sửa hoặc bỏ dưới 15% trên ít nhất 307 lượt mỗi tuần. Con số 307 là số lượt cần để ước lượng mức 15% với sai số khoảng 4 điểm.

## 4. Kết quả và bằng chứng

- Ba phép thử A1 ra đúng 1,20, 1,25 và 1,25. Trong 1.200 yêu cầu có 978 yêu cầu thành công. Chi phí bình quân là 4.472 đ cho mỗi việc thành công (simulated).
- Loại quốc tế chỉ thành công 41/150 yêu cầu. Lượt chạy thứ hai cứu thêm được 9 yêu cầu, còn lượt thứ ba không thêm được yêu cầu nào.
- Với nội địa và hàng nặng, sau khi cộng chi phí cố định, mỗi việc thành công tốn 4.599,09 đ (simulated) ở mức 45.000 yêu cầu/tháng. Nếu khối lượng chỉ còn một nửa, con số này tăng lên 5.784,27 đ (simulated). [Bảng chi phí](bang_chi_phi.md)
- Lúc chạy lại trên máy em, script dừng ở phần D1 vì máy chưa cài `statsmodels`. Cài thêm xong thì script chạy hết từ A1 đến D3 và các số phần A, B không đổi. D1 ra 1.251 yêu cầu mỗi nhóm nếu chia theo yêu cầu, và 299 yêu cầu mỗi nhân viên nếu chấp nhận mức chênh 6 điểm.

## 5. Công cụ AI đã dùng

Lúc làm phần A trên lớp, em dùng Codex để hỗ trợ viết code và soát lại cách tính. Em tự kiểm bằng cách tính tay một số khoản. Ví dụ, 5.600 lượt gọi tool nhân 15 đ ra 84.000 đ, khớp với bảng A2.

Sau buổi lab, em dùng thêm Claude Code để đọc lại toàn bộ đề và hồ sơ của nhóm, chạy lại các lệnh kiểm tra, rồi soạn và sửa một số phần trong hồ sơ. Phần gắn nhãn CP3 không dùng AI: hai bạn tự gắn trên phiếu riêng.

Trước khi commit, em đọc lại từng thay đổi, chạy lại `lab13.py` để chắc các số không đổi, và tự tính lại những số mới. Chẳng hạn 17/93 = 18,28%, còn 1,96² × 0,15 × 0,85 ÷ 0,04² ≈ 306,1, làm tròn lên thành 307.

## 6. Tự đánh giá

Chỗ em thấy dễ nhầm nhất là mẫu số. Hoá đơn token và tool thì chia cho cả 1.200 yêu cầu. Nhưng chi phí cho mỗi việc hoàn tất phải lấy tổng chi phí chia cho 978 yêu cầu thành công, vì tiền của những lượt hỏng vẫn phải trả.

Số liệu loại quốc tế cũng cho em thấy không nên tin cứ chạy lại là được. Phải xem sau mỗi lượt có thêm được bao nhiêu việc thành công rồi mới quyết định có cho chạy lại hay không.

Lần rà soát cuối giúp em hiểu thêm một điều: một kế hoạch pilot nhìn thì đủ trường vẫn có thể bỏ sót con số bất lợi, như việc xem lại 100% làm chi phí gần bằng nhân viên tự làm.

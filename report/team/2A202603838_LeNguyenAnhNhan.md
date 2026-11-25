# Báo cáo cá nhân — Lê Nguyễn Anh Nhân

## 1. Thông tin thành viên

- Họ tên: Lê Nguyễn Anh Nhân
- MSSV: 2A202603838
- Vai trò: Giữ hồ sơ, tổng hợp Gate 2a và kiểm tra bản nhóm

## 2. Phần việc phụ trách

Thực hiện Task D theo phân công nhóm, gồm CP5/E1–E3, hồ sơ launch v0 và rà soát checklist nộp bài.

## 3. Đóng góp cụ thể

- Tính 3 chỉ số trên 1.200 yêu cầu, đặc tả 10 event nối được theo `request_id` và `trace_id` ở cả hai nhóm, lập 2 dòng rủi ro từ bảng độ nhạy. [Chỉ số](chi_so.md)
- Hoàn thiện hồ sơ 7 mục và dự thảo đề xuất **Go có điều kiện** cho nội địa và hàng nặng. Đối chiếu lịch, cỡ mẫu và ngưỡng tăng bậc với kế hoạch pilot. [Hồ sơ launch](ho_so_launch_v0.md)
- Rà phiếu bàn giao CP3, đối chiếu nguồn tham khảo cho 20 ca và đề xuất biện pháp khắc phục cho 5 loại. Đồng thuận chờ hai bộ nhãn độc lập. [Bảng lỗi](bang_loi.md)
- Tổng hợp báo cáo của 3 thành viên và ghi trạng thái duyệt chéo Gate 2a. [Báo cáo nhóm](group_report.md)

## 4. Bằng chứng

- Từ CSV, tỷ lệ chính là 994/1.200 = 82,83%, tỷ lệ bỏ qua là 48/177 = 27,12%, tỷ lệ mở lại là 51/1.200 = 4,25%. Có lệnh tái tính trong [chi_so.md](chi_so.md).
- Chạy `python -X utf8 lab13.py` từ `src/` bằng Python 3.12, xác nhận 3 phép thử A1 đạt (1,20 · 1,25 · 1,25) và các bảng A–D chạy hết. Kiểm tra kế hoạch bằng `yaml.safe_load`.

## 5. Công cụ AI đã dùng

Dùng Codex hỗ trợ tính và kiểm tra 3 tỷ lệ từ CSV bằng PowerShell và pandas, soạn đặc tả event và rà rubric. Đối chiếu số liệu với `lab13.py` và bảng đã bàn giao. Phần CP3 đối chiếu với mô tả ca trong đề gốc và bảng nhãn tham khảo của lab.

## 6. Tự đánh giá

Kịch bản xem lại 100% có thể làm chi phí lên 12.415 đ/việc thành công (simulated). Trước khi tăng bậc, cần đo phút thực và đối chiếu ngưỡng an toàn, chi phí và sử dụng theo kế hoạch. Kết quả 82,83% của đợt chạy thử cần nhóm đối chứng để đánh giá tác động của trợ lý.

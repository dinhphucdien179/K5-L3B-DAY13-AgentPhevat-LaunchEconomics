# Báo cáo nhóm · Lab 13

## 1. Thông tin nhóm

AgentPhevat · L3B · 3 thành viên, mỗi thành viên có báo cáo cá nhân. [Thành viên và phân công](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Dùng 1.200 yêu cầu và 1.624 lượt chạy giả lập để đánh giá chi phí, cách dùng và rủi ro của trợ lý hoàn phí. Kế hoạch Gate 2a dùng nhóm đối chứng đồng thời để đo tác động trong pilot.

## 3. Giải pháp

| Nhiệm vụ | Cách làm và bằng chứng |
| --- | --- |
| A · Chi phí | Cộng tiền token và tool của mọi lượt với công xem lại và làm lại. Chia cho 978 việc thành công, phân tích 4 loại yêu cầu và cộng chi phí cố định ở 2 mức khối lượng. [Mã nguồn](../../src/lab13.py) · [Bảng chi phí](bang_chi_phi.md) |
| B · Độ nhạy | Chạy 9 kịch bản và đối chiếu phương án 1–3 lượt. Giới hạn 2 lượt cho tổng chi phí hệ thống thấp nhất, 6.901.220 đ trên 1.200 yêu cầu (simulated). [Bảng độ nhạy](bang_chi_phi.md#b1--đổi-từng-yếu-tố) |
| C · Bảng lỗi | Đã đối chiếu tài liệu tham khảo cho 20 ca và đề xuất khắc phục 5 loại lỗi. Kết quả đồng thuận chờ 2 bộ nhãn độc lập đã chốt. [Bảng lỗi](bang_loi.md) |
| D · Pilot | Phân ngẫu nhiên theo nhân viên, phân tầng depot, có 20 người và ít nhất 5.980 yêu cầu mỗi nhóm. Kế hoạch có 4 luật dừng và mốc quyết định 09/02/2027. [Kế hoạch pilot](pilot_plan.yaml) |
| E · Chỉ số và launch | Tính 3 chỉ số, đặc tả 10 event cho hai nhóm và đưa 2 rủi ro kinh tế vào hồ sơ Gate 2a. [Chỉ số](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md) |

## 4. Kết quả

Chi phí chạy thử là 4.472 đ/việc thành công chưa gồm cố định (simulated). Ba chỉ số là 82,83% đóng trong 24 giờ và không mở lại, 27,12% bỏ qua gợi ý và 4,25% mở lại. Đây là các tỷ lệ của đợt chạy thử.

Đề xuất **Go có điều kiện** cho nội địa và hàng nặng. Xem lại 100% có thể lên 12.415 đ/việc thành công (simulated), nên cần đo thời gian thực và áp dụng luật giữ bậc. [Hồ sơ launch](ho_so_launch_v0.md)

Duyệt chéo và phản hồi dành cho nhóm đang chờ xác nhận. [Phiếu chấm](phieu_cham.md)

## 5. Khó khăn và cách xử lý

Lệnh `..\.venv\Scripts\python.exe -X utf8 lab13.py` từ `src/` báo `No Python at ...Python312\python.exe`. Kiểm tra lại trên máy Task D bằng Python 3.12 có sẵn và thư viện cài cục bộ. Script chạy hết A1–D3, cả 3 phép thử A1 đạt và YAML đọc được bằng `yaml.safe_load`.

## 6. Tổng hợp đóng góp

Đinh Phúc Diên làm phần chi phí A. Lê Nguyễn Anh Khôi làm độ nhạy B và thiết kế pilot D. Lê Nguyễn Anh Nhân rà CP3, đề xuất các biện pháp khắc phục và tổng hợp CP5. [Phân công](../../TEAM.md)

## 7. Hạn chế và hướng cải thiện

Phút xem lại và làm lại là simulated. Pilot đo phút thực ở cả hai nhóm. Với 20 cụm mỗi nhóm, power ở mức chênh +5 điểm khoảng 64%; cần ghi thiếu bằng chứng nếu không đủ mẫu hoặc thời gian theo dõi ở ngày quyết định.

## 8. Tài liệu tham khảo

[Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) · [Hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) · [Rubric](../../RUBRIC.md)

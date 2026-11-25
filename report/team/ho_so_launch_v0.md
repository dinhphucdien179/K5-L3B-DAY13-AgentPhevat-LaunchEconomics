# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm AgentPhevat · Lớp L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu **4.472 đ/việc** chưa gồm cố định (simulated), với 978 việc thành công trên 1.200 yêu cầu. [A2](bang_chi_phi.md#a2--mô-hình-chi-phí-từ-trace) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại gấp đôi **+51,8%**, tỷ lệ xem lại gấp đôi **+40,7%**, lương tăng 25% **+23,1%** (simulated). [B2](bang_chi_phi.md#b2--đổi-một-cặp-và-xếp-hạng) | Giả lập | Chuyên viên phân tích chi phí |
| 3 · So với nhân viên tự làm | Hệ thống tốn **6.449–7.338 đ/yêu cầu** (simulated) ở hai mức 45.000 và 22.500 yêu cầu/tháng, đã tính 40 triệu đ cố định/tháng và ca thủ công, ở mức xem lại của đợt chạy thử (128/982 = 13,03% yêu cầu trong phạm vi). Mốc thủ công **12.000 đ/yêu cầu**. [A4](bang_chi_phi.md#a4--chi-phí-cố-định-phạm-vi-noi_dia--hang_nang) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, dùng, an toàn | Chạy thử **82,83%** đóng trong 24 giờ và không mở lại trong 7 ngày, **27,12%** bỏ qua gợi ý, **4,25%** mở lại trong 7 ngày. [E1](chi_so.md) | Xong, có bằng chứng | Chuyên viên phân tích dữ liệu |
| 5 · Bảng lỗi và cách khắc phục | **5/5 loại lỗi** có biện pháp và cách đo đề xuất. Đồng thuận cho **20 ca** chờ 2 bộ nhãn độc lập. [CP3](bang_loi.md) | Chưa | Trưởng nhóm QA |
| 6 · Pilot plan | Phân ngẫu nhiên theo nhân viên, **20 + 20**, **5.980 yêu cầu/nhóm**. Power 80% cho +6 điểm, khoảng 64% cho +5 điểm. Quyết định **09/02/2027**. [Pilot](pilot_plan.yaml) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Xem lại 100% trong 5 phút đẩy chi phí lên **11.743–12.415 đ/việc** = 0,98–1,03× mức thủ công, hòa vốn khoảng **4,8 phút** xem lại (simulated). Chỉ giảm xem lại `noi_dia` còn 50% khi sửa hoặc bỏ dưới 15% trên ít nhất 307 lượt/tuần. Đợt chạy thử đang ở **18,28%**, chưa đạt. Đo giờ thật và giữ bậc theo luật chi phí. [B4](bang_chi_phi.md#b4--nếu-phải-xem-lại-tất-cả) | Giả lập | Trưởng nhóm CSKH |

**Phạm vi pilot** gồm `noi_dia` và `hang_nang` ở 12 depot, tương ứng 0,22× và 0,69× mức chi phí thủ công (simulated). `quoc_te` tốn 1,88× (simulated), `doi_tac` chỉ thành công 37/68 và có điều khoản riêng. Hai loại này tiếp tục xử lý thủ công. [A3](bang_chi_phi.md#a3--tách-theo-loại-yêu-cầu)

**Điều kiện kiểm tra theo lịch pilot**

- **04/12/2026 · Trưởng nhóm QA** kiểm thử 5 biện pháp khắc phục, ưu tiên chống hoàn trùng và đối soát số tiền hoàn.
- **06/12/2026 · Giám đốc vận hành** xác nhận đủ 40 nhân viên, khả năng đạt 299 yêu cầu/người và chấp nhận power khoảng 64% nếu chênh lệch thật là +5 điểm.
- **06/12/2026 · Trưởng nhóm kỹ thuật** kiểm thử log ở cả hai nhóm.
- **20/12/2026 · Trưởng nhóm CSKH** đối chiếu phút xem lại và làm lại đo thật trước mốc tăng bậc 25%, áp dụng ngưỡng chi phí biến đổi 12.000 đ/yêu cầu.
- **03/01/2027 · Trưởng nhóm CSKH** chốt mức xem lại cho cửa sổ phân tích 04/01–31/01/2027. Chỉ giảm xem lại `noi_dia` còn 50% khi đạt ngưỡng ở mục 7. Không đạt thì giữ 100% và ghi chi phí 0,98–1,03× mức thủ công (simulated) vào báo cáo ngày quyết định.

**Đề xuất — Go có điều kiện**

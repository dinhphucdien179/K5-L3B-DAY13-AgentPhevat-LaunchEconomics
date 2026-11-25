# Bảng lỗi và cách khắc phục · Nhiệm vụ C

Phân loại 20 ca theo nguyên nhân gốc. Mỗi người gắn nhãn đọc mục **Hai mươi ca lỗi** trong [đề bài](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx) và chốt riêng đủ 20 ca trước khi xem nhãn của người kia hoặc mở phần tham khảo dưới đây.

## Hai bộ nhãn độc lập

Bộ nhãn "lượt 1" có trong repo trước đây mang tên Lê Nguyễn Anh Khôi, nhưng thực chất là bản nháp do Codex gắn. RULES.md không cho dùng AI để tạo nhãn lỗi, nên nhóm bỏ bản này và không dùng nó để tính đồng thuận.

Nhóm có 3 người, nên hai người gắn nhãn là Lê Nguyễn Anh Khôi (người kiểm số) và Lê Nguyễn Anh Nhân (người giữ hồ sơ). Mỗi bạn tự gắn đủ 20 ca trên một phiếu trống riêng, không trao đổi với nhau. Trên phiếu, mỗi bạn ghi giờ bắt đầu, giờ chốt và cho biết trước đó đã từng xem nhãn tham khảo hay chưa. Đinh Phúc Diên không gắn nhãn, chỉ nhận hai phiếu để ghép và tính kết quả.

Tỷ lệ đồng thuận là số ca hai người gắn trùng nhau chia cho 20, và cần đạt ít nhất 16/20. Số ca khớp đáp án được tính riêng, bằng cách so nhãn thống nhất của nhóm với nhãn tham khảo.

Hai bộ nhãn gốc giữ nguyên sau khi so. Với mỗi ca lệch, nhóm ghi một câu quy tắc phân biệt và nhãn đã thống nhất. Nếu đồng thuận dưới 80%, nhóm viết lại định nghĩa rồi gắn lại vòng hai, nhưng vẫn giữ tỷ lệ của vòng đầu.

<details>
<summary>Nhãn tham khảo của 20 ca — chỉ mở sau khi chốt hai phiếu</summary>

## Bảng đối chiếu

Cột **Nhãn tham khảo** lấy từ [hướng dẫn Lab 13, mục Nhãn tham khảo cho 20 ca](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca). Dấu — đánh dấu ô chờ hai phiếu gốc hoặc kết quả thống nhất của nhóm.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng | Nhãn thống nhất | Nhãn tham khảo |
| ---: | --- | --- | --- | --- | --- |
| 1 | — | — | — | — | Do người dùng |
| 2 | — | — | — | — | Hệ thống |
| 3 | — | — | — | — | Ngữ cảnh |
| 4 | — | — | — | — | Giới hạn hệ thống |
| 5 | — | — | — | — | Ngầm |
| 6 | — | — | — | — | Do người dùng |
| 7 | — | — | — | — | Hệ thống |
| 8 | — | — | — | — | Hệ thống |
| 9 | — | — | — | — | Do người dùng |
| 10 | — | — | — | — | Ngữ cảnh |
| 11 | — | — | — | — | Giới hạn hệ thống |
| 12 | — | — | — | — | Ngầm |
| 13 | — | — | — | — | Giới hạn hệ thống |
| 14 | — | — | — | — | Do người dùng |
| 15 | — | — | — | — | Hệ thống |
| 16 | — | — | — | — | Ngữ cảnh |
| 17 | — | — | — | — | Ngầm |
| 18 | — | — | — | — | Ngữ cảnh |
| 19 | — | — | — | — | Giới hạn hệ thống |
| 20 | — | — | — | — | Hệ thống |

### Quy tắc phân biệt khi đối chiếu

- **Ca 6 và 9** thuộc lỗi do người dùng vì khách chọn sai loại yêu cầu hoặc nhập sai mã. Xác nhận hoặc gợi ý trên giao diện là cách phòng lỗi.
- **Ca 8 và 15** thuộc lỗi hệ thống vì có sai lệch cụ thể so với chính sách, thể hiện ngay trong nội dung hoặc bị bắt ở bước xem lại. **Ca 5 và 17** là lỗi ngầm vì sai lệch chỉ lộ ra khi kiểm tra.
- **Ca 10, 16 và 18** thuộc lỗi ngữ cảnh. Hệ thống làm đúng theo chính sách hoặc thiết kế, nhưng lời hứa, giờ thông báo hoặc cách giải thích lệch kỳ vọng của khách.
- **Ca 13 và 19** thuộc giới hạn hệ thống vì yêu cầu nằm ngoài phạm vi hoặc ngoài khoảng dữ liệu truy cập được. Ghi thêm vấn đề giao tiếp nếu trợ lý giải thích giới hạn chưa rõ.

</details>

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Các ngưỡng dưới đây là đề xuất cho pilot. Ca và loại lỗi lấy từ đề bài và bảng tham khảo.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| ---: | --- | --- | --- | --- |
| 6 | Do người dùng | Ghi `refund_reason_mismatch` kèm lý do đã chọn và lý do phát hiện từ mô tả, nối bằng `request_id` và `trace_id`. Kiểm tra mỗi lần gửi, kích hoạt xác nhận từ 1 mâu thuẫn. | Hỏi lại khách xem kiện bị vỡ hay giao trễ, cho sửa mục đã chọn trước khi áp dụng chính sách. | PM trợ lý hoàn phí |
| 20 | Hệ thống | Mỗi ca trực, đối chiếu `refund_ledger_write` theo `refund_intent_id` xuyên các `request_id`. Từ 2 giao dịch thành công cho cùng khoản hoàn thì kế toán xác minh, 1 ca hoàn trùng đã xác nhận kích hoạt luật dừng. | Tạo khóa chống trùng từ định danh khoản hoàn ổn định phía máy chủ. Khi khách gửi lại, trả trạng thái giao dịch trước và đối soát khoản đã hoàn. | Kỹ sư trưởng sổ cái |
| 16 | Ngữ cảnh | Ghi `refund_notification_sent` kèm giờ địa phương, kênh và `trace_id`. Rà mỗi ngày, báo từ 1 thông báo Zalo gửi từ 22:00 đến trước 07:00. | Ghi kết quả hoàn vào ứng dụng ngay khi xong. Hẹn thông báo Zalo đến khung giờ khách nhận hoặc theo tùy chọn đã lưu. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Mỗi khi truy xuất, kiểm tra tuổi đơn với giới hạn 12 tháng. Đối chiếu hằng ngày những yêu cầu vượt giới hạn với `handoff_to_staff` có `reason = ngoai_cua_so_du_lieu`. Báo từ 1 yêu cầu thiếu bàn giao. | Giải thích giới hạn tra cứu, chuyển yêu cầu cùng mã đơn, ngày đặt và tóm tắt để nhân viên tra nguồn lưu trữ. | Trưởng nhóm vận hành hoàn phí |
| 5 | Ngầm | Đối soát hằng tuần tối đa 100 yêu cầu đủ điều kiện, ưu tiên đơn có mã giảm giá ở cả hai nhóm. Dùng `audit_sample_checked` so số hoàn thực với số đúng trên giá sau giảm. Báo từ 1 ca lệch. | Tính theo dòng tiền thực thu sau giảm, lưu nguồn số tiền vào trace và đối soát nhóm đơn đã hoàn từ cùng phiên bản tính phí. | Kế toán trưởng |

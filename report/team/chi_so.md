# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Tử số / mẫu số | Đợt chạy thử (1.200 yêu cầu) |
| --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` / mọi yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỷ lệ bỏ qua gợi ý | Yêu cầu đã xem lại có quyết định `sua` hoặc `bo` / yêu cầu có `duoc_xem_lai = 1` | **27,12% (48/177)** |
| An toàn | Tỷ lệ mở lại trong 7 ngày | Yêu cầu có `mo_lai_trong_7_ngay = 1` / mọi yêu cầu | **4,25% (51/1.200)** |
| Dùng | Tỷ lệ mở trợ lý | Yêu cầu có ít nhất một lần nhân viên mở trợ lý / mọi yêu cầu đủ điều kiện được phân vào nhóm trợ lý | Đề xuất đo trong pilot |
| An toàn | Tỷ lệ hoàn sai tiền qua đối soát | Yêu cầu có tổng tiền thực hoàn khác số tiền đúng / số yêu cầu được lấy mẫu và đối soát xong | Đề xuất đo hằng tuần ở cả hai nhóm |

Ba tỷ lệ mô tả đợt chạy thử trên dữ liệu giả lập. Đợt chạy thử chưa có nhóm đối chứng. Từ `src/`, đối chiếu các tử số và mẫu số với CSV bằng lệnh sau.

```powershell
python -c "import pandas as pd; r = pd.read_csv('logix_requests.csv', keep_default_na=False); x = r[r.duoc_xem_lai == 1]; print(((r.dong_trong_24h == 1) & (r.mo_lai_trong_7_ngay == 0)).sum(), len(r)); print(x.quyet_dinh_xem_lai.isin(['sua', 'bo']).sum(), len(x)); print((r.mo_lai_trong_7_ngay == 1).sum(), len(r))"
```

## Danh sách event

Mỗi event ghi `event_id`, `event_at`, `request_id` và `trace_id`. Hệ thống tạo `trace_id` ngay khi tiếp nhận, ở cả nhóm đối chứng, rồi truyền qua mọi lượt và lần chuyển ca. Nối theo `request_id`, loại sự kiện lặp theo `event_id` và đếm yêu cầu phân biệt trong các tỷ lệ.

| Event | Ai tạo | Khoá nối | Thuộc tính chính ngoài các trường chung | Thời điểm |
| --- | --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận | `request_id`, `trace_id` | `staff_id` được phân ban đầu, `depot`, `loai`, `so_tien_vnd`, `arm`, `eligible`, `rollout_stage`, `review_required` (bốc mẫu xem lại theo `review_policy`) | Khi tiếp nhận và ghi phân bổ |
| `agent_opened` | Giao diện nhân viên | `request_id`, `trace_id` | `staff_id` thực hiện | Khi nhân viên mở trợ lý cho yêu cầu |
| `agent_run_completed` | Trợ lý | `request_id`, `trace_id` | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status` | Sau mỗi lượt, kể cả lượt lỗi |
| `staff_review_decision` | Giao diện nhân viên | `request_id`, `trace_id` | `staff_id`, `run_id`, `decision` (`giu`, `sua`, `bo`), `is_final` | Khi lưu quyết định xem lại |
| `staff_work_completed` | Giao diện nhân viên | `request_id`, `trace_id` | `staff_id`, `work_id`, `work_type` (`review`, `rework`, `manual`), `duration_minutes` đo thực tế trong khoảng làm việc không trùng | Khi hoàn tất một lượt xem lại, làm lại hoặc xử lý thủ công |
| `handoff_to_staff` | Hệ thống điều phối | `request_id`, `trace_id` | `from_staff_id`, `to_staff_id`, `reason` | Khi chuyển ca, kể cả sau 2 lượt hoặc khi tắt trợ lý |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `trace_id` | `refund_intent_id`, `idempotency_key`, `ledger_txn_id`, `amount_vnd`, `status` | Sau mỗi lần ghi sổ |
| `ticket_closed` | Hệ thống ticket | `request_id`, `trace_id` | `staff_id`, `closed_at` | Mỗi lần đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `request_id`, `trace_id` | `reopened_at`, `reason` | Mỗi lần mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `request_id`, `trace_id` | `audit_batch_id`, `actual_refund_vnd`, `expected_refund_vnd` | Khi đối soát xong từng yêu cầu lấy mẫu hằng tuần ở mỗi nhóm |

- **Chính và an toàn.** Lấy mọi yêu cầu đủ điều kiện và đã theo dõi đủ 7 ngày từ `refund_request_created`, theo `arm` ban đầu. Nối `ticket_closed` để kiểm tra lần đóng đầu trong 24 giờ và `ticket_reopened` để đếm mở lại sau khi đóng nhưng trong 7 ngày kể từ tiếp nhận. Phân tích chính chỉ lấy yêu cầu từ bậc 50% trong cửa sổ của kế hoạch pilot, kể cả yêu cầu chuyển thủ công.
- **Sử dụng.** Lấy quyết định xem lại cuối của từng yêu cầu từ `staff_review_decision` để tính bỏ qua theo tuần. Tách riêng theo `loai` để biết `noi_dia` đã đủ điều kiện giảm xem lại chưa, tức dưới 15% trên ít nhất 307 lượt mỗi tuần. Trong đợt chạy thử, con số này là 17/93 = 18,28%. Tính tỷ lệ mở từ `agent_opened` trên nhóm trợ lý trong cùng bậc. Theo dõi cả lượt mở từ tài khoản đối chứng để phát hiện lẫn nhóm.
- **Kiểm tra mẫu.** Nối `audit_sample_checked` với nhóm phân bổ ban đầu, đếm sai tiền theo từng nhóm. Kiểm tra hoàn trùng qua nhiều `ledger_txn_id` ghi thành công cho cùng `refund_intent_id`; kế toán xác minh trước khi kích hoạt luật dừng.
- **Chi phí.** Khử trùng theo `run_id` và `work_id` trước khi tính tiền token, tool và công lao động thật. Chia tổng chi phí biến đổi theo tuần cho mọi yêu cầu đủ điều kiện trong nhóm trợ lý. Ghi công xử lý thủ công ở cả hai nhóm. [Kế hoạch pilot](pilot_plan.yaml)

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Tín hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng | B1 toàn mẫu tăng **51,8%**, lên **6.787 đ/việc thành công** nếu số ca làm lại gấp đôi (simulated). | Tỷ lệ yêu cầu có `work_type = rework` trong tuần vượt 7%. Mốc chạy thử trong phạm vi là 48/982 (4,89%). | Rà tối đa 20 trace làm lại, ưu tiên hàng nặng, rồi xử lý nguyên nhân trước khi tăng bậc. | PM trợ lý hoàn phí |
| Xem lại 100% kéo dài | B4 trong phạm vi pilot là **11.743 đ/việc thành công** với 9 phút làm lại hoặc **12.415 đ** với 15,30 phút làm lại (simulated). | Thời gian xem lại trung bình trên 4,8 phút/lượt (mốc hòa vốn simulated của kịch bản thứ hai). | Chuẩn hóa màn hình và checklist để rút ngắn thời gian, giữ xác nhận số tiền và kiểm tra hoàn trùng. Từ bậc 25%, chỉ giảm xem lại `noi_dia` còn 50% khi tỷ lệ sửa hoặc bỏ dưới 15% trên ít nhất 307 lượt/tuần (chạy thử 18,28%). `hang_nang` giữ 100%. Dùng phút đo thật khi xét tăng bậc. | Trưởng nhóm CSKH |

Nguồn số liệu và giả định cho các kịch bản E2 nằm trong [bảng chi phí B1, B4](bang_chi_phi.md).

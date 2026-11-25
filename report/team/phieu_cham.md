# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1.

- Nhóm chấm (hội đồng): AgentPhevat (L3B)
- Nhóm được chấm: Aliba6 (L3B), [repo K5-L3B-DAY13-Aliba6-LaunchEconomics](https://github.com/justcoffeee/K5-L3B-DAY13-Aliba6-LaunchEconomics)
- Bản được chấm: nhánh `main`, commit `91175e9` lúc 17:36 ngày 25/11/2026

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| C6 · Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp với số của nhóm: trong phạm vi `noi_dia` + `hang_nang`, mỗi việc thành công tốn 3.414 đ, cộng chi phí cố định thành 4.599 đ = 0,38× mức tự làm (simulated). Nhóm nêu thẳng ba con số bất lợi và có cách xử lý cho từng số. Power chỉ còn 0,64 nếu tác động thật là 5 điểm: Giám đốc vận hành ký chấp nhận (điều kiện 2). Xem lại 100% đẩy chi phí lên 11.743–12.415 đ = 0,98–1,03× (simulated): xử lý bằng điều kiện 4 và luật dừng 4. Tỉ lệ mở lại hiện tại 4,25%: đặt ngưỡng chênh 2 điểm so với đối chứng kèm trần 6%. |
| C7 · Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập, phạm vi thu hẹp có lý do bằng số | 5 | Phạm vi thu hẹp có lý do bằng số: giữ `noi_dia` (0,22×) và `hang_nang` (0,69×), loại `quoc_te` (1,88×, 27,3% thành công) và `doi_tac` (0,85×, 54,4% thành công) (simulated). Phần lớn số giả lập đã có nhãn, nhưng còn ba chỗ thiếu: 1,88× ở dòng đề xuất của `ho_so_launch_v0.md` (dòng 17), xếp hạng +51,8% / +40,7% / +23,1% ở B2 (`bang_chi_phi.md` dòng 68), và mức hoà vốn 5,1 / 4,8 phút ở B4 (dòng 84). Vì vậy chưa đạt mức "nhãn ở mọi số giả lập". |
| C8 · Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên theo nhân viên 20 + 20, phân tầng theo depot, đối chứng làm cùng tuần, đủ 20 cụm mỗi nhóm. Cỡ mẫu tính đúng: mde 0,06, 859 mỗi nhóm, DE 6,96, ít nhất 299 yêu cầu mỗi người, và có nói rõ power 0,64 ở mức 5 điểm. Bốn luật dừng đều có ngưỡng (2 điểm hoặc 6%, 8.000 đ, 40%, 50% hoặc 5 phút), có thời hạn (3 ngày, 2 tuần, 1 tuần, tuần cuối bước 0.25) và có người có quyền dừng (Giám đốc vận hành, PM, Trưởng nhóm CSKH). Ngày quyết định 2027-01-11 đã chừa đủ 7 ngày theo dõi mở lại. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện, đồng ý với đề xuất của Aliba6.

**Lý do:** Kể cả khi cộng chi phí cố định, chi phí trong phạm vi chỉ bằng 0,38–0,48× mức nhân viên tự làm (simulated). Pilot tách được tác động và luật dừng đủ bốn vế. Hội đồng thêm ba điều kiện:

1. Gắn nhãn simulated cho các số còn thiếu ở hồ sơ dòng 17 và ở B2, B4 trong bảng chi phí.
2. Sửa trạng thái mục 5 của hồ sơ. Mục này ghi đồng thuận 20/20 là "Xong, có bằng chứng", nhưng `TEAM.md` của chính nhóm ghi rằng lúc soạn bằng Codex đã thấy nhãn của người 2, nên hai bộ nhãn chưa độc lập. `group_report.md` cũng ghi là còn phải đối chiếu lại hai bộ nhãn.
3. Nói rõ lộ trình giảm xem lại. `chi_so.md` chỉ cho giảm khi tỉ lệ sửa + bỏ dưới 15%, nhưng trong đợt chạy thử, tỉ lệ này trong phạm vi đã là 21,09% (27/128).

**Câu hỏi cho đội trình:** Ngưỡng giảm xem lại của nhóm là sửa + bỏ dưới 15%, mà trong phạm vi đợt chạy thử con số này đã là 21,09%. Nếu đến cuối bước 0.25 vẫn chưa giảm được, xem lại sẽ giữ 100% với chi phí 0,98–1,03× (simulated) và luật dừng 4 sẽ giữ rollout ở bước 0.25. Khi đó ngày quyết định 2027-01-11 dời sang ngày nào, và nhóm còn giữ đề xuất Go có điều kiện không?

**Câu trả lời của đội trình:** (điền theo lời Aliba6 trả lời tại buổi)

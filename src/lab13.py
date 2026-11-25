"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng mỗi tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    thanh_cong = ti_le_thanh_cong(p, k)
    if p == 0:
        return math.inf if k is None else k
    return thanh_cong / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất thành công sau tối đa k lần chạy độc lập có cùng xác suất p."""
    if not 0 <= p <= 1 or (k is not None and k < 0):
        raise ValueError('p phải thuộc [0, 1] và k phải không âm')
    if p == 0 or k == 0:
        return 0.0
    if p == 1 or k is None:
        return 1.0
    # Tính 1 - (1 - p)**k ổn định khi p rất nhỏ.
    return -math.expm1(k * math.log1p(-p))


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # E[số lượt] / P(thành công) = 1/p khi xác suất thành công dương.
    return 1 / p if ti_le_thanh_cong(p, k) > 0 else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chi phí và số việc thành công cho tập yêu cầu truyền vào.

    token và tool gồm mọi lượt đã tính phí, kể cả lượt lỗi. chay_lai là
    phần token và tool của các lượt từ thứ hai. Chi phí xem_lai, lam_lai
    lấy từ phút simulated và dùng các hệ số để phân tích độ nhạy ở CP2.
    cps chia tổng chi phí cho số việc thành công, còn hoa_don_moi_yc chia
    chi phí token và tool cho toàn bộ yêu cầu. Kết quả giữ nguyên độ chính xác.
    """
    runs = runs.loc[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs.loc[runs['attempt'] <= max_lan_chay]
        reqs = reqs.copy()
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    token_moi_luot = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tool_moi_luot = runs['tool_calls'] * gia_tool
    token = token_moi_luot.sum()
    tool = tool_moi_luot.sum()
    chay_lai = (token_moi_luot + tool_moi_luot).loc[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int(reqs['ket_qua'].eq('thanh_cong').sum())

    return {
        'token': token,
        'tool': tool,
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong if thanh_cong else math.inf,
        'hoa_don_moi_yc': (token + tool) / len(reqs) if len(reqs) else math.nan,
    }


def in_bang_a3(runs, reqs):
    """In số liệu chi phí theo loại yêu cầu và hiệu quả chạy lại cho quốc tế."""
    print('\nA3 · Chi phí theo loại yêu cầu')
    print(f"{'Loại':10s} {'Yêu cầu':>8s} {'Thành công':>12s} {'Lượt/YC':>9s} "
          f"{'CPS (đ, simulated)':>20s} {'So với 12.000 đ':>17s}")
    for loai, nhom in reqs.groupby('loai', sort=False):
        ket_qua = mo_hinh(runs, nhom)
        ti_le = ket_qua['thanh_cong'] / len(nhom)
        luot_moi_yeu_cau = nhom['so_lan_chay'].mean()
        cps = ket_qua['cps']
        print(f'{loai:10s} {len(nhom):8d} {ti_le:12.1%} {luot_moi_yeu_cau:9.2f} '
              f'{cps:20,.0f} {cps / BASELINE:16.2f}×')

    reqs_quoc_te = reqs.loc[reqs['loai'] == 'quoc_te', ['request_id', 'ket_qua', 'so_lan_chay']]
    runs_quoc_te = runs.merge(reqs_quoc_te, on='request_id')
    for lan, luot in runs_quoc_te.groupby('attempt'):
        so_ok = luot['status'].eq('ok').sum()
        so_thanh_cong = (luot['so_lan_chay'].eq(lan) & luot['ket_qua'].eq('thanh_cong')).sum()
        print(f'Quốc tế lượt {lan}: {so_ok}/{len(luot)} ok ({so_ok / len(luot):.1%}), '
              f'{so_thanh_cong} yêu cầu thành công sau lượt này')


def in_bang_a4(runs, reqs):
    """In dự phóng chi phí có cố định khi chỉ dùng trợ lý cho nội địa và hàng nặng."""
    reqs_pham_vi = reqs.loc[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ket_qua = mo_hinh(runs, reqs_pham_vi)
    ti_le_thanh_cong_toan_mau = ket_qua['thanh_cong'] / len(reqs)
    # Theo B3, mọi yêu cầu trợ lý chưa hoàn tất được tính 12.000 đ xử lý thủ công.
    thu_cong = (len(reqs) - ket_qua['thanh_cong']) * BASELINE
    he_thong_moi_yeu_cau = (ket_qua['tong'] + thu_cong) / len(reqs)

    print('\nA4 · Chi phí có cố định trong phạm vi noi_dia + hang_nang')
    print(f"{'Yêu cầu/tháng':>14s} {'Việc thành công':>16s} {'Cố định/việc (đ)':>18s} "
          f"{'CPS + cố định (đ, simulated)':>29s} {'Hệ thống/YC (đ, simulated)':>28s}")
    for khoi_luong in (45_000, 22_500):
        viec_thanh_cong = khoi_luong * ti_le_thanh_cong_toan_mau
        co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_thanh_cong
        cps_co_dinh = ket_qua['cps'] + co_dinh_moi_viec
        he_thong_co_dinh = he_thong_moi_yeu_cau + CHI_PHI_CO_DINH / khoi_luong
        print(f'{khoi_luong:14,d} {viec_thanh_cong:16,.0f} {co_dinh_moi_viec:18,.2f} '
              f'{cps_co_dinh:29,.2f} {he_thong_co_dinh:28,.2f}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Mô hình chi phí từ trace')
    for ten, gia_tri in ket_qua.items():
        nhan = ' simulated' if ten in {'xem_lai', 'lam_lai', 'tong', 'cps'} else ''
        so_le = 2 if ten == 'hoa_don_moi_yc' else 0
        print(f'{ten:16s} {gia_tri:14,.{so_le}f}{nhan}')
    ti_so = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    khoan_lon_nhat = max(('token', 'tool', 'xem_lai', 'lam_lai'), key=ket_qua.__getitem__)
    ti_trong = ket_qua[khoan_lon_nhat] / ket_qua['tong']
    print(f'CPS / hóa đơn mỗi yêu cầu: {ti_so:.2f}× (simulated)')
    print(f'Khoản lớn nhất: {khoan_lon_nhat} ({ti_trong:.1%}, simulated)')
    in_bang_a3(runs, reqs)
    in_bang_a4(runs, reqs)
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower

"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

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


def in_bang_b1_b3(runs, reqs, cps_goc):
    """In độ nhạy so với A2 và so sánh chi phí theo giới hạn lượt chạy."""
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA),
        'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=1.25 * LUONG_PHUT),
    }
    cps = {ten: mo_hinh(runs, reqs, **tham_so)['cps'] for ten, tham_so in kich_ban.items()}
    theo_gioi_han = {k: mo_hinh(runs, reqs, max_lan_chay=k) for k in (1, 2, 3)}
    cps['Chỉ cho chạy tối đa 2 lần'] = theo_gioi_han[2]['cps']
    cps['Chỉ cho chạy 1 lần'] = theo_gioi_han[1]['cps']
    thay_doi = {ten: gia_tri / cps_goc - 1 for ten, gia_tri in cps.items()}

    print('\nB1 · Đổi từng yếu tố')
    print(f'{"Kịch bản":30s} {"CPS (đ, simulated)":>20s} {"Thay đổi (simulated)":>22s}')
    for ten, gia_tri in cps.items():
        print(f'{ten:30s} {gia_tri:20,.0f} {thay_doi[ten]:+22.1%}')

    print('\nB2 · Đổi một cặp và xếp hạng')
    cps_doi = mo_hinh(runs, reqs, **kich_ban['Giá token gấp đôi'],
                      **kich_ban['Tỉ lệ xem lại gấp đôi'])['cps']
    tong_tac_dong = thay_doi['Giá token gấp đôi'] + thay_doi['Tỉ lệ xem lại gấp đôi']
    print(f'Giá token và tỉ lệ xem lại cùng gấp đôi: {cps_doi:,.0f} đ ({cps_doi / cps_goc - 1:+.1%}, simulated)')
    print(f'Tổng tác động riêng của token và xem lại: {tong_tac_dong:+.1%} (simulated)')
    tac_dong = {
        'Giá token': thay_doi['Giá token gấp đôi'],
        'Tỉ lệ xem lại': thay_doi['Tỉ lệ xem lại gấp đôi'],
        'Số ca làm lại': thay_doi['Số ca làm lại gấp đôi'],
        'Lương nhân viên': thay_doi['Lương nhân viên tăng 25%'],
        'Giới hạn lượt chạy': max(thay_doi['Chỉ cho chạy 1 lần'],
                                  thay_doi['Chỉ cho chạy tối đa 2 lần'], key=abs),
    }
    xep_hang = sorted(tac_dong, key=lambda ten: abs(tac_dong[ten]), reverse=True)
    for hang, ten in enumerate(xep_hang[:3], 1):
        print(f'{hang}. {ten}: {tac_dong[ten]:+.1%} (simulated)')

    print('\nB3 · So sánh giới hạn lượt chạy')
    print(f'{"Số lượt":>7s} {"Không thành công":>17s} {"Trợ lý (đ, simulated)":>23s} '
          f'{"Hệ thống (đ, simulated)":>25s} {"CPS (đ, simulated)":>20s}')
    for gioi_han, ket_qua in theo_gioi_han.items():
        chua_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        he_thong = ket_qua['tong'] + BASELINE * chua_thanh_cong
        print(f"{gioi_han:7d} {chua_thanh_cong:17d} {ket_qua['tong']:23,.0f} "
              f"{he_thong:25,.0f} {ket_qua['cps']:20,.0f}")


def in_bang_b4(runs, reqs):
    """In chi phí khi xem lại mọi yêu cầu có lượt ok trong phạm vi B4."""
    reqs_pham_vi = reqs.loc[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pham_vi = runs.loc[runs['request_id'].isin(reqs_pham_vi['request_id'])]
    ket_qua = mo_hinh(runs_pham_vi, reqs_pham_vi)
    token_tool = ket_qua['token'] + ket_qua['tool']
    thanh_cong = ket_qua['thanh_cong']
    so_xem_lai = runs_pham_vi.loc[runs_pham_vi['status'].eq('ok'), 'request_id'].nunique()
    so_lam_lai = reqs_pham_vi['ket_qua'].eq('lam_lai').sum()
    xem_lai = so_xem_lai * 5 * LUONG_PHUT
    lam_lai_toan_mau = reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated']
    phut_trung_binh = lam_lai_toan_mau.mean()

    print('\nB4 · Xem lại 100% trong phạm vi noi_dia + hang_nang')
    print(f'{len(reqs_pham_vi):,d} yêu cầu, {thanh_cong:,d} thành công, {so_lam_lai:,d} ca làm lại')
    print(f'Token và tool: {token_tool:,.0f} đ. Xem lại: {so_xem_lai:,d} × 5 phút = {xem_lai:,.0f} đ (simulated)')
    print(f'Phút làm lại trung bình trên {len(lam_lai_toan_mau)} ca toàn mẫu: '
          f'{phut_trung_binh:.2f} phút (simulated)')
    for ten, phut in (('Giả định đề bài', 9), ('Trung bình toàn mẫu', phut_trung_binh)):
        lam_lai = so_lam_lai * phut * LUONG_PHUT
        tong = token_tool + xem_lai + lam_lai
        cps = tong / thanh_cong
        phut_hoa_von = (BASELINE * thanh_cong - token_tool - lam_lai) / (so_xem_lai * LUONG_PHUT)
        print(f'{ten}: làm lại {lam_lai:,.0f} đ, tổng {tong:,.0f} đ, '
              f'CPS {cps:,.0f} đ ({cps / BASELINE:.2f}× {BASELINE:,d} đ), '
              f'hòa vốn ở {phut_hoa_von:.1f} phút/lượt xem lại (simulated)')


def co_mau_hai_ti_le(p1, p2, alpha, power):
    """Cỡ mẫu mỗi nhóm theo công thức so sánh hai tỉ lệ trong đề."""
    chuan = NormalDist()
    z_alpha = chuan.inv_cdf(1 - alpha / 2)
    z_power = chuan.inv_cdf(power)
    p_trung_binh = (p1 + p2) / 2
    do_lech_gop = math.sqrt(2 * p_trung_binh * (1 - p_trung_binh))
    do_lech_rieng = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((z_alpha * do_lech_gop + z_power * do_lech_rieng) / (p2 - p1)) ** 2)


def in_co_mau_d1():
    """In cỡ mẫu của năm phương án và power ở mức chênh 5 điểm."""
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize

    baseline, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    so_nhan_vien_nhom, so_depot_nhom = 20, 6
    n_5 = co_mau_hai_ti_le(baseline, 0.75, alpha, power)
    n_6 = co_mau_hai_ti_le(baseline, 0.76, alpha, power)

    m_75 = 75
    de_75 = 1 + (m_75 - 1) * icc
    n_75 = math.ceil(n_5 * de_75)
    nhan_vien_75 = math.ceil(n_75 / m_75)

    # Giải số yêu cầu mỗi nhân viên từ bất đẳng thức c * m / DE >= n_6.
    m_toi_thieu = math.ceil(n_6 * (1 - icc) / (so_nhan_vien_nhom - n_6 * icc))
    de = 1 + (m_toi_thieu - 1) * icc
    n_thuc = so_nhan_vien_nhom * m_toi_thieu
    n_hieu_dung = n_thuc / de
    hieu_ung_5 = proportion_effectsize(baseline, 0.75)
    power_5 = NormalIndPower().power(hieu_ung_5, nobs1=n_hieu_dung, alpha=alpha)

    print('\nD1 · Cỡ mẫu pilot')
    print(f'a) Chia theo yêu cầu (+5 điểm): {n_5:,d} yêu cầu/nhóm')
    print(f'b) {m_75} yêu cầu/nhân viên: DE {de_75:.2f}, cần ít nhất {n_75:,d} yêu cầu/nhóm '
          f'và {nhan_vien_75} nhân viên/nhóm ({nhan_vien_75 * m_75:,d} yêu cầu khi làm tròn cụm)')
    print(f'c) {so_nhan_vien_nhom} nhân viên/nhóm: n hiệu dụng < {so_nhan_vien_nhom / icc:,.0f}')
    print(f'd) {so_depot_nhom} depot/nhóm: n hiệu dụng < {so_depot_nhom / icc:,.0f}')
    print(f'e) +6 điểm: cần {n_6:,d} hiệu dụng/nhóm, tối thiểu {m_toi_thieu} yêu cầu/nhân viên, '
          f'DE {de:.2f}, {n_thuc:,d} yêu cầu/nhóm cho {n_hieu_dung:,.2f} hiệu dụng/nhóm')
    print(f'   Power ở +5 điểm với thiết kế này: {power_5:.1%}')


def in_ty_le_mo_lai_d3(reqs):
    """In mốc an toàn cho toàn mẫu và phạm vi pilot."""
    reqs_pham_vi = reqs.loc[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    print('\nD3 · Tỉ lệ mở lại trong 7 ngày của đợt chạy thử')
    for ten, nhom in (('Toàn mẫu', reqs), ('noi_dia + hang_nang', reqs_pham_vi)):
        mo_lai = nhom['mo_lai_trong_7_ngay'].eq(1).sum()
        print(f'{ten}: {mo_lai}/{len(nhom):,d} ({mo_lai / len(nhom):.2%})')


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
    in_bang_b1_b3(runs, reqs, ket_qua['cps'])
    in_bang_b4(runs, reqs)
    in_co_mau_d1()
    in_ty_le_mo_lai_d3(reqs)

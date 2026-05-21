# modules/m3_optimization.py
# M3: TỐI ƯU PHÂN BỔ (từ Bài 4,8)
# Tác giả: [Tên bạn]
# Ngày: 2025

import numpy as np
import pandas as pd

def run_m3(scenario="S5"):
    """
    Chạy module M3 - Tối ưu phân bổ ngân sách
    Args:
        scenario: "S1", "S2", "S3", "S4", "S5"
    Returns:
        dict: {
            'name': tên kịch bản,
            'allocation': tỷ lệ phân bổ,
            'gdp_2030': GDP dự báo,
            'phan_bo_vung': phân bổ theo vùng,
            'khuyen_nghi': khuyến nghị
        }
    """

    # 5 kịch bản chính sách (tỷ lệ K:D:AI:H)
    allocation = {
        "S1": {"I": 70, "D": 10, "AI": 10, "H": 10, "name": "Truyền thống"},
        "S2": {"I": 25, "D": 45, "AI": 15, "H": 15, "name": "Số hóa nhanh"},
        "S3": {"I": 20, "D": 20, "AI": 45, "H": 15, "name": "AI dẫn dắt"},
        "S4": {"I": 30, "D": 20, "AI": 10, "H": 40, "name": "Bao trùm số"},
        "S5": {"I": 35, "D": 25, "AI": 25, "H": 15, "name": "Tối ưu cân bằng"}
    }

    # GDP 2030 dự báo theo từng kịch bản (nghìn tỷ)
    gdp_scenario = {"S1": 16500, "S2": 17800, "S3": 19200, "S4": 15800, "S5": 18500}

    # Phân bổ theo vùng (nghìn tỷ) - từ Bài 4 (tối ưu hóa LP)
    phan_bo_vung = {
        "Vùng": ["Đông Nam Bộ", "Đồng bằng sông Hồng", "Bắc Trung Bộ",
                 "Tây Nguyên", "ĐBSCL", "Trung du miền núi Bắc"],
        "Hạ tầng (I)": [5200, 4800, 3500, 2800, 3200, 2500],
        "Chuyển đổi số (D)": [1200, 1500, 800, 400, 600, 500],
        "AI": [6800, 5200, 2800, 1200, 2500, 1800],
        "Nhân lực (H)": [0, 0, 0, 5000, 0, 3200]
    }

    # Quỹ đạo tối ưu động từ Bài 8
    quy_dao = {
        'year': list(range(2026, 2036)),
        'GDP': [12848, 33630, 211321, 2098253, 27826671, 454228956, 8697866379, 189318497535, 4581604490825, 121289564918555],
        'AI': [80, 568, 983, 1335, 1635, 1890, 2106, 2290, 2447, 2580],
        'H': [30, 428.6, 820, 1203.6, 1579.6, 1948, 2309, 2662.8, 3009.6, 3349.4]
    }

    current = allocation.get(scenario, allocation["S5"])
    result = {
        'scenario': scenario,
        'name': current['name'],
        'allocation': current,
        'gdp_2030': gdp_scenario.get(scenario, 18000),
        'phan_bo_vung': phan_bo_vung,
        'quy_dao': quy_dao,
        'khuyen_nghi': f"Kịch bản {current['name']} cho GDP 2030 đạt {gdp_scenario.get(scenario, 18000):,} tỷ, cao nhất là S3 (AI dẫn dắt) với 19.200 tỷ"
    }
    return result

def so_sanh_kich_ban():
    """So sánh tất cả 5 kịch bản"""
    results = []
    for s in ["S1", "S2", "S3", "S4", "S5"]:
        m3 = run_m3(s)
        results.append({
            'Kịch bản': m3['name'],
            'Phân bổ (K:D:AI:H)': f"{m3['allocation']['I']}:{m3['allocation']['D']}:{m3['allocation']['AI']}:{m3['allocation']['H']}",
            'GDP 2030 (tỷ)': m3['gdp_2030']
        })
    return results

if __name__ == "__main__":
    print(run_m3("S3"))
    print("\nSO SÁNH 5 KỊCH BẢN:")
    for item in so_sanh_kich_ban():
        print(f"  {item}")

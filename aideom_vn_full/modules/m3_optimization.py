
# modules/m3_optimization.py

def run_m3(scenario="S5"):
    """Chạy module M3 - Tối ưu phân bổ ngân sách"""
    allocation = {
        "S1": {"I": 70, "D": 10, "AI": 10, "H": 10, "name": "Truyền thống"},
        "S2": {"I": 25, "D": 45, "AI": 15, "H": 15, "name": "Số hóa nhanh"},
        "S3": {"I": 20, "D": 20, "AI": 45, "H": 15, "name": "AI dẫn dắt"},
        "S4": {"I": 30, "D": 20, "AI": 10, "H": 40, "name": "Bao trùm số"},
        "S5": {"I": 35, "D": 25, "AI": 25, "H": 15, "name": "Tối ưu cân bằng"}
    }
    gdp_scenario = {"S1": 16500, "S2": 17800, "S3": 19200, "S4": 15800, "S5": 18500}
    vung_phabo = {
        "Vùng": ["Đông Nam Bộ", "Đồng bằng sông Hồng", "Bắc Trung Bộ",
                 "Tây Nguyên", "ĐBSCL", "Trung du miền núi Bắc"],
        "Hạ tầng (I)": [5200, 4800, 3500, 2800, 3200, 2500],
        "AI": [6800, 5200, 2800, 1200, 2500, 1800],
        "Nhân lực (H)": [0, 0, 0, 5000, 0, 3200]
    }
    current = allocation.get(scenario, allocation["S5"])
    return {
        'name': current['name'],
        'allocation': current,
        'gdp_2030': gdp_scenario.get(scenario, 18000),
        'phan_bo_vung': vung_phabo
    }

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

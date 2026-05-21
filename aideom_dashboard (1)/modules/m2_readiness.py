# modules/m2_readiness.py
# M2: ĐÁNH GIÁ SẴN SÀNG SỐ (từ Bài 3,6)
# Tác giả: [Tên bạn]
# Ngày: 2025

import numpy as np
import pandas as pd

def run_m2():
    """
    Chạy module M2 - Đánh giá sẵn sàng số
    Returns:
        dict: {
            'xep_hang': list xếp hạng các ngành,
            'top3': 3 ngành đầu tiên,
            'khuyen_nghi': khuyến nghị chính sách,
            'topsis_6vung': xếp hạng 6 vùng theo TOPSIS
        }
    """
    # === XẾP HẠNG NGÀNH (Bài 3) ===
    data = {
        'sector_name_vi': [
            'CNTT-Truyền thông', 'Tài chính-Ngân hàng', 'CN chế biến chế tạo',
            'Logistics-Vận tải', 'Bán buôn-bán lẻ', 'Giáo dục-Đào tạo',
            'Nông-Lâm-Thủy sản', 'Xây dựng', 'Y tế', 'Khai khoáng'
        ],
        'growth_rate_2024_pct': [7.85, 7.36, 9.64, 9.93, 7.10, 6.42, 3.27, 7.45, 6.85, -1.20],
        'productivity_million_VND': [713.8, 1072.4, 241.2, 321.4, 145.3, 205.7, 103.4, 168.8, 437.1, 1290.5],
        'spillover_coef_0_1': [0.92, 0.85, 0.78, 0.72, 0.55, 0.65, 0.35, 0.42, 0.60, 0.30],
        'export_billion_USD': [178.0, 1.2, 290.9, 3.1, 5.5, 0.0, 40.5, 2.5, 0.0, 8.2],
        'labor_million': [0.62, 0.55, 11.50, 1.95, 7.80, 2.15, 13.20, 4.80, 0.75, 0.30],
        'ai_readiness_0_100': [88, 72, 54, 42, 48, 38, 15, 20, 45, 30],
        'automation_risk_pct': [28, 52, 42, 35, 38, 22, 18, 25, 18, 55]
    }

    df = pd.DataFrame(data)

    # Chuẩn hóa min-max
    def norm_benefit(x): return (x - x.min()) / (x.max() - x.min())
    def norm_cost(x): return (x.max() - x) / (x.max() - x.min())

    cols_benefit = ['growth_rate_2024_pct', 'productivity_million_VND', 'spillover_coef_0_1',
                    'export_billion_USD', 'labor_million', 'ai_readiness_0_100']
    df_norm = df[cols_benefit].apply(norm_benefit)
    df_norm['risk_norm'] = norm_cost(df['automation_risk_pct'])

    # Tính Priority Index
    w = np.array([0.15, 0.15, 0.20, 0.15, 0.10, 0.20])
    priority = df_norm[cols_benefit].values @ w - 0.15 * df_norm['risk_norm'].values
    df['Priority'] = priority
    df_sorted = df.sort_values('Priority', ascending=False).reset_index(drop=True)

    # === XẾP HẠNG 6 VÙNG THEO TOPSIS (Bài 6) ===
    vung_data = {
        'region_name_vi': ['Đông Nam Bộ', 'Đồng bằng sông Hồng', 'Bắc Trung Bộ',
                           'Tây Nguyên', 'ĐBSCL', 'Trung du miền núi Bắc'],
        'grdp_per_capita': [245.8, 185.5, 98.3, 72.5, 92.5, 85.2],
        'fdi': [12.5, 8.5, 2.8, 0.6, 1.8, 1.2],
        'digital_index': [82, 78, 55, 32, 48, 38],
        'ai_readiness': [78, 72, 48, 28, 42, 35],
        'gini': [0.38, 0.35, 0.33, 0.30, 0.34, 0.32]
    }
    df_vung = pd.DataFrame(vung_data)
    criteria = ['grdp_per_capita', 'fdi', 'digital_index', 'ai_readiness', 'gini']
    is_benefit = [True, True, True, True, False]

    X = df_vung[criteria].values.astype(float)
    R = X / np.sqrt((X**2).sum(axis=0))
    w_expert = np.array([0.20, 0.15, 0.25, 0.30, 0.10])
    V = R * w_expert
    A_star = np.where(is_benefit, V.max(axis=0), V.min(axis=0))
    A_neg = np.where(is_benefit, V.min(axis=0), V.max(axis=0))
    S_star = np.sqrt(((V - A_star)**2).sum(axis=1))
    S_neg = np.sqrt(((V - A_neg)**2).sum(axis=1))
    C_star = S_neg / (S_star + S_neg)
    df_vung['TOPSIS'] = C_star
    df_vung_sorted = df_vung.sort_values('TOPSIS', ascending=False).reset_index(drop=True)

    result = {
        'xep_hang_nganh': df_sorted.head(5)[['sector_name_vi', 'Priority']].to_dict('records'),
        'top3_nganh': df_sorted.head(3)['sector_name_vi'].tolist(),
        'xep_hang_vung': df_vung_sorted[['region_name_vi', 'TOPSIS']].to_dict('records'),
        'top1_vung': df_vung_sorted.iloc[0]['region_name_vi'],
        'khuyen_nghi': f"Ưu tiên đầu tư AI cho ngành {df_sorted.iloc[0]['sector_name_vi']} và vùng {df_vung_sorted.iloc[0]['region_name_vi']}"
    }
    return result

if __name__ == "__main__":
    print(run_m2())

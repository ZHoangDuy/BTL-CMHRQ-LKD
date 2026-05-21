# modules/m5_risk.py
# M5: ĐÁNH GIÁ RỦI RO (từ Bài 7,10)
# Tác giả: [Tên bạn]
# Ngày: 2025

import numpy as np
import pandas as pd

def run_m5():
    """
    Chạy module M5 - Đánh giá rủi ro
    Returns:
        dict: {
            'data': so sánh các phương pháp,
            'best_method': phương pháp tốt nhất,
            'best_regret': max regret thấp nhất,
            'khuyen_nghi': khuyến nghị,
            'so_sanh_tradeoff': trade-off giữa các mục tiêu
        }
    """

    # Kết quả từ Bài 7 (Pareto, trade-off)
    tradeoff = {
        'Mục tiêu': ['Tăng trưởng GDP', 'Bất bình đẳng', 'Phát thải', 'Rủi ro an ninh'],
        'Trọng số ưu tiên': [0.40, 0.25, 0.20, 0.15],
        'Mức độ đánh đổi': ['Cao', 'Trung bình', 'Thấp', 'Rất cao']
    }

    # Kết quả từ Bài 10 (Stochastic, EV, Robust)
    risk_data = {
        "Phương pháp": ["Stochastic (SP)", "Expected Value (EV)", "Robust (minimax)"],
        "Max regret (tỷ)": [52250, 44000, 20952],
        "Z* (tỷ)": [98575, 100000, None],
        "Ưu điểm": ["Tối ưu kỳ vọng, tính đến bất định", "Đơn giản, dễ hiểu", "An toàn nhất, bảo vệ kịch bản xấu"],
        "Nhược điểm": ["Rủi ro ở kịch bản xấu", "Không tính đến bất định", "Hy sinh lợi ích kỳ vọng"]
    }

    # EVPI và VSS từ Bài 10
    evpi = 4025  # Expected Value of Perfect Information
    vss = -225   # Value of Stochastic Solution

    result = {
        'data': risk_data,
        'tradeoff': tradeoff,
        'evpi': evpi,
        'vss': vss,
        'best_method': 'Robust (minimax)',
        'best_regret': 20952,
        'khuyen_nghi': f'Nên dùng Robust optimization cho lĩnh vực an ninh quốc gia (max regret thấp nhất: 20.952 tỷ). EVPI = {evpi} tỷ là số tiền tối đa nên chi cho dự báo.'
    }
    return result

if __name__ == "__main__":
    print(run_m5())


# modules/m5_risk.py
import pandas as pd

def run_m5():
    """Chạy module M5 - Đánh giá rủi ro"""
    risk_data = {
        "Phương pháp": ["Stochastic (SP)", "Expected Value (EV)", "Robust (minimax)"],
        "Max regret (tỷ)": [52250, 44000, 20952],
        "Ưu điểm": ["Tối ưu kỳ vọng", "Đơn giản, dễ hiểu", "An toàn nhất"],
        "Nhược điểm": ["Rủi ro ở kịch bản xấu", "Không tính bất định", "Hy sinh lợi ích"]
    }
    return {
        'data': risk_data,
        'best_method': 'Robust (minimax)',
        'best_regret': 20952,
        'khuyen_nghi': 'Nên dùng Robust optimization cho các lĩnh vực an ninh quốc gia'
    }

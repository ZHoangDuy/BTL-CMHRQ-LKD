
# modules/m2_readiness.py
import pandas as pd

def run_m2():
    """Chạy module M2 - Đánh giá sẵn sàng số"""
    nganh = ['CNTT-Truyền thông', 'Tài chính-Ngân hàng', 'CN chế biến chế tạo',
             'Logistics-Vận tải', 'Bán buôn-bán lẻ', 'Giáo dục-Đào tạo',
             'Nông-Lâm-Thủy sản', 'Xây dựng']
    ai_readiness = [88, 72, 54, 42, 48, 38, 15, 20]
    digital_index = [85, 78, 55, 50, 45, 40, 25, 30]

    df = pd.DataFrame({'Ngành': nganh, 'AI Readiness': ai_readiness, 'Digital Index': digital_index})
    df['Tổng điểm'] = df['AI Readiness'] * 0.6 + df['Digital Index'] * 0.4
    df = df.sort_values('Tổng điểm', ascending=False).reset_index(drop=True)

    return {
        'xep_hang': df.to_dict('records'),
        'top3': df.head(3)['Ngành'].tolist(),
        'khuyen_nghi': f"Ưu tiên đầu tư AI cho {df.iloc[0]['Ngành']} và {df.iloc[1]['Ngành']}"
    }


# modules/m4_labor.py
import pandas as pd

def run_m4():
    """Chạy module M4 - Mô phỏng tác động AI lên lao động"""
    laodong_data = {
        "Ngành": ["CN chế biến chế tạo", "Tài chính-Ngân hàng", "CNTT-Truyền thông",
                  "Giáo dục-Đào tạo", "Nông-Lâm-Thủy sản", "Xây dựng"],
        "Mất việc (ngàn)": [125, 45, 28, 12, 85, 62],
        "Việc mới (ngàn)": [180, 95, 210, 45, 65, 55],
        "Rủi ro (%)": [42, 52, 28, 22, 18, 25]
    }
    df = pd.DataFrame(laodong_data)
    df['NetJob (ngàn)'] = df['Việc mới (ngàn)'] - df['Mất việc (ngàn)']

    return {
        'data': df.to_dict('records'),
        'tong_netjob': int(df['NetJob (ngàn)'].sum()),
        'nganh_rui_ro_cao': df.nlargest(2, 'Rủi ro (%)')['Ngành'].tolist(),
        'khuyen_nghi': "Cần đào tạo lại lao động ngành Nông nghiệp và Xây dựng"
    }

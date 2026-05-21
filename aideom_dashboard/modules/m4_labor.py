# modules/m4_labor.py
# M4: MÔ PHỎNG LAO ĐỘNG (từ Bài 9)
# Tác giả: [Tên bạn]
# Ngày: 2025

import numpy as np
import pandas as pd

def run_m4():
    """
    Chạy module M4 - Mô phỏng tác động AI lên thị trường lao động
    Returns:
        dict: {
            'data': dữ liệu từng ngành,
            'tong_netjob': tổng NetJob,
            'nganh_rui_ro_cao': danh sách ngành rủi ro cao,
            'khuyen_nghi': khuyến nghị chính sách,
            'bieu_do': dữ liệu cho biểu đồ
        }
    """

    # Dữ liệu 6 ngành trọng yếu (từ Bài 9)
    laodong_data = {
        "Ngành": ["CN chế biến chế tạo", "Tài chính-Ngân hàng", "CNTT-Truyền thông",
                  "Giáo dục-Đào tạo", "Nông-Lâm-Thủy sản", "Xây dựng"],
        "Lao động (triệu)": [11.50, 0.55, 0.62, 2.15, 13.20, 4.80],
        "Mất việc (ngàn)": [125, 45, 28, 12, 85, 62],
        "Việc mới (ngàn)": [180, 95, 210, 45, 65, 55],
        "Rủi ro (%)": [42, 52, 28, 22, 18, 25]
    }
    df = pd.DataFrame(laodong_data)
    df['NetJob (ngàn)'] = df['Việc mới (ngàn)'] - df['Mất việc (ngàn)']

    # Tính toán thêm
    tong_netjob = int(df['NetJob (ngàn)'].sum())
    ty_le_that_nghiep = (df['Mất việc (ngàn)'].sum() / (df['Lao động (triệu)'].sum() * 1000)) * 100

    result = {
        'data': df.to_dict('records'),
        'tong_netjob': tong_netjob,
        'ty_le_that_nghiep': round(ty_le_that_nghiep, 2),
        'nganh_rui_ro_cao': df.nlargest(2, 'Rủi ro (%)')['Ngành'].tolist(),
        'nganh_netjob_am': df[df['NetJob (ngàn)'] < 0]['Ngành'].tolist(),
        'khuyen_nghi': "Cần đào tạo lại lao động ngành Nông nghiệp và Xây dựng (NetJob âm). Ngành CNTT và Tài chính có thể tận dụng AI để tạo việc làm mới."
    }
    return result

if __name__ == "__main__":
    print(run_m4())

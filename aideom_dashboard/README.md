# AIDEOM-VN Dashboard

## Mô tả
Dashboard mô phỏng và ra quyết định chính sách kinh tế số Việt Nam, tích hợp 5 module M1-M5.

## Cấu trúc
```
modules/
├── m1_forecast.py      # Dự báo kinh tế (Bài 1)
├── m2_readiness.py     # Đánh giá sẵn sàng số (Bài 3,6)
├── m3_optimization.py  # Tối ưu phân bổ (Bài 4,8)
├── m4_labor.py         # Mô phỏng lao động (Bài 9)
└── m5_risk.py          # Đánh giá rủi ro (Bài 7,10)
dashboard.py            # Streamlit dashboard
test_modules.py         # Unit test
```

## Cài đặt
```bash
pip install -r requirements.txt
```

## Chạy dashboard
```bash
streamlit run dashboard.py
```

## Chạy test
```bash
pytest test_modules.py -v
```

## Nguồn dữ liệu
- Tổng cục Thống kê Việt Nam (GSO) 2020-2025
- Bộ Khoa học và Công nghệ (MoST)
- Ngân hàng Thế giới (WB)

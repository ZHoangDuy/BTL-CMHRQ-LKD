# AIDEOM-VN Dashboard

## Mo ta
Dashboard mo phong va ra quyet dinh chinh sach kinh te so Viet Nam, tich hop 5 module M1-M5.

## Sinh vien
- **Ho ten:** Le Khương Duy
- **Ma so sinh vien:** 23051211
- **Hoc phan:** Cac mo hinh ra quyet dinh

## Cau truc du an
```
aideom_vn/
├── data/
│   ├── vietnam_macro_2020_2025.csv
│   ├── vietnam_sectors_2024.csv
│   └── vietnam_regions_2024.csv
├── modules/
│   ├── m1_forecast.py
│   ├── m2_readiness.py
│   ├── m3_optimization.py
│   ├── m4_labor.py
│   └── m5_risk.py
├── dashboard.py
├── test_modules.py
├── requirements.txt
└── README.md
```

## Cai dat
```bash
pip install -r requirements.txt
```

## Chay dashboard
```bash
streamlit run dashboard.py
```

## Chay test
```bash
pytest test_modules.py -v
```

## Nguon du lieu
- Tong cuc Thong ke Viet Nam (GSO) 2020-2025
- Bo Khoa hoc va Cong nghe (MoST)
- Ngan hang The gioi (WB)

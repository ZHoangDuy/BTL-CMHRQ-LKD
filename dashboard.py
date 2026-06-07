import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('.')

from modules import run_m1, run_m2, run_m3, run_m4, run_m5, so_sanh_kich_ban

# Dữ liệu
DATA = {
    "bai1": {"A": [27.7466,28.7638,30.3501,30.9751,32.9171,34.9136], "Agrowth":4.7, "Amean":30.944, "Y2030":16328.8, "decomp":[["TFP",49.08],["Vốn K",31.78],["Lao động L",-0.34],["Số hóa D",10.37],["AI",6.24],["Nhân lực H",2.87]]},
    "bai2": {"x":[25,15,20,40],"Z":112.25},
    "bai3": {"ranking":[["CNTT-Truyền thông",0.7327],["CN chế biến",0.6536],["Tài chính",0.5486],["Y tế",0.4535],["Logistics",0.4332],["Giáo dục",0.4014],["Bán buôn",0.3797],["Nông nghiệp",0.3157],["Xây dựng",0.3049],["Khai khoáng",0.1776]]},
    "bai4": {"region_names":["Trung du miền núi","ĐB sông Hồng","Bắc Trung Bộ","Tây Nguyên","Đông Nam Bộ","ĐB sông Cửu Long"], "matrix":[[0,5600,0,0],[0,0,11200,0],[0,0,0,5000],[0,8600,0,2600],[0,0,12000,0],[0,600,0,4400]]},
    "bai5": {"selected":[2,5,7,8,9,10,12,14,15],"Z":115400,"cost":59700},
    "bai6": {"region_names":["Trung du","ĐB sông Hồng","Bắc Trung Bộ","Tây Nguyên","Đông Nam Bộ","ĐB sông Cửu Long"], "expert":[0.0993,0.8981,0.3597,0.0312,0.9402,0.171]},
    "bai7": {"compromise":{"f1":51660,"f2":549.7,"f3":8786,"f4":-5911,"C":0.7281}},
    "bai8": {"years":[2026,2027,2028,2029,2030,2031,2032,2033,2034,2035], "Y":[12848,24023,28821,33411,38683,45143,53263,63594,76837,93914], "C":[10748,21923,26721,31311,36583,43043,51163,61494,74737,91814]},
    "bai9": {"sectors":["Nông-LT","CN chế biến","Xây dựng","Bán buôn","Tài chính","Logistics","CNTT","Giáo dục"], "netjob":[67500,42000,52500,48000,33000,45000,66326,1072500]},
    "bai10": {"Zsp":98575,"VSS":0,"EVPI":0},
    "bai11": {"policies":[{"desc":"VN 2026 thực tế","state":"GDP TB, Số hóa TB, AI thấp, Nhân lực TB","action":"Số hóa nhanh","Q":2.525}]}
}

st.set_page_config(page_title="AIDEOM-VN", layout="wide")
st.title("AIDEOM-VN")
st.caption("Chuyên khảo · Mô hình ra quyết định cho kinh tế Việt Nam thời đại AI")

with st.sidebar:
    st.markdown("### DIEU KHIEN")
    st.markdown("---")
    st.markdown("**Sinh Viên:** Lê Khương Duy")
    st.markdown("**Mã sinh viên:** 23051211")
    st.markdown("**Học Phần:** Các Mô Hình Ra Quyết Định")
    st.markdown("---")
    pages = ["Tổng quan", "Bài 1", "Bài 2", "Bài 3", "Bài 4", "Bài 5", "Bài 6", "Bài 7", "Bài 8", "Bài 9", "Bài 10", "Bài 11", "Bài 12"]
    selected_page = st.radio("", pages, index=0)
    st.markdown("---")
    st.caption("AIDEOM-VN Dashboard")

# ==================== TỔNG QUAN ====================
if selected_page == "Tổng quan":
    st.header("Phát triển kinh tế Việt Nam trong kỉ nguyên AI")
    col1,col2,col3,col4 = st.columns(4)
    with col1: st.metric("GDP 2025", "12.847,6 tỷ", "+8.02%")
    with col2: st.metric("Kinh tế số/GDP", "19.5%", "+1.2%")
    with col3: st.metric("FDI 2025", "27,6 tỷ USD", "+8.9%")
    with col4: st.metric("GDP/người", "5.026 USD", "+6.9%")
    m1 = run_m1()
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(m1['years'], m1['GDP'], 'bo-', linewidth=2)
    ax.fill_between(m1['years'], m1['GDP'], alpha=0.3)
    ax.set_xlabel("Năm")
    ax.set_ylabel("GDP (nghìn tỷ)")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

# ==================== BÀI 1 ====================
elif selected_page == "Bài 1":
    b1 = DATA["bai1"]
    st.header("Hàm sản xuất Cobb-Douglas mở rộng")
    col1,col2,col3,col4 = st.columns(4)
    with col1: st.metric("TFP 2025", f"{b1['A'][-1]:.2f}")
    with col2: st.metric("TFP tăng", f"{b1['Agrowth']:.1f}%/năm")
    with col3: st.metric("GDP 2030", f"{b1['Y2030']:.0f} tỷ")
    with col4: st.metric("TFP tb", f"{b1['Amean']:.3f}")
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot([2020,2021,2022,2023,2024,2025], b1['A'], 'ro-', linewidth=2)
    ax.fill_between([2020,2021,2022,2023,2024,2025], b1['A'], alpha=0.3)
    ax.set_xlabel("Năm")
    ax.set_ylabel("TFP")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    st.subheader("Phân rã đóng góp vào tăng trưởng GDP")
    decomp_data = b1['decomp']
    fig, ax = plt.subplots()
    ax.bar([d[0] for d in decomp_data], [d[1] for d in decomp_data])
    ax.set_ylabel("Đóng góp (điểm %/năm)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ==================== BÀI 2 ====================
elif selected_page == "Bài 2":
    b2 = DATA["bai2"]
    st.header("Phân bổ ngân sách 4 hạng mục")
    col1,col2,col3,col4 = st.columns(4)
    with col1: st.metric("Z*", f"{b2['Z']:.2f}")
    with col2: st.metric("R&D", f"{b2['x'][3]:.0f}")
    with col3: st.metric("AI+R&D", "55%")
    with col4: st.metric("Shadow price", "1.35")
    labels = ["Hạ tầng", "AI", "Nhân lực", "R&D"]
    fig, ax = plt.subplots()
    ax.bar(labels, b2['x'], color=['#3498db','#2ecc71','#e74c3c','#f39c12'])
    ax.set_ylabel("Nghìn tỷ")
    st.pyplot(fig)

# ==================== BÀI 3 ====================
elif selected_page == "Bài 3":
    b3 = DATA["bai3"]
    st.header("Chỉ số ưu tiên ngành Priority")
    df = pd.DataFrame(b3['ranking'], columns=["Ngành", "Priority"])
    st.dataframe(df, use_container_width=True)

# ==================== BÀI 4 ====================
elif selected_page == "Bài 4":
    b4 = DATA["bai4"]
    st.header("LP phân bổ ngân sách theo vùng")
    df = pd.DataFrame(b4['matrix'], index=b4['region_names'], columns=["I","D","AI","H"])
    st.dataframe(df, use_container_width=True)

# ==================== BÀI 5 ====================
elif selected_page == "Bài 5":
    b5 = DATA["bai5"]
    st.header("MIP chọn dự án")
    col1,col2,col3 = st.columns(3)
    with col1: st.metric("Z*", f"{b5['Z']:,} tỷ")
    with col2: st.metric("Chi phí", f"{b5['cost']:,} tỷ")
    with col3: st.metric("Số dự án", f"{len(b5['selected'])}")
    st.write("Dự án chọn:", b5['selected'])

# ==================== BÀI 6 ====================
elif selected_page == "Bài 6":
    b6 = DATA["bai6"]
    st.header("TOPSIS xếp hạng 6 vùng")
    df = pd.DataFrame(list(zip(b6['region_names'], b6['expert'])), columns=["Vùng", "C*"])
    st.dataframe(df, use_container_width=True)

# ==================== BÀI 7 ====================
elif selected_page == "Bài 7":
    b7 = DATA["bai7"]
    st.header("NSGA-II đa mục tiêu Pareto")
    col1,col2 = st.columns(2)
    with col1: st.metric("GDP gain", f"{b7['compromise']['f1']:,} tỷ")
    with col2: st.metric("Gini", f"{b7['compromise']['f2']}")
    st.info(f"C* = {b7['compromise']['C']:.4f}")

# ==================== BÀI 8 ====================
elif selected_page == "Bài 8":
    b8 = DATA["bai8"]
    st.header("Tối ưu động")
    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(b8['years'], b8['Y'], 'b-', linewidth=2, label="GDP")
    ax.plot(b8['years'], b8['C'], 'r--', linewidth=2, label="Tiêu dùng")
    ax.set_xlabel("Năm")
    ax.set_ylabel("Nghìn tỷ")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

# ==================== BÀI 9 ====================
elif selected_page == "Bài 9":
    b9 = DATA["bai9"]
    st.header("Tác động AI lên lao động")
    df = pd.DataFrame({"Ngành": b9['sectors'], "NetJob": b9['netjob']})
    st.dataframe(df, use_container_width=True)

# ==================== BÀI 10 ====================
elif selected_page == "Bài 10":
    b10 = DATA["bai10"]
    st.header("Quy hoạch ngẫu nhiên")
    col1,col2,col3 = st.columns(3)
    with col1: st.metric("Z*_SP", f"{b10['Zsp']:,} tỷ")
    with col2: st.metric("VSS", f"{b10['VSS']:,} tỷ")
    with col3: st.metric("EVPI", f"{b10['EVPI']:,} tỷ")

# ==================== BÀI 11 ====================
elif selected_page == "Bài 11":
    b11 = DATA["bai11"]
    st.header("Q-learning")
    for p in b11['policies']:
        st.write(f"**{p['desc']}** - {p['action']} (Q={p['Q']:.3f})")
        st.caption(p['state'])
        st.markdown("---")

# ==================== BÀI 12 ====================
else:
    st.header("AIDEOM-VN — Nguyên mẫu tích hợp 6 module")
    st.subheader("Quỹ đạo GDP 5 kịch bản")
    years_scenario = [2026,2027,2028,2029,2030]
    scenarios_gdp = {
        "S1: Truyền thống": [15420,15890,16380,16890,17420],
        "S2: Số hóa nhanh": [16180,16650,17120,17600,18100],
        "S3: AI dẫn dắt": [16780,17300,17850,18420,19000],
        "S4: Bao trùm số": [15890,16320,16780,17250,17730],
        "S5: Tối ưu": [16520,17000,17500,18020,18550]
    }
    fig, ax = plt.subplots(figsize=(12,5))
    colors_list = ['#95a5a6','#3498db','#2ecc71','#e74c3c','#f39c12']
    for i, (name, data) in enumerate(scenarios_gdp.items()):
        ax.plot(years_scenario, data, 'o-', linewidth=2, color=colors_list[i], label=name)
    ax.set_xlabel("Năm")
    ax.set_ylabel("GDP (nghìn tỷ)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    st.subheader("So sánh KPI 5 kịch bản 2030")
    df_scenarios = pd.DataFrame({
        "Kịch bản": ["S1: Truyền thống", "S2: Số hóa nhanh", "S3: AI dẫn dắt", "S4: Bao trùm số", "S5: Tối ưu"],
        "GDP (tỷ)": [15420,16180,16780,15890,16520],
        "NetJob (tr)": [0.8,1.2,0.9,1.4,1.3],
        "Gini": [0.375,0.392,0.418,0.348,0.365]
    })
    st.dataframe(df_scenarios, use_container_width=True)
    
    st.info("**Kết luận:** S3 (AI dẫn dắt) cho GDP cao nhất nhưng Gini xấu nhất. S5 (Tối ưu) cân bằng các mục tiêu.")

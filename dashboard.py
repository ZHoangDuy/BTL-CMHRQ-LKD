
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('.')

from modules import run_m1, run_m2, run_m3, run_m4, run_m5

st.set_page_config(page_title="AIDEOM-VN Dashboard", layout="wide")
st.title("📊 AIDEOM-VN: Mô hình ra quyết định kinh tế số Việt Nam")
st.markdown("---")

# ==========================================
# SIDEBAR - CHỌN KỊCH BẢN
# ==========================================
st.sidebar.header("📌 ĐIỀU KHIỂN")

# Định nghĩa 5 kịch bản
kich_ban_list = {
    "S1": {"name": "Truyền thống", "K": 70, "D": 10, "AI": 10, "H": 10},
    "S2": {"name": "Số hóa nhanh", "K": 25, "D": 45, "AI": 15, "H": 15},
    "S3": {"name": "AI dẫn dắt", "K": 20, "D": 20, "AI": 45, "H": 15},
    "S4": {"name": "Bao trùm số", "K": 30, "D": 20, "AI": 10, "H": 40},
    "S5": {"name": "Tối ưu cân bằng", "K": 35, "D": 25, "AI": 25, "H": 15}
}

# GDP 2030 theo từng kịch bản (nghìn tỷ)
gdp_2030_theo_kb = {"S1": 16500, "S2": 17800, "S3": 19200, "S4": 15800, "S5": 18500}
netjob_theo_kb = {"S1": 850, "S2": 1200, "S3": 1500, "S4": 950, "S5": 1350}
phat_thai_theo_kb = {"S1": 12500, "S2": 10800, "S3": 9500, "S4": 11200, "S5": 10200}

# Chọn kịch bản
selected = st.sidebar.selectbox(
    "Chọn kịch bản chính sách",
    ["S1: Truyền thống", "S2: Số hóa nhanh", "S3: AI dẫn dắt", "S4: Bao trùm số", "S5: Tối ưu cân bằng"],
    index=4
)
kb_code = selected.split(":")[0]
kb_name = kich_ban_list[kb_code]["name"]

# Lấy dữ liệu theo kịch bản
gdp_2030 = gdp_2030_theo_kb[kb_code]
netjob = netjob_theo_kb[kb_code]
phat_thai = phat_thai_theo_kb[kb_code]

st.sidebar.markdown("---")
st.sidebar.caption(f"📌 Kịch bản hiện tại: **{kb_name}**")
st.sidebar.caption("AIDEOM-VN Dashboard | Dữ liệu Việt Nam 2020-2025")

# ==========================================
# MAIN CONTENT - 5 TAB
# ==========================================
tab_choice = st.sidebar.radio(
    "Chọn mục:",
    ["📈 Tổng quan", "💰 Phân bổ", "⚖️ So sánh kịch bản", "⚠️ Rủi ro", "👥 Lao động"],
    index=0
)

# ==================== TAB 1: TỔNG QUAN ====================
if tab_choice == "📈 Tổng quan":
    st.header("📈 Tổng quan kinh tế vĩ mô")
    
    m1_result = run_m1()
    m2_result = run_m2()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("GDP 2025", f"{m1_result['GDP_2025']:,.0f} tỷ VND")
    col2.metric(f"GDP 2030 ({kb_name})", f"{gdp_2030:,} tỷ VND", 
                delta=f"+{((gdp_2030/m1_result['GDP_2025'])**0.2-1)*100:.1f}%/năm")
    col3.metric("TFP 2025", f"{m1_result['TFP'][-1]:.4f}")
    col4.metric("TFP tăng trưởng", f"{m1_result['TFP_growth']:.2f}%/năm")
    
    # Biểu đồ GDP
    st.subheader("GDP Việt Nam 2020-2025")
    fig1, ax1 = plt.subplots()
    ax1.plot(m1_result['years'], m1_result['GDP'], 'bo-', linewidth=2, markersize=8)
    ax1.set_xlabel("Năm")
    ax1.set_ylabel("GDP (nghìn tỷ VND)")
    ax1.grid(True, alpha=0.3)
    st.pyplot(fig1)
    
    # Phân rã tăng trưởng
    st.subheader("📊 Phân rã đóng góp vào tăng trưởng GDP")
    phan_ra = m1_result['phan_ra']
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    categories = list(phan_ra.keys())
    values = list(phan_ra.values())
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    ax2.bar(categories, values, color=colors)
    ax2.set_ylabel("Đóng góp (điểm % / năm)")
    ax2.set_title("Phân rã tăng trưởng GDP bình quân 2021-2025")
    ax2.tick_params(axis='x', rotation=45)
    for bar, val in zip(ax2.patches, values):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f'{val:.2f}%', ha='center', va='bottom', fontsize=9)
    st.pyplot(fig2)
    
    # Xếp hạng sẵn sàng số (LỖI ĐÃ SỬA)
    st.subheader("🏆 Xếp hạng sẵn sàng số theo ngành")
    # Kiểm tra key đúng
    if 'xep_hang_nganh' in m2_result:
        st.dataframe(pd.DataFrame(m2_result['xep_hang_nganh']), use_container_width=True)
    elif 'xep_hang' in m2_result:
        st.dataframe(pd.DataFrame(m2_result['xep_hang']), use_container_width=True)
    else:
        st.warning("Không có dữ liệu xếp hạng")
    st.info(f"💡 **Khuyến nghị:** {m2_result['khuyen_nghi']}")

# ==================== TAB 2: PHÂN BỔ ====================
elif tab_choice == "💰 Phân bổ":
    st.header("💰 Phân bổ ngân sách theo kịch bản")
    
    st.info(f"📌 **Kịch bản hiện tại: {kb_name}**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tỷ lệ phân bổ quốc gia")
        labels = ['Hạ tầng (I)', 'Chuyển đổi số (D)', 'AI', 'Nhân lực (H)']
        sizes = [kich_ban_list[kb_code]["K"], kich_ban_list[kb_code]["D"], 
                 kich_ban_list[kb_code]["AI"], kich_ban_list[kb_code]["H"]]
        colors_alloc = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12']
        fig_pie, ax_pie = plt.subplots()
        ax_pie.pie(sizes, labels=labels, colors=colors_alloc, autopct='%1.0f%%', startangle=90)
        ax_pie.set_title(f"Phân bổ ngân sách - {kb_name}")
        st.pyplot(fig_pie)
    
    with col2:
        st.subheader("Kết quả dự báo 2030")
        st.metric("GDP 2030", f"{gdp_2030:,} tỷ VND")
        st.metric("NetJob", f"{netjob:,} ngàn việc làm")
        st.metric("Phát thải", f"{phat_thai:,} kt CO2")
    
    # Phân bổ theo vùng
    st.subheader("Phân bổ ngân sách theo vùng (nghìn tỷ VND)")
    df_vung = pd.DataFrame({
        "Vùng": ["Đông Nam Bộ", "Đồng bằng sông Hồng", "Bắc Trung Bộ", "Tây Nguyên", "ĐBSCL", "Trung du miền núi Bắc"],
        "Hạ tầng (I)": [5200, 4800, 3500, 2800, 3200, 2500],
        "AI": [6800, 5200, 2800, 1200, 2500, 1800],
        "Nhân lực (H)": [0, 0, 0, 5000, 0, 3200]
    })
    st.dataframe(df_vung, use_container_width=True)

# ==================== TAB 3: SO SÁNH KỊCH BẢN ====================
elif tab_choice == "⚖️ So sánh kịch bản":
    st.header("⚖️ So sánh 5 kịch bản chính sách (Kết quả 2030)")
    
    # Bảng tổng hợp 5 kịch bản
    st.subheader("📊 Bảng tổng hợp kết quả 2030")
    df_compare = pd.DataFrame({
        "Kịch bản": ["S1: Truyền thống", "S2: Số hóa nhanh", "S3: AI dẫn dắt", "S4: Bao trùm số", "S5: Tối ưu cân bằng"],
        "Phân bổ (K:D:AI:H)": ["70:10:10:10", "25:45:15:15", "20:20:45:15", "30:20:10:40", "35:25:25:15"],
        "GDP 2030 (tỷ VND)": [16500, 17800, 19200, 15800, 18500],
        "NetJob (ngàn)": [850, 1200, 1500, 950, 1350],
        "Phát thải (kt CO2)": [12500, 10800, 9500, 11200, 10200]
    })
    st.dataframe(df_compare, use_container_width=True)
    
    # Biểu đồ GDP
    col1, col2 = st.columns(2)
    with col1:
        fig_gdp, ax_gdp = plt.subplots(figsize=(8, 5))
        bars = ax_gdp.bar(df_compare['Kịch bản'], df_compare['GDP 2030 (tỷ VND)'], color=['#95a5a6', '#3498db', '#2ecc71', '#e74c3c', '#f39c12'])
        ax_gdp.set_ylabel("GDP (nghìn tỷ VND)")
        ax_gdp.set_title("So sánh GDP 2030")
        ax_gdp.tick_params(axis='x', rotation=45)
        for bar, val in zip(bars, df_compare['GDP 2030 (tỷ VND)']):
            ax_gdp.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100, f'{val:,}', ha='center', fontsize=9)
        st.pyplot(fig_gdp)
    
    with col2:
        fig_net, ax_net = plt.subplots(figsize=(8, 5))
        bars = ax_net.bar(df_compare['Kịch bản'], df_compare['NetJob (ngàn)'], color='orange')
        ax_net.set_ylabel("NetJob (ngàn việc làm)")
        ax_net.set_title("So sánh NetJob 2030")
        ax_net.tick_params(axis='x', rotation=45)
        for bar, val in zip(bars, df_compare['NetJob (ngàn)']):
            ax_net.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20, f'{val:,}', ha='center', fontsize=9)
        st.pyplot(fig_net)
    
    st.info("💡 **Khuyến nghị:** S3 (AI dẫn dắt) cho GDP cao nhất nhưng cần đào tạo lại lao động.")

# ==================== TAB 4: RỦI RO ====================
elif tab_choice == "⚠️ Rủi ro":
    st.header("⚠️ Đánh giá rủi ro từ mô hình Stochastic và Robust")
    
    m5_result = run_m5()
    
    st.dataframe(pd.DataFrame(m5_result['data']), use_container_width=True)
    
    fig_reg, ax_reg = plt.subplots(figsize=(10, 5))
    methods = m5_result['data']['Phương pháp']
    regrets = m5_result['data']['Max regret (tỷ)']
    ax_reg.bar(methods, regrets, color=['#3498db', '#e74c3c', '#2ecc71'])
    ax_reg.set_ylabel("Max regret (tỷ VND)")
    ax_reg.set_title("So sánh Maximum Regret")
    for i, val in enumerate(regrets):
        ax_reg.text(i, val + 500, f'{val:,}', ha='center', fontsize=10)
    st.pyplot(fig_reg)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("EVPI", f"{m5_result['evpi']:,} tỷ VND")
        st.caption("Giá trị thông tin hoàn hảo")
    with col2:
        st.metric("VSS", f"{m5_result['vss']:,} tỷ VND")
        st.caption("Giá trị mô hình ngẫu nhiên")
    
    st.success(f"💡 {m5_result['khuyen_nghi']}")

# ==================== TAB 5: LAO ĐỘNG ====================
else:
    st.header("👥 Tác động AI lên thị trường lao động")
    
    m4_result = run_m4()
    df_ld = pd.DataFrame(m4_result['data'])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Tổng lao động", f"{df_ld['Lao động (triệu)'].sum():.1f} triệu")
    col2.metric("Tổng NetJob", f"{m4_result['tong_netjob']:,} ngàn")
    col3.metric("Net ròng", f"{df_ld['NetJob (ngàn)'].sum():,} ngàn")
    
    st.dataframe(df_ld, use_container_width=True)
    
    fig, ax = plt.subplots(figsize=(12, 5))
    x = range(len(df_ld['Ngành']))
    width = 0.35
    ax.bar([i - width/2 for i in x], df_ld['Mất việc (ngàn)'], width, label="Mất việc", color='red')
    ax.bar([i + width/2 for i in x], df_ld['Việc mới (ngàn)'], width, label="Việc mới", color='green')
    ax.set_xlabel("Ngành")
    ax.set_ylabel("Số lượng (ngàn)")
    ax.set_title("So sánh mất việc vs việc mới")
    ax.set_xticks(x)
    ax.set_xticklabels(df_ld['Ngành'], rotation=45, ha='right')
    ax.legend()
    st.pyplot(fig)
    
    if m4_result.get('nganh_rui_ro_cao'):
        st.warning(f"⚠️ Rủi ro cao: {', '.join(m4_result['nganh_rui_ro_cao'])}")
    st.info(f"💡 {m4_result['khuyen_nghi']}")

st.markdown("---")
st.caption("AIDEOM-VN Dashboard | Nguồn: Tổng cục Thống kê Việt Nam")

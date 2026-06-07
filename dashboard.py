import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('.')

from modules import run_m1, run_m2, run_m3, run_m4, run_m5, so_sanh_kich_ban

st.set_page_config(page_title="AIDEOM-VN", layout="wide")
st.title("AIDEOM-VN")
st.caption("Chuyên khảo · Mô hình ra quyết định cho kinh tế Việt Nam thời đại AI")

with st.sidebar:
    st.markdown("### DIEU KHIEN")
    st.markdown("---")
    st.markdown("**Sinh Viên:** Lê Khương Duy")
    st.markdown("**Mã sinh viên:** 23051211")
    st.markdown("---")
    pages = ["Tong quan", "Bai 1", "Bai 2", "Bai 3", "Bai 4", "Bai 5", "Bai 6", "Bai 7", "Bai 8", "Bai 9", "Bai 10", "Bai 11", "Bai 12"]
    selected_page = st.radio("", pages, index=0)
    st.caption("AIDEOM-VN Dashboard")

if selected_page == "Tong quan":
    st.header("Tong quan")
    m1 = run_m1()
    st.metric("GDP 2025", f"{m1['GDP_2025']:.0f} ty")

elif selected_page == "Bai 1":
    st.header("Bai 1")
    m1 = run_m1()
    st.metric("GDP 2030", f"{m1['GDP_2030']:.0f} ty")

elif selected_page == "Bai 2":
    st.header("Bai 2")
    from modules.m3_optimization import run_m3
    m3 = run_m3("S1")
    st.metric("GDP 2030 S1", f"{m3['gdp_2030']:,} ty")

elif selected_page == "Bai 3":
    st.header("Bai 3")
    m2 = run_m2()
    st.dataframe(pd.DataFrame(m2['xep_hang']))

elif selected_page == "Bai 4":
    st.header("Bai 4")
    st.info("Xem module m4")

elif selected_page == "Bai 5":
    st.header("Bai 5")
    st.info("Xem module m5")

elif selected_page == "Bai 6":
    st.header("Bai 6")
    st.info("Xem module m6")

elif selected_page == "Bai 7":
    st.header("Bai 7")
    st.info("Xem module m7")

elif selected_page == "Bai 8":
    st.header("Bai 8")
    st.info("Xem module m8")

elif selected_page == "Bai 9":
    st.header("Bai 9")
    st.info("Xem module m9")

elif selected_page == "Bai 10":
    st.header("Bai 10")
    st.info("Xem module m10")

elif selected_page == "Bai 11":
    st.header("Bai 11")
    st.info("Xem module m11")

elif selected_page == "Bai 12":
    st.header("Bai 12")
    st.info("Xem module m12")

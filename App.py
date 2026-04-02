import streamlit as st

# 1. Page Config
st.set_page_config(page_title="برو بيت ماستر", layout="wide")

# 2. Custom CSS for Arabic Support and Colors
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    h1, h2, h3 { color: #FF0000 !important; text-align: right; }
    div[data-testid="stVerticalBlock"] { text-align: right; direction: rtl; }
    .stSidebar { direction: rtl; }
    </style>
    """, unsafe_allow_index=True)

# 3. Sidebar Navigation
st.sidebar.title("🏆 القائمة")
selection = st.sidebar.radio("اذهب إلى:", ["الرئيسية", "توقعات مجانية"])

# 4. Content Logic
if selection == "الرئيسية":
    st.title("🏆 برو بيت ماستر")
    st.write("منصة التحليل الرياضي الاحترافية.")
else:
    st.header("⚽ توقعات اليوم")
    st.success("مباراة اليوم: ريال مدريد 🆚 برشلونة -> أكثر من 1.5 هدف")

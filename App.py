import streamlit as st

# 1. Page Config
st.set_page_config(page_title="برو بيت ماستر", layout="wide")

# 2. Custom CSS for Arabic Support and Colors
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    h1, h2, h3 { color: #FF0000 !important; text-align: right; }
    .stButton>button { background-color: #FF0000; color: white; border-radius: 10px; width: 100%; }
    /* Right to Left for Arabic */
    div[data-testid="stVerticalBlock"] { text-align: right; direction: rtl; }
    .stSidebar { direction: rtl; }
    </style>
    """, unsafe_allow_index=True)

# 3. Sidebar Navigation
st.sidebar.title("🏆 القائمة الرئيسية")
nav_options = ["الصفحة الرئيسية", "توقعات مجانية (10+)", "منطقة VIP 💎", "نتائج مباشرة"]
selection = st.sidebar.radio("اذهب إلى:", nav_options)

# 4. Content Logic
if selection == "الصفحة الرئيسية":
    st.title("🏆 برو بيت ماستر - Pro Bet Master")
    st.subheader("مرحباً بك في منصتك الاحترافية للتحليل الرياضي")
    st.write("نحن نعتمد على أحدث النماذج الرياضية والإحصائيات لتقديم أدق التوقعات في عالم كرة القدم.")
    st.divider()
    st.info("اكتشف توقعاتنا المجانية اليوم من القائمة الجانبية.")

elif selection == "توقعات مجانية (10+)":
    st.header("⚽ توقعات اليوم المجانية")
    st.write("قائمة بـ 10 مباريات مختارة بعناية:")
    
    # List of matches
    matches_list = [
        "1. ليفربول 🆚 ريال مدريد -> أكثر من 1.5 هدف",
        "2. بايرن ميونخ 🆚 باريس سان جيرمان -> فوز البايرن",
        "3. مانشستر سيتي 🆚 إنتر ميلان -> فوز السيتي",
        "4. برشلونة 🆚 بوروسيا دورتموند -> أكثر من 2.5 هدف",
        "5. أرسنال 🆚 ميلان -> كلا الفريقين يسجلان",
        "6. الوداد الرياضي 🆚 الرجاء الرياضي -> تعادل أو فوز الوداد",
        "7. يوفنتوس 🆚 أتلتيكو مدريد -> أقل من 2.5 هدف",
        "8. باير ليفركوزن 🆚 لايبزيغ -> أكثر من 1.5 هدف",
        "9. أياكس 🆚 بنفيكا -> كلا الفريقين يسجلان",
        "10. نابولي 🆚 روما -> فوز نابولي"
    ]
    
    for match in matches_list:
        st.success(match)

elif selection == "منطقة VIP 💎":
    st.header("🔐 ركن المشتركين VIP")
    st.write("هذا القسم مخصص للمباريات ذات نسبة النجاح العالية جداً.")
    
    user_password = st.text_input("أدخل القن السري للدخول:", type="password")
    
    if user_password == "2026":
        st.balloons()
        st.warning("🔥 التوقع الماسي اليوم: ريال مدريد 🆚 مان سيتي -> فوز ريال مدريد (DNB)")
        st.write("حظ موفق لجميع المشتركين!")
    elif user_password != "":
        st.error("القن السري خاطئ! المرجو التواصل مع الإدارة.")

elif selection == "نتائج مباشرة":
    st.header("⏱️ تتبع النتائج المباشرة")
    st.info("هذا القسم قيد التطوير وسيتم ربطه بـ API النتائج قريباً.")


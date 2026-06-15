import streamlit as st
import pandas as pd
import numpy as np
import datetime

# ==========================================
# 1. تهيئة الإعدادات العامة للموقع والطابع البصري
# ==========================================
st.set_page_config(
    page_title="منظومة إدارة الأعمال الرقمية",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تطبيق الطابع العصري الفاخر (أسود، أبيض، رمادي) مستوحى من البوابات الرسمية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
        direction: rtl;
    }
    .main-title {
        color: #1a1a1a;
        font-weight: 700;
        border-bottom: 3px solid #1a1a1a;
        padding-bottom: 10px;
        margin-bottom: 25px;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e0e0e0;
        margin-bottom: 15px;
    }
    .metric-box {
        background: linear-gradient(135deg, #1a1a1a 0%, #333333 100%);
        color: white;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
    }
    .stButton>button {
        background-color: #1a1a1a;
        color: white;
        border-radius: 5px;
        border: none;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #444444;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_index=True)

# ==========================================
# 2. إدارة البيانات الافتراضية (Session State)
# ==========================================
if 'employees' not in st.session_state:
    st.session_state.employees = [
        {"id": 1, "name": "أحمد العلوي", "group": "الدعم الفني", "location": "عن بُعد"},
        {"id": 2, "name": "سارة Mسرورية", "group": "الرقابة الإدارية", "location": "المقر الرئيسي"},
        {"id": 3, "name": "سالم البلوشي", "group": "الدعم الفني", "location": "ميداني"},
    ]

if 'tasks' not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "مراجعة السجلات الصادرة", "emp": "أحمد العلوي", "period": "يومية", "priority": "عالي", "status": "قيد التنفيذ"},
        {"id": 2, "title": "إعداد التقرير الدوري للمؤشرات", "emp": "سارة Mسرورية", "period": "أسبوعية", "priority": "متوسط", "status": "مكتمل"},
    ]

if 'announcement' not in st.session_state:
    st.session_state.announcement = "مرحباً بكم في المنظومة الرقمية لإدارة الأعمال اليومية. يرجى تحديث حالات المهام دورياً لضمان كفاءة سير العمل المرن."

if 'banner_link' not in st.session_state:
    st.session_state.banner_link = "https://portal.sjc.gov.om"

# ==========================================
# 3. القائمة الجانبية والتنقل (Sidebar Tabs)
# ==========================================
st.sidebar.title("لوحة التحكم للمسؤول")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "انتقل بين الأقسام:",
    ["🏠 الصفحة الرئيسية", "📅 توزيع وإدارة المهام", "💬 مركز المراسلات الذكي", "👥 إدارة الكادر البشري", "📊 التحليلات وقياس الأداء"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 نظام مخصص ومتوافق مع شاشات الهواتف الذكية وأجهزة iPhone.")

# ==========================================
# 4. محتوى الصفحات والأقسام
# ==========================================

# --- القسم الأول: الصفحة الرئيسية ---
if menu == "🏠 الصفحة الرئيسية":
    st.markdown("<h1 class='main-title'>🏠 الواجهة الرئيسية
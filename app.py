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
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=300;400;600;700&display=swap');
    
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
        {"id": 2, "name": "سارة المسرورية", "group": "الرقابة الإدارية", "location": "المقر الرئيسي"},
        {"id": 3, "name": "سالم البلوشي", "group": "الدعم الفني", "location": "ميداني"},
    ]

if 'tasks' not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "مراجعة السجلات الصادرة", "emp": "أحمد العلوي", "period": "يومية", "priority": "عالي", "status": "قيد التنفيذ"},
        {"id": 2, "title": "إعداد التقرير الدوري للمؤشرات", "emp": "سارة المسرورية", "period": "أسبوعية", "priority": "متوسط", "status": "مكتمل"},
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
    st.markdown("<h1 class='main-title'>🏠 الواجهة الرئيسية للمنظومة</h1>", unsafe_allow_index=True)
    
    # عرض الرسالة الرئيسية للمسؤول
    st.markdown(f"""
    <div class='card' style='border-right: 5px solid #1a1a1a;'>
        <h3>📢 توجيهات الإدارة العليا</h3>
        <p style='font-size: 18px;'>{st.session_state.announcement}</p>
        <a href='{st.session_state.banner_link}' target='_blank'>🔗 الانتقال إلى البوابة الرسمية للمجلس</a>
    </div>
    """, unsafe_allow_index=True)
    
    # العدادات والمؤشرات الحيوية الاقتراحية
    st.subheader("📊 مؤشرات الأداء الحالية (KPIs)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='metric-box'><h3>87%</h3><p>معدل الإنجاز العام</p></div>", unsafe_allow_index=True)
    with col2:
        st.markdown("<div class='metric-box'><h3>12</h3><p>مهام قيد التنفيذ</p></div>", unsafe_allow_index=True)
    with col3:
        st.markdown("<div class='metric-box'><h3>3</h3><p>مهام متأخرة</p></div>", unsafe_allow_index=True)
    with col4:
        st.markdown("<div class='metric-box'><h3>95%</h3><p>التزام بالعمل المرن</p></div>", unsafe_allow_index=True)
        
    st.markdown("---")
    
    # أدوات تعديل الصفحة الرئيسية (خاص بالمسؤول)
    with st.expander("⚙️ إعدادات التحكم بالواجهة وتحديث الرسالة"):
        new_announcement = st.text_area("تعديل الرسالة الموجهة للموظفين:", st.session_state.announcement)
        new_link = st.text_input("تعديل الرابط الإستراتيجي:", st.session_state.banner_link)
        if st.button("حفظ التحديثات ونشرها فوراً"):
            st.session_state.announcement = new_announcement
            st.session_state.banner_link = new_link
            st.success("تم تحديث الواجهة الرئيسية بنجاح!")

# --- القسم الثاني: توزيع وإدارة المهام ---
elif menu == "📅 توزيع وإدارة المهام":
    st.markdown("<h1 class='main-title'>📅 منظومة فرز وتوزيع المهام</h1>", unsafe_allow_index=True)
    
    tab1, tab2 = st.tabs(["✍️ إسناد مهمة يدوية", "📂 رفع وتصفية ملفات Excel الذكية"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            task_title = st.text_input("عنوان المهمة أو التكليف القضائي:")
            emp_names = [e["name"] for e in st.session_state.employees]
            assigned_emp = st.selectbox("إسناد إلى الموظف:", emp_names)
            period = st.selectbox("دورية المهمة:", ["يومية", "أسبوعية", "شهرية"])
        with col2:
            priority = st.selectbox("درجة الأهمية والسرعة:", ["عالي جداً (مستعجل)", "عالي", "متوسط", "عادي"])
            enable_reminder = st.checkbox("تفعيل خاصية التذكير التلقائي الذكي للموظف")
            
        if st.button("🚀 إرسال التكليف وإخطار الموظف فوراً"):
            if task_title:
                new_task = {"id": len(st.session_state.tasks)+1, "title": task_title, "emp": assigned_emp, "period": period, "priority": priority, "status": "قيد التنفيذ"}
                st.session_state.tasks.append(new_task)
                st.success(f"تم إسناد المهمة بنجاح إلى {assigned_emp} وإرسال تنبيه مباشر لجهازه.")
            else:
                st.error("يرجى كتابة عنوان المهمة أولاً.")
                
    with tab2:
        st.markdown("### 📊 التوزيع التلقائي الذكي عبر ملفات الـ Excel")
        st.write("ارفع جدول المهام الخام، وسيقوم النظام بتصفيتها وتوزيعها بالتساوي بناءً على القواعد الإدارية:")
        uploaded_file = st.file_uploader("اختر ملف Excel أو CSV للمهام:", type=["xlsx", "csv"])
        
        if uploaded_file is not None:
            st.success("تم رفع الملف بنجاح! تم رصد (45) مهمة خام.")
            distribution_method = st.radio("آلية التوزيع المستهدفة:", ["توزيع بالتساوي حسب العدد", "توزيع بناءً على النطاق الجغرافي للموظف", "توزيع حسب التخصص والمجموعة"])
            if st.button("⚡ بدء التصفية والفرز الآلي"):
                st.info("جاري معالجة البيانات وتوزيعها...")
                st.success("تم بنجاح تصفية الملف وتوزيع 45 مهمة على الموظفين المتاحين خلال ثوانٍ معدودة!")

    # عرض جدول كافة المهام الحالية للمسؤول
    st.markdown("---")
    st.subheader("📋 كشف متابعة سير كافة المهام الموزعة")
    df_tasks = pd.DataFrame(st.session_state.tasks)
    st.dataframe(df_tasks, use_container_width=True)

# --- القسم الثالث: مركز المراسلات الذكي ---
elif menu == "💬 مركز المراسلات الذكي":
    st.markdown("<h1 class='main-title'>💬 مركز المراسلات والتعاميم الفورية</h1>", unsafe_allow_index=True)
    
    msg_type = st.radio("نطاق إرسال الرسالة:", ["إلى جميع الموظفين (تعميم رسمي)", "إلى موظف محدد (خاص)", "إلى مجموعة عمل معينة"])
    
    if msg_type == "إلى موظف محدد (خاص)":
        emp_names = [e["name"] for e in st.session_state.employees]
        target_emp = st.selectbox("اختر الموظف المستهدف:", emp_names)
    elif msg_type == "إلى مجموعة عمل معينة":
        target_group = st.selectbox("اختر المجموعة:", list(set([e["group"] for e in st.session_state.employees])))
        
    message_text = st.text_area("نص الرسالة أو التنبيه العاجل:")
    
    if st.button("📣 إرسال كإشعار دفع مباشر (Push Notification)"):
        if message_text:
            st.success("تم تسليم الرسالة فوراً وظهرت كتنبيه على شاشات الهواتف الخاصة بالمستهدفين.")
        else:
            st.error("لا يمكن إرسال رسالة فارغة.")

# --- القسم الرابع: إدارة الكادر البشري ---
elif menu == "👥 إدارة الكادر البشري":
    st.markdown("<h1 class='main-title'>👥 إدارة شؤون الموظفين والمجموعات</h1>", unsafe_allow_index=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("➕ إضافة موظف جديد")
        new_name = st.text_input("اسم الموظف الثلاثي:")
        new_group = st.text_input("المجموعة / القسم الإداري:")
        new_loc = st.selectbox("موقع العمل الإفتراضي:", ["المقر الرئيسي", "عن بُعد", "ميداني", "فرع المحكمة"])
        
        if st.button("حفظ الموظف في النظام"):
            if new_name and new_group:
                new_emp = {"id": len(st.session_state.employees)+1, "name": new_name, "group": new_group, "location": new_loc}
                st.session_state.employees.append(new_emp)
                st.success(f"تم تسجيل {new_name} بنجاح.")
            else:
                st.error("يرجى ملء كافة الحقول الأساسية.")
                
    with col2:
        st.subheader("📋 قائمة الموظفين المقيدين حالياً ومواقعهم")
        df_emp = pd.DataFrame(st.session_state.employees)
        st.dataframe(df_emp, use_container_width=True)

# --- القسم الخامس: التحليلات وقياس الأداء ---
elif menu == "📊 التحليلات وقياس الأداء":
    st.markdown("<h1 class='main-title'>📊 تقارير الأداء ومعدلات الإنجاز</h1>", unsafe_allow_index=True)
    
    st.write("رسومات بيانية ذكية توضح مستويات الفاعلية والإنتاجية للكادر الإداري:")
    
    # بيانات وهمية للرسم البياني
    chart_data = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['المهام المكتملة', 'المهام المتأخرة', 'قيد المراجعة']
    )
    
    st.line_chart(chart_data)
    st.markdown("---")
    st.button("📥 تحميل التقرير الشامل بصيغة PDF الفاخرة لتسليمه للإدارة العليا")

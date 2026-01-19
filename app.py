# HealthHub Pro - Complete Healthcare App
# Run with: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import random
import io
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Optional: For desktop notifications (install with: pip install plyer)
try:
    from plyer import notification
    NOTIFICATIONS_ENABLED = True
except ImportError:
    NOTIFICATIONS_ENABLED = False

# Optional: For PDF export (install with: pip install reportlab)
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    PDF_ENABLED = True
except ImportError:
    PDF_ENABLED = False

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="HealthHub Pro",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLES ---
st.markdown("""
<style>
    /* Main styling */
    .main { background-color: #f0fdf4; }
    
    /* Header */
    .main-header {
        background: linear-gradient(135deg, #16a085 0%, #1abc9c 50%, #2ecc71 100%);
        padding: 20px;
        border-radius: 16px;
        color: white;
        margin-bottom: 20px;
    }
    .main-header h1 { margin: 0; font-size: 2rem; }
    .main-header p { margin: 5px 0 0 0; opacity: 0.9; }
    
    /* Cards */
    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
    }
    .stat-number { font-size: 2rem; font-weight: bold; }
    .stat-label { color: #666; font-size: 0.9rem; }
    
    /* Reminder cards */
    .reminder-pending {
        background: linear-gradient(135deg, #fff9e6 0%, #fff3cd 100%);
        border-left: 5px solid #f39c12;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .reminder-done {
        background: linear-gradient(135deg, #e8f8f0 0%, #d1f2eb 100%);
        border-left: 5px solid #27ae60;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .reminder-alert {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left: 5px solid #ef4444;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        animation: pulse 2s infinite;
    }
    
    /* Meal cards */
    .meal-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin: 10px 0;
    }
    .meal-type {
        font-weight: bold;
        color: #16a085;
        margin-bottom: 5px;
    }
    
    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Section titles */
    .section-title {
        color: #16a085;
        font-weight: 700;
        font-size: 1.3rem;
        margin: 20px 0 10px 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Emergency button */
    .emergency-btn {
        background: linear-gradient(135deg, #ef4444, #dc2626) !important;
        color: white !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "reminders" not in st.session_state:
    st.session_state.reminders = []
if "emergency_contact" not in st.session_state:
    st.session_state.emergency_contact = {"name": "", "phone": ""}
if "health_profile" not in st.session_state:
    st.session_state.health_profile = {
        "age": 25, "gender": "Male", "weight": 70.0, 
        "height": 170.0, "activity": "Moderately Active", "goal": "Maintain Weight"
    }
if "meal_plan" not in st.session_state:
    st.session_state.meal_plan = None
if "completion_history" not in st.session_state:
    st.session_state.completion_history = {"meds": 0, "water": 0, "exercise": 0, "meals": 0}

# --- CATEGORY ICONS ---
CATEGORY_ICONS = {
    "medication": "💊",
    "water": "💧",
    "exercise": "🚶",
    "meal": "🍽️",
    "appointment": "🏥",
    "other": "📋"
}

# --- MEAL DATABASE ---
MEAL_DATABASE = {
    "vegetarian": {
        "breakfast": ["Oatmeal with fruits & nuts", "Vegetable upma", "Poha with peanuts", "Idli sambar", "Smoothie bowl", "Avocado toast", "Pancakes with honey", "Masala dosa"],
        "lunch": ["Dal rice with vegetables", "Paneer curry with roti", "Veggie stir fry with rice", "Rajma chawal", "Mixed vegetable curry", "Quinoa salad bowl", "Chole bhature", "Vegetable biryani"],
        "dinner": ["Vegetable soup with bread", "Palak paneer with naan", "Mixed dal with rice", "Stuffed bell peppers", "Vegetable pasta", "Mushroom risotto", "Khichdi with pickle"],
        "snack": ["Fruit salad", "Greek yogurt", "Mixed nuts", "Hummus with veggies", "Cheese sandwich", "Smoothie", "Dhokla", "Sprout chaat"]
    },
    "non-vegetarian": {
        "breakfast": ["Egg omelet with toast", "Chicken sandwich", "Scrambled eggs", "Protein pancakes", "Egg bhurji with paratha", "Bacon and eggs", "Keema paratha"],
        "lunch": ["Grilled chicken with rice", "Fish curry with rice", "Chicken biryani", "Turkey wrap", "Salmon salad", "Chicken stir fry", "Mutton curry with roti"],
        "dinner": ["Grilled fish with vegetables", "Chicken tikka with naan", "Mutton curry with rice", "Baked salmon", "Chicken soup", "Beef steak with salad", "Tandoori chicken"],
        "snack": ["Boiled eggs", "Chicken strips", "Tuna sandwich", "Protein shake", "Turkey roll", "Fish fingers"]
    },
    "vegan": {
        "breakfast": ["Chia pudding", "Smoothie bowl", "Avocado toast", "Tofu scramble", "Oatmeal with nuts", "Fruit bowl", "Vegan pancakes"],
        "lunch": ["Buddha bowl", "Lentil soup", "Veggie wrap", "Falafel plate", "Bean burrito", "Quinoa salad", "Vegan curry with rice"],
        "dinner": ["Vegetable curry", "Tofu stir fry", "Lentil dal with rice", "Stuffed peppers", "Vegan pasta", "Bean stew", "Cauliflower rice bowl"],
        "snack": ["Fresh fruits", "Trail mix", "Hummus plate", "Edamame", "Energy balls", "Roasted chickpeas"]
    },
    "keto": {
        "breakfast": ["Eggs with avocado", "Keto pancakes", "Bacon and cheese omelet", "Bulletproof coffee with eggs", "Cheese roll-ups"],
        "lunch": ["Grilled chicken salad", "Salmon with asparagus", "Cauliflower rice bowl", "Zucchini noodles with meat", "Bunless burger"],
        "dinner": ["Steak with butter", "Baked fish with greens", "Pork chops with veggies", "Chicken thighs", "Shrimp stir fry"],
        "snack": ["Cheese cubes", "Boiled eggs", "Pork rinds", "Almonds", "Celery with cream cheese"]
    },
    "balanced": {
        "breakfast": ["Whole grain cereal with milk", "Eggs with toast", "Yogurt parfait", "Breakfast burrito", "Oatmeal with fruits"],
        "lunch": ["Grilled chicken with salad", "Fish with rice and veggies", "Sandwich with soup", "Pasta with lean meat", "Rice bowl with protein"],
        "dinner": ["Baked salmon with quinoa", "Lean meat with vegetables", "Soup with bread", "Stir fry with rice", "Grilled fish with salad"],
        "snack": ["Mixed nuts", "Fruit and yogurt", "Cheese and crackers", "Protein bar", "Smoothie"]
    }
}

# --- HELPER FUNCTIONS ---
def format_time(time_str):
    """Convert 24h time to 12h format"""
    try:
        time_obj = datetime.strptime(time_str, "%H:%M")
        return time_obj.strftime("%I:%M %p")
    except:
        return time_str

def get_next_hour():
    """Get next hour time string"""
    now = datetime.now() + timedelta(hours=1)
    return now.strftime("%H:%M")

def calculate_bmi(weight, height_cm):
    """Calculate BMI"""
    height_m = height_cm / 100
    return weight / (height_m ** 2)

def get_bmi_category(bmi):
    """Get BMI category"""
    if bmi < 18.5:
        return "Underweight", "#3b82f6"
    elif bmi < 25:
        return "Normal", "#22c55e"
    elif bmi < 30:
        return "Overweight", "#f59e0b"
    else:
        return "Obese", "#ef4444"

def calculate_calories(weight, height, age, gender, activity):
    """Calculate daily calorie needs using Mifflin-St Jeor equation"""
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extra Active": 1.9
    }
    return int(bmr * activity_multipliers.get(activity, 1.55))

def generate_meal_plan(diet_type, days, target_calories, condition, allergies_list):
    """Generate a meal plan"""
    meals = MEAL_DATABASE.get(diet_type.lower().replace("-", "").replace(" ", ""), MEAL_DATABASE["balanced"])
    plan = []
    
    for day in range(1, days + 1):
        # Random calorie variation
        day_calories = int(target_calories * random.uniform(0.9, 1.1))
        protein = int(day_calories * 0.25 / 4)
        carbs = int(day_calories * 0.45 / 4)
        fat = int(day_calories * 0.30 / 9)
        
        # Select meals avoiding allergies
        def safe_choice(meal_list):
            safe_meals = [m for m in meal_list if not any(a.lower() in m.lower() for a in allergies_list)]
            return random.choice(safe_meals) if safe_meals else random.choice(meal_list)
        
        plan.append({
            "Day": day,
            "Breakfast": safe_choice(meals["breakfast"]),
            "Lunch": safe_choice(meals["lunch"]),
            "Dinner": safe_choice(meals["dinner"]),
            "Snack": safe_choice(meals["snack"]),
            "Calories": day_calories,
            "Protein (g)": protein,
            "Carbs (g)": carbs,
            "Fat (g)": fat
        })
    
    return pd.DataFrame(plan)

def create_pdf(plan_df, profile):
    """Create PDF from meal plan"""
    if not PDF_ENABLED:
        return None
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    
    # Title
    elements.append(Paragraph("HealthHub Pro - Personalized Meal Plan", styles["Title"]))
    elements.append(Spacer(1, 12))
    
    # Profile info
    profile_text = f"Age: {profile['age']} | Gender: {profile['gender']} | Weight: {profile['weight']}kg | Height: {profile['height']}cm"
    elements.append(Paragraph(profile_text, styles["Normal"]))
    elements.append(Spacer(1, 20))
    
    # Table
    data = [plan_df.columns.tolist()] + plan_df.values.tolist()
    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#16a085")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f0fdf4")])
    ]))
    elements.append(table)
    
    doc.build(elements)
    buffer.seek(0)
    return buffer.getvalue()

def send_notification(title, message):
    """Send desktop notification"""
    if NOTIFICATIONS_ENABLED:
        try:
            notification.notify(
                title=title,
                message=message,
                timeout=10
            )
        except:
            pass

# --- HEADER ---
st.markdown("""
<div class="main-header">
    <h1>🏥 HealthHub Pro</h1>
    <p>Complete Healthcare Companion - Reminders • Diet Coach • Health Tracking</p>
</div>
""", unsafe_allow_html=True)

# Show current time
col_time1, col_time2 = st.columns([3, 1])
with col_time2:
    st.markdown(f"**🕐 {datetime.now().strftime('%I:%M %p')}** | {datetime.now().strftime('%b %d, %Y')}")

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["💊 Reminders", "🍽️ Diet Coach", "👤 Health Profile", "📊 Reports"])

# ==================== REMINDERS TAB ====================
with tab1:
    # Quick Stats
    pending = len([r for r in st.session_state.reminders if not r["done"]])
    done = len([r for r in st.session_state.reminders if r["done"]])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number" style="color: #f59e0b;">{pending}</div>
            <div class="stat-label">⏰ Pending</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number" style="color: #22c55e;">{done}</div>
            <div class="stat-label">✅ Completed</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        next_reminder = "--:--"
        pending_reminders = [r for r in st.session_state.reminders if not r["done"]]
        if pending_reminders:
            next_reminder = format_time(min(pending_reminders, key=lambda x: x["time"])["time"])
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number" style="color: #16a085;">{next_reminder}</div>
            <div class="stat-label">🔔 Next</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Emergency Contact
    with st.expander("🚨 Emergency Contact", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            emergency_name = st.text_input("Contact Name", value=st.session_state.emergency_contact["name"], key="em_name")
        with col2:
            emergency_phone = st.text_input("Phone Number", value=st.session_state.emergency_contact["phone"], key="em_phone")
        
        if st.button("💾 Save Emergency Contact", use_container_width=True):
            st.session_state.emergency_contact = {"name": emergency_name, "phone": emergency_phone}
            st.success(f"✅ Emergency contact saved: {emergency_name}")
        
        if st.session_state.emergency_contact["phone"]:
            st.markdown(f"**📞 Call:** [{st.session_state.emergency_contact['name']}](tel:{st.session_state.emergency_contact['phone']})")
    
    # Quick Add Buttons
    st.markdown("<div class='section-title'>⚡ Quick Add</div>", unsafe_allow_html=True)
    qcol1, qcol2, qcol3, qcol4 = st.columns(4)
    
    with qcol1:
        if st.button("💊 Medicine", use_container_width=True):
            st.session_state.reminders.append({
                "id": str(datetime.now().timestamp()),
                "message": "💊 Take Medicine",
                "time": get_next_hour(),
                "category": "medication",
                "frequency": "daily",
                "done": False
            })
            st.rerun()
    with qcol2:
        if st.button("💧 Water", use_container_width=True):
            st.session_state.reminders.append({
                "id": str(datetime.now().timestamp()),
                "message": "💧 Drink Water",
                "time": get_next_hour(),
                "category": "water",
                "frequency": "daily",
                "done": False
            })
            st.rerun()
    with qcol3:
        if st.button("🚶 Walk", use_container_width=True):
            st.session_state.reminders.append({
                "id": str(datetime.now().timestamp()),
                "message": "🚶 Take a Walk",
                "time": get_next_hour(),
                "category": "exercise",
                "frequency": "daily",
                "done": False
            })
            st.rerun()
    with qcol4:
        if st.button("🍽️ Meal", use_container_width=True):
            st.session_state.reminders.append({
                "id": str(datetime.now().timestamp()),
                "message": "🍽️ Meal Time",
                "time": get_next_hour(),
                "category": "meal",
                "frequency": "daily",
                "done": False
            })
            st.rerun()
    
    # Add Custom Reminder
    st.markdown("<div class='section-title'>➕ Add Custom Reminder</div>", unsafe_allow_html=True)
    
    with st.form("add_reminder_form", clear_on_submit=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            message = st.text_input("Reminder Message", placeholder="e.g., Take blood pressure medicine")
        with col2:
            reminder_time = st.time_input("Time", value=datetime.now().replace(second=0, microsecond=0))
        
        col3, col4 = st.columns(2)
        with col3:
            category = st.selectbox("Category", ["medication", "water", "exercise", "meal", "appointment", "other"])
        with col4:
            frequency = st.selectbox("Frequency", ["daily", "weekly", "once"])
        
        submitted = st.form_submit_button("➕ Add Reminder", use_container_width=True)
        if submitted and message:
            st.session_state.reminders.append({
                "id": str(datetime.now().timestamp()),
                "message": message,
                "time": reminder_time.strftime("%H:%M"),
                "category": category,
                "frequency": frequency,
                "done": False
            })
            st.success(f"✅ Reminder added: {message} at {format_time(reminder_time.strftime('%H:%M'))}")
            st.rerun()
    
    # Active Alerts
    current_time = datetime.now().strftime("%H:%M")
    active_alerts = [r for r in st.session_state.reminders if not r["done"] and r["time"] == current_time]
    
    if active_alerts:
        st.markdown("<div class='section-title'>🚨 Active Alerts!</div>", unsafe_allow_html=True)
        for alert in active_alerts:
            st.markdown(f"""
            <div class="reminder-alert">
                <h4>{CATEGORY_ICONS.get(alert['category'], '📋')} {alert['message']}</h4>
                <p>⏰ It's time for your reminder!</p>
            </div>
            """, unsafe_allow_html=True)
            send_notification("HealthHub Reminder", alert['message'])
    
    # Reminders List
    st.markdown("<div class='section-title'>📋 All Reminders</div>", unsafe_allow_html=True)
    
    if not st.session_state.reminders:
        st.info("No reminders yet. Add your first reminder above! 📝")
    else:
        # Sort: pending first, then by time
        sorted_reminders = sorted(st.session_state.reminders, key=lambda x: (x["done"], x["time"]))
        
        for idx, reminder in enumerate(sorted_reminders):
            icon = CATEGORY_ICONS.get(reminder["category"], "📋")
            status_class = "reminder-done" if reminder["done"] else "reminder-pending"
            status_text = "✅ Done" if reminder["done"] else "⏰ Pending"
            
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                st.markdown(f"""
                <div class="{status_class}">
                    <strong>{icon} {reminder['message']}</strong><br>
                    <small>🕐 {format_time(reminder['time'])} | {reminder['frequency'].title()} | {status_text}</small>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if not reminder["done"]:
                    if st.button("✅ Done", key=f"done_{reminder['id']}"):
                        reminder["done"] = True
                        st.session_state.completion_history[reminder["category"]] = \
                            st.session_state.completion_history.get(reminder["category"], 0) + 1
                        st.rerun()
            
            with col3:
                if not reminder["done"]:
                    if st.button("🔁 +5min", key=f"snooze_{reminder['id']}"):
                        old_time = datetime.strptime(reminder["time"], "%H:%M")
                        new_time = old_time + timedelta(minutes=5)
                        reminder["time"] = new_time.strftime("%H:%M")
                        st.rerun()
            
            with col4:
                if st.button("🗑️", key=f"delete_{reminder['id']}"):
                    st.session_state.reminders.remove(reminder)
                    st.rerun()
        
        # Clear completed button
        if done > 0:
            if st.button("🗑️ Clear Completed", use_container_width=True):
                st.session_state.reminders = [r for r in st.session_state.reminders if not r["done"]]
                st.rerun()

# ==================== DIET COACH TAB ====================
with tab2:
    st.markdown("<div class='section-title'>🍽️ AI Diet Coach</div>", unsafe_allow_html=True)
    st.markdown("Generate personalized meal plans based on your preferences and health conditions.")
    
    with st.form("diet_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            diet_type = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan", "Keto", "Balanced"])
            cuisine_pref = st.selectbox("Cuisine Preference", ["Any", "Indian", "Mediterranean", "Asian", "American", "Mexican"])
            health_condition = st.selectbox("Health Condition", ["None", "Diabetes", "Hypertension", "Heart Disease", "High Cholesterol", "Obesity"])
        
        with col2:
            plan_days = st.slider("Plan Duration (days)", 7, 30, 7)
            target_calories = st.number_input("Target Calories/Day", 1200, 4000, 2000, step=100)
            meals_per_day = st.selectbox("Meals per Day", ["3 Meals", "3 Meals + Snack", "3 Meals + 2 Snacks"])
        
        allergies = st.text_input("Allergies (comma-separated)", placeholder="e.g., nuts, dairy, gluten")
        
        generate_btn = st.form_submit_button("🪄 Generate Meal Plan", use_container_width=True)
    
    if generate_btn:
        with st.spinner("Generating your personalized meal plan..."):
            allergies_list = [a.strip() for a in allergies.split(",") if a.strip()]
            st.session_state.meal_plan = generate_meal_plan(diet_type, plan_days, target_calories, health_condition, allergies_list)
        st.success(f"✅ {plan_days}-day meal plan generated!")
    
    # Display Meal Plan
    if st.session_state.meal_plan is not None:
        plan_df = st.session_state.meal_plan
        
        # Macro Summary
        st.markdown("<div class='section-title'>📊 Daily Averages</div>", unsafe_allow_html=True)
        
        avg_cal = int(plan_df["Calories"].mean())
        avg_protein = int(plan_df["Protein (g)"].mean())
        avg_carbs = int(plan_df["Carbs (g)"].mean())
        avg_fat = int(plan_df["Fat (g)"].mean())
        
        mcol1, mcol2, mcol3, mcol4 = st.columns(4)
        with mcol1:
            st.metric("🔥 Calories", f"{avg_cal}")
        with mcol2:
            st.metric("🥩 Protein", f"{avg_protein}g")
        with mcol3:
            st.metric("🍞 Carbs", f"{avg_carbs}g")
        with mcol4:
            st.metric("🧈 Fat", f"{avg_fat}g")
        
        # Macro Chart
        col1, col2 = st.columns(2)
        
        with col1:
            fig1, ax1 = plt.subplots(figsize=(5, 4))
            colors_pie = ['#3b82f6', '#22c55e', '#f59e0b']
            ax1.pie([avg_protein, avg_carbs, avg_fat], labels=['Protein', 'Carbs', 'Fat'], 
                   colors=colors_pie, autopct='%1.1f%%', startangle=90)
            ax1.set_title("Macro Distribution")
            st.pyplot(fig1)
        
        with col2:
            fig2, ax2 = plt.subplots(figsize=(5, 4))
            ax2.bar(['Calories', 'Protein', 'Carbs', 'Fat'], 
                   [avg_cal, avg_protein, avg_carbs, avg_fat],
                   color=['#ef4444', '#3b82f6', '#22c55e', '#f59e0b'])
            ax2.set_ylabel("Amount")
            ax2.set_title("Daily Averages")
            st.pyplot(fig2)
        
        # Meal Plan Table
        st.markdown("<div class='section-title'>📅 Your Meal Plan</div>", unsafe_allow_html=True)
        st.dataframe(plan_df, use_container_width=True, hide_index=True)
        
        # Download Options
        col1, col2 = st.columns(2)
        
        with col1:
            csv = plan_df.to_csv(index=False)
            st.download_button(
                "📥 Download CSV",
                csv,
                f"meal_plan_{datetime.now().strftime('%Y%m%d')}.csv",
                "text/csv",
                use_container_width=True
            )
        
        with col2:
            if PDF_ENABLED:
                pdf_data = create_pdf(plan_df, st.session_state.health_profile)
                if pdf_data:
                    st.download_button(
                        "📄 Download PDF",
                        pdf_data,
                        f"meal_plan_{datetime.now().strftime('%Y%m%d')}.pdf",
                        "application/pdf",
                        use_container_width=True
                    )
            else:
                st.info("Install reportlab for PDF export: `pip install reportlab`")
        
        # Tips
        st.markdown("<div class='section-title'>💡 Tips & Precautions</div>", unsafe_allow_html=True)
        tips = [
            "Stay hydrated - drink at least 8 glasses of water daily",
            "Follow the plan consistently for 2-4 weeks for best results",
            "Consult a physician if you experience any adverse reactions",
            "Prefer whole grains over refined carbohydrates",
            "Include fiber-rich vegetables in every meal",
            "Avoid processed and packaged snacks"
        ]
        for tip in random.sample(tips, 3):
            st.markdown(f"✅ {tip}")

# ==================== HEALTH PROFILE TAB ====================
with tab3:
    st.markdown("<div class='section-title'>👤 Health Profile</div>", unsafe_allow_html=True)
    
    with st.form("health_profile_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Age", 1, 120, st.session_state.health_profile["age"])
            weight = st.number_input("Weight (kg)", 20.0, 300.0, st.session_state.health_profile["weight"], step=0.5)
            activity = st.selectbox("Activity Level", 
                ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"],
                index=["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"].index(st.session_state.health_profile["activity"]))
        
        with col2:
            gender = st.selectbox("Gender", ["Male", "Female", "Other"],
                index=["Male", "Female", "Other"].index(st.session_state.health_profile["gender"]))
            height = st.number_input("Height (cm)", 100.0, 250.0, st.session_state.health_profile["height"], step=1.0)
            goal = st.selectbox("Goal", ["Maintain Weight", "Lose Weight", "Gain Weight"],
                index=["Maintain Weight", "Lose Weight", "Gain Weight"].index(st.session_state.health_profile["goal"]))
        
        save_profile = st.form_submit_button("💾 Save Profile", use_container_width=True)
        
        if save_profile:
            st.session_state.health_profile = {
                "age": age, "gender": gender, "weight": weight,
                "height": height, "activity": activity, "goal": goal
            }
            st.success("✅ Profile saved successfully!")
    
    # BMI Calculator
    st.markdown("<div class='section-title'>📏 BMI Calculator</div>", unsafe_allow_html=True)
    
    profile = st.session_state.health_profile
    bmi = calculate_bmi(profile["weight"], profile["height"])
    bmi_category, bmi_color = get_bmi_category(bmi)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number" style="color: {bmi_color};">{bmi:.1f}</div>
            <div class="stat-label">BMI - {bmi_category}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # BMI Scale
        st.progress(min(bmi / 40, 1.0))
        st.caption("Underweight < 18.5 | Normal 18.5-24.9 | Overweight 25-29.9 | Obese 30+")
    
    # Calorie Calculator
    with col2:
        calories = calculate_calories(profile["weight"], profile["height"], profile["age"], profile["gender"], profile["activity"])
        
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number" style="color: #f59e0b;">{calories}</div>
            <div class="stat-label">Daily Calorie Need</div>
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Lose", f"{calories - 500}", "-500")
        with c2:
            st.metric("Maintain", f"{calories}")
        with c3:
            st.metric("Gain", f"{calories + 500}", "+500")

# ==================== REPORTS TAB ====================
with tab4:
    st.markdown("<div class='section-title'>📊 Health Reports</div>", unsafe_allow_html=True)
    
    # Completion Stats
    total = len(st.session_state.reminders)
    completed = len([r for r in st.session_state.reminders if r["done"]])
    completion_rate = (completed / total * 100) if total > 0 else 0
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Reminder Completion")
        
        fig, ax = plt.subplots(figsize=(5, 5))
        sizes = [completion_rate, 100 - completion_rate]
        colors_ring = ['#16a085', '#e5e7eb']
        ax.pie(sizes, colors=colors_ring, startangle=90, 
               wedgeprops=dict(width=0.4, edgecolor='white'))
        ax.text(0, 0, f'{completion_rate:.0f}%', ha='center', va='center', fontsize=24, fontweight='bold')
        ax.set_title("Today's Progress")
        st.pyplot(fig)
        
        st.markdown(f"**Completed:** {completed} | **Pending:** {total - completed}")
    
    with col2:
        st.markdown("### 📊 Activity Summary")
        
        categories = ['Meds', 'Water', 'Exercise', 'Meals']
        values = [
            st.session_state.completion_history.get("medication", 0),
            st.session_state.completion_history.get("water", 0),
            st.session_state.completion_history.get("exercise", 0),
            st.session_state.completion_history.get("meal", 0)
        ]
        
        fig, ax = plt.subplots(figsize=(5, 4))
        colors_bar = ['#ef4444', '#3b82f6', '#22c55e', '#f59e0b']
        ax.bar(categories, values, color=colors_bar)
        ax.set_ylabel("Completed")
        ax.set_title("Tasks by Category")
        st.pyplot(fig)
    
    # Weight Projection
    st.markdown("### 📉 Weight Projection (12 Weeks)")
    
    profile = st.session_state.health_profile
    current_weight = profile["weight"]
    goal = profile["goal"]
    
    if goal == "Lose Weight":
        weekly_change = -0.5
    elif goal == "Gain Weight":
        weekly_change = 0.3
    else:
        weekly_change = 0
    
    weeks = list(range(13))
    weights = [current_weight + (weekly_change * w) for w in weeks]
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(weeks, weights, marker='o', color='#16a085', linewidth=2, markersize=8)
    ax.fill_between(weeks, weights, alpha=0.2, color='#16a085')
    ax.set_xlabel("Week")
    ax.set_ylabel("Weight (kg)")
    ax.set_title(f"Projected Weight Trend ({goal})")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>HealthHub Pro</strong> - Complete Healthcare Companion</p>
    <p>Built with ❤️ using Streamlit | © 2024</p>
</div>
""", unsafe_allow_html=True)

# --- AUTO-REFRESH for alerts (optional) ---
# Uncomment below to enable auto-refresh every 60 seconds
# import time
# time.sleep(60)
# st.rerun()

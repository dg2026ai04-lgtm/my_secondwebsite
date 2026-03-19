# my_secondwebsite
import streamlit as st
import datetime
import random

st.set_page_config(page_title="운세 여행 🔮", page_icon="✨")

# ======================
# 버튼 스타일
# ======================
st.markdown("""
<style>
div.stButton > button {
    background-color: #ffffff;
    color: #000000;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #ffd166;
}
</style>
""", unsafe_allow_html=True)

# ======================
# 상태
# ======================
if "page" not in st.session_state:
    st.session_state.page = 0

if "data" not in st.session_state:
    st.session_state.data = {}

# ======================
# 🎨 배경 함수
# ======================
def set_bg(color1, color2, text_color="white"):
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(to bottom, {color1}, {color2});
        color: {text_color};
    }}
    </style>
    """, unsafe_allow_html=True)

# ======================
# 🎉 아이콘 떨어지는 효과
# ======================
def falling_icons(icon):
    st.markdown(f"""
    <style>
    .falling {{
        position: fixed;
        top: -10px;
        font-size: 30px;
        animation: fall 5s linear infinite;
    }}

    @keyframes fall {{
        0% {{transform: translateY(0); opacity:1;}}
        100% {{transform: translateY(100vh); opacity:0;}}
    }}
    </style>

    <div class="falling" style="left:10%;">{icon}</div>
    <div class="falling" style="left:30%; animation-delay:1s;">{icon}</div>
    <div class="falling" style="left:50%; animation-delay:2s;">{icon}</div>
    <div class="falling" style="left:70%; animation-delay:3s;">{icon}</div>
    <div class="falling" style="left:90%; animation-delay:4s;">{icon}</div>
    """, unsafe_allow_html=True)

# =====================
# 0️⃣ 시작 페이지 (오로라)
# =====================
if st.session_state.page == 0:

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0c3fc, #8ec5fc, #fbc2eb);
        color: #222;
    }

    label {
        color: #4a148c !important;
        font-weight: bold;
    }

    .stTextInput input, .stDateInput input {
        background-color: white !important;
        color: black !important;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🔮 운세 여행 시작")

    name = st.text_input("🧑 이름")
    birthday = st.date_input(
        "🎂 생일",
        min_value=datetime.date(1900,1,1),
        max_value=datetime.date.today()
    )

    if st.button("✨ 시작"):
        if name and birthday:

            today = datetime.date.today()
            seed = birthday.month*100 + birthday.day + today.day
            random.seed(seed)

            st.session_state.data = {
                "name": name,
                "study": random.randint(50,100),
                "love": random.randint(50,100),
                "money": random.randint(50,100),
                "luck": random.randint(50,100),
                "color": random.choice(["빨강 🔴","파랑 🔵","보라 🟣"]),
                "food": random.choice(["치킨 🍗","피자 🍕","떡볶이 🌶️"]),
                "number": random.randint(1,99)
            }

            st.session_state.page = 1
            st.rerun()

# =====================
# 1️⃣ 전체운 (기존 유지)
# =====================
elif st.session_state.page == 1:

    set_bg("#0f2027", "#2c5364")
    d = st.session_state.data

    st.title("🌟 전체 운세")

    avg = (d['study']+d['love']+d['money']+d['luck'])//4

    st.write(f"{d['name']}님의 전체 운세: {avg}점")
    st.progress(avg)

    st.balloons()

    if st.button("➡️ 공부운"):
        st.session_state.page = 2
        st.rerun()

# =====================
# 2️⃣ 공부운 (파스텔 + 책 떨어짐)
# =====================
elif st.session_state.page == 2:

    set_bg("#e3f2fd", "#bbdefb", "black")
    falling_icons("📚")

    d = st.session_state.data

    st.title("📚 공부운")
    st.progress(d["study"])

    st.write(f"집중력이 중요한 날! 점수: {d['study']}점")

    if st.button("➡️ 연애운"):
        st.session_state.page = 3
        st.rerun()

# =====================
# 3️⃣ 연애운 (하트 효과)
# =====================
elif st.session_state.page == 3:

    set_bg("#fce4ec", "#f8bbd0", "black")
    falling_icons("💖")

    d = st.session_state.data

    st.title("💖 연애운")
    st.progress(d["love"])

    st.write(f"감정 표현이 중요한 하루! {d['love']}점")

    if st.button("➡️ 금전운"):
        st.session_state.page = 4
        st.rerun()

# =====================
# 4️⃣ 금전운 (돈 효과)
# =====================
elif st.session_state.page == 4:

    set_bg("#e8f5e9", "#c8e6c9", "black")
    falling_icons("💰")

    d = st.session_state.data

    st.title("💰 금전운")
    st.progress(d["money"])

    st.write(f"소비 조심! {d['money']}점")

    if st.button("➡️ 행운지수"):
        st.session_state.page = 5
        st.rerun()

# =====================
# 5️⃣ 행운지수 (반짝이 효과)
# =====================
elif st.session_state.page == 5:

    set_bg("#e3f2fd", "#b3e5fc", "black")
    falling_icons("✨")

    d = st.session_state.data

    st.title("🍀 행운지수")
    st.progress(d["luck"])

    st.write(f"""
행운 점수: {d['luck']}

🎁 색: {d['color']}
🍔 음식: {d['food']}
🔢 숫자: {d['number']}
""")

    st.balloons()

    if st.button("🔄 다시"):
        st.session_state.page = 0
        st.rerun()

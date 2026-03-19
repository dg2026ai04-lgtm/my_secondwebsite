# my_secondwebsite
import streamlit as st
import datetime
import random

st.set_page_config(page_title="운세 여행 🔮", page_icon="✨")

# ======================
# 🎨 버튼 스타일
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
# 상태 초기화
# ======================
if "page" not in st.session_state:
    st.session_state.page = 0

if "data" not in st.session_state:
    st.session_state.data = {}

# ======================
# 배경 함수
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
# 🎉 아이콘 효과
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
        font-size: 18px;
    }

    .stTextInput input, .stDateInput input {
        background-color: white !important;
        color: black !important;
        border-radius: 10px;
        border: 2px solid #b39ddb;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🔮 운세 여행 시작")
    st.write("✨ 당신의 운명을 확인하러 떠나보세요")

    name = st.text_input("🧑 이름을 입력하세요")
    birthday = st.date_input(
        "🎂 생일을 선택하세요",
        min_value=datetime.date(1900,1,1),
        max_value=datetime.date.today()
    )

    if st.button("✨ 운세 보러 가기"):
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

        else:
            st.warning("⚠️ 입력을 모두 해주세요!")

# =====================
# 1️⃣ 전체운
# =====================
elif st.session_state.page == 1:

    set_bg("#0f2027", "#2c5364")
    d = st.session_state.data

    st.title("🌟 전체 운세")

    avg = (d['study']+d['love']+d['money']+d['luck'])//4

    st.subheader(f"{d['name']}님의 오늘의 전체 흐름")

    st.write(f"""
✨ 오늘은 전반적으로 균형이 중요한 하루입니다.  
현재 운세 점수는 **{avg}점**으로 안정적인 흐름입니다.

👉 무리한 도전보다는 꾸준함이 중요합니다.  
👉 작은 선택 하나가 하루를 바꿀 수 있어요!

💡 긍정적인 태도를 유지하세요!
""")

    st.progress(avg)
    st.balloons()

    if st.button("➡️ 공부운 보기"):
        st.session_state.page = 2
        st.rerun()

# =====================
# 2️⃣ 공부운
# =====================
elif st.session_state.page == 2:

    set_bg("#e3f2fd", "#bbdefb", "black")
    falling_icons("📚")

    d = st.session_state.data

    st.title("📚 공부운")

    st.progress(d["study"])

    st.write(f"""
📖 오늘의 공부운은 **{d['study']}점**입니다.

👉 집중력이 {"높은 상태" if d["study"] > 75 else "조금 부족한 상태"}입니다.

✔️ 추천 행동:
- 짧게 집중 → 쉬기 반복
- 쉬운 문제부터 해결

⚠️ 주의:
- 핸드폰 사용 증가

💡 오늘은 꾸준함이 핵심입니다!
""")

    if st.button("➡️ 연애운 보기"):
        st.session_state.page = 3
        st.rerun()

# =====================
# 3️⃣ 연애운
# =====================
elif st.session_state.page == 3:

    set_bg("#fce4ec", "#f8bbd0", "black")
    falling_icons("💖")

    d = st.session_state.data

    st.title("💖 연애운")

    st.progress(d["love"])

    st.write(f"""
💌 오늘의 연애운은 **{d['love']}점**입니다.

👉 감정 표현이 중요한 하루입니다.

✔️ 좋은 흐름:
- 먼저 연락하기
- 솔직한 대화

⚠️ 주의:
- 작은 오해 가능

💡 한마디가 관계를 바꿀 수 있어요!
""")

    if st.button("➡️ 금전운 보기"):
        st.session_state.page = 4
        st.rerun()

# =====================
# 4️⃣ 금전운
# =====================
elif st.session_state.page == 4:

    set_bg("#e8f5e9", "#c8e6c9", "black")
    falling_icons("💰")

    d = st.session_state.data

    st.title("💰 금전운")

    st.progress(d["money"])

    st.write(f"""
💵 오늘의 금전운은 **{d['money']}점**입니다.

👉 소비 습관 점검이 필요한 날입니다.

✔️ 추천:
- 계획적인 소비
- 충동구매 피하기

⚠️ 주의:
- 작은 지출 누적

💡 절약이 미래를 만듭니다!
""")

    if st.button("➡️ 행운지수 보기"):
        st.session_state.page = 5
        st.rerun()

# =====================
# 5️⃣ 행운지수
# =====================
elif st.session_state.page == 5:

    set_bg("#e3f2fd", "#b3e5fc", "black")
    falling_icons("✨")

    d = st.session_state.data

    st.title("🍀 행운 지수")

    st.progress(d["luck"])

    st.write(f"""
🌟 오늘의 행운 지수는 **{d['luck']}점**입니다.

👉 예상치 못한 기회가 찾아올 수 있습니다!

✔️ 추천:
- 새로운 도전
- 평소와 다른 선택

🎁 행운 아이템:
- 색: {d['color']}
- 음식: {d['food']}
- 숫자: {d['number']}

💡 작은 시도가 큰 행운을 부릅니다!
""")

    st.balloons()

    if st.button("🔄 처음으로"):
        st.session_state.page = 0
        st.rerun()

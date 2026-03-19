# my_secondwebsite
import streamlit as st
import datetime
import random

# 페이지 설정
st.set_page_config(page_title="운세 여행 🔮", page_icon="✨")

# ======================
# 🎨 공통 버튼 스타일
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
    color: black;
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
def set_bg(color1, color2):
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(to bottom, {color1}, {color2});
        color: white;
    }}
    </style>
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
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 10px;
        padding: 8px;
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
현재 당신의 운세 점수는 **{avg}점**으로 안정적인 흐름을 보이고 있어요.

👉 무리한 도전보다는 꾸준함이 중요합니다.  
👉 작은 선택 하나가 하루를 바꿀 수 있어요!

💡 긍정적인 태도를 유지해보세요!
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

    set_bg("#141e30", "#243b55")
    d = st.session_state.data

    st.title("📚 공부운")

    st.progress(d["study"])

    st.write(f"""
📖 공부운 점수: **{d['study']}점**

👉 집중력은 {"좋은 상태" if d["study"] > 75 else "조금 흐트러질 수 있음"}

✔️ 추천:
- 짧게 집중 → 쉬기 반복
- 쉬운 문제부터 시작

⚠️ 주의:
- 핸드폰 유혹

💡 오늘은 꾸준함이 핵심!
""")

    st.snow()

    if st.button("➡️ 연애운 보기"):
        st.session_state.page = 3
        st.rerun()

# =====================
# 3️⃣ 연애운
# =====================
elif st.session_state.page == 3:

    set_bg("#3a1c71", "#d76d77")
    d = st.session_state.data

    st.title("💖 연애운")

    st.progress(d["love"])

    st.write(f"""
💌 연애운 점수: **{d['love']}점**

👉 감정 표현이 중요한 하루

✔️ 좋은 흐름:
- 먼저 다가가기
- 솔직한 대화

⚠️ 주의:
- 오해 가능성

💡 한마디가 관계를 바꿉니다!
""")

    if st.button("➡️ 금전운 보기"):
        st.session_state.page = 4
        st.rerun()

# =====================
# 4️⃣ 금전운
# =====================
elif st.session_state.page == 4:

    set_bg("#134e5e", "#71b280")
    d = st.session_state.data

    st.title("💰 금전운")

    st.progress(d["money"])

    st.write(f"""
💵 금전운 점수: **{d['money']}점**

👉 소비 관리가 중요한 날

✔️ 추천:
- 계획 소비
- 충동구매 피하기

⚠️ 주의:
- 작은 지출 누적

💡 절약이 기회를 만듭니다!
""")

    if st.button("➡️ 행운지수 보기"):
        st.session_state.page = 5
        st.rerun()

# =====================
# 5️⃣ 행운지수
# =====================
elif st.session_state.page == 5:

    set_bg("#000428", "#004e92")
    d = st.session_state.data

    st.title("🍀 행운 지수")

    st.progress(d["luck"])

    st.write(f"""
🌟 행운 점수: **{d['luck']}점**

👉 예상치 못한 기회 가능!

✔️ 추천:
- 새로운 시도
- 평소와 다른 선택

🎁 행운 아이템
- 색: {d['color']}
- 음식: {d['food']}
- 숫자: {d['number']}

💡 작은 도전이 큰 행운으로!
""")

    st.balloons()

    if st.button("🔄 처음으로"):
        st.session_state.page = 0
        st.rerun()

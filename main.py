# my_secondwebsite
import streamlit as st
import datetime
import random

# 페이지 설정
st.set_page_config(page_title="운세 여행 🔮", page_icon="✨")

# 버튼 스타일 수정 (핵심!)
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

# 페이지 상태
if "page" not in st.session_state:
    st.session_state.page = 0

if "data" not in st.session_state:
    st.session_state.data = {}

# 배경 함수
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
# 0️⃣ 시작 페이지
# =====================
if st.session_state.page == 0:

    set_bg("#1e1e2f", "#3a0ca3")

    st.title("🔮 운세 여행 시작")

    name = st.text_input("🧑 이름")
    birthday = st.date_input("🎂 생일",
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

👉 무리하게 큰 변화를 시도하기보다는  
지금 하고 있는 일을 꾸준히 유지하는 것이 더 좋은 결과를 가져옵니다.

💡 작은 선택 하나가 하루의 분위기를 바꿀 수 있으니  
신중하면서도 긍정적인 태도를 유지해보세요!
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
📖 오늘의 공부운 점수는 **{d['study']}점**입니다.

👉 집중력이 평소보다 {"높은" if d["study"]>75 else "조금 부족한"} 상태입니다.

✔️ 추천 행동:
- 짧게 집중 → 쉬기 반복
- 어려운 문제보다 쉬운 문제 먼저 해결

⚠️ 주의:
- 핸드폰 사용 시간이 늘어날 수 있어요

💡 팁:
오늘은 완벽함보다 "꾸준함"이 더 중요합니다!
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
💌 오늘의 연애운은 **{d['love']}점**입니다.

👉 감정 표현이 중요한 하루입니다.

✔️ 좋은 흐름:
- 먼저 연락하면 좋은 반응 가능 😊
- 솔직한 대화가 관계를 더 깊게 만듦

⚠️ 주의:
- 오해가 생기기 쉬운 날

💡 팁:
짧은 한마디가 큰 변화를 만들 수 있어요!
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
💵 오늘의 금전운은 **{d['money']}점**입니다.

👉 소비 습관을 점검해야 하는 날입니다.

✔️ 추천:
- 꼭 필요한 소비만 하기
- 충동구매 피하기

⚠️ 주의:
- 작은 지출이 쌓일 수 있음

💡 팁:
오늘 아낀 돈이 미래의 기회를 만듭니다!
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
🌟 오늘의 행운 지수는 **{d['luck']}점**입니다.

👉 예상치 못한 기회가 찾아올 수 있어요!

✔️ 행운 활용법:
- 새로운 도전 해보기
- 평소 안 하던 선택 해보기

🎁 오늘의 행운 아이템:
- 색: {d['color']}
- 음식: {d['food']}
- 숫자: {d['number']}

💡 작은 시도가 큰 행운을 부릅니다!
""")

    st.balloons()

    if st.button("🔄 처음으로"):
        st.session_state.page = 0
        st.rerun()

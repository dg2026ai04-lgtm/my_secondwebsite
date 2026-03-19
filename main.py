# my_secondwebsite
import streamlit as st
import streamlit as st
import datetime
import random

# 페이지 설정
st.set_page_config(page_title="오늘의 운세 🔮", page_icon="✨")

# 페이지 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = 0

# 공통 데이터 저장
if "data" not in st.session_state:
    st.session_state.data = {}

# 배경 색 함수
def set_bg(color1, color2):
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(to bottom, {color1}, {color2});
            color: white;
        }}
        </style>
    """, unsafe_allow_html=True)

# 입력 페이지
if st.session_state.page == 0:

    set_bg("#1e1e2f", "#3a0ca3")

    st.title("🔮 운세 여행 시작")
    name = st.text_input("🧑 이름을 입력하세요")

    birthday = st.date_input(
        "🎂 생일 선택",
        min_value=datetime.date(1900,1,1),
        max_value=datetime.date.today()
    )

    if st.button("✨ 시작하기"):
        if name and birthday:

            today = datetime.date.today()
            seed = birthday.month*100 + birthday.day + today.day
            random.seed(seed)

            # 점수 생성
            data = {
                "name": name,
                "zodiac": "",
                "study": random.randint(50,100),
                "love": random.randint(50,100),
                "money": random.randint(50,100),
                "luck": random.randint(50,100),
                "story": random.choice([
                    "오늘은 기회가 당신을 찾아옵니다 ✨",
                    "노력이 빛을 발하는 하루 💪",
                    "사람들과의 관계에서 좋은 일 😊",
                    "조금 쉬어가도 괜찮아요 🛌"
                ]),
                "color": random.choice(["빨강 🔴","파랑 🔵","보라 🟣"]),
                "food": random.choice(["치킨 🍗","피자 🍕","떡볶이 🌶️"]),
                "number": random.randint(1,99)
            }

            st.session_state.data = data
            st.session_state.page = 1
            st.rerun()

        else:
            st.warning("⚠️ 입력을 모두 해주세요!")

# 1️⃣ 전체운
elif st.session_state.page == 1:

    set_bg("#0f2027", "#2c5364")

    d = st.session_state.data

    st.title("🌟 전체 운세")
    st.subheader(f"{d['name']}님의 운세")

    st.write(f"📖 {d['story']}")

    st.write("📊 전체 점수")
    st.progress(d["study"])
    st.progress(d["love"])
    st.progress(d["money"])
    st.progress(d["luck"])

    st.write(f"총 평균: {(d['study']+d['love']+d['money']+d['luck'])//4}점")

    st.balloons()

    if st.button("➡️ 공부운 보기"):
        st.session_state.page = 2
        st.rerun()

# 2️⃣ 공부운
elif st.session_state.page == 2:

    set_bg("#141e30", "#243b55")

    d = st.session_state.data

    st.title("📚 공부운")

    st.progress(d["study"])
    st.write(f"{d['study']}점")

    st.snow()

    if st.button("➡️ 연애운 보기"):
        st.session_state.page = 3
        st.rerun()

# 3️⃣ 연애운
elif st.session_state.page == 3:

    set_bg("#3a1c71", "#d76d77")

    d = st.session_state.data

    st.title("💖 연애운")

    st.progress(d["love"])
    st.write(f"{d['love']}점")

    if st.button("➡️ 금전운 보기"):
        st.session_state.page = 4
        st.rerun()

# 4️⃣ 금전운
elif st.session_state.page == 4:

    set_bg("#134e5e", "#71b280")

    d = st.session_state.data

    st.title("💰 금전운")

    st.progress(d["money"])
    st.write(f"{d['money']}점")

    if st.button("➡️ 행운지수 보기"):
        st.session_state.page = 5
        st.rerun()

# 5️⃣ 행운지수
elif st.session_state.page == 5:

    set_bg("#000428", "#004e92")

    d = st.session_state.data

    st.title("🍀 행운 지수")

    st.progress(d["luck"])
    st.write(f"{d['luck']}점")

    st.divider()

    st.write("🎁 행운 아이템")
    st.write(f"🍀 색: {d['color']}")
    st.write(f"🍔 음식: {d['food']}")
    st.write(f"🔢 숫자: {d['number']}")

    st.balloons()

    if st.button("🔄 다시하기"):
        st.session_state.page = 0
        st.rerun()

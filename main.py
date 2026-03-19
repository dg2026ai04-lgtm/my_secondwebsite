# my_secondwebsite
import streamlit as st
st.title('오늘의 운세를 확인하세요')
import streamlit as st
import datetime
import random

# 페이지 설정
st.set_page_config(page_title="오늘의 운세 🔮", page_icon="✨")

# 제목
st.title("🔮 오늘의 운세 보기")
st.write("생일을 입력하면 오늘의 운세를 알려드려요! 🎂")

# 생일 입력
birthday = st.date_input("🎈 당신의 생일을 선택하세요")

# 운세 리스트
fortunes = [
    "오늘은 행운이 따르는 날이에요! 🍀",
    "작은 기회가 큰 결과로 이어질 수 있어요 ✨",
    "친구와의 대화에서 좋은 일이 생길지도 😊",
    "오늘은 휴식이 필요한 날이에요 🛌",
    "도전하면 좋은 결과가 있을 거예요 💪",
    "뜻밖의 선물이 찾아올 수 있어요 🎁",
    "행복한 일이 당신을 기다리고 있어요 😄",
    "조금만 더 노력하면 성공이 가까워요 🚀"
]

# 버튼
if st.button("🔮 운세 보기"):
    if birthday:
        today = datetime.date.today()

        # 생일 기반 랜덤 시드 (같은 생일이면 비슷한 결과)
        seed = birthday.month * 100 + birthday.day + today.day
        random.seed(seed)

        fortune = random.choice(fortunes)

        st.success(f"✨ 오늘의 운세 ✨\n\n{fortune}")

        # 풍선 효과 🎈
        st.balloons()

        # 추가 메시지
        st.write("💡 오늘도 좋은 하루 보내세요!")
    else:
        st.warning("⚠️ 생일을 먼저 입력해주세요!")

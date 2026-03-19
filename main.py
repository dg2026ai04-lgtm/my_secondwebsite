# my_secondwebsite
import streamlit as st
import streamlit as st
import datetime
import random

# 페이지 설정
st.set_page_config(page_title="운세 게임 🔮", page_icon="✨")

# 제목
st.title("🔮 오늘의 운세 게임")
st.write("이름과 생일을 입력하고 오늘의 운세를 확인해보세요! 🎂")

# 이름 입력
name = st.text_input("🧑 이름을 입력하세요")

# 날짜 범위 설정
min_date = datetime.date(1900, 1, 1)
max_date = datetime.date.today()

# 생일 입력
birthday = st.date_input(
    "🎈 생일을 선택하세요",
    min_value=min_date,
    max_value=max_date
)

# 운세 종류 선택
fortune_type = st.selectbox(
    "🎯 보고 싶은 운세를 선택하세요",
    ["전체운", "공부운 📚", "연애운 💖", "금전운 💰"]
)

# 별자리 계산 함수
def get_zodiac(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "양자리 ♈"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "황소자리 ♉"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "쌍둥이자리 ♊"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "게자리 ♋"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "사자자리 ♌"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 23):
        return "처녀자리 ♍"
    elif (month == 9 and day >= 24) or (month == 10 and day <= 22):
        return "천칭자리 ♎"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        return "전갈자리 ♏"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 24):
        return "사수자리 ♐"
    elif (month == 12 and day >= 25) or (month == 1 and day <= 19):
        return "염소자리 ♑"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "물병자리 ♒"
    else:
        return "물고기자리 ♓"

# 운세 문장들
stories = [
    "오늘은 예상치 못한 기회가 찾아옵니다. 작은 선택이 큰 결과로 이어질 수 있어요 ✨",
    "당신의 노력이 빛을 발하는 하루입니다. 자신감을 가지세요 💪",
    "주변 사람과의 관계에서 좋은 일이 생길 수 있어요 😊",
    "조금 쉬어가는 것도 중요한 하루입니다 🛌",
    "도전하면 뜻밖의 성공을 얻을 수 있어요 🚀"
]

# 행운 요소 리스트
colors = ["빨강 🔴", "파랑 🔵", "초록 🟢", "노랑 🟡", "보라 🟣"]
foods = ["피자 🍕", "햄버거 🍔", "떡볶이 🌶️", "초콜릿 🍫", "치킨 🍗"]

# 버튼
if st.button("🔮 운세 보기"):

    if not name:
        st.warning("⚠️ 이름을 입력해주세요!")
    elif not birthday:
        st.warning("⚠️ 생일을 입력해주세요!")
    else:
        today = datetime.date.today()

        # 랜덤 시드
        seed = birthday.month * 100 + birthday.day + today.day
        random.seed(seed)

        # 별자리
        zodiac = get_zodiac(birthday.month, birthday.day)

        # 점수 생성
        study_score = random.randint(50, 100)
        love_score = random.randint(50, 100)
        money_score = random.randint(50, 100)
        luck_score = random.randint(50, 100)

        # 랜덤 요소
        story = random.choice(stories)
        lucky_color = random.choice(colors)
        lucky_food = random.choice(foods)
        lucky_number = random.randint(1, 99)

        # 결과 출력
        st.subheader(f"🌟 {name}님의 오늘 운세 ({zodiac})")

        # 애니메이션 효과
        st.snow()

        st.write(f"📖 {story}")

        st.divider()

        # 선택한 운세만 강조
        if fortune_type == "공부운 📚":
            st.write("📚 공부운")
            st.progress(study_score)
            st.write(f"{study_score}점")
        elif fortune_type == "연애운 💖":
            st.write("💖 연애운")
            st.progress(love_score)
            st.write(f"{love_score}점")
        elif fortune_type == "금전운 💰":
            st.write("💰 금전운")
            st.progress(money_score)
            st.write(f"{money_score}점")
        else:
            st.write("📊 전체 운세")
            st.write("📚 공부운")
            st.progress(study_score)

            st.write("💖 연애운")
            st.progress(love_score)

            st.write("💰 금전운")
            st.progress(money_score)

            st.write("🍀 행운지수")
            st.progress(luck_score)

        st.divider()

        # 행운 아이템
        st.write("🎁 오늘의 행운 아이템")
        st.write(f"🍀 행운 색: {lucky_color}")
        st.write(f"🍔 행운 음식: {lucky_food}")
        st.write(f"🔢 행운 숫자: {lucky_number}")

        # 풍선 효과
        st.balloons()

        # 다시하기 안내
        st.info("🔄 다시 버튼을 눌러 또 확인해보세요!")

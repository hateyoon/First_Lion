import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import openai

# OpenAI API 키 설정
openai.api_key = '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'

# 데이터 가져오기
df = pd.read_excel('data.xlsx')

# 한글 폰트 경로 설정

# 한국어 폰트 경로
korean_font_path = "경로/한국어폰트.ttf"

# 스트림릿에 한국어 폰트 설정
st.write("한국어 텍스트", font=korean_font_path)


# Streamlit 애플리케이션 구현
st.title("지역별 업장 분석 대시보드")

# 데이터 정제 및 테이블 출력
st.write(df.head(10))

# 데이터 개수 확인
st.metric(label="데이터 갯수", value=f"{df.shape[0]} 개")

# 위치별 라운지 개수 확인 및 그래프 생성
st.bar_chart(df['구분'].value_counts(), height=400, width=600, use_container_width=False)

# 업장 규모 열의 데이터 수치화 및 막대 그래프 생성
st.bar_chart(df['테이블 규모'].value_counts(), height=400, width=600, use_container_width=False)

# 음악 종류에 대한 데이터 빈도 계산
music_count = df['음악종류'].value_counts()

# 원형 그래프 생성 및 표시
st.title("음악 종류별 빈도")
fig, ax = plt.subplots()
ax.pie(music_count.values, labels=music_count.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# 사용자 입력을 받아서 OpenAI로 전송하고 응답을 받아 표시하는 부분
st.title('OpenAI Chatbot')
user_input = st.text_input("사용자 입력", "")
if st.button("전송"):
    response = openai.ChatCompletion.create(
        model="text-davinci-002",
        messages=[
            {"role": "user", "content": user_input}
        ]
    ).choices[0].message['content']
    st.text_area("챗봇 응답", value=response, height=200)

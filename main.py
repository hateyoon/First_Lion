import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from streamlit_option_menu import option_menu
# 한글 폰트 경로 설정
plt.rcParams['font.family'] ='Malgun Gothic'

with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Projects","Contact"],
    icons = ["house","book","envelope"],
    menu_icon = "cast",
    default_index = 0,

  )
st.title("지역별 업장 분석 대시보드")

# 데이터 가져오기
df = pd.read_excel('data.xlsx')
# df
col1, col2 = st.columns(2)
with col1:
    # 데이터 정제
    selected_columns = ['업장명', '구분','위치','테이블 규모','음악종류']
    df_selected = df[selected_columns]
    df_selected[:10]
# 데이터 분석
with col2:
    # 데이터 개수 확인
    lounge_count = df.shape[0]
    st.metric(label="데이터 갯수", value="{} 개".format(lounge_count))
# 위치별 라운지 개수 확인
lounge_count_by_location = df['구분'].value_counts()
lounge_count_by_location
# 그래프 그리기

# Streamlit 애플리케이션 구현
st.bar_chart(lounge_count_by_location,
             height=400,
             width=600,
             use_container_width=False)

# 업장 규모 열의 데이터 수치화
size_count = df['테이블 규모'].value_counts()

# 수치화된 데이터를 바탕으로 막대 그래프 생성
st.bar_chart(size_count,
             height=400,
             width=600,
             use_container_width=False)


import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = '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'

# 대화 생성 함수 정의
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="text-davinci-002",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Streamlit 애플리케이션 구현
st.title('OpenAI Chatbot')

user_input = st.text_input("사용자 입력", "")
if st.button("전송"):
    response = generate_response(user_input)
    st.text_area("챗봇 응답", value=response, height=200)

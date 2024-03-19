import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from streamlit_option_menu import option_menu

# 한글 폰트 경로 설정
plt.rcParams['font.family'] ='Malgun Gothic'

# 첫 번째 Streamlit 애플리케이션: 대시보드
with st.sidebar:
    # 메뉴 옵션 설정
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# 대시보드 표시
if selected == "Home":  # Home 메뉴가 선택되었을 때
    st.title("지역별 업장 분석 대시보드")

    # 데이터 가져오기
    df = pd.read_excel('data.xlsx')
    col1, col2 = st.columns(2)
    with col1:
        # 데이터 정제
        selected_columns = ['업장명', '구분', '위치', '테이블 규모', '음악종류']
        df_selected = df[selected_columns]
        df_selected[:92]
        # Streamlit 애플리케이션 구현

    # 음악종류별 업장 분석 제목
    st.title("음악종류별 업장 분석")

    # 업장 정보 조회 및 출력
    music_type_counts = df['음악종류'].value_counts()

    # 수치화된 데이터를 바탕으로 막대 그래프 생성
    st.bar_chart(music_type_counts,
                 height=400,
                 width=600,
                 use_container_width=False)

    # 데이터 분석
    with col2:
        # 데이터 개수 확인
        lounge_count = df.shape[0]
        st.metric(label="데이터 갯수", value="{} 개".format(lounge_count))

    # 위치별 라운지 개수 확인
    lounge_count_by_location = df['구분'].value_counts()

    # 그래프 그리기
    # '위치' 열의 데이터를 카운트하여 시각화
    location_counts = df['위치'].value_counts()

    # 원형 그래프 생성
    fig, ax = plt.subplots()
    ax.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Streamlit 애플리케이션에 그래프 표시
    st.pyplot(fig)
    st.title("위치별 라운지 개수")

    plt.rcParams['font.family'] = 'Malgun Gothic'

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
    

# 두 번째 Streamlit 애플리케이션: 업장 정보 검색
elif selected == "Contact":  # Contact 메뉴가 선택되었을 때
    st.title("업장 정보 검색")

    # 데이터 가져오기
    df = pd.read_excel('data.xlsx')

    # NaN 값을 제거하여 데이터프레임 업데이트
    df = df.dropna(subset=['업장명'])

    # 사용자로부터 업장명 입력 받기
    search_query = st.text_input("검색할 업장명을 입력하세요:")

    # 업장 정보 조회 및 출력
    if search_query:
        result = df[df['업장명'].str.contains(search_query, na=False)]
        if not result.empty:
            st.write("### 검색 결과:")
            st.write(result)
        else:
            st.write("일치하는 업장이 없습니다.")

import streamlit as st
from openai import OpenAI

client = OpenAI(
  api_key=st.secrets["api_key"],  
)
#openai api key
#openai.api_key = st.secrets["api_key"]

#페이지 레이아웃 설정
st.set_page_config(layout="wide")

#페이지의 메인 이름
st.title("0814 여름학교 ChatGPT API 실습")

# #가로 줄
st.divider()

# #헤더 
st.header("호텔 챗봇")

# #텍스트 출력하기
text = '''
'''
st.write(text)
# st.write("~~~") 의 형태로도 출력 가능

#링크 넣기
st.markdown("[호텔 홈페이지](https://ko.wikipedia.org/wiki/%EC%84%B8%EC%A2%85)")

#학생들이 텍스트 입력하는 곳 만들기
#조사한 자료를 research에 저장
#research = st.text_input("질문을 입력해 주세요:")

#st.write(research)

st.divider()

# 호텔 챗봇
from search import answer_question

# 먼저 메시지 표시하기

# 대화 기록
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# 입력 창 초기화를 위한 키 설정
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# 사용자 입력과 응답을 처리하는 함수
def handle_input():
    user_input = st.text_input("질문을 입력해 주세요:", value=st.session_state.user_input, key="input")
    if st.button("질문하기"):
        if user_input:
            st.session_state.conversation_history.append({"role": "user", "content": user_input})
            answer = answer_question(user_input, st.session_state.conversation_history)
            st.write("ChatGPT: ", answer)
            st.session_state.conversation_history.append({"role": "assistant", "content": answer})
            st.session_state.user_input = ""  # 입력 창 초기화

# 대화 기록 및 입력 창 삭제 함수
def clear_history():
    st.session_state.conversation_history = []
    st.session_state.user_input = ""

# 질문하기 버튼과 삭제하기 버튼
handle_input()
if st.button("삭제하기"):
    clear_history()
    st.write("대화 기록이 삭제되었습니다.")



#while True:
    # 사용자가 입력한 문자를 'user_input' 변수에 저장
 #   user_input = st.text_input("질문을 입력해 주세요:")
    
  #  conversation_history.append({"role": "user", "content": user_input})
   # answer = answer_question(user_input, conversation_history)

    #print("ChatGPT:", answer)
    #conversation_history.append({"role": "assistant", "content":answer})

#ChatGPT API 활용하기 response를 불러오는 함수 만들기
#@st.cache_data #반복 수행을 막아줌
#def gptapi(persona, user):
#    response = client.chat.completions.create(
#        model="gpt-3.5-turbo",
#        messages=[
#            {"role": "system", "content" : persona},
#            {"role": "user", "content": user}
#       ],
#        max_tokens = 200,
#        temperature = 1
#    )
#    return response.choices[0].message.content

#prompt 설정하기
#persona_prompt1 = '''
#너는 역사선생님이야. 세종대왕에 대해 학생들에게 가르쳤어. 학생들이 조사해온 자료를 요약해줘
#'''

#persona_prompt2 = '''
#    너는 역사선생님이야. 학생들이 조사해온 자료를 요악한 내용을 보고, 문제를 만들어줘
#    '''

#클릭해야 실행되도록 버튼 만들기
#if st.button("질문하기"): 
    #복잡한 단계는 나누어 진행하기
#    step1 = gptapi(persona_prompt1, research)
#    st.write(step1)

#    step2 = gptapi(persona_prompt2, step1)
#    st.write(step2)
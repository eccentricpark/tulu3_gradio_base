"""
============================================
Langchain based tulu3

- 이전 답변을 기억
- 스트리밍 형태로 작성
============================================
"""

import gradio as gr
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from src.models.css import get_css

# 모델 설정
model_name = "tulu3"
llmModel = OllamaLLM(model=model_name)

# 메시지 기록 저장
message_history = [
    {
        "role": "system", 
        "content": "당신은 초등학교 선생님입니다. 사용자가 입력한 단어를 초등학생 기준으로 친절하고 다정하게 설명해야 하며, 적절한 예시와 순화표현을 제공해야 합니다."
    }
]

# 응답 생성 함수
def generateResponseStreaming(user_input):
    # 사용자 입력을 메시지 기록에 추가
    message_history.append({
        "role": "user", 
        "content": user_input
    })
    
    # Ollama 모델 호출
    response = llmModel.stream(message_history)
    answer = ""
    for chunk in response:
        answer += chunk
        yield answer

    # 응답을 메시지 기록에 추가
    message_history.append({
        "role": "assistant", 
        "content": answer
    })
    
    return answer

# 응답 생성 함수
def generateResponse(user_input):
    # 사용자 입력을 메시지 기록에 추가
    message_history.append({
        "role": "user", 
        "content": user_input
    })
    
    # Ollama 모델 호출
    response = llmModel.invoke(message_history)
    
    # 응답을 메시지 기록에 추가
    message_history.append({
        "role": "assistant", 
        "content": response
    })
    
    return response

# Gradio 인터페이스 설정
def get_model_by_tulu3_langchain():
    return gr.Interface(
        fn=generateResponseStreaming,
        inputs=gr.Textbox(elem_id='custom_input'),
        outputs=gr.Markdown(elem_id='custom_output'),
        title="Tulu3 8B",
        description="Tulu3 8B입니다.\n\nLangchain이 적용됐습니다.\n기본 프롬프트는 없습니다.",
        analytics_enabled=True,
        css=get_css()
    )

# 인터페이스 실행
if __name__ == "__main__":
    get_model_by_tulu3_langchain().launch()

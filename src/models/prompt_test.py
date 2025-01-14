"""
============================================
Tulu3 8B
프롬프트 테스트를 목적으로 구축된 페이지입니다.
============================================
"""
import gradio as gr
import ollama
import json
from src.models.css import get_css

model_name = "tulu3"
file_path = './src/prompts/meta_prompt.json'
messageList = []

def getPromptByJson():
    with open(file_path, 'r', encoding="utf-8") as file:
        file_data = json.load(file)
    return file_data


def ai_response(input):
    # 사용자 입력을 대화 기록에 추가
    messageList.append({
        'role' : "user",
        "content" : input
    })

    # 시스템 메시지와 대화 기록을 포함한 메시지 목록 생성
    response = ollama.chat(
        model="tulu3", 
        messages=[getPromptByJson(),*messageList], 
        stream=True
    )
    answer = ""

    # 스트리밍 응답 생성
    for chunk in response:
        answer += chunk['message']['content']
        yield answer

    # 모델의 최종 응답을 대화 기록에 추가
    messageList.append({'role': 'assistant', 'content': answer})

def get_model_by_prompt_test():
    # Gradio 입력항목 설정
    return gr.Interface(
        fn=ai_response,
        inputs=gr.Textbox(elem_id='custom_input'),
        outputs=gr.Markdown(elem_id='custom_output'),
        title="Tulu3 8B",
        description="프롬프트 테스트를 목적으로 구축된 페이지입니다.",
        analytics_enabled=True,
        css=get_css()
    )
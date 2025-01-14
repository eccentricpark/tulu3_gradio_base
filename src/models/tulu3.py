"""
============================================
Tulu3 8B
이전 답변을 기억하고 스트리밍 답변을 제공
파일 업로드 기능 추가가
============================================
"""
import gradio as gr
import ollama
from src.models.css import get_css

model_name = "tulu3"
messageList = []


def ai_response(input, file=None):
    # 사용자 입력을 대화 기록에 추가
    messageList.append({
        'role' : "user",
        "content" : input
    })

    if file is not None:
        with open(file.name, 'r', encoding='utf8') as f:
            file_content = f.read()
        messageList.append({
            "role" : "user",
            "content" : f"\n파일내용:{file_content}\n"
        })

    # 시스템 메시지와 대화 기록을 포함한 메시지 목록 생성
    response = ollama.chat(
        model="tulu3", 
        messages=[
            {
                "role" : "system",
                "content" : "",
            },
            *messageList
        ], 
        stream=True
    )
    answer = ""

    # 스트리밍 응답 생성
    for chunk in response:
        answer += chunk['message']['content']
        yield answer

    # 모델의 최종 응답을 대화 기록에 추가
    messageList.append({'role': 'assistant', 'content': answer})

def get_model_by_tulu3():
    # Gradio 입력항목 설정
    return gr.Interface(
        fn=ai_response,
        inputs=[
            gr.Textbox(elem_id='custom_input'),
            gr.File(label="파일 업로드")
        ],
        outputs=gr.Markdown(elem_id='custom_output'),
        title="Tulu3 8B",
        description="Tulu3 8B입니다. 기본 프롬프트는 없습니다.",
        analytics_enabled=True,
        css=get_css()
    )
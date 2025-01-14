"""
============================================
json to text

json 형식의 문자열열은 모두 한 줄로 입력 돼 있습니다.
평문으로 된 문단이나 구조가 잡혀 있는 글로 변환합니다.
============================================
"""
import gradio as gr
import json
from src.models.css import get_css

def response(input: str):
    try:
        # JSON 문자열을 Python 문자열로 변환 (이스케이프 해제)
        output = json.loads(f'"{input}"')
    except json.JSONDecodeError:
        # 잘못된 JSON 입력 처리
        output = "유효하지 않은 JSON 문자열입니다."
    return output

def get_model_json_to_text():
    # Gradio 입력항목 설정
    return gr.Interface(
        fn=response,
        inputs=gr.Textbox(elem_id='custom_input'),
        outputs=gr.Textbox(elem_id='custom_output'),
        title="json to text",
        description="json 형식의 문자열을 평문으로 된 문단이나 구조화 된 글로 변환합니다.",
        analytics_enabled=True,
        css=get_css() # CSS 지정에 반드시 필요합니다.
    )
"""
============================================
Text to Json

평문으로 된 문단이나 혹은 구조가 잡혀 있는 글을
json파일에 입력될 수 있도록, 한 줄로 변환해드립니다.
============================================
"""
import gradio as gr
import json
from src.utils.utils import get_css

def ai_response(input : str):
    output = json.dumps(input, ensure_ascii=False)
    output = output[1:-1]
    return output
def get_model_text_to_json():
    # Gradio 입력항목 설정
    return gr.Interface(
        fn=ai_response,
        inputs=gr.Code(language='html', elem_classes='cm-line'),
        outputs=gr.Textbox(elem_id='custom_output'),
        title="text to json",
        description="json 파일에 들어갈 수 있도록 한 줄로 변환합니다.",
        analytics_enabled=True,
        css=get_css() # CSS 지정에 반드시 필요합니다.
    )
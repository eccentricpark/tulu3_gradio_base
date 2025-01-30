import json
from datetime import datetime

# CSS를 지정합니다.
def get_css():
    custom_css = """ 
    #custom_input textarea .prose * {
        font-size: 16px;
    }
    #custom_output .prose * {
        font-size: 16px;
    }
    .cm-line {
        font-size: 18px !important;
    }
    """
    return custom_css

# 파일이름 연결하여 가져오기, 기본은 ""
def get_file_name_for_save(name=""):
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return f"conversation_{timestamp}_{name}.md"

# json 파일로 저장된 프롬프트 가져오기
def getPromptByJson(filename):
    file_name = f'./src/prompts/{filename}.json'
    with open(file_name, 'r', encoding="utf-8") as file:
        file_data = json.load(file)
    return file_data
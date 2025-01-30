import gradio as gr
import ollama
from src.utils.utils import get_css, get_file_name_for_save, getPromptByJson

model_name = "tulu3"
messageList = []

def ai_response(user_input, chat_history):
    if chat_history is None:
        chat_history = []

    # (1) 사용자 입력을 chat_history와 messageList에 추가
    chat_history.append((user_input, ""))  
    messageList.append({"role": "user", "content": user_input})

    # (2) 입력란 즉시 초기화 -> 첫 번째 yield
    yield chat_history, ""

    # Ollama 스트리밍
    partial_answer = ""
    response = ollama.chat(
        model=model_name,
        messages=[getPromptByJson("landingpage_generate"),*messageList],
        stream=True
    )

    # (3) Partial Response - 스트리밍 진행
    for chunk in response:
        partial_answer += chunk["message"]["content"]
        # chat_history의 마지막 assistant 메시지를 점진적으로 업데이트
        chat_history[-1] = (user_input, partial_answer)
        # Textbox는 계속 빈 문자열 유지
        yield chat_history, ""

    # (4) 최종 답변을 messageList에 저장
    messageList.append({"role": "assistant", "content": partial_answer})
    # 마지막으로 전체 대화 & 빈 입력란을 반환
    yield chat_history, ""


# 파일로 저장
def save_conversation_as_md(chat_history):
    if not chat_history:
        return "대화 내역이 없습니다."

    # 타임스탬프를 이용해 고유한 파일명 생성 (예: conversation_2025_01_31_10_22_35.md)
    filename = get_file_name_for_save(name="landingpage")

    # 대화 내역을 Markdown 형식으로 변환
    md_lines = []
    md_lines.append("# Conversation Log\n")

    for i, (user_msg, assistant_msg) in enumerate(chat_history, start=1):
        md_lines.append(f"**[대화 {i}]**")
        md_lines.append(f"- **User**: {user_msg}")
        md_lines.append(f"- **Assistant**: {assistant_msg}\n")

    # 파일에 쓰기
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    return f"{filename} 파일이 생성되었습니다!"


def get_model_by_landing_page():
    """
    Gradio Blocks로 Chatbot + Textbox 구성 + 파일로 저장 기능 추가
    """
    with gr.Blocks(css=get_css()) as demo:
        gr.Markdown("## Tulu3 8B (Landing page Generator)")

        chatbot = gr.Chatbot(
            elem_id='custom_output', 
            label="대화창",
            height=550
        )

        user_input = gr.Textbox(
            elem_id='custom_input',
            label="사용자 입력",
            placeholder="메시지를 입력하세요..."
        )

        # 엔터로 제출 => ai_response
        user_input.submit(
            fn=ai_response,
            inputs=[user_input, chatbot],
            outputs=[chatbot, user_input]
        )

        # 전송 버튼 클릭 => ai_response
        send_button = gr.Button("전송")
        send_button.click(
            fn=ai_response,
            inputs=[user_input, chatbot],
            outputs=[chatbot, user_input]
        )

        save_button = gr.Button("파일로 저장")

        # 저장 결과를 표시할 영역
        save_result = gr.Markdown()

        # "파일로 저장" 버튼 클릭 => save_conversation_as_md
        save_button.click(
            fn=save_conversation_as_md,
            inputs=[chatbot],     # chat_history
            outputs=[save_result] # 파일 저장 결과 메시지
        )

    return demo
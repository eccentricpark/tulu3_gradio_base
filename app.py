from src.models.index import get_model_by_prompt_fastapi, get_model_by_prompt_flutter, get_model_by_prompt_test, get_model_text_to_json, get_model_json_to_text, get_model_by_tulu3_langchain, get_model_by_tulu3
from fastapi import FastAPI
from gradio import mount_gradio_app

app = FastAPI()
@app.get("/")
def home():
    return "Welcome to Flask with Gradio!"

app = mount_gradio_app(app, get_model_by_prompt_fastapi(), path="/fastapi")
app = mount_gradio_app(app, get_model_by_prompt_flutter(), path="/flutter")
app = mount_gradio_app(app, get_model_text_to_json(), path="/texttojson")
app = mount_gradio_app(app, get_model_json_to_text(), path="/jsontotext")
app = mount_gradio_app(app, get_model_by_prompt_test(), path="/prompttest")
app = mount_gradio_app(app, get_model_by_tulu3(), path="/tulu3")
app = mount_gradio_app(app, get_model_by_tulu3_langchain(), path="/langchain")
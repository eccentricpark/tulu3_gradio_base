from src.models.index import get_model_by_prompt_flutter, get_model_by_landing_page, get_model_text_to_json, get_model_json_to_text, get_model_by_prompt_express_typescript, get_model_by_tulu3
from fastapi import FastAPI
from gradio import mount_gradio_app
from fastapi.responses import HTMLResponse

app = FastAPI()

BASE_URL="http://localhost:8000"
urlDict = {
    "tulu3Url" : '/tulu3',
    # "langchainUrl" : '/langchain',
    "flutterUrl" : '/flutter',
    "textToJsonUrl" : '/texttojson',
    "jsonToTextUrl" : '/jsontotext',
    "landingpageUrl" : '/landingpage',
    "expresstypescriptUrl" : '/express'
}

@app.get("/", response_class=HTMLResponse)
def home():
    innerContent = ""
    for key, value in urlDict.items():
        innerContent = innerContent + f"<h2><a href={BASE_URL}{value}>{key}</a></h2>\n"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head><title>FastAPI HTML Page</title></head>
        <body>
            <h1>Welcome to FastAPI</h1>
            {innerContent}
        </body>
    </html>
    """
    return html_content

app = mount_gradio_app(app, get_model_by_tulu3(), path=urlDict['tulu3Url'])
app = mount_gradio_app(app, get_model_by_prompt_express_typescript(), path=urlDict['expresstypescriptUrl'])
app = mount_gradio_app(app, get_model_by_prompt_flutter(), path=urlDict['flutterUrl'])
app = mount_gradio_app(app, get_model_text_to_json(), path=urlDict['textToJsonUrl'])
app = mount_gradio_app(app, get_model_json_to_text(), path=urlDict['jsonToTextUrl'])
app = mount_gradio_app(app, get_model_by_landing_page(), path=urlDict['landingpageUrl'])
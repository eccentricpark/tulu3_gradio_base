# gradio + ollama 사용하기

[https://innovative-camera-391.notion.site/ollama-python-96566896a32b4b1583dba6cb05df11e5?pvs=4]

- 실제로 제 노트북에서 구동해봤습니다. 문제 없이 잘 돌아갑니다.

## 사전작업
- 이 프로젝트는 **Python 3.10**에서 작업했습니다.
- 가능하면 venv나 conda와 같은 가상환경에서 작업하세요. 
- ollama가 실행된 상태여야 합니다. ollama는 아래 링크에서 다운로드 하세요.
[https://ollama.com/]
<br>

- ollama 실행 유무는 작업표시줄 우측 하단에서 확인할 수 있습니다.
<br><br>

- ollama에서 모델을 하나 내려받아야 합니다. 
- 모델은 아래 명령어 중, 하나를 선택하십시오.
<br><br><br>

```bash
ollama pull Tulu3
ollama pull Llama3.2:1b
ollama pull deepseek-r1:1.5b
ollama pull Llama3.1:8b
```



## 설치하기
가능하면 venv나 anaconda에서 가상환경을 만들어 작업하세요.<br><br>
필요한 라이브러리들은 requirements.txt에 있으니, 아래 명령어로 먼저 라이브러리들을 내려받으십시오.

```bash
pip install -r requirements.txt
```

<br>


## 실행하기
아래 명령어로 실행하면 됩니다.

```bash
uvicorn app:app --reload
```

<br><br>
또는 아래 파일을 실행하는 것도 방법입니다.
```bash
exe.bat
```
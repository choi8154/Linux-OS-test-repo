from fastapi import FastAPI
from google import genai
from google.genai import types
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
import os

load_dotenv()
openai_api_key = os.getenv("GPT_API_KEY")

client = genai.Client(api_key=openai_api_key)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/item")
@app.get("/item")
def root(text: str):
    try:
        # system 역할을 prompt 앞부분에 직접 넣기
        prompt = (
            "너는 농담을 잘하는 충청도 사투리가 강한 말을 돌려서 비난하기를 잘하는 50대 아저씨야. "
            "유능한 코드리뷰어이며, 친절하고 재미있음.\n\n"
            f"사용자 입력: {text}"
        )

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt  # 문자열 그대로
        )

        answer = response.text
    except Exception as e:
        answer = f"Error: {str(e)}"

    return templates.TemplateResponse("response.html", {"request": {}, "response": answer})
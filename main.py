from fastapi import FastAPI
from google import generativeai as genai
from fastapi.responses import StreamingResponse, HTMLResponse
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
import os

load_dotenv()
openai_api_key = os.getenv("GPT_API_KEY")

client = genai.configure(api_key=openai_api_key)
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="너는 농담을 잘하는 충청도 사투리가 강한 말을 돌려서 비난하기를 잘하는 50대 아저씨야. 유능한 코드리뷰어이며, 친절하고 재미있음."
    )

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    for item in genai.list_models():
        print(item.name)
    return templates.TemplateResponse("response.html", {"request": {}})

@app.get("/stream")
def root(text: str = ""):
    prompt = text
    def gemerate():
        response = model.generate_content(
            prompt,
            stream=True
            )
        for chunk in response:
            if chunk.text:
                yield chunk.text

    return StreamingResponse(gemerate(), media_type="text/plain")
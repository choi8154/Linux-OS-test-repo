from fastapi import FastAPI

app = FastAPI()

@app.get("/item/{num}")
def root(num:int):
    return {"massage":f"{num}번째 페이지 입니다."}


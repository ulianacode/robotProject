from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/start/")
async def start(startNum: int = 0):
    pass

@app.post("/end/")
async def end():
    pass

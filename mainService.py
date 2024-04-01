from fastapi import FastAPI
from subprocess import Popen
app = FastAPI()

robot_process = None

@app.get("/start")
async def start_robot():
    global robot_process
    if robot_process is None:
        robot_process = Popen(["python", "robotScript.py", str(0)])
        return {"Robot started."}
    else:
        return {"Robot is already started."}

@app.get("/start/{start_number}")
async def start_robot(start_number: int = 0):
    global robot_process
    if robot_process is None:
        robot_process = Popen(["python", "robotScript.py", str(start_number)])
        return {"Robot started."}
    else:
        return {"Robot is already started."}

@app.get("/stop_robot")
async def stop_robot():
    global robot_process
    pass


from fastapi import FastAPI
from subprocess import Popen

app = FastAPI()


class RobotProcess:
    def __init__(self):
        self.process = None

    def start(self, n):
        if self.process is None:
            self.process = Popen(["python", "robotScript.py", str(n)])
            return True
        return False

    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None
            return True
        return False


robot_process = RobotProcess()


@app.get("/")
async def start_robot():
    return {"This is a robot site."}


@app.get("/start")
async def start_robot():
    if robot_process.start(0):
        return {"Robot started."}


@app.get("/start/{start_number}")
async def start_robot(start_number):
    if robot_process.start(start_number):
        return {"Robot started."}


@app.get("/stop")
async def stop_robot():
    if robot_process.stop():
        return "Robot process stopped."

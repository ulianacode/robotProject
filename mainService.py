from datetime import datetime
from fastapi import FastAPI
from subprocess import Popen

import dataBase

app = FastAPI()


class RobotProcess:
    def __init__(self):
        self.process = None
        self.start_time = None
        self.start_number = None
        self.duration = None
        dataBase.create_database()

    def start(self, start_num):
        if self.process is None:
            self.process = Popen(["python", "robotScript.py", str(start_num)])
            self.start_time = datetime.now()
            self.start_number = start_num if start_num is not None else 0
            return True
        return False

    def stop(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None
            duration = (datetime.now() - self.start_time).total_seconds()
            dataBase.add_database(self.start_time.isoformat(), duration, self.start_number)
            self.start_time = None
            self.start_number = None
            self.duration = None
            return True
        return False


robot_process = RobotProcess()


@app.get("/")
async def main_window():
    return {"This is a robot site."}


@app.get("/start")
async def start_robot():
    robot_process.start(0)
    return {"Robot started. Move to /stop for new session."}


@app.get("/start/{start_number}")
async def start_robot(start_number):
    robot_process.start(start_number)
    return {"Robot started. Move to /stop for new session."}


@app.get("/stop")
async def stop_robot():
    robot_process.stop()
    return "Robot process stopped."


@app.get("/base")
async def data_base():
    data = dataBase.start_database()
    return [{"id": d[0], "start_time": d[1], "duration": d[2], "start_number": d[3]} for d in data]

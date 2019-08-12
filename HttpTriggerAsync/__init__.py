import asyncio
import time
import azure.functions as func

from . import asyncRobot

async def main(req: func.HttpRequest) -> func.HttpResponse:
    s = time.perf_counter()

    robot = asyncRobot.AsyncRobot()
    await robot.doChores()
    
    elapsed = time.perf_counter() - s

    return func.HttpResponse(f"Chores executed in {elapsed:0.2f} seconds.")

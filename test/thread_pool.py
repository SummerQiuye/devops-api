import time
from concurrent.futures import ThreadPoolExecutor
from flask import Flask


app = Flask(__name__)

threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
@app.route("/<int:timenum>")
def threadtest(timenum):
    threadResult = threadPool.submit(timesleep, timenum)
    print(threadResult.result())
    return "success"


def timesleep(timenum):
    time.sleep(timenum)
    print("this is sleep:", timenum)

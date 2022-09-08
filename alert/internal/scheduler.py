import signal

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from threading import Thread

import config

scheduler = BlockingScheduler()


# 定时获取微信接口验证token并更新配置
# @scheduler.scheduled_job('interval', seconds=7201)
def wechatAccessTokenGet():
    access_token = requests.post(url=config.dingApiConfig["getAccessToken"], json=config.dingGetTokenBody).json()[
        "accessToken"]
    config.dingApiConfig["accessToken"] = access_token
    print("get new token:", config.dingApiConfig["accessToken"])


# @scheduler.scheduled_job('interval', seconds=30)
def homeInitData():
    requests.request(url="http://127.0.0.1:5051/cmdb/home/get/initdata", method="post")


# wechatAccessTokenGet()
# 初始化获取最新token
# wechatAccessTokenGet()
# scheduler.add_job(first, 'interval', seconds=5)
# job = Thread(target=scheduler.start)
# job.daemon = True
# job.start()


from apscheduler.schedulers.blocking import BlockingScheduler
import json
from threading import Thread
import subprocess
from ksCluster.module.podStatus import podStatus
from alert.module.sendAlert import SendAlert
from __init__ import app
from config import *
import redis

scheduler = BlockingScheduler()

redisConn = redis.StrictRedis(host=redisHost, port=redisPort, db=redisDB)


# 定时获取微信接口验证token并更新配置
# @scheduler.scheduled_job('interval', seconds=30)
def updatePodStatus():

    devResult = subprocess.Popen("kubectl get po -n test -o wide | tail -n +2",
                                  shell=True, stdout=subprocess.PIPE)
    redisConn.set("devData", devResult.stdout.read().decode("utf8"))
    return json.dumps({"code": 200, "status": "success"})


# @scheduler.scheduled_job('interval', seconds=120)
def checkProdPodStatus():
    # prodPodData = getPodStatusApi("prod")s
    # print(prodPodData)
    with app.app_context():
        statusRe = podStatus("prod").getterPord
        for pod in statusRe:
            ErrorPod = ""
            if pod["podStatus"] != "Running":
                print(pod["podName"])
                ErrorPod += "|"+pod["podName"]
                alertMsg = {
                            "您好，收到自定义报警信息": "",
                            ">告警来源": "python scheduler",
                            ">告警状态": "<font color=\"warning\">触发</font>",
                            ">告警内容": "线上pod状态异常",
                            ">告警条件": "<font color=\"red\">pod status != Running </font>",
                            ">告警服务": ErrorPod
                           }
                SendAlert("wechat", alertMsg, "none").sendAlertByWechat("qiuye")


# 初始化获取最新token
# updatePodStatus()
# scheduler.add_job(first, 'interval', seconds=5)
# job = Thread(target=scheduler.start)
# job.daemon = True
# job.start()

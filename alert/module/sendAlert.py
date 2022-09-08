import datetime
import time

from flask import request, jsonify
import config
import requests
from alert.internal.scheduler import wechatAccessTokenGet
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# noinspection PyTypeChecker
class SendAlert:

    def __init__(self, sendtype, msg, msgfrom):
        self.msg = msg
        self.sendtype = sendtype
        self.msgfrom = msgfrom

    def sendAlertByDing(self, users):
        sendMsgRes = ""
        # print(users)
        config.dingMsgModule["userIds"] = users
        # 格式化传入告警信息json数据
        self.formatMsg()
        # print(self.msg, self.sendtype)
        # 告警消息内容主体
        msgData = config.dingMsgModule
        msgParam = {
            "title": "监控报警：",
            "text": self.msg
        }
        msgData["msgParam"] = str(msgParam)
        print(msgData)

        # 尝试发送消息，重试次数:10，根据状态码判断成功与否
        print("now token:", config.dingApiConfig["accessToken"])
        try:
            for retry in range(10):
                sendMsgUrl = config.dingApiConfig["sendMsg"]
                headers = {"x-acs-dingtalk-access-token": config.dingApiConfig["accessToken"]}
                sendMsgRes = requests.post(url=sendMsgUrl, json=msgData, headers=headers)
                if sendMsgRes.status_code == 200:
                    print("发送消息成功", sendMsgRes.content)
                    break
                else:
                    print("发送消息失败,重试中,", retry + 1, sendMsgRes.content)
                    wechatAccessTokenGet()
                    time.sleep(1)
            if sendMsgRes.status_code != 200:
                print("发送消息失败")
                return jsonify(status="error", code=502, msg="send msg failed.")
        except Exception as e:
            print(e)
            return jsonify(status="error", code=502, msg="send msg failed.")
        return jsonify(status="ok", code=200, msg="send msg success.")

    # 格式化接口告警传入json数据
    def formatMsg(self):
        print(self.msgfrom, self.msg)
        print("====== alertmanater msg =======")
        # 告警来源为cloud的格式化逻辑
        if self.msg and self.msgfrom == "cloud":
            msg = self.msg
            # 重新格式化数据
            try:
                status = ""
                timeResult = ""
                if msg["alarmStatus"] == "1":
                    status = "告警状态: <font color=\"warning\">触发</font> "
                    timeResult = f'触发时间: {msg["firstOccurTime"]}'
                elif msg["alarmStatus"] == "0":
                    status = "告警状态: <font color=\"info\">恢复</font>"
                    timeResult = f'触发时间: {msg["firstOccurTime"]} \n恢复时间: {msg["recoverTime"]}'
                if msg['alarmType'] == 'metric':
                    condition = msg["alarmPolicyInfo"]["conditions"]["metricShowName"] + \
                                msg["alarmPolicyInfo"]["conditions"]["calcType"] + \
                                msg["alarmPolicyInfo"]["conditions"]["calcValue"] + \
                                msg["alarmPolicyInfo"]["conditions"]["unit"]
                    alertData = msg["alarmPolicyInfo"]["conditions"]["currentValue"] + \
                                msg["alarmPolicyInfo"]["conditions"]["unit"]

                    alertObj = ''
                    for obj in msg["alarmObjInfo"]["dimensions"]:
                        alertObj += "\n ---" + obj + ": " + msg["alarmObjInfo"]["dimensions"][obj]
                    msg = f'''您好，接收到腾讯云报警信息：
                            >{status}
                            >告警策略: {msg["alarmPolicyInfo"]["policyName"]}
                            >告警条件: {condition}
                            >当前数据: {alertData}
                            >告警对象: 
                            >{alertObj}
                            >
                            >地域: {msg["alarmObjInfo"]["region"]}
                            >{timeResult}
                            >持续时间: {msg["durationTime"]}s
                            >告警时间: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
                    '''
                    print(msg)
                elif msg['alarmType'] == 'event':
                    print("event")
                    msg = f'''您好，接收到腾讯云报警信息：
                            >{status}
                            >告警策略: {msg["alarmPolicyInfo"]["policyName"]}
                            >告警内容: {msg["alarmPolicyInfo"]["conditions"]["eventShowName"]}
                            >告警对象: {msg["alarmObjInfo"]["dimensions"]["objDetail"]}
                            >地域: {msg["alarmObjInfo"]["region"]}
                            >{timeResult}
                            >持续时间: {msg["durationTime"]}s
                            >告警时间: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
                    '''
                self.msg = msg
            except Exception as e:
                print(e)
                self.msg = str(msg)
                print("msg format can not discern")
        elif self.msg and self.msgfrom == "alertmanager":
            # print(self.msg)
            msg = self.msg

            status = ""
            timeResult = ""
            # alertmanager时间转格式化
            UTC_FORMAT = "%Y-%m-%dT%H:%M:%S"
            total = ""
            for alertDatas in msg["alerts"]:
                # 报警开始时间
                print(alertDatas)
                timeStart = alertDatas["startsAt"].split(".")[0]
                utcTimeStart = datetime.datetime.strptime(timeStart, UTC_FORMAT)
                timeStartFormat = utcTimeStart + datetime.timedelta(hours=8)

                if alertDatas["status"] == "firing":

                    status = "### 告警状态: <font color=\"warning\">触发</font> "

                    # 报警时间数据添加
                    timeResult = f'### 触发时间: {timeStartFormat}'

                elif alertDatas["status"] == "resolved":

                    status = "### 告警状态: <font color=\"info\">恢复</font> "

                    # 结束时间
                    timeEnd = alertDatas["endsAt"].split(".")[0]
                    utcTimeEnd = datetime.datetime.strptime(timeEnd, UTC_FORMAT)
                    timeEndFormat = utcTimeEnd + datetime.timedelta(hours=8)

                    # 持续时间
                    timeTotal = utcTimeEnd - utcTimeStart
                    print(timeTotal)

                    # 报警时间数据添加
                    timeResult = f'### 触发时间: {timeStartFormat} \n' \
                                 f'### 恢复时间: {timeEndFormat} \n' \
                                 f'### 持续时间: {timeTotal}'

                # 告警内容格式化
                alertObj = ""
                for alertLabel in alertDatas["labels"]:
                    alertObj += f'### -{alertLabel} : {alertDatas["labels"][alertLabel]} \n'
                    # print(alertObj)
                msg = f'![hunteron](https://hh.hunteron.com/static/img/logo.dd435b6.png "test") \n' \
                      f'# 您好，监控中心报警信息： \n' \
                      f'{status} \n' \
                      f'### 告警策略: {alertDatas["labels"]["alertname"]} \n' \
                      f'### 告警对象: {alertDatas["annotations"]["description"]} \n' \
                      f'### 告警内容: \n' \
                      f'{alertObj} \n' \
                      f'{timeResult} \n' \
                      f'[链接: 报警详情](http://alert.devops.com)'
                total += str(msg)
            self.msg = total
            print(self.msg)
        elif self.msg:
            msg = ""
            for data in self.msg:
                print(data)
                msg += "### " + str(data["alarmMessage"]) + "\n"
            self.msg = msg + "### 告警时间: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"

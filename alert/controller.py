import time

from __init__ import app
from flask import request, jsonify, abort
from alert.module.sendAlert import SendAlert
# from alert.module.sendTelAlert import callPhone
# noinspection PyUnresolvedReferences
from alert.internal import scheduler
import config
from flasgger import swag_from


@app.route("/sendAlert/<string:sendtype>/<string:msgfrom>/<string:token>", methods=["POST"])
@swag_from('/alert/document/sendAlert.yml')
def sendAlertApi(sendtype, token, msgfrom):
    timeRangeStart = request.args.get("timeStart")
    timeRangeEnd = request.args.get("timeEnd")
    currTime = time.strftime("%H", time.localtime())
    if timeRangeStart and timeRangeEnd:
        print(int(timeRangeStart), int(timeRangeEnd), int(currTime))
        if int(currTime) in range(int(timeRangeStart), int(timeRangeEnd)):
            return "告警过滤时间内"
    if config.token != token:
        return abort(403)
    msg = request.json
    # assert msg
    methodInvoking = SendAlert(sendtype=sendtype, msg=msg, msgfrom=msgfrom)
    if sendtype == "ding":
        # users = str(request.args.get("user")).replace(";", "|").replace("_", "|").split("|")
        usergroup = request.args.get("usergroup")
        if usergroup == "bigdata":
            users = config.dingBigdataUserList
        elif usergroup == "saas":
            users = config.dingSaasUserList
        elif usergroup == "hunteron":
            users = config.dingHunteronUserList
        elif usergroup == "ops":
            users = config.dingOpsUserList
        else:
            users = config.dingOpsUserList
        print(users)
        return methodInvoking.sendAlertByDing(users)
    elif sendtype == "mail":
        return methodInvoking.sendAlertByMail()
    return jsonify(status="error", msg="argument can not resolved.")


# @app.route("/sendTelAlert/<string:params>/<string:token>", methods=["POST"])
# @swag_from('/alert/document/sendTelAlert.yml')
# def sendTelAlertApi(params, token):
#     # currTime = time.strftime("%H", time.localtime())
#     # print(currTime)
#     if config.token != token:
#         return abort(403)
#     telArgs = str(request.args.get("tel")).split("_")
#     if telArgs[0] != 'None':
#         phoneList = telArgs
#     else:
#         phoneList = config.phone_numbers
#     print(phoneList)
#     return callPhone(params, phoneList)

import uuid
import os
import random
from datetime import datetime
from sqlAlchemy import *
from flask_maple.serializer import Serializer
from flask import jsonify
from sentry_sdk import capture_exception, capture_message

class userMask:

    def __init__(self, **kwargs):
        self.args = kwargs['args']

    def auth(self):
        userMac = self.args["mac"]
        userName = self.args["username"]
        try:
            result = ProxyGateway.query \
                .filter(ProxyGateway.proxyMac == userMac, ProxyGateway.proxyUserName == userName).all()
            data = Serializer(result).data
            print(data)
            userMacList = []
            for userData in data:
                print(userData)
                userMacList.append(userData["proxyMac"])
            db.session.commit()
            assert userMac in userMacList
            print("mac地址校验通过:", userMac)
            token = ''.join(random.sample('AbcaubB12KL3JNbu7wqeCXAS45D343csdcdwpik2jNKVTUVcwe467cq', 15))
            userProxyName = userName + userMac + token + ".pac"
            print(userProxyName)
            os.system("rm -rf mac_address_proxy_file/" +
                      userName +
                      "* & cp proxy.pac mac_address_proxy_file/" + userProxyName)
            return "http://ip:8200/" + userProxyName
        except Exception as e:
            print(e)
            capture_exception(e)
            print("mac地址校验失败:", userMac)
            db.session.rollback()
            return "failed"
        finally:
            print(datetime.now(), "[devops-api] [info] [T1] ", "message: 返回用户proxy地址成功. success!")

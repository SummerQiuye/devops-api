from config import *
import redis

redisConn = redis.StrictRedis(host=redisHost, port=redisPort, db=redisDB)


class podStatus:

    def __init__(self, env):
        self.env = env

    @property
    def getterDev(self):
        return self.serializeStatus("dev")

    @property
    def getterPord(self):
        return self.serializeStatus("prod")

    @staticmethod
    def serializeStatus(dataEnv):
        global data
        if dataEnv == "dev":
            data = redisConn.get("devData").decode("utf-8")
        elif dataEnv == "prod":
            data = redisConn.get("prodData").decode("utf-8")
        podDict = []
        for dataLines in data.split("\n"):
            dataList = dataLines.split(" ")
            while '' in dataList:
                dataList.remove('')
            # print(dataList)
            if dataList and len(dataList) > 0:
                podDict.append({
                    "podName": dataList[0],
                    "podNum": dataList[1],
                    "podStatus": dataList[2],
                    "podRestartCount": dataList[3],
                    "podAge": dataList[4],
                    "podClusterIp": dataList[5],
                    "podRunNode": dataList[6]
                })
        return podDict




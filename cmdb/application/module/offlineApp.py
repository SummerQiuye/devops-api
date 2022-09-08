from flask import request, jsonify
import subprocess
import config


class Manager:

    def __init__(self, **kwargs):
        super().__init__()
        self.kwargs = kwargs


    def getter(self):
        print("this env:", self.kwargs['appenv'])
        data = subprocess.Popen(f"kubectl get pod -n {self.kwargs['appenv']} -o wide "
                                f"| tail -n +2 | grep '{self.kwargs['filter']}'",
                                     shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf8")
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
                    "podRunNode": dataList[6],
                    "podEnv": self.kwargs['appenv']
                })
        print(podDict)
        return {"stats": "200", "msg": "调用成功", "data": podDict, "count": len(podDict)}

    def terminal(self):
        self.appname = self.kwargs["appname"]
        self.appenv = self.kwargs["appenv"]
        if self.appenv in ["test", "uat", "htest"]:
            self.shell = "/bin/bash"
        else:
            self.shell = "/bin/sh"
        print("this:", self.appenv, self.appname)
        assert self.appname,self.appenv
        url = f"http://172.20.10.1:8088/?arg={self.appname}&arg=-n&arg={self.appenv}&arg={self.shell}"
        return {"stats": "200", "msg": "调用成功", "data": url}

    def logs(self):
        self.appname = self.kwargs["appname"]
        self.appenv = self.kwargs["appenv"]
        print("this:", self.appenv, self.appname)
        data = subprocess.Popen(f"kubectl logs --tail=100 {self.appname} -n {self.appenv}",
                                shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf8")
        return {"stats": "200", "msg": "调用成功", "data": data}

    def searchLogs(self):
        print("this:",
              self.kwargs["appname"],
              self.kwargs["appenv"],
              self.kwargs["filter"]['data'].replace(' ','').replace(';', '|')
              )

        filters = self.kwargs["filter"]['data'].replace(' ','').replace(';', '|')

        if filters == '':
            return {"stats": "200", "msg": "调用成功", "data": '筛选条件为空.'}

        data = subprocess.Popen(f"kubectl logs {self.kwargs['appname']} -n {self.kwargs['appenv']} | egrep '{filters}' | tail -n 100",
                                shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf8")
        if data == '':
            return {"stats": "200", "msg": "调用成功", "data": '没有查到您要的数据.'}
        # print(data)
        return {"stats": "200", "msg": "调用成功", "data": data}

    def restart(self):
        self.appname = self.kwargs["appname"]
        self.appenv = self.kwargs["appenv"]
        print("this:", self.appenv, self.appname)
        data = subprocess.Popen(f"kubectl delete po {self.appname} -n {self.appenv} --force",
                                shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf8")

        return {"stats": "200", "msg": "调用成功", "data": data}
import requests
import json
import time


class initMonitorData:

    def __init__(self):
        self.promurl = "http://prome.devops.com/api/v1/query?"
        self.promurl_online = "http://172.30.0.42:30003/api/v1/query?"
        self.sumdata = {
            "ecs": self.ecs(),
            "mysql": self.mysql(),
            "redis": self.redis(),
            "k8sprod": self.k8sprod(),
            "k8sdev": self.k8sdev(),
            "nginx": self.nginx(),
            "php": self.php(),
            "total": self.total()
        }

    def requestprom(self, url, query):
        if url == "online":
            data = self.promurl_online
        else:
            data = self.promurl
        try:
            response = requests.post(data + query)
            value = json.dumps(response.json()["data"]["result"][0])
            # print("cvm", json.loads(value)["value"][1])
            return int(json.loads(value)["value"][1])
        except Exception as e:
            print("no data", e)
            return 0

    def ecs(self):
        return [self.requestprom("ops", 'query=sum(up{job="node_exporter"} == 0) by (job)'),
                self.requestprom("ops", 'query=sum(up{job="node_exporter"} == 1) by (job)')]

    def nginx(self):
        return [self.requestprom("ops", 'query=sum(up{job="nginx_exporter"} == 0) by (job)'),
                self.requestprom("ops", 'query=sum(up{job="nginx_exporter"} == 1) by (job)')]

    def k8sdev(self):
        return [self.requestprom("ops",
                                 'query=sum(kube_pod_container_status_ready{namespace="dev"} == 0) by (namespace)'),
                self.requestprom("ops",
                                 'query=sum(kube_pod_container_status_ready{namespace="dev"} == 1) by (namespace)')]

    def k8sprod(self):
        ops_ok = self.requestprom("ops",
                                  'query=sum(kube_pod_container_status_ready{namespace="prod"} == 1) by (namespace)')
        online_ok = self.requestprom("online",
                                     'query=sum(kube_pod_container_status_ready{namespace="prod"} == 1) by (namespace)')
        ops_down = self.requestprom("ops",
                                    'query=sum(kube_pod_container_status_ready{namespace="prod"} == 0) by (namespace)')
        online_down = self.requestprom("online",
                                       'query=sum(kube_pod_container_status_ready{namespace="prod"} == 0) '
                                       'by (namespace)')
        # print("k8sprod", str(int(ops_num) + int(online_num)))
        return [ops_down + online_down, ops_ok + online_ok]

    def redis(self):
        return [self.requestprom("ops", 'query=sum(up{job="redis_exporter"} == 0) by (job)'),
                self.requestprom("ops", 'query=sum(up{job="redis_exporter"} == 1) by (job)')]

    def mysql(self):
        return [self.requestprom("ops", 'query=sum(up{job="mysqld_exporter"} == 0) by (job)'),
                self.requestprom("ops", 'query=sum(up{job="mysqld_exporter"} == 1) by (job)')]

    def php(self):
        return [self.requestprom("ops", 'query=sum(up{instance=~".*:9253"} == 0)'),
                self.requestprom("ops", 'query=sum(up{instance=~".*:9253"} == 1)')]

    def total(self):
        ops_ok = self.requestprom("ops", 'query=sum(up == 1)')
        online_ok = self.requestprom("online", 'query=sum(up == 1)')
        ops_down = self.requestprom("ops", 'query=sum(up == 0)')
        online_down = self.requestprom("online", 'query=sum(up == 0)')
        print(ops_ok, online_ok)
        return [ops_down + online_down, ops_ok + online_ok]

    def sumDataResponse(self):
        print(self.sumdata)
        return self.sumdata

# print(time.time())
# initMonitorData().sumDataResponse()
# print(time.time())

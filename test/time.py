import time
import datetime


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

test = {
    'sessionId': '7MgySx6a1cbSEGuUZCQLwPPE',
    'alarmStatus': '0',
    'alarmType': 'metric',
    'alarmObjInfo': {'region': 'sh', 'namespace': 'qce/cdb', 'dimensions': {'objId': 'a2a5d35b-bc0e-11ea-b5fe-80b575d7cbda', 'objName': 'cdbro-8q4tsa9s(实例名:bingtang-log,IP:172.17.16.18:3306)', 'uInstanceId': 'cdbro-8q4tsa9s'}}, 'alarmPolicyInfo': {'policyId': 'policy-7iw4zh99', 'policyType': 'cdb_detail', 'policyName': 'mysql(定时任务过滤)', 'policyTypeCName': '云数据库-MySQL-主机监控', 'policyTypeEname': '', 'conditions': {'metricName': 'cpu_use_rate', 'metricShowName': 'CPU利用率 ', 'calcType': '>', 'calcValue': '90', 'currentValue': '18.149', 'unit': '%', 'period': '60', 'periodNum': '60', 'alarmNotifyType': 'singleAlarm', 'alarmNotifyPeriod': 3}},
    'firstOccurTime': '2020-11-23 17:36:00',
    'durationTime': 240,
    'recoverTime': '2020-11-23 17:40:00'
}

if 7 in range(23, 24):
    print("告警过滤时间内")
if 7 in range(0, 9):
    print("告警过滤时间内")

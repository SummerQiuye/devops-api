# project config center
# import logging
# import graypy
from DBUtils.PooledDB import PooledDB
import pymysql
import pymysql.cursors

pymysql.install_as_MySQLdb()

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    cursorclass=pymysql.cursors.DictCursor,
    maxconnections=60,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=10,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=10,  # 这个参数没多大用，最大可以被大家共享的链接
    # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，
    # 所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested,
    # 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    charset='utf8',
    host="172.20.10.1",
    port=3306,
    user="root",
    password="",
    database=""
)
#
# my_logger = logging.getLogger('devops-api')
# my_logger.setLevel(logging.INFO)
#
#
# handler = graypy.GELFTCPHandler('10.0.0.3', 30068)
# my_logger.addHandler(handler)
#
# my_logger.info('devops api server started.')

# get all git project api，per_pae & page={page_num}
gitUrl = "http://gitlab.devops.com/api/v4/projects?private_token=tAxx4Qq9rXsyzgxBET9R&per_page=100&page="
gitWeb = 'http://gitlab.devops.com'
gitToken = ""

# 加密接口调用私钥认证
token = ""

# 监控报警应用access_token获取api
# wechatApi = {"getAccessToken": "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww447ba72061aff183&"
#                                "corpsecret=OLFBZKkl9Y37YPM6L4hXHA7KRNTjYp0JRUhsubsXs64",
#              "sendMsg": "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}",
#              "accessToken": ""
#              }
# # 企业微信应用id
# wechatAPPid = 1000017


# 钉钉<监控中心>机器人配置信息
dingApiConfig = {"getAccessToken": "https://api.dingtalk.com/v1.0/oauth2/accessToken",
                 "sendMsg": "https://api.dingtalk.com/v1.0/robot/oToMessages/batchSend",
                 "accessToken": ""
                 }
# 钉钉<监控中心>机器人获取消息推送token验证配置数据
dingGetTokenBody = {
    "appKey": "",
    "appSecret": ""
}
# 钉钉<监控中心>机器人appkey
dingAppKey = ""
dingAppId = 14232002
# 钉钉报警用户id列表
dingUserIdList = {
    
}
dingSaasUserList = []
dingHunteronUserList = []
dingBigdataUserList = []
dingOpsUserList = []
# 钉钉报警消息模板
dingMsgModule = {
    "robotCode": "dingzmukihagryekhrp5",
    "userIds": [],
    "msgKey": "sampleMarkdown",
    "msgParam": ""
}

# 应用状态缓存库
redisHost = ""
redisPort = 6379
redisDB = 0

# ldap
ldap = {"server": "172.20.10.1", "dc": "cn=admin,dc=ldap,dc=com", "passwd": ""}

# 语音消息应用 SDK AppID
appid = 1400466223  # SDK AppID 以1400开头
# 语音消息应用 App Key
appkey = ""
# 需要发送语音消息的手机号码
phone_numbers = ["13012862013"]
# 语音模板 ID，需要在语音消息控制台中申请
template_id = 823115  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在语音消息控制台中申请

adminRole = ["ye.qiu", "jin.he"]

lineappdata = {
    "hunteron": {
        "prod": 6,
        "qa": 6,
        "dev": 0,
        "uat": 0
    },
    "saas": {
        "prod": 25,
        "qa": 25,
        "dev": 0,
        "uat": 0
    },
    "ops": {
        "prod": 15,
        "qa": 15,
        "dev": 0,
        "uat": 0
    },
    "bigdata": {
        "prod": 5,
        "qa": 5,
        "dev": 0,
        "uat": 0
    }
}

document = {
    "运维中台": "http://url/",
    "监控图表": "http://grafana",
}

platform_notice = '''
    <p style='color:blue'>发布日：每周二、周四.<p> \
    <br> \
    <p style='color:red'>2022-09-06: <p> \
    <br> \
    增加：测服集群服务搜索功能. <br> \
    <br> \
    优化：部分UI. <br> \
    <br> \
    <p style='color:red'>2022-09-05: <p> \
    <br> \
    增加：测服集群日志搜索功能. <br> \
    <br> \
    优化：部分界面展示及自适应. <br> \
    <br> \
    <p style='color:red'>2022-09-02: <p> \
    <br> \
    增加：线下集群管理模块(集群基础状态、服务控制台、服务日志、服务重启。) <br> \
    <br> \
    修复：部分UI显示问题 <br> \
    <br> \
    <p style='color:blue'>更新日志：20220826_v1<p> \
    <br> \
    <p style='color:red'>联系运维：ops@hunteron.com。<p>
'''

work_order = {
    "工单-20220726-001": " 平台功能测试"
}

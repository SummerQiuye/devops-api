# 公共方法生成模块
def defineApiType(id, type):
    # 根据传入项目id及api调用方法生成api接口
    return "http://gitlab.devops.com/api/v4/projects/{}/repository/{}?" \
           "private_token=tAxx4Qq9rXsyzgxBET9R&per_page=100".format(id, type)

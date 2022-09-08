#--* utf-8 *--
import logging
from functools import lru_cache
import requests
from flask import Flask, request, jsonify, render_template, url_for
import config


app = Flask(__name__)
url = config.gitUrl


# log module
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("cicd.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


# 定义接口地址
def defineApiType(id, type):
    # 根据传入项目id及api调用方法生成api接口
    return "http://gitlab-tech.shruisong.cn/api/v4/projects/{}/repository/{}?" \
           "private_token=bh2b3sxpxSJoTdSH2z3o&per_page=100".format(id, type)


# 获取项目tags列表
@app.route("/branchTagList/<int:id>", methods=["POST", "GET"])
def TagsManager(id):
    """
    :param
        /branchTagList?id=[project_id]
    :return:
    """
    branch_url = defineApiType(id, "branches")
    tag_url = defineApiType(id, "tags")
    branchInfo = requests.get(branch_url)
    tagInfo = requests.get(tag_url)
    branch_result = branchInfo.json()
    tag_result = tagInfo.json()
    returnList = []
    for name in tag_result:
        returnList.append(name["name"])
    for name in branch_result:
        returnList.append(name["name"])
    # print(len(returnList))
    return str(returnList)


# 创建项目tag
@app.route("/createTag", methods=["POST", "GET"])
def createTag():
    env = request.args.get("env")
    tag_url = defineApiType("tags")
    ref = request.args.get('ref')
    # num = envTagNumCalcute()
    num = 1
    branchName = str(ref).split("/")[0]
    branchId = str(ref).split("/")[1]
    if env == "prod":
        if num != "0":
            return "prod just allow one time to build."
        name = str(ref).split("/")[1]
    else:
        if branchName == "feature" or branchName == "longterm":
            name = branchName+"-"+branchId+"."+str(int(num)+1)
        else:
            name = str(ref).split("/")[1]+"-"+str(env)+"."+str(int(num)+1)
    tag_name = name
    print("tag_name:",tag_name)
    createTagFromLastBranch = tag_url + "&tag_name={}&name={}&ref={}".format(tag_name, name, ref)
    print("create tag url:",createTagFromLastBranch)
    createNewTag = requests.post(createTagFromLastBranch)
    print("this tag is :",tag_name)
    return str(tag_name)


# 获取项目所有分支名
@app.route("/branchList", methods=["POST", "GET"])
def getAllProjectBranch():
    '''
    :param
        /branchs?project=[projectName]&env=[envName]
    :return:
    '''
    project_url = defineApiType("branches")
    apiInfo = requests.get(project_url)
    branch_result = apiInfo.json()
    branch_list = []
    for i in branch_result:
        branch_name = i['name']
        branch_list.append(branch_name)
    return jsonify(branch_list)

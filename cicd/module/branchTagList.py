import requests
from flask import jsonify

from cicd.module.defineApiType import defineApiType
import gitlab
from config import *

# private token or personal token authentication
gl = gitlab.Gitlab(gitWeb, private_token=gitToken, api_version="4")


def branchTagList(project_id):
    """
    :param
        /branchTagList?id=[project_id]
    :return:
    """
    branch_url = defineApiType(project_id, "branches")
    print(branch_url)
    tag_url = defineApiType(project_id, "tags")
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
    try:
        returnList.index("dev")
        returnList.remove("dev")
        returnList.append("dev")
    except Exception as e:
        print(e)
    return jsonify(returnList)


# 调用python-gitlab模块操作gitlab api
def branchTagListV2(project_id):
    print(project_id)
    project = gl.projects.get(project_id)
    print(project)
    branchlist = project.branches.list(all=True)
    # tagList = project.tags.list(per_page=50)
    # mergeList = tagList+branchlist
    mergeList = branchlist
    returnList = []
    for i in mergeList:
        returnList.append(i.attributes["name"])
    # print(returnList)
    try:
        returnList.index("dev")
        returnList.remove("dev")
        returnList.append("dev")
    except Exception as e:
        print(e)
    return jsonify(returnList)

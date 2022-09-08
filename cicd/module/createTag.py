import time

from flask import request, jsonify
from cicd.module.defineApiType import defineApiType
import requests
import json
from config import *

import gitlab

# private token or personal token authentication
gl = gitlab.Gitlab(gitWeb, private_token=gitToken)


# 创建项目tag
def createTag(project_id, ref, build_id):
    '''
    :param build_id:
    :param project_id:
    :param ref:
    :return:
    '''
    tag_url = defineApiType(project_id, "tags")
    tag_time = time.strftime("%m-%d_%H.%M", time.localtime())
    tag_name = tag_time+'_'+ref
    print("tag_name:", tag_name)
    createTagFromLastBranch = tag_url + "&tag_name={}&name={}&ref={}".format(tag_name+'_'+build_id, tag_name, ref)
    print("create tag url:", createTagFromLastBranch)
    createNewTag = requests.post(createTagFromLastBranch)
    print("this tag is :", createNewTag.json())
    return jsonify({"content": createNewTag.json()})


# 调用python-gitlab模块进行gitlab创建tag操作
def createTagV2(project_id, ref, version, set_release_description):
    project = gl.projects.get(project_id)
    # print(project)
    try:
        tags = project.tags.create({'tag_name': version, 'ref': ref})
        # 添加tags描述 -- release说明
        # print(set_release_description)
        # tags.set_release_description(set_release_description['description'])
        # 输出转字典格式
        resultData = tags.attributes
        # print(resultData)
        print({"code": "200", "status": "create tag success."})
    except Exception as e:
        print(e)
        return jsonify({"code": "400", "status": "create tag error or tag exists."})
    return jsonify(resultData)


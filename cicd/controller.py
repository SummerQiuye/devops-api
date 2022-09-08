from flasgger import swag_from

from __init__ import app
from cicd.module.branchTagList import *
from cicd.module.createTag import *
from flask import request


@app.route("/branchTagList/<int:project_id>", methods=["GET"])
@swag_from('/cicd/document/branchTagList.yml')
def branchTagListApi(project_id):
    return branchTagList(project_id)


@app.route("/branchTagList/v2/<int:project_id>", methods=["GET"])
@swag_from('/cicd/document/branchTagListV2.yml')
def branchTagListApiV2(project_id):
    return branchTagListV2(project_id)


@app.route("/createTag/<int:project_id>/<string:ref>/<string:build_id>", methods=["GET"])
@swag_from('/cicd/document/createTag.yml')
def createTagApi(project_id, ref, build_id):
    return createTag(project_id, ref, build_id)


@app.route("/createTag/v2/<int:project_id>/<string:ref>/<string:version>", methods=["POST"])
@swag_from('/cicd/document/createTagV2.yml')
def createTagApiV2(project_id, ref, version):
    set_release_description = request.json
    return createTagV2(project_id, ref, version, set_release_description)


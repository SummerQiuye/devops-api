from flasgger import swag_from
from alert.module.roleAuthMatching import authwapper
from __init__ import app
from flask import request
from cmdb.config.module import getConfig, searchConfig, updateConfig, removeConfig


@app.route("/cmdb/config/get/<string:configEnv>", methods=["GET"])
@swag_from('/cmdb/config/document/getConfig.yml')
def getConfigApi(configEnv):
    """
    :param configEnv:
    :return:
    """

    args = request.args if request.args else {}

    if configEnv == "dev":
        return getConfig.getDevConfig(args)
    elif configEnv == "prod":
        return getConfig.getProdConfig(args)


@app.route("/cmdb/config/search/<string:configEnv>", methods=["GET"])
@swag_from('/cmdb/config/document/searchConfig.yml')
def searchConfigApi(configEnv):

    args = request.args if request.args else {}

    if configEnv == "dev":
        return searchConfig.searchDevConfig(args)
    elif configEnv == "prod":
        return searchConfig.searchProdConfig(args)


@app.route("/cmdb/config/update/<string:configEnv>", methods=["POST"])
@swag_from('/cmdb/config/document/updateConfig.yml')
def updateConfigApi(configEnv):

    args = request.json if request.json else {}
    user = request.headers["Authentication"].split(';')[1].split('=')[1]

    if configEnv == "dev":
        return updateConfig.updateDevConfig(args, user)
    elif configEnv == "prod":
        return updateConfig.updateProdConfig(args,  user)


@app.route("/cmdb/config/remove/<string:configEnv>", methods=["DELETE"])
# @swag_from('/cmdb/property/document/offlineProperty.yml')
@authwapper
def removeConfigApi(configEnv):
    """
    :param: internal_ip
    :return:
    """

    args = request.json if request.json else {}

    if configEnv == "dev":
        return removeConfig.removeDevConfig(args)
    elif configEnv == "prod":
        return removeConfig.removeProdConfig(args)

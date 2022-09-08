from flasgger import swag_from

from __init__ import app
from flask import jsonify
# from ksCluster.internal import scheduler
from ksCluster.module.podStatus import podStatus


@app.route("/getPodStatus/<string:env>", methods=["GET"])
@swag_from('/ksCluster/document/getPodStatus.yml')
def getPodStatusApi(env):
    if env == "dev":
        statusRe = podStatus(env).getterDev
    elif env == "prod":
        statusRe = podStatus(env).getterPord
    else:
        return jsonify({"msg": "env args error."})
    # print(statusRe)
    return jsonify(statusRe)

from flasgger import swag_from
from __init__ import app
from flask import request
from cmdb.proxyGateway.module.userMask import userMask


@app.route("/cmdb/proxygateway/mask", methods=["GET", "POST"])
# @swag_from('/cmdb/navigation/document/getInitData.yml')
def mask():
    """
    :return:
    """
    args = request.args if request.args else {}
    return userMask(args=args).auth()

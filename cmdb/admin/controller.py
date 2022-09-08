from flasgger import swag_from
from __init__ import app
from flask import request
from cmdb.admin.module.vpnUserList import VpnUserList


@app.route("/cmdb/admin/vpn/getUserList", methods=["GET", "POST"])
# @swag_from('/cmdb/navigation/document/getInitData.yml')
def getUserListApi():
    """
    :return:
    """
    args = request.args if request.args else {}
    return VpnUserList(args).getter()

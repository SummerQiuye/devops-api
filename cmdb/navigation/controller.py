from flasgger import swag_from
from __init__ import app
from cmdb.navigation.module.initData import InitData


@app.route("/cmdb/navigation/get", methods=["GET", "POST"])
# @swag_from('/cmdb/navigation/document/getInitData.yml')
def getNavigation():
    """
    :return:
    """

    return InitData().getter()

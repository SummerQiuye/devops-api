from flasgger import swag_from
from alert.module.roleAuthMatching import authwapper
from __init__ import app
from flask import request
from cmdb.property.module.cloud import Cloud


@app.route("/cmdb/property/get/<string:ptype>", methods=["POST"])
@swag_from('/cmdb/property/document/getProperty.yml')
def getPropertyApi(ptype):
    """
    :param ptype:
    :return:
    """
    args = request.args if request.args else {}

    return Cloud(ptype=ptype).getter(args=args)


@app.route("/cmdb/property/search/<string:ptype>/<string:searchType>", methods=["POST"])
@swag_from('/cmdb/property/document/searchProperty.yml')
def searchPropertyApi(ptype, searchType):
    """
    :param ptype:
    :param searchType:
    :return:
    """
    args = request.args if request.args else {}

    return Cloud(ptype=ptype, searchType=searchType).search(args=args)


@app.route("/cmdb/property/add/<string:ptype>", methods=["POST"])
# @swag_from('/cmdb/property/document/addProperty.yml')
@authwapper
def addPropertyApi(ptype):
    """
    :param ptype:
    :return:
    """
    args = request.json if request.json else {}

    return Cloud(ptype=ptype).add(args=args)


@app.route("/cmdb/property/detail/<string:ptype>/<string:internal_ip>", methods=["POST"])
@swag_from('/cmdb/property/document/getDetail.yml')
def getDetailApi(ptype, internal_ip):
    """
    :param internal_ip:
    :param ptype:
    :return:
    """

    return Cloud(ptype=ptype, internal_ip=internal_ip).detail()


@app.route("/cmdb/property/offline/<string:internal_ip>", methods=["DELETE"])
# @swag_from('/cmdb/property/document/offlineProperty.yml')
@authwapper
def offlinePropertyApi(internal_ip):
    """
    :param: internal_ip
    :return:
    """

    return Cloud(internal_ip=internal_ip).offline()


@app.route("/cmdb/property/dbpassword/<string:internal_ip>", methods=["POST"])
# @swag_from('/cmdb/property/document/getDetail.yml')
@authwapper
def getDBpasswordApi(internal_ip):
    """
    :param internal_ip:
    :param ptype:
    :return:
    """

    return Cloud(internal_ip=internal_ip).getDBpassword()


@app.route("/cmdb/property/update", methods=["POST"])
# @swag_from('/cmdb/property/document/updateProperty.yml')
@authwapper
def updatePropertyApi():
    """
    :return:
    """
    args = request.json if request.json else {}

    return Cloud().update(args=args)

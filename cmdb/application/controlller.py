from __init__ import app, cache
from flasgger import swag_from
from flask import request
import config
from cmdb.application.module import offlineApp, onlineApp, nodeApp

@app.route("/cmdb/application/offline/initdata", methods=["POST"])
# @swag_from('/cmdb/home/document/initdata.yml')
# @cache.cached(timeout=600)
def getOfflineData():
    appenv = request.args.get("appenv")
    filter = request.args.get("filter")
    return offlineApp.Manager(appenv=appenv, filter=filter).getter()


@app.route("/cmdb/application/offline/apptty", methods=["POST"])
# @swag_from('/cmdb/home/document/initdata.yml')
# @cache.cached(timeout=600)
def getOfflineTty():
    appenv = request.args.get("appenv")
    appname = request.args.get("appname")
    return offlineApp.Manager(appenv=appenv,appname=appname).terminal()


@app.route("/cmdb/application/offline/restart", methods=["POST"])
# @swag_from('/cmdb/home/document/initdata.yml')
# @cache.cached(timeout=600)
def restartOffline():
    appenv = request.args.get("appenv")
    appname = request.args.get("appname")
    return offlineApp.Manager(appenv=appenv,appname=appname).restart()


@app.route("/cmdb/application/offline/applogs", methods=["POST"])
# @swag_from('/cmdb/home/document/initdata.yml')
# @cache.cached(timeout=600)
def getOfflineLogs():
    appenv = request.args.get("appenv")
    appname = request.args.get("appname")
    return offlineApp.Manager(appenv=appenv,appname=appname).logs()


@app.route("/cmdb/application/offline/applogs/search", methods=["POST"])
# @swag_from('/cmdb/home/document/initdata.yml')
# @cache.cached(timeout=600)
def searchOfflineLogs():
    appenv = request.args.get("appenv")
    appname = request.args.get("appname")
    filter = request.json
    print(filter)
    return offlineApp.Manager(appenv=appenv,appname=appname, filter=filter).searchLogs()


@app.route("/cmdb/application/initdata/online", methods=["POST"])
# @swag_from('/cmdb/home/document/initdata.yml')
# @cache.cached(timeout=600)
def getOnlineData():
    return "success"


@app.route("/cmdb/application/initdata/node", methods=["POST"])
# @swag_from('/cmdb/home/document/initdata.yml')
# @cache.cached(timeout=15)
def getNodeData():
    return "success"

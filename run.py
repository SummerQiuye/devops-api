import os
import sys
from __init__ import app
from cicd import controller
from alert import controller
from ksCluster import controller
from ldap import controller
from cmdb.property import controller
from cmdb.config import controller
from cmdb.home import controller
from cmdb.navigation import controller
from cmdb.proxyGateway import controller
from cmdb.admin import controller
from cmdb.application import controlller


# from skywalking import agent, config
#
# config.init(collector='172.17.16.77:11800', service='devops-api')
# config.flask_collect_http_params = True
# agent.start()


if __name__ == "__main__":
    # print("app starting...")
    app.run("0.0.0.0", port=5051, debug=True)


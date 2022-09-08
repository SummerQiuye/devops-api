from __init__ import app, cache
from flasgger import swag_from
import config
from .module.initPropertyData import initPropertyData
from .module.initMonitorData import initMonitorData
from .module.initLineAppData import initLineAppData


@app.route("/cmdb/home/get/initdata", methods=["POST"])
# @swag_from('/cmdb/home/document/initdata.yml')
@cache.cached(timeout=60)
def getInitData():
    """
    :param: null
    :return: Dict
    """

    # data = {
    #     "property": initPropertyData().sumDataResponse(),
    #     "monitor": initMonitorData().sumDataResponse(),
    #     "line": initLineAppData().sumDataResponse(),
    #     "document": config.document,
    #     "platformNotice": config.platform_notice,
    #     "workOrder": config.work_order
    # }
    return {'property': initPropertyData().sumDataResponse(),
            'monitor': {'ecs': [0, 0], 'mysql': [0, 0], 'redis': [0, 0], 'k8sprod': [0, 0], 'k8sdev': [0, 0], 'nginx': [0, 0], 'php': [0, 0], 'total': [0, 0]},
            "line": initLineAppData().sumDataResponse(),
            "document": config.document,
            "platformNotice": config.platform_notice,
            "workOrder": config.work_order,
            }





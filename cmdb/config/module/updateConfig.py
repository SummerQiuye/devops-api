from sqlAlchemy import *


def updateConfig(data, configDB, user, env):
    try:
        # 记录旧配置数据
        data["historyConfig"]["configEnv"] = env
        data["historyConfig"].pop("id")
        db.session.execute(
            ConfigHistory.__table__.insert(),
            [data["historyConfig"]]
        )
        db.session.commit()
        # print(data)
        # 更新数据
        configDB.query \
            .filter(configDB.name == data["newConfig"]["name"]) \
            .update({"config": data["newConfig"]["config"],
                     "owner": data["newConfig"]["owner"],
                     "usage": data["newConfig"]["usage"],
                     "version": data["version"],
                     "updateCount": data["newConfig"]["updateCount"] + 1,
                     "lastUpdateUser": user,
                     "lastUpdateRemark": data["lastUpdateRemark"]})
        db.session.commit()
        return {"stats": "200", "msg": "sql执行成功", "data": "更新完成"}
    except Exception as e:
        print(e)
        return {"stats": "502", "msg": "sql执行失败", "data": "更新失败"}


def updateDevConfig(data, user):
    return updateConfig(data, ConfigDev, user, "dev")


def updateProdConfig(data, user):
    return updateConfig(data, ConfigProd, user, "prod")

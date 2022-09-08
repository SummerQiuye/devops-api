from sqlAlchemy import *


def removeConfig(args, configDB):
    print(args, configDB)
    print(args["id"])
    # 删除数据
    configDB.query \
        .filter(configDB.id == args["id"]).delete()
    db.session.commit()
    return {"stats": "200", "msg": "sql执行成功", "data": "done"}


def removeDevConfig(args):
    return removeConfig(args, ConfigDev)


def removeProdConfig(args):
    return removeConfig(args, ConfigProd)

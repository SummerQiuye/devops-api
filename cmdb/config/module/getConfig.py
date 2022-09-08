from sqlAlchemy import ConfigDev, ConfigProd
from flask_maple.serializer import Serializer


def getConfig(args, configDB):
    # 参数判断赋值
    try:
        limit = args["limit"] if "limit" in args else 50
        offset = args["offset"] if "offset" in args else 0
        name = args["name"] if "name" in args else "%"
        print(name)
        result = configDB.query \
            .filter(configDB.name.like(name)) \
            .order_by(configDB.id.asc()) \
            .limit(limit) \
            .offset(offset) \
            .all()

        # 统计表行数用于前端分页
        count = configDB.query.count()

        # 数据序列化
        data = Serializer(result).data
        # print(data)
        return {"stats": "200", "msg": "sql执行成功", "data": data, "count": count, "limit": limit, "offset": offset}
    except Exception as e:
        print(e)
        return {"stats": "502", "msg": "sql执行失败", "data": "获取失败"}


def getDevConfig(args):
    return getConfig(args, ConfigDev)


def getProdConfig(args):
    return getConfig(args, ConfigProd)



from sqlAlchemy import *
from flask_maple.serializer import Serializer


def searchConfig(args, configDB):
    try:
        global sqlFilter
        # 参数判断赋值
        limit = args["limit"] if "limit" in args else 50
        offset = args["offset"] if "offset" in args else 0
        searchType = args["type"]
        searchText = args["data"]
        if searchType == "name":
            sqlFilter = configDB.name.like("%" + searchText + "%")
        elif searchType == "owner":
            sqlFilter = configDB.owner.like("%" + searchText + "%")
        result = configDB.query \
            .filter(sqlFilter) \
            .order_by(configDB.id.asc()) \
            .limit(limit) \
            .offset(offset) \
            .all()

        # 统计表行数用于前端分页
        count = configDB.query.filter(sqlFilter).count()

        # 数据序列化
        data = Serializer(result).data
        return {"stats": "200", "msg": "sql执行成功", "data": data, "count": count, "limit": limit, "offset": offset}
    except Exception as e:
        print(e)
        return {"stats": "502", "msg": "sql执行失败", "data": "查询失败"}


def searchDevConfig(args):
    return searchConfig(args, ConfigDev)


def searchProdConfig(args):
    return searchConfig(args, ConfigProd)

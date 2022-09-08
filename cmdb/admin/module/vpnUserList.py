from sqlAlchemy import *
from flask_maple.serializer import Serializer
from flask import jsonify


class VpnUserList:

    def __init__(self, args):
        self.args = args

    def getter(self):

        # 参数判断赋值
        limit = self.args["limit"] if "limit" in self.args else 50
        offset = self.args["offset"] if "offset" in self.args else 0
        data = ""
        try:
            result = ProxyGateway.query.limit(limit) \
                    .offset(offset)  \
                    .all()
            data = Serializer(result).data
            count = ProxyGateway.query.count()
            db.session.commit()
            return {"stats": "200", "msg": "sql执行成功", "data": data, "count": count, "limit": limit, "offset": offset}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"stats": "502", "msg": "sql执行失败", "track": str(e)}

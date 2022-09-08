from sqlAlchemy import *
from flask_maple.serializer import Serializer
from functools import wraps


class Cloud(object):

    # db.create_all()

    def __init__(self, **kwargs):
        self.ptype = kwargs.get("ptype")
        self.pname = kwargs.get("pname")
        self.searchType = kwargs.get("searchType")
        self.internal_ip = kwargs.get("internal_ip")

    # 获取资产基础信息
    def getter(self, args):

        # 参数判断赋值
        limit = args["limit"] if "limit" in args else 50
        line = args["line"] if "line" in args else '%'
        offset = args["offset"] if "offset" in args else 0
        env = args["env"] if "env" in args else '%'
        print(env)
        try:
            # 判断获取类型，并根据过滤参数返回数据
            if str.upper(self.ptype) == "%":
                result = CloudPropertyPublic.query \
                    .filter(CloudPropertyPublic.line.like(line),
                            CloudPropertyPublic.env.like(env),
                            CloudPropertyPublic.status == "使用中") \
                    .order_by(CloudPropertyPublic.id.desc()) \
                    .limit(limit) \
                    .offset(offset) \
                    .all()
            else:
                result = CloudPropertyPublic.query \
                    .filter(CloudPropertyPublic.type == str.upper(self.ptype),
                            CloudPropertyPublic.line.like(line),
                            CloudPropertyPublic.env.like(env),
                            CloudPropertyPublic.status == "使用中")\
                    .order_by(CloudPropertyPublic.id.desc()) \
                    .limit(limit) \
                    .offset(offset) \
                    .all()

            # 统计表行数用于前端分页
            count = CloudPropertyPublic.query.filter(CloudPropertyPublic.type.like(str.upper(self.ptype)),
                                                       CloudPropertyPublic.line.like(line),
                                                       CloudPropertyPublic.env.like(env),
                                                       CloudPropertyPublic.status == "使用中").count()

            # 数据序列化
            data = Serializer(result).data
            db.session.commit()
            return {"stats": "200", "msg": "sql执行成功", "data": data, "count": count, "limit": limit, "offset": offset}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"stats": "502", "msg": "sql执行失败", "track": str(e)}
        finally:
            db.session.close()

    # 搜索资产信息
    def search(self, args):
        # 参数判断赋值
        global filterCon
        try:
            data = args["data"] if "data" in args else "%"
            limit = args["limit"] if "limit" in args else 50
            offset = args["offset"] if "offset" in args else 0
            line = args["line"] if "line" in args else '%'
            env = args["env"] if "env" in args else '%'
            print(self.ptype)
            if self.searchType == "name":
                data = data.upper()
                filterCon = CloudPropertyPublic.name.ilike("%"+data+"%")
            elif self.searchType == "internal_ip":
                filterCon = CloudPropertyPublic.internal_ip.like("%" + data + "%")
            elif self.searchType == "external_ip":
                filterCon = CloudPropertyPublic.external_ip.like("%" + data + "%")
            elif self.searchType == "owner":
                filterCon = CloudPropertyPublic.owner.like("%" + data + "%")
            result = CloudPropertyPublic.query \
                .filter(filterCon,
                        CloudPropertyPublic.type.like(str.upper(self.ptype)),
                        CloudPropertyPublic.line.like(line),
                        CloudPropertyPublic.env.like(env),
                        CloudPropertyPublic.status == "使用中") \
                .order_by(CloudPropertyPublic.id.desc()) \
                .limit(limit) \
                .offset(offset) \
                .all()
            # 统计表行数用于前端分页
            count = CloudPropertyPublic.query.filter(filterCon,
                                                       CloudPropertyPublic.type.like(str.upper(self.ptype)),
                                                       CloudPropertyPublic.status == "使用中").count()
            data = Serializer(result).data
            db.session.commit()
            return {"stats": "200", "msg": "sql执行成功", "data": data, "count": count, "limit": limit, "offset": offset}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"stats": "400", "msg": "sql执行失败", "data": str(e)}
        finally:
            db.session.close()

    # 添加资产信息
    def add(self, args):
        print(self.ptype)
        print(args["basic"])
        print(args["more"])
        basic = args["basic"]
        basic["type"] = str.upper(self.ptype)
        basic["status"] = "使用中"
        more = args["more"]
        more["internal_ip"] = basic["internal_ip"]
        try:
            db.session.execute(
                CloudPropertyPublic.__table__.insert(),
                [basic]
            )
            if str.upper(self.ptype) == "ECS":
                db.session.execute(
                    CloudHost.__table__.insert(),
                    [more]
                )
            elif str.upper(self.ptype) == "RDS":
                db.session.execute(
                    CloudDatabase.__table__.insert(),
                    [more]
                )
            else:
                print(more)
                db.session.execute(
                    CloudOthers.__table__.insert(),
                    [more]
                )
            db.session.commit()
            return {"stats": "200", "msg": "sql执行成功", "data": []}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"stats": "400", "msg": "sql执行失败", "data": str(e)}
        finally:
            db.session.close()

    # 更新资产信息
    def update(self, args):
        print(args["data"])
        data = args["data"]
        del data["_index"]
        del data["_rowKey"]
        del data["createDate"]
        del data["updateDate"]
        # 更新数据
        try:
            CloudPropertyPublic.query \
                .filter(CloudPropertyPublic.id == data["id"]) \
                .update(data)
            db.session.commit()
            return {"stats": "200", "msg": "sql执行成功", "data": []}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"stats": "400", "msg": "sql执行失败", "data": str(e)}
        finally:
            db.session.close()

    # 下架资产
    def offline(self):
        try:
            CloudPropertyPublic.query\
                                 .filter(CloudPropertyPublic.internal_ip == self.internal_ip)\
                                 .update({"status": "已下架"})
            db.session.commit()
            return {"stats": "200", "msg": "sql执行成功", "data": []}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"stats": "400", "msg": "sql执行失败", "data": str(e)}
        finally:
            db.session.close()

    # 查看资产详细信息
    def detail(self):
        try:
            detailData = ""
            if str.upper(self.ptype) == "ECS":
                detailData = CloudHost.query.filter(CloudHost.internal_ip == self.internal_ip).all()
                # print(detailData)
            elif str.upper(self.ptype) == "DATABASE":
                detailData = CloudDatabase.query.filter(CloudDatabase.internal_ip == self.internal_ip).all()
                # print(detailData)
            else:
                detailData = CloudOthers.query.filter(CloudOthers.internal_ip == self.internal_ip).all()
            data = Serializer(detailData).data
            # 注释详细信息中密码字段
            if len(data) != 0 and data[0].get("password"):
                print("屏蔽密码字段")
                data[0].pop("password")
            db.session.commit()
            return {"stats": "200", "msg": "sql执行成功", "data": data}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"stats": "400", "msg": "sql执行失败", "data": str(e)}
        finally:
            db.session.close()

    # 查看数据库密码
    def getDBpassword(self):
        try:
            detailData = CloudDatabase.query.filter(CloudDatabase.internal_ip == self.internal_ip).all()
            data = Serializer(detailData).data
            print(data)
            db.session.commit()
            return {"stats": "200", "msg": "sql执行成功", "data": data[0]}
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"stats": "400", "msg": "sql执行失败", "data": str(e)}
        finally:
            db.session.close()
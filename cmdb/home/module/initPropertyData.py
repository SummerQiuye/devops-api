from flask import jsonify
from sqlAlchemy import *
from flask_maple.serializer import Serializer


class initPropertyData:

    def __init__(self):
        self.sumData = {
            "property": self.property(),
            "database": self.database(),
            "eip": self.eip(),
            "oss": self.oss(),
            "nas": self.nas(),
            "nat": self.nat(),
            "slb": self.slb(),
            "application": self.application(),
            "configuration": self.confirguration()
        }
        print(self.sumData)

    @staticmethod
    def property():
        result = CloudPropertyPublic.query \
            .filter(CloudPropertyPublic.status == "使用中", CloudPropertyPublic.type == "ECS") \
            .count()
        db.session.commit()
        return result

    @staticmethod
    def database():
        rdsC = CloudPropertyPublic.query \
            .filter(CloudPropertyPublic.status == "使用中", CloudPropertyPublic.type == "RDS") \
            .count()
        mongoC = CloudPropertyPublic.query \
            .filter(CloudPropertyPublic.status == "使用中", CloudPropertyPublic.type == "MONGO") \
            .count()
        redisC = CloudPropertyPublic.query \
            .filter(CloudPropertyPublic.status == "使用中", CloudPropertyPublic.type == "REDIS") \
            .count()
        db.session.commit()
        return rdsC+mongoC+redisC

    @staticmethod
    def eip():
        result = CloudPropertyPublic.query \
            .filter(CloudPropertyPublic.status == "使用中", CloudPropertyPublic.type == "EIP") \
            .count()
        db.session.commit()
        return result

    @staticmethod
    def oss():
        result = CloudPropertyPublic.query \
            .filter(CloudPropertyPublic.status == "使用中", CloudPropertyPublic.type == "OSS") \
            .count()
        db.session.commit()
        return result

    @staticmethod
    def nat():
        result = CloudPropertyPublic.query \
            .filter(CloudPropertyPublic.status == "使用中", CloudPropertyPublic.type == "NAT") \
            .count()
        db.session.commit()
        return result

    @staticmethod
    def slb():
        result = CloudPropertyPublic.query \
            .filter(CloudPropertyPublic.status == "使用中", CloudPropertyPublic.type == "SLB") \
            .count()
        db.session.commit()
        return result

    @staticmethod
    def nas():
        result = CloudPropertyPublic.query \
            .filter(CloudPropertyPublic.status == "使用中", CloudPropertyPublic.type == "NAS") \
            .count()
        db.session.commit()
        return result

    @staticmethod
    def application():
        result = ConfigProd.query.count()
        db.session.commit()
        return result

    @staticmethod
    def confirguration():
        dev = ConfigDev.query.count()
        prod = ConfigProd.query.count()
        db.session.commit()
        return dev+prod

    def sumDataResponse(self):
        return self.sumData


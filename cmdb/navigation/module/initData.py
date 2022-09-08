from sqlAlchemy import *
from flask_maple.serializer import Serializer
from flask import jsonify


class InitData:

    def __init__(self):
        pass

    def getter(self):
        data = ""
        try:
            result = NavigationDatum.query \
                     .all()
            data = Serializer(result).data
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return jsonify(data)

from flask import request ,Flask,abort
from flask_restful import Resource,reqparse
from Model import db, Ipath, IpathSchema

ipath_namelist_schema = IpathSchema(many=True)
ipath_schema = IpathSchema()
parser = reqparse.RequestParser()
parser.add_argument('tradepoints', type=int)

class IpathResource(Resource):
    def get(self):
        ipath_namelist = Ipath.query.all()
        ipath_namelist = ipath_namelist_schema.dump(ipath_namelist)
        return {'status': 'success', 'data': ipath_namelist}, 200

class NicknameResource(Resource):
    def get(self,query_nickname):
        ipath_namelist = Ipath.query.filter_by(nickname=query_nickname).first()
        ipath_namelist = ipath_schema.dump(ipath_namelist)
        return {'status': 'success', 'data': ipath_namelist}, 200
    def post(self,query_nickname):
        args = parser.parse_args()
        ipath_namelist = Ipath.query.filter_by(nickname=query_nickname).first()
        ipath_namelist.points += args['tradepoints']
        db.session.commit()
        ipath_namelist = ipath_schema.dump(ipath_namelist)
        return {'status': 'success', 'data': ipath_namelist}, 200
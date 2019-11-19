from flask import Blueprint
from flask_restful import Api
from resources.Ipath import IpathResource,NicknameResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(IpathResource, '/IPath')
api.add_resource(NicknameResource, '/IPath/<string:query_nickname>')
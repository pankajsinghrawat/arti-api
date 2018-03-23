from flask import Blueprint, request
from flask_restplus import Api
from flask_restplus import Resource
import json
import paralleldots

coreapiblueprint = Blueprint('coreapi', __name__)
coreapi = Api(coreapiblueprint)

nscoreapi = coreapi.namespace('arti', description='Analysis APIs')

@nscoreapi.route('')
class apicalls(Resource):
    def get(self):
        return json.dumps(paralleldots.usage())

@nscoreapi.route('/apikey', methods = ['POST'])
class setapikey(Resource):
    def post(self):
        paralleldots.set_api_key( request.json.get("payload") )
        return {'message': 'Api Key is successfully configured'}

@nscoreapi.route('/similarity', methods = ['POST'])
class getsimilarity(Resource):
    def post(self):
        payload = request.json.get("payload")
        response = paralleldots.similarity(payload)
        response.pop("usage", None)
        return response

@nscoreapi.route('/sentiment', methods = ['POST'])
class getsentiment(Resource):
    def post(self):
        payload = request.json.get("payload")
        response = paralleldots.sentiment(payload)
        response.pop("usage", None)
        return response

@nscoreapi.route('/abusescore', methods = ['POST'])
class getabusescore(Resource):
    def post(self):
        payload = request.json.get("payload")
        response = paralleldots.abuse(payload)
        response.pop("usage", None)
        return response

@nscoreapi.route('/emotionscore', methods = ['POST'])
class getemotion(Resource):
    def post(self):
        payload = request.json.get("payload")
        response = paralleldots.emotion(payload)
        response.pop("usage", None)
        return response

# payload will have path of image
@nscoreapi.route('/popularityscore', methods = ['POST'])
class getpopularity(Resource):
    def post(self):
        payload = request.json.get("payload")
        response = paralleldots.popularity(payload)
        response.pop("usage", None)
        return response

from flask import Blueprint, request
from flask_restplus import Api
from flask_restplus import Resource, swagger
import json
import paralleldots
import os
import requests

coreapiblueprint = Blueprint('coreapi', __name__)
coreapi = Api(coreapiblueprint)

nscoreapi = coreapi.namespace('arti', description='Analysis APIs')

@nscoreapi.route('')
class apicalls(Resource):
    def get(self):
        return json.dumps(paralleldots.usage())

@nscoreapi.route('/apikey', methods = ['POST'])
class setapikey(Resource):
    @nscoreapi.doc(params={'apikey': 'api key'})
    def post(self):
        paralleldots.set_api_key( request.json.get("apikey") )
        return {'message': 'Api Key is successfully configured'}

@nscoreapi.route('/similarity', methods = ['POST'])
class getsimilarity(Resource):
    @nscoreapi.doc(params={'text1': 'text for calculating similarity', 'text2': 'text for calculating similarity'})
    def post(self):
        payload1 = request.json.get("text1")
        payload2 = request.json.get("text2")
        response = paralleldots.similarity(payload1, payload2)
        response.pop("usage", None)
        print(response)
        return response

@nscoreapi.route('/sentiment', methods = ['POST'])
class getsentiment(Resource):
    @nscoreapi.doc(params={'payload': 'text for validating sentiment'})
    def post(self):
        payload = request.json.get("payload")
        response = paralleldots.sentiment(payload)
        response.pop("usage", None)
        print(response)
        return response

@nscoreapi.route('/abusescore', methods = ['POST'])
class getabusescore(Resource):
    @nscoreapi.doc(params={'payload': 'text for validating abuse'})
    def post(self):
        payload = request.json.get("payload")
        response = paralleldots.abuse(payload)
        response.pop("usage", None)
        print(response)
        return response

@nscoreapi.route('/emotionscore', methods = ['POST'])
class getemotion(Resource):
    @nscoreapi.doc(params={'payload': 'text for validating emotion'})
    def post(self):
        payload = request.json.get("payload")
        response = paralleldots.emotion(payload)
        response.pop("usage", None)
        print(response)
        return response

# payload will have path of image
@nscoreapi.route('/popularityscore', methods = ['POST'])
class getpopularity(Resource):
    @nscoreapi.doc(params={'payload': 'path for url'})
    def post(self):
        #payload = request.json.get("payload")
        payload = "app/data/gangnam-style-viral-campaign.jpg"
        response = paralleldots.popularity(os.path.abspath(payload))
        response.pop("usage", None)
        print(response)
        return response

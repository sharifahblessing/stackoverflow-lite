from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from app.views import Questions,SingleQuestion,PostAnswer

app = Flask(__name__)
Swagger(app)

"""initializing an API"""
api = Api(app)


api.add_resource(Questions,'/api/v1/questions')
api.add_resource(SingleQuestion,'/api/v1/questions/<questionId>')
api.add_resource(PostAnswer,'/api/v1/questions/<questionId>/answers')

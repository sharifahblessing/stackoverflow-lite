from flask import Flask
from flask_restful import Api
from app.views import Questions

app = Flask(__name__)
app.secret_key="sh"

"""initializing an API"""
api = Api(app)

api.add_resource(Questions,'/api/v1/questions')

from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import datetime
from app.models import Question_model
import json

questions_list =[]
class Questions (Resource):
    def post(self):
        parser= reqparse.RequestParser()

        """collecting arguments"""
        parser.add_argument('id',type=int,required=True)
        parser.add_argument('title',type=str,required=True)
        parser.add_argument('body',type=str,required=True)
        parser.add_argument('tag',type=str,required=True)
        parser.add_argument('postedby',type=str,required=True)

        """getting specific arguments"""

        argument = parser.parse_args()

        id = argument['id']
        title = argument['title']
        body = argument['body']
        tag = argument['tag']
        postedby = argument['postedby']
        time = str(datetime.datetime.now())

        """creating an object"""
        obj = Question_model(id,title,body,tag,postedby,time)

        """convert object to JSON"""
        convert_obj_data = json.loads(obj.my_json())

        
        """checking for duplicates"""

        for our_list in questions_list:
            if str(title).strip() == str(our_list['title']).strip():
                 return make_response(jsonify(
            {
            'message':'This question already exists'           
        }
        ),409)


        """insert into the list"""
        questions_list.append(convert_obj_data)


        return make_response(jsonify(
            {
            'message':'created a question successfully'           
        }
        ),201)


   

        


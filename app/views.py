from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import datetime
from app.models import Question_model, Answer_model
import json

questions_list =[]
answers_list =[]
class Questions (Resource):
    def post(self):
        parser= reqparse.RequestParser()

        """collecting arguments"""
        parser.add_argument('questionid',type=int,required=True)
        parser.add_argument(str('title').strip(),required=True)
        parser.add_argument('body',type=str,required=True)
        parser.add_argument('tag',type=str,required=True)
        parser.add_argument('postedby',type=str,required=True)

        """getting specific arguments"""

        argument = parser.parse_args()

        questionid = argument['questionid']
        title = argument['title']
        body = argument['body']
        tag = argument['tag']
        postedby = argument['postedby']
        time = str(datetime.datetime.now())

        """creating an object"""
        questionobj = Question_model(questionid,title,body,tag,postedby,time)

        """convert object to JSON"""
        convert_questionobj_data = json.loads(questionobj.my_json())

        """checking whether the empty questionid feild and negative id"""
        if  questionid < 0:
            return make_response(jsonify(
        {
            'message':'The questionid has to be a positive int for this question to be posted'  
                }
            ),400)

        if questionid == 0:
            return make_response(jsonify(
        {

            'message':'The questionid should  be above zero'
            }

            ),400)
        
        
        
        """checking whether the empty title feild"""
        if  not title:
            return make_response(jsonify(
        {
            'message':'The title is needed for this question to be posted'  
                }
            ),400)
        """checking whether the empty body feild"""
        if  not body:
            return make_response(jsonify(
        {
            'message':'Body is needed for this question to be posted'  
                }
            ),400)
        """checking whether the empty tag feild"""
        if  not tag:
            return make_response(jsonify(
        {
            'message':'Tag is needed for this question to be posted'  
                }
            ),400)
        """checking whether the empty posted by feild"""
        if  not postedby:
            return make_response(jsonify(
        {
            'message':'postedby is needed for this question to be posted'  
                }
            ),400)
        
        
        """checking for duplicates"""

        for our_list in questions_list:
            if str(title).strip() == str(our_list['title']).strip():
                 return make_response(jsonify(
            {
            'message':'This question already exists'           
        }
        ),409)


        """insert into the list"""
        questions_list.append(convert_questionobj_data)


        return make_response(jsonify(
            {
            'message':'created a question successfully'           
        }
        ),201)

    def get(self):
        return {'questions':questions_list},200


class SingleQuestion(Resource):

    def get(self,questionId):

        for our_list in questions_list:
            if int(questionId) == int (our_list['questionid']):
                final_data = {
                    'questionid' : our_list['questionid'],
                    'title':our_list['title'],
                    'body':our_list['body'],
                    'tag':our_list['tag'],
                    'time':our_list['time'],
                    'postedby':our_list['postedby']
                }
                return {'question': final_data}, 200

        return make_response(jsonify({
            'message':'Sorry the question does not exist'
        }),404)


class PostAnswer(Resource):


    
    def post(self,questionId):

        parser= reqparse.RequestParser()
        """collecting arguments"""
        parser.add_argument('answerid',type=int,required=True)
        parser.add_argument('content',type=str,required=True)
        

        """getting specific arguments"""

        argument = parser.parse_args()

        answerid = argument['answerid']
        content = argument['content']

        for our_list in questions_list:
            if int(questionId) == int (our_list['questionid']):

                """creating an object"""
                answerobj = Answer_model(answerid,content)

                """convert object to JSON"""
                convert_answerobj_data = json.loads(answerobj.my_json())

                """checking whether the empty answerid feild"""
                if  not answerid:
                    return make_response(jsonify(
                {
                  'message':'The answerid is needed for this answer to be posted'  
                }
                    ),400)
                
                """checking whether the content answerid feild"""
                if  not content:
                    return make_response(jsonify(
                {
                  'message':'The content is needed for this answer to be posted'  
                }
                    ),400)

                """insert into the list"""
                answers_list.append(convert_answerobj_data)
                return {'message': 'answer posted successfully.'}, 201

        return make_response(jsonify({
            'message':'Sorry the question does not exist'
        }),404)




        



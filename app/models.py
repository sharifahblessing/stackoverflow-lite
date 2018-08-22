import json
class Question_model:
    def __init__(self, questionid, title, body, tag, postedby, time):
        self.questionid = questionid
        self.title = title
        self.body = body
        self.tag = tag
        self.postedby = postedby
        self.time = time

    def my_json(self):
        return json.dumps({
            'questionid':self.questionid,
            'title':self.title,
            'body':self.body,
            'tag':self.tag,
            'postedby':self.postedby,
            'time':self.time
        })


class Answer_model:
    def __init__(self, answerid, content):
        self.answerid = answerid
        self.content = content
      

    def my_json(self):
        return json.dumps({
            'answerid':self.answerid,
            'content':self.content,
          
        })

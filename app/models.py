import json
class Question_model:
    def __init__(self, id, title, body, tag, postedby, time):
        self.id = id
        self.title = title
        self.body = body
        self.tag = tag
        self.postedby = postedby
        self.time = time

    def my_json(self):
        return json.dumps({
            'id':self.id,
            'title':self.title,
            'body':self.body,
            'tag':self.tag,
            'postedby':self.postedby,
            'time':self.time
        })


class Answer_model:
    def __init__(self, id, content):
        self.id = id
        self.content = content
      

    def my_json(self):
        return json.dumps({
            'id':self.id,
            'content':self.content,
          
        })

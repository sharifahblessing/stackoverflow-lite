from flask import Flask
from app import app
from flasgger import Swagger




@app.route('/',methods=['GET'])
def index():
    return('welcome to stackoverflow lite')

if __name__=="__main__":
    app.run(port=5000,debug=True)
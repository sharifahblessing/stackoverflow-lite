from flask import Flask, redirect
from flask_restful import Resource, Api
from app import app

@app.route('/',methods=['GET'])
def index():
    return redirect("https://stackoverflowlite6.docs.apiary.io/#",code=302)
if __name__ == '__main__':
    app.run(port=5000,debug=True)
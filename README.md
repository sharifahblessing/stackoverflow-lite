# stackoverflow lite
[![Build Status](https://travis-ci.org/sharifahblessing/stackoverflow-lite.svg?branch=develop)](https://travis-ci.org/sharifahblessing/stackoverflow-lite)
[![Coverage Status](https://coveralls.io/repos/github/sharifahblessing/stackoverflow-lite/badge.svg?branch=develop)](https://coveralls.io/github/sharifahblessing/stackoverflow-lite?branch=develop)

StackOverflow-lite is a platform where people can ask questions and provide answers.  

To acces this API online visit [API Link ](https://stackoverflow-app-lite.herokuapp.com)

### Requirements Building blocks.
- ```Python3``` - A programming language that lets us work more quickly (The universe loves speed!).

- ```Flask``` - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.

- ```Virtualenv``` - A tool to create isolated virtual environment

### Installation on WIndows

First clone this repository
```
 git clone @https://github.com/sharifahblessing/stackoverflow-lite
 cd stackoverflow-lite
 ```

Create virtual environment and install it on Windows

 ```
 virtualenv --python=python3 venv
 .\venv\bin\activate.bat
 ```

Then install all the necessary dependencies by
 ```
pip install -r requirements.txt
 ```

Then run the application
 ```
 python run.py
 ```
 Testing and knowing coverage run 
 ```
nosetests 
 ```

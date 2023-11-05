from flask import Flask, request, jsonify
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
import pandas as pd
import SourceDataObj
from tinydb import TinyDB, Query

app = Flask(__name__)
api = Api(app, prefix='/api/v1')
auth = HTTPBasicAuth()

db = TinyDB('db.json')

@app.route('/login', methods=['POST'])
def verify_login():
    User = Query()
    user_data = {
        'username': request.form.get('username'),
        'password': request.form.get('password'),
    }
    if db.search(User.username == user_data['username'] and User.password == user_data['password']):
        response_data = {'message': 'Login successful'}
        return jsonify(response_data), 200
    else:
        response_data = {'message': 'User does not match.'}
        return jsonify(response_data), 409

@app.route('/register', methods=['POST'])
def verify_register():
    User = Query()
    user_data = {
        'username': request.form.get('username'),
        'password': request.form.get('password'),
        'email': request.form.get('email')
    }
    if not db.search(User.username == user_data['username']):
        db.insert(user_data)
        response_data = {'message': 'Registration successful'}
        return jsonify(response_data), 200
    else:
        print('User is already in the database!')
        response_data = {'message': 'User is already in database.'}
        return jsonify(response_data), 409

@app.route('/')
def hello():
    return 'Welcome to my real estate app!'

@app.route('/getZHVI')
def getZipCodeData():
    zillow = SourceDataObj.Zillow()
    print(zillow.data["ZHVI"])
    return 'Zillow Data'

if(__name__ == '__main__'):
    app.run()

#Issues: Slow Data Loading
# Zillow Home Value Index (ZHVI): 
# A measure of the typical home value and market changes across a given region and housing type.
#  It reflects the typical value for homes in the 35th to 65th percentile range.
#  Available as a smoothed, seasonally adjusted measure and as a raw measure.
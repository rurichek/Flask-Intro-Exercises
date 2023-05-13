from flask import Flask, request

app = Flask(__name__)
# app.config['DEBUG'] = True

@app.route('/welcom')
def welcome():
    return 'welcome'

@app.route('/welcom/home')
def welcome():
    return 'welcome home'

@app.route('/welcom/back')
def welcome():
    return 'welcome back'


from flask import Flask, jsonify, request, redirect, url_for, abort, render_template, flash
from models import *
import json
import logging

app = Flask(__name__)
app.config.from_object('settings')

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    return "Micro service is running"

@app.route('/monitors/',method = ['GET','POST'])
def users():
    if request.method == 'GET':
        users = Monitors.objects.all()
        try :
            users = json.dumps(users)
        except TypeError:
            users = "{}"
        return users
    if request.method == 'POST':
        if not request.json or not 'name' in request.json:
            return not_found()
        monitor = Monitors()
        monitor.name = request.json['name']
        monitor.monitorType = request.json['type']
        monitor.frequency = request.json['frequency']



@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()

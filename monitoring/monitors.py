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

@app.route('/monitors/', methods = ['GET','POST'])
def monitors():
    if request.method == 'GET':
        monitor = Monitors.objects().to_json()
        try :
            monitor = json.dumps(monitor)
        except TypeError:
            monitor = "{}"
        return monitor
    if request.method == 'POST':
        if not request.json or not 'name' in request.json:
            return not_found()
        monitor = Monitors()
        monitor.name = request.json['name']
        monitor.monitorType = request.json['type']
        monitor.frequency = request.json['frequency']
        logging.debug(monitor)
        monitor.save()
        return json.dumps({"status":"ok","message":"monitor created"})

@app.route('/monitors/<int:id>', methods=['PUT'])
def updateMonitor(id):
    monitor = Monitors.objects(id=id).to_json()
    if len(monitor) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'type' in request.json and type(request.json['type']) is not unicode:
        abort(400)
    if 'frequency' in request.json and type(request.json['frequency']) is not int:
        abort(400)
    monitor.name = request.json['name']
    monitor.type = request.json['type']
    monitor.frequency = request.json['frequency']
    monitor.sava()
    return json.dumps({"status":"ok","message":"monitor updated"})

@app.route('/monitors/<int:id>', methods=['DELETE'])
def deleteMonitor(id):
    monitor = Monitors.objects(id=id).to_json()
    if len(monitor) == 0:
        abort(404)
    monitor.remove(id=id)
    return json.dumps({"status":"ok","message":"monitor deleted"})


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

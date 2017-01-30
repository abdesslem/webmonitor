from flask import Flask, jsonify, request, redirect, url_for, abort, render_template, flash
from models import *
import json

app = Flask(__name__)
app.config.from_object('settings')


@app.route('/')
def index():
    return "Micro service is running"


@app.route('/monitors/')
def users():
    users = Monitors.objects.all()
    try :
        users = json.dumps(users)
    except TypeError:
        users = "{}"
    return users

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
        


if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()

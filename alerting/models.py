import logging
from datetime import datetime
from mongoengine import *
from mongoengine import signals

connect('alerts')

class Alerts(Document):
    name         = StringField(max_length=120, required=True)
    user         = StringField(max_length=120, required=True)
    creationdate = DateTimeField(default=datetime.now())
    meta         = {'allow_inheritance': True}

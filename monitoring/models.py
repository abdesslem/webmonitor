import logging
from datetime import datetime
from mongoengine import *
from mongoengine import signals

connect('monitors')

class User(Document):
    username = StringField(required=True)
    email = StringField(required=True)
    firstName = StringField(max_length=50)
    lastName = StringField(max_length=50)
    password = StringField(max_length=200)
    phone = StringField(max_length=50)
    address = StringField(max_length=200)
    creationDate = DateTimeField()

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        logging.debug("Pre Save: %s" % document.username)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        logging.debug("Post Save: %s" % document.username)
        if 'created' in kwargs:
            if kwargs['created']:
                logging.debug("Created")
            else:
                logging.debug("Updated")


class Monitors(Document):
    name         = StringField(max_length=120, required=True)
    user         = ReferenceField(User)
    creationdate = DateTimeField(default=datetime.now())
    frequency    = DecimalField() # check every x second
    monitorType  = StringField()
    url          = StringField()
    meta         = {'allow_inheritance': True}

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        logging.debug("Pre Save: %s" % document.name)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        logging.debug("Post Save: %s" % document.name)
        if 'created' in kwargs:
            if kwargs['created']:
                if document.monitorType == 'http':
                    monitor = httpLogs()
                    monitor.name = document.name
                    monitor.save()
                elif document.monitorType == 'ping':
                    monitor = sslLogs()
                    monitor.name = document.name
                    monitor.save()
                else :
                    monitor = sslLogs()
                    monitor.name = document.name
                    monitor.save()
                logging.debug("Created")
            else:
                logging.debug("Updated")

# monitoring du protocol HTTP, send HTTP GET request every x second
class httpLogs(Monitors):
    status    = StringField() # OK or not OK

# monitoring du ssl certificate
class sslLogs(Monitors):
    expirationDate = DateTimeField()

# monitoring du ssl certificate
class pingLogs(Monitors):
    status = DateTimeField()

signals.pre_save.connect(User.pre_save, sender=User)
signals.post_save.connect(User.post_save, sender=User)
signals.pre_save.connect(Monitors.pre_save, sender=Monitors)
signals.post_save.connect(Monitors.post_save, sender=Monitors)

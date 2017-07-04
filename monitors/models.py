import logging
from datetime import datetime
from mongoengine import *
from mongoengine import signals

connect('monitors')


class Monitors(Document):
    name         = StringField(max_length=120, required=True)
    #user         = ReferenceField(User)
    user         = StringField(max_length=120, required=True)
    creationdate = DateTimeField(default=datetime.now())
    frequency    = DecimalField() # check every x second
    monitorType  = StringField()
    url          = StringField()
    notification = StringField()
    meta         = {'allow_inheritance': True}

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        logging.debug("Pre Save: %s" % document.name)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        logging.debug("Post Save: %s" % document.name)
        if 'created' in kwargs:
            if kwargs['created']:
                logging.debug("Created")
            else:
                logging.debug("Updated")


signals.pre_save.connect(Monitors.pre_save, sender=Monitors)
signals.post_save.connect(Monitors.post_save, sender=Monitors)

from models import *
import json
from consumer import alertListner
import logging
import loader

file_handler = logging.FileHandler('alerts.log')

print loader.getPlugins()

for i in loader.getPlugins():
    plugin = loader.loadPlugin(i)
    plugin.alert()



alertListner()

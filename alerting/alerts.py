from models import *
import json
from consumer import alertListner
import logging

file_handler = logging.FileHandler('alerts.log')

alertListner()

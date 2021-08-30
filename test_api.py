import unittest
import requests

from app import app
# set the application to testing mode
app.testing = True

class TestApi(unittest.TestCase):
    BASE = "http://127.0.0.1:5000/"

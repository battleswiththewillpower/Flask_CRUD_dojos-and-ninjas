from flask import Flask
app = Flask(__name__)

DATABASE = 'dojos_and_ninjas_schema'

from flask_app.controllers import dojos, ninjas, routes 
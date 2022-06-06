from multiprocessing import context
from flask_app import app
from flask import render_template,redirect,request,session

#import model
#keep this file only dojos

from flask_app.models import dojo


@app.route('/dojos')
def index():
    context = {
        'dojos': dojo.Dojo.get_all()
    }
    

    return render_template('dojos.html', **context)
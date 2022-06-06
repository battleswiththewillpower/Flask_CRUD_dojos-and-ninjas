
from flask_app import app
from flask import render_template,redirect,request,session

#import model
#keep this file only dojos
from flask_app.models import dojo


@app.route('/dojo/create', methods=['POST'])
def dojo_create():
    # print("create user")
    # print(request.form)
    dojo.Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def dojo_show(id):
    context = {
        "dojo": dojo.Dojo.get_one_ninjas({'id': id})
    }
    return render_template("dojo-show.html", **context)

# @app.route('/dojo/<int:id>/edit')
# def dojo_edit(id):
#     pass

# @app.route('/dojo/<int:id>/update', methods=['POST'])
# def dojo_update(id):
#     pass

# @app.route('/dojo/<int:id>/delete')
# def dojo_destroy(id):
#     pass
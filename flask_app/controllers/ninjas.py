
from flask_app import app
from flask import render_template,redirect,request,session

#import model
#keep this file only ninjas
from flask_app.models import ninja, dojo


@app.route('/ninjas')
def ninjas():
    context = {
        'ninja': ninja.Ninja.get_all(),
        'dojo': dojo.Dojo.get_all()
    }
    return render_template("dojo-show.html", **context)

@app.route('/ninja/new')
def ninja_new():
    # gain acess to the dojo for every ninja
    context = {
        'dojos': dojo.Dojo.get_all()
    }
    return render_template('ninjas.html', **context)

@app.route('/ninja/create', methods=['POST'])
def ninja_create():
    ninja.Ninja.create(request.form)

    # will redirect to ninja show bc ninja show renders to dojo-show
    return redirect(f'/dojo/{request.form["dojo_id"]}')

@app.route('/ninja/<int:id>')
def ninja_show(id):
    # invoke get_one
    context = {
        "ninja": ninja.Ninja.get_one({'id': id})
    }
    return render_template("dojo-show.html", **context)

# @app.route('/ninja/<int:id>/edit')
# def ninja_edit(id):
#     pass

# @app.route('/ninja/<int:id>/update', methods=['POST'])
# def ninja_update(id):
#     pass

# @app.route('/ninja/<int:id>/delete')
# def ninja_delete(id):
#     pass
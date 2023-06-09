from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos():
    dojo_list = Dojo.get_all()
    return render_template("dojos.html", dojos = dojo_list)

@app.route('/dojos/process', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["dojo_name"]
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show(id):
    data = {
        "id": id
    }
    session['dojo_id'] = id
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("show_dojo.html", dojo = dojo)
from flask import render_template, redirect, request, url_for, session
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def create_ninja():
    dojos=Dojo.get_all()
    return render_template("create_ninjas.html", all_dojos=dojos)

@app.route('/ninjas/process', methods=['POST'])
def process_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.create_ninja(data)
    return redirect('/dojos')

@app.route('/dojos/ninjas/update/<int:ninja_id>')
def update(ninja_id):
    ninja=Ninja.get_one(ninja_id)
    dojos=Dojo.get_all()
    return render_template("update_ninja.html", ninja = ninja, all_dojos=dojos)

@app.route('/dojos/ninjas/update/process',methods=['POST'])
def update_process():
    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    
    Ninja.update(data)
    return redirect( url_for("show", id = request.form["dojo_id"]))

@app.route("/dojos/ninjas/delete/<int:id>")
def delete(id):
    Ninja.delete_ninja({"id": id})
    return redirect (url_for("show", id = session['dojo_id']))
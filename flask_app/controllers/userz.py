# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users import User

@app.route("/")
def index():
    return render_template("new.html")


@app.route("/users")
def show_users():
    all_users = User.get_all()
    return render_template("show_users.html", users=all_users)


@app.route("/users/create", methods=['POST'])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(request.form)
    return redirect('/users')


@app.route("/users/show/<int:user_id>")
def show(user_id):
    user = User.get_one(user_id)
    return render_template("user_card.html", user=user)


@app.route("/users/update", methods=['POST'])
def update():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(request.form)
    return redirect('/users')


@app.route("/users/delete/<int:user_id>")
def delete(user_id):
    User.delete(user_id)
    return redirect('/users')


@app.route("/users/edit/<int:user_id>")
def edit(user_id):
    user = User.get_one(user_id)
    return render_template("edit.html", user=user)


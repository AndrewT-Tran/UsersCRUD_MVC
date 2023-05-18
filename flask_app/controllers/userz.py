# burgers.py
from flask import flash, redirect, render_template, request, session
from flask_app import app
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
    User.save(request.form)
    return redirect('/users')


@app.route("/users/show/<int:user_id>")
def show(user_id):
    user = User.get_one(user_id)
    return render_template("user_card.html", user=user)

@app.route("/users/update", methods=['POST'])
def update():
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


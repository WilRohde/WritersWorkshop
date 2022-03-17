from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.Author import Author
from flask_app.models.Group import Group
from flask_app.models.Submission import Submission
from flask_app.models.Genre import Genre

bcrypt = Bcrypt(app)

@app.route('/')
def registration():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if not Author.validate(request.form):
        return redirect('/')
    data = {
        "firstname": request.form['firstname'],
        "lastname": request.form['lastname'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session['Author_id'] = Author.save(data)
    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # see if the Author name provided exists in the database
    data = { "email" : request.form["login-email"] }
    Author_in_db = Author.get_Author_by_email(data)
    # Author is not registered in the db
    if not Author_in_db:
        flash("Invalid Email/Password","login")
        return redirect("/")
    if not bcrypt.check_password_hash(Author_in_db.password, request.form['login-password']):
        # if we get False after checking the password
        flash("Invalid Email/Password","login")
        return redirect('/')
    # if the passwords matched, we set the Author_id into session
    session['Author_id'] = Author_in_db.id
    session['firstname'] = Author_in_db.first_name
    session['lastname'] = Author_in_db.last_name

    return redirect('/dashboard')

@app.route('/dashboard')
def home():
    data = {
        'id': session['Author_id']
    }
    return render_template('dashboard.html',groups = Group.get_all(), submissions = Submission.get_all(data), genres = Genre.get_all() )

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
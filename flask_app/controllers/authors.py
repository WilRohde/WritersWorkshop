from flask import session, render_template, request, redirect, flash
import json
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

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/register', methods=['POST'])
def register():
    if not Author.validate(request.form):
        return redirect('/signup')
    data = {
        "firstname": request.form['firstname'],
        "lastname": request.form['lastname'],
        "username": request.form['username'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    oAuthor = Author.save(data)
    if (oAuthor == False):
        # return to the registration but we have to tell them something
        return redirect('/')
    session['Author_id'] = oAuthor.id
    session['firstname'] = oAuthor.first_name
    session['lastname'] = oAuthor.last_name
    session['username'] = oAuthor.username
    return redirect('/dashboard')

@app.route('/signin')
def signin():
    return render_template("signin.html")
    
@app.route('/login', methods=['POST'])
def login():
    # see if the Author name provided exists in the database
    data = { "credential" : request.form["credential"] }
    Author_in_db = Author.get_Author_by_credential(data)
    # Author is not registered in the db
    if not Author_in_db:
        flash("We're sorry, your login credentials do not match","login")
        return redirect("/signin")
    if not bcrypt.check_password_hash(Author_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("We're sorry, your login credentials do not match","login")
        return redirect('/signin')
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
    groups = Group.get_all()
    ogroups = []
    for group in groups:
        groupjsondata = json.dumps(group.toJson(), indent=4)
        groupjson = json.loads(groupjsondata)
        ogroups.append(groupjson)
    return render_template('dashboard.html', groups=Group.get_all(), submissions=Submission.get_all(data), genres=Genre.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/api/author/<username>')
def author_by_username(username):
    data = {
        'username': username
    }
    author = Author.get_Author_by_username(data)
    authorDict = author_dictionary(author)
    result = {
        'status': 'success',
        'author': authorDict
    }
    return result

@app.route('/api/register', methods=['POST'])
def api_register():
    results =  Author.api_validate(request.form)
    if results['status'] == 'False':
        result = {
            'status': 'failure',
            'messages': results['messages']
        }
        return result
    data = {
        "firstname": request.form['firstname'],
        "lastname": request.form['lastname'],
        "username": request.form['username'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    oAuthor = Author.save(data)
    if (oAuthor == False):
        # return to the registration but we have to tell them something
        messages = {
            'create': 'An exception occurred in Author.save(), could not create Author'
        }
        result = {
            'status': 'failure',
            'messages': messages
            }
        return result
    session['Author_id'] = oAuthor.id
    session['firstname'] = oAuthor.first_name
    session['lastname'] = oAuthor.last_name
    session['username'] = oAuthor.username
    result = {
        'status': 'success',
        'author': author_dictionary(oAuthor)
    }
    return result

@app.route('/app/login', methods=['POST'])
def app_login():
    # see if the Author name provided exists in the database
    data = { "credential" : request.form["credential"] }
    Author_in_db = Author.get_Author_by_credential(data)
    result = {
        'status': 'success'
    }
    messages = {}
    # Author is not registered in the db
    if not Author_in_db:
        result['status'] = 'failure'
        messages['credentials'] = "We're sorry, your login credentials do not match"
        result['messages'] = messages
        return result
    if not bcrypt.check_password_hash(Author_in_db.password, request.form['password']):
        result['status'] = 'failure'
        messages['credentials'] = "We're sorry, your login credentials do not match"
        result['messages'] = messages
        return result
    # NOTE: not sure how session will work with the api stuff 05/19/22
    session['Author_id'] = Author_in_db.id
    session['firstname'] = Author_in_db.first_name
    session['lastname'] = Author_in_db.last_name
    session['username'] = Author_in_db.username

    result['author'] = author_dictionary(Author_in_db)
    result = {
        'status': 'success',
        'author': author_dictionary(Author_in_db)
    }
    return result

def author_dictionary(author):
    authorDict = {
        'author_id' : author.id,
        'firstname' : author.first_name,
        'lastname'  : author.last_name,
        'username'  : author.username,
        'email'     : author.email,
        'created_at': author.created_at,
        'updated_at': author.update_at
    }
    return authorDict

@app.route('/api/logout')
def api_logout():
    session.clear()
    return True # not sure if it matters what we do here.


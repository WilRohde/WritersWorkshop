import pprint
from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_app.models.Group import Group
from flask_app.models.Genre import Genre
from flask_app.models.Submission import Submission

@app.route('/group/<int:id>')
def view(id):
    data = {
        'group_id': id,
        'author_id': session['Author_id']
    }
    isMember = Group.is_member(data)
    print(f"isMember = {isMember}")
    data = {
        'id': id
    }
    return render_template('group.html',group = Group.get_by_id(data), is_member = isMember, submissions = Submission.get_all_by_group(data))

@app.route('/group/join/<int:id>')
def join(id):
    data = {
        'group_id': id,
        'author_id': session['Author_id']
    }
    Group.join(data)
    data = {
        'id': id
    }
    #return render_template('group.html',group = Group.get_by_id(data), submissions = Submission.get_all_by_group(data))
    return redirect('/dashboard')
    
@app.route('/group/new')
def new_group():
    return render_template('create_group.html', genres = Genre.get_all())

@app.route('/group/create', methods=['POST'])
def create_group():
    data = {
        'name': request.form['groupname'],
        'genre_id': request.form['genre'],
        'founding_date': request.form['founding_date'],
        'short_description': request.form['short_description'],
        'description': request.form['description'],
        'creator_id': session['Author_id']
    }
    Group.save(data)
    return redirect('/dashboard')





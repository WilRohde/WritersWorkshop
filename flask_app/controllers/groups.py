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
    # make sure author isn't already a member
    if (Group.is_member(data)):
        flash("You are already a member of this group.")
        return redirect('/dashboard')

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
    if not Group.validate(request.form):
        return redirect('/group/new')

    data = {
        'name': request.form['groupname'],
        'genre_id': request.form['genre'],
        'founding_date': request.form['founding_date'],
        'short_description': request.form['short_description'],
        'description': request.form['description'],
        'creator_id': session['Author_id']
    }
    # make sure the group doesn't already exist
    if (Group.is_group(data)):
        flash("A group by this name already exists","Group")
        return redirect('/group/new')

    Group.save(data)
    return redirect('/dashboard')

@app.route('/group/edit/<int:id>')
def edit_group(id):
    data = {
        'id': id
    }
    return render_template('edit_group.html', genres = Genre.get_all(), group = Group.get_by_id(data))

@app.route('/group/update', methods=['POST'])
def update_group():
    if not Group.validate(request.form):
        return redirect('/group/edit/'+request.form['group_id'])

    data = {
        'name': request.form['groupname'],
        'genre_id': request.form['genre'],
        'founding_date': request.form['founding_date'],
        'short_description': request.form['short_description'],
        'description': request.form['description'],
        'creator_id': session['Author_id']
    }
    Group.update(data)
    return redirect('/dashboard')


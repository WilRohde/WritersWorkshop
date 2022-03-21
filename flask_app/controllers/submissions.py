from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_app.models.Submission import Submission
from flask_app.models.Group import Group

@app.route('/submit/review/<int:id>')
def review_submission(id):
    data = {
        'id': id
    }
    return render_template('review_submission.html', submission = Submission.get(data))
    
@app.route('/submit/edit/<int:id>')
def edit_submission(id):
    data = {
        'id': id
    }
    return render_template('update_submission.html', submission = Submission.get(data))

@app.route('/submit/new/<int:id>')
def new_submission(id):
    data = {
        'id': id
    }
    return render_template('upload_submission.html', group = Group.get_by_id(data))

@app.route('/submit/create')
def create_submission():
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'text': request.form['submission_text'],
        'author_id': session['Author_id']
    }
    Submission.save(data)
    return redirect('/dashboard')

@app.route('/submit/save', methods=['POST'])
def upload_submission():
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'submission_text': request.form['submission_text'],
        'group_id': request.form['group_id'],
        'Author_id': session['Author_id']
    }
    Submission.save(data)
    return redirect('/dashboard')

@app.route('/submit/update/<int:id>', methods=['POST'])
def update_submission(id):
    data = {
        'id': id,
        'title': request.form['title'],
        'description': request.form['description'],
        'submission_text': request.form['submission_text'],
        'group_id': request.form['group_id'],
        'Author_id': session['Author_id']
    }
    Submission.update(data)
    return redirect('/dashboard')

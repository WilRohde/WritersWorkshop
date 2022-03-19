from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_app.models.Submission import Submission
from flask_app.models.Genre import Genre
import os.path

@app.route('/submission/<int:id>')
def edit_submission():
    pass

@app.route('/submit/new')
def new_submission():
    return render_template('upload_submission.html')

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

@app.route('/submit/read')
def upload_submission():
    filename = request.form['filename']
    file = open(filename) # (r)ead and (t)ext are default values
    filedata = {
        'filetype': os.path.splitext(request.form['filename'])[1],
        'filesize': os.path.getsize(request.form['filename']),
    }
    return render_template('create_submission.html',submission_text = file.read(), file_data = filedata)

@app.route('/submit/manual')
def manual_submission():
    filedata = {
        'filetype': "",
        'filesize': ""
    }
    return render_template('create_submission.html', submission_text = "", file_data = filedata)

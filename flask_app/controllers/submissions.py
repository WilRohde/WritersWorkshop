from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_app.models.Submission import Submission

@app.route('/submission/<int:id>')
def edit_submission():
    pass

@app.route('/submission/new')
def new_submission(id):
    return render_template('create_review.html', submission = Submission.get(id))

@app.route('/submission/create')
def create_submission():
    data = {
        'text': request.form['review_text'],
        'submission_id': request.form['submission_id'],
        'reviewer_id': session['id']
    }
    Review.save(data)
    return redirect('\dashboard')

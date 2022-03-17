from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_app.models.Review import Review
from flask_app.models.Submission import Submission

@app.route('/genre/<int:id>')
def edit_review():
    pass

@app.route('/review/<int:id>/new')
def new_review(id):
    return render_template('create_review.html', submission = Submission.get(id))

@app.route('/review/create')
def create_review():
    data = {
        'text': request.form['review_text'],
        'submission_id': request.form['submission_id'],
        'reviewer_id': session['id']
    }
    Review.save(data)
    return redirect('\dashboard')

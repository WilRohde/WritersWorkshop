from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_app.models.Review import Review
from flask_app.models.Submission import Submission

@app.route('/review/<int:id>')
def review_submission(id):
    data = {
        'id': id,
        'reviewer_id': session['Author_id']
    }
    existing_review = Review.get_by_reviewer_submission(data)
    print(existing_review)
    data = {
        'id': id
    }
    if (existing_review == None):
        return render_template('review_submission.html', submission = Submission.get(data))
    else:
        return render_template('update_review.html', review = existing_review, submission = Submission.get(data))

@app.route('/review/post', methods=['POST'])
def post_review():
    data = {
        'text': request.form['review_text'],
        'submission_id': request.form['submission_id'],
        'reviewer_id': session['Author_id']
    }
    Review.save(data)
    return redirect('/dashboard')

@app.route('/review/update/<int:id>', methods=['POST'])
def update_review(id):
    data = {
        'id': id,
        'text': request.form['review_text'],
        'submission_id': request.form['submission_id'],
        'reviewer_id': session['Author_id']
    }
    Review.update(data)
    return redirect('/dashboard')
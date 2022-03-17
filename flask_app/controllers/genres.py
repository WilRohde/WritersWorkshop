from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_app.models.Genre import Genre

@app.route('/genre/<int:id>')
def edit():
    # NOTE You cannot modify a genre. Genres are immutable once added to the database
    pass

@app.route('/genre/new')
def new_genre():
    return render_template('create_genre.html')

@app.route('/genre/create', methods=['POST'])
def create_genre():
    data = {
        'name': request.form['genrename'],
        'short_description': request.form['short_description'],
        'description': request.form['description']
    }
    Genre.save(data)
    return redirect('/dashboard')

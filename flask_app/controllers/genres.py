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
    if not Genre.validate(request.form):
        return redirect('/genre/new')

    data = {
        'name': request.form['genrename'],
        'short_description': request.form['short_description'],
        'description': request.form['description']
    }
    Genre.save(data)
    return redirect('/dashboard')

def genre_dictionary(genre):
    genreDict = {
        'id': genre.id,
        'name': genre.name,
        'description': genre.description,
        'short_description': genre.short_description,
        'created_at': genre.created_at,
        'updated_at': genre.updated_at
    }
    return genreDict

@app.route('/api/genre/all')
def get_all_genres():
    genres = Genre.get_all()
    k = 0
    allGenres = {}
    for genre in genres:
        allGenres[k] = genre_dictionary(genre)
        k = k + 1
    result = {
        'status': 'success',
        'count': k,
        'genres': allGenres
    }
    return result

@app.route('/api/genre/<int:id>')
def api_get_genre(id):
    data = {
        'genre_id': id
    }
    genre = genre.get_by_id(data)
    genreDict = genre_dictionary(genre)
    allGenres = {}
    allGenres[0] = genreDict
    result = {
        "status": "success",
        "count": 1,
        "genres": allGenres
    }
    return result

@app.route('/api/genre/create', methods=['POST'])
def api_create_genre():
    result = {}
    messages = {}
    if not Genre.validate(request.form):
        result['status'] = 'failure'
        messages['validate'] = 'Genre data is invalid'
        result['messages'] = messages
        return result
    data = {
        'id': request.form['id'],
        'name': request.form['genrename'],
        'short_description': request.form['short_description'],
        'description': request.form['description'],
    }
    # make sure the group doesn't already exist
    if (Genre.is_genre(data)):
        result['status'] = 'failure'
        messages['duplicate'] = "A genre by this name already exists"
        result['messages'] = messages
        return result
        
    genre = Genre.save(data)
    if genre == False:
        result['status'] = 'failure'
        messages['error'] = "An error occurred creating this genre"
        result['messages'] = messages
        return result
    else:
        result['status'] = 'success'
        result['count'] = 1
        result['genres'] = genre_dictionary(genre)
        return result
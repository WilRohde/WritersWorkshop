from flask_app import app
from flask_app.controllers.authors import Author
from flask_app.controllers.groups import Group
from flask_app.controllers.genres import Genre
from flask_app.controllers.reviews import Review
from flask_app.controllers.submissions import Submission

if __name__=="__main__":
    app.run(debug=True)
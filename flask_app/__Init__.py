# __init__.py
from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__)
app.secret_key = "saskdfjalsiejinnldknlsdskdf;slkdjflsk333"

CORS(app)
api_v1_cors_config = {
    "methods": ["OPTIONS", "GET", "POST"],
    "origins": ["http://localhost:5000"]
}
CORS(app, resources={"/api/*": api_v1_cors_config})
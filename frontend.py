from app import app, db
import models
from flask import render_template

@app.route('/')
def index():
    context = {model.__name__.lower()+'s': model.select() for model in db.models}
    context['profile'] = models.Profile.get()
    return render_template('index.html', **context)

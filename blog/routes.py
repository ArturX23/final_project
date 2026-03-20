# final_project/blog/routes.py

from flask import render_template
from blog import app
from blog.models import Entry

@app.route("/")
def index():
    posts = Entry.query.filter_by(is_published=True).all()
    return render_template("index.html", posts=posts)
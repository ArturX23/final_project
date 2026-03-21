# final_project/blog/routes.py

from flask import render_template, request, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

@app.route("/")
def index():
    posts = Entry.query.filter_by(is_published=True).all()
    return render_template("index.html", posts=posts)

# ADD/EDIT POST REFACTORED

@app.route("/post/", defaults={'entry_id': None}, methods=["GET", "POST"])
@app.route("/post/<int:entry_id>", methods=["GET", "POST"])
def manage_entry(entry_id):
    if entry_id:
        entry = Entry.query.get_or_404(entry_id)
        form = EntryForm(obj=entry)
    else:
        entry = None
        form = EntryForm()

    if form.validate_on_submit():
        if entry:  # edycja
            form.populate_obj(entry)
        else:      # nowy wpis
            entry = Entry(
                title=form.title.data,
                body=form.body.data,
                is_published=form.is_published.data
            )
            db.session.add(entry)

        db.session.commit()
        return redirect(url_for('index'))

    return render_template("entry_form.html", form=form)
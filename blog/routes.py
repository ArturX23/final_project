# final_project/blog/routes.py

from flask import render_template, request, session, flash, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm, LoginForm

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
        if form.validate_on_submit():
            if entry:
                form.populate_obj(entry)
                flash("Wpis został zaktualizowany!")
            else:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
                flash("Twój wpis został dodany!")

            db.session.commit()
            return redirect(url_for('index'))

    return render_template("entry_form.html", form=form)

@app.route("/login/", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   errors = None
   next_url = request.args.get('next')
   if request.method == 'POST':
       if form.validate_on_submit():
           session['logged_in'] = True
           session.permanent = True  # Use cookie to store session.
           flash('You are now logged in.', 'success')
           return redirect(next_url or url_for('index'))
       else:
           errors = form.errors
   return render_template("login_form.html", form=form, errors=errors)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
   if request.method == 'POST':
       session.clear()
       flash('You are now logged out.', 'success')
   return redirect(url_for('index'))
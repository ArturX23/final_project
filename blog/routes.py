# final_project/blog/routes.py

from flask import render_template, request, session, flash, redirect, url_for, abort
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm, LoginForm
from blog.utils import login_required

@app.route("/")
def index():
    posts = Entry.query.filter_by(is_published=True).all()
    return render_template("index.html", posts=posts)

# ADD/EDIT POST REFACTORED

@app.route("/post/", defaults={'entry_id': None}, methods=["GET", "POST"])
@app.route("/post/edit/<int:entry_id>", methods=["GET", "POST"])
@login_required
def manage_entry(entry_id):
    if entry_id:
        entry = Entry.query.get_or_404(entry_id)
        form = EntryForm(obj=entry)
    else:
        entry = None
        form = EntryForm()

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

@app.route("/drafts/")
@login_required
def list_drafts():
    drafts = Entry.query.filter_by(is_published=False)\
                        .order_by(Entry.pub_date.desc())\
                        .all()
    return render_template("drafts.html", drafts=drafts)

@app.route("/delete/<int:entry_id>", methods=["POST"])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)

    db.session.delete(entry)
    db.session.commit()

    flash("Wpis został usunięty!")

    return redirect(url_for('index'))


@app.route("/post/<int:entry_id>")
def view_entry(entry_id):
    post = Entry.query.get_or_404(entry_id)

    # jeśli post nieopublikowany i niezalogowany → 404
    if not post.is_published and not session.get('logged_in'):
        abort(404)

    return render_template("view_post.html", post=post)
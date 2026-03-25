# --------------------------------------
# routes.py
# Definicje tras (widoków) aplikacji blogowej
#
# Odpowiada za:
# - wyświetlanie listy wpisów
# - podgląd pojedynczego wpisu
# - dodawanie i edycję postów
# - usuwanie wpisów
# - logowanie i wylogowanie użytkownika
# - wyświetlanie szkiców (draftów)
# --------------------------------------

from flask import render_template, request, session, flash, redirect, url_for, abort
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm, LoginForm
from blog.utils import login_required


# --------------------------------------
# Strona główna – lista opublikowanych wpisów
# --------------------------------------
@app.route("/")
def index():
    posts = Entry.query.filter_by(is_published=True).all()
    return render_template("index.html", posts=posts)


# --------------------------------------
# Dodawanie i edycja wpisu (wspólna funkcja)
#
# - GET: wyświetla formularz
# - POST: zapisuje nowy wpis lub aktualizuje istniejący
# - dostęp tylko dla zalogowanych użytkowników
# --------------------------------------
@app.route("/post/", defaults={'entry_id': None}, methods=["GET", "POST"])
@app.route("/post/edit/<int:entry_id>", methods=["GET", "POST"])
@login_required
def manage_entry(entry_id):

    # Jeśli podano ID → edycja istniejącego wpisu
    if entry_id:
        entry = Entry.query.get_or_404(entry_id)
        form = EntryForm(obj=entry)
    else:
        # Tworzenie nowego wpisu
        entry = None
        form = EntryForm()

    # Obsługa wysłania formularza
    if form.validate_on_submit():

        if entry:
            # Aktualizacja istniejącego wpisu
            form.populate_obj(entry)
            flash("Wpis został zaktualizowany!")
        else:
            # Tworzenie nowego wpisu
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


# --------------------------------------
# Logowanie użytkownika
#
# - GET: wyświetla formularz logowania
# - POST: weryfikuje dane i ustawia sesję
# - obsługuje przekierowanie do poprzedniej strony (next)
# --------------------------------------
@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = None

    # URL do przekierowania po logowaniu
    next_url = request.args.get('next')

    if request.method == 'POST':
        if form.validate_on_submit():
            # Ustawienie sesji użytkownika
            session['logged_in'] = True
            session.permanent = True

            flash('You are now logged in.', 'success')

            return redirect(next_url or url_for('index'))
        else:
            errors = form.errors

    return render_template("login_form.html", form=form, errors=errors)


# --------------------------------------
# Wylogowanie użytkownika
#
# - usuwa dane sesji
# - dostęp przez POST (bezpieczeństwo)
# --------------------------------------
@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        flash('You are now logged out.', 'success')

    return redirect(url_for('index'))


# --------------------------------------
# Lista szkiców (nieopublikowanych wpisów)
# Dostęp tylko dla zalogowanych użytkowników
# --------------------------------------
@app.route("/drafts/")
@login_required
def list_drafts():
    drafts = Entry.query.filter_by(is_published=False)\
                        .order_by(Entry.pub_date.desc())\
                        .all()

    return render_template("drafts.html", drafts=drafts)


# --------------------------------------
# Usuwanie wpisu
#
# - dostęp tylko dla zalogowanych użytkowników
# - usuwa wpis na podstawie ID
# --------------------------------------
@app.route("/delete/<int:entry_id>", methods=["POST"])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)

    db.session.delete(entry)
    db.session.commit()

    flash("Wpis został usunięty!")

    return redirect(url_for('index'))


# --------------------------------------
# Widok pojedynczego wpisu (Czytaj więcej)
#
# - ogólnodostępny dla wszystkich użytkowników
# - jeśli wpis nieopublikowany → dostęp tylko dla zalogowanych
# - w przeciwnym przypadku zwracany błąd 404
# --------------------------------------
@app.route("/post/<int:entry_id>")
def view_entry(entry_id):
    post = Entry.query.get_or_404(entry_id)

    # Blokada dostępu do szkiców dla niezalogowanych
    if not post.is_published and not session.get('logged_in'):
        abort(404)

    return render_template("view_post.html", post=post)
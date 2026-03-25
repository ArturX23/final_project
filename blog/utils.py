# --------------------------------------
# utils.py
# Funkcje pomocnicze aplikacji blogowej
#
# Zawiera:
# - dekorator login_required do ochrony widoków
# --------------------------------------

import functools
from flask import session, redirect, url_for, request


# --------------------------------------
# Dekorator wymagający logowania
#
# Ogranicza dostęp do wybranych widoków tylko dla
# zalogowanych użytkowników.
#
# Jeśli użytkownik nie jest zalogowany:
# - zostaje przekierowany na stronę logowania
# - przekazywany jest parametr "next" (powrót po logowaniu)
# --------------------------------------
def login_required(view_func):

    @functools.wraps(view_func)
    def check_permissions(*args, **kwargs):

        # Sprawdzenie czy użytkownik jest zalogowany
        if session.get('logged_in'):
            return view_func(*args, **kwargs)

        # Przekierowanie do logowania z zapamiętaniem ścieżki
        return redirect(url_for('login', next=request.path))

    return check_permissions
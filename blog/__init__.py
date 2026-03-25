# --------------------------------------
# __init__.py
# Inicjalizacja aplikacji Flask
#
# Odpowiada za:
# - utworzenie aplikacji Flask
# - konfigurację ustawień (Config)
# - inicjalizację bazy danych (SQLAlchemy)
# - konfigurację migracji (Flask-Migrate)
# - rejestrację modułów (routes, models)
# - konfigurację kontekstu powłoki (flask shell)
# --------------------------------------

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# --------------------------------------
# Tworzenie instancji aplikacji Flask
# --------------------------------------
app = Flask(__name__)

# Załadowanie konfiguracji z pliku config.py
app.config.from_object(Config)

# --------------------------------------
# Inicjalizacja bazy danych
# --------------------------------------
db = SQLAlchemy(app)

# Obsługa migracji bazy danych
migrate = Migrate(app, db)

# --------------------------------------
# Import modułów aplikacji
# (ważne: na końcu, aby uniknąć circular import)
# --------------------------------------
from blog import routes, models

# --------------------------------------
# Rozszerzony kontekst powłoki
# Dodaje funkcję do generowania przykładowych danych
# --------------------------------------
from blog.models import Entry, generate_entries

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Entry': Entry,
        'generate_entries': generate_entries
    }

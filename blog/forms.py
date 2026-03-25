# --------------------------------------
# forms.py
# Definicje formularzy aplikacji blogowej
#
# Zawiera formularze:
# - dodawania i edycji wpisów (EntryForm)
# - logowania użytkownika (LoginForm)
# --------------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.routing import ValidationError
from config import Config


# --------------------------------------
# Formularz wpisu blogowego
# Używany do dodawania i edycji postów
# --------------------------------------
class EntryForm(FlaskForm):

    # Tytuł wpisu (pole wymagane)
    title = StringField('Tytuł wpisu', validators=[DataRequired()])

    # Treść wpisu (pole wymagane)
    body = TextAreaField('Treść wpisu', validators=[DataRequired()])

    # Status publikacji (checkbox)
    is_published = BooleanField('Opublikowany')

    # Przycisk zapisu formularza
    submit = SubmitField('Zapisz wpis')


# --------------------------------------
# Formularz logowania użytkownika
# Weryfikuje dane administratora na podstawie konfiguracji
# --------------------------------------
class LoginForm(FlaskForm):

    # Login użytkownika
    username = StringField('Username', validators=[DataRequired()])

    # Hasło użytkownika
    password = PasswordField('Password', validators=[DataRequired()])

    # --------------------------------------
    # Walidacja loginu
    # Sprawdza zgodność z danymi w Config
    # --------------------------------------
    def validate_username(self, field):
        if field.data != Config.ADMIN_USERNAME:
            raise ValidationError("Invalid username")
        return field.data

    # --------------------------------------
    # Walidacja hasła
    # Sprawdza zgodność z danymi w Config
    # --------------------------------------
    def validate_password(self, field):
        if field.data != Config.ADMIN_PASSWORD:
            raise ValidationError("Invalid password")
        return field.data
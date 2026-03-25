# --------------------------------------
# models.py
# Definicje modeli bazy danych oraz narzędzi pomocniczych
#
# Zawiera:
# - model Entry (wpis blogowy)
# - funkcję do generowania przykładowych danych (Faker)
# --------------------------------------

from . import db
import datetime
from faker import Faker


# --------------------------------------
# Model wpisu blogowego
#
# Reprezentuje pojedynczy post w bazie danych
# --------------------------------------
class Entry(db.Model):

    # Unikalny identyfikator wpisu (klucz główny)
    id = db.Column(db.Integer, primary_key=True)

    # Tytuł wpisu (wymagany, max 80 znaków)
    title = db.Column(db.String(80), nullable=False)

    # Treść wpisu (wymagana, bez limitu długości)
    body = db.Column(db.Text, nullable=False)

    # Data publikacji (domyślnie aktualny czas UTC)
    pub_date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.utcnow
    )

    # Status publikacji:
    # True  → wpis opublikowany
    # False → szkic (draft)
    is_published = db.Column(db.Boolean, default=False)


# --------------------------------------
# Generator danych testowych (Faker)
#
# Umożliwia szybkie wypełnienie bazy przykładowymi wpisami
# Przydatne podczas developmentu i testowania UI
# --------------------------------------
fake = Faker()


def generate_entries(how_many=10):
    """
    Tworzy określoną liczbę przykładowych wpisów.

    :param how_many: liczba wpisów do wygenerowania (domyślnie 10)
    """

    for _ in range(how_many):
        entry = Entry(
            title=fake.sentence(nb_words=6),
            body='\n'.join(fake.paragraphs(3)),
            is_published=True
        )

        db.session.add(entry)

    # Zapis wszystkich zmian do bazy danych
    db.session.commit()

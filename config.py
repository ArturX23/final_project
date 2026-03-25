# --------------------------------------
# config.py
# Plik konfiguracyjny aplikacji Flask
#
# Zawiera ustawienia:
# - klucza bezpieczeństwa (SECRET_KEY)
# - połączenia z bazą danych (SQLAlchemy)
# - dane administratora (logowanie)
# --------------------------------------

import os


class Config:
    """
    Klasa konfiguracyjna aplikacji.

    Przechowuje wszystkie podstawowe ustawienia projektu,
    które są wykorzystywane przez Flask i rozszerzenia.
    """

    # --------------------------------------
    # Klucz bezpieczeństwa aplikacji
    # Używany do zabezpieczania sesji i formularzy (CSRF)
    # --------------------------------------
    SECRET_KEY = 'jakis-klucz'

    # --------------------------------------
    # Konfiguracja bazy danych (SQLite)
    # --------------------------------------
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # Wyłączenie śledzenia zmian (zmniejsza zużycie pamięci)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------------------------------------
    # Dane administratora
    # Pobierane z zmiennych środowiskowych (jeśli istnieją),
    # w przeciwnym razie używane są wartości domyślne
    # --------------------------------------
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "change-me")
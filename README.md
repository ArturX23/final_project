# 🚀 Mój Blog - Projekt Flask

Prosty blog stworzony w **Pythonie** z użyciem **Flask**, umożliwiający tworzenie, edycję i przeglądanie wpisów. 
Projekt obsługuje logowanie administratora oraz zarządzanie szkicami i opublikowanymi postami.

---

## 📑 Funkcjonalności

- ✏️ Tworzenie nowych wpisów (tytuł, treść, status publikacji)  
- 📝 Edycja istniejących wpisów  
- 📃 Lista wszystkich wpisów opublikowanych  
- 🗂️ Lista szkiców (nieopublikowanych) — dostępna tylko dla zalogowanego administratora  
- 🔍 Widok pojedynczego wpisu ("Czytaj więcej")  
- 🗑️ Usuwanie wpisów  
- 🔔 Powiadomienia przy dodaniu, edycji lub usunięciu wpisu  
- 🤖 Automatyczne generowanie przykładowych wpisów przy użyciu **Faker**  

---

## 🛠 Technologie

- Python 3.11+  
- Flask 3.x  
- Flask-WTF  
- Flask-SQLAlchemy  
- Flask-Migrate  
- SQLite (domyślna baza danych)  
- Bootstrap 4 (frontend)  

---

## ⚡ Instalacja

1. **Sklonuj repozytorium:**

```bash
git clone <URL_REPOZYTORIUM>
cd final_project
Utwórz i aktywuj wirtualne środowisko:
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / Mac
python -m venv .venv
source .venv/bin/activate
Zainstaluj wymagane pakiety:
pip install -r requirements.txt
▶️ Uruchamianie
Migracje bazy danych:
flask db init      # tylko pierwszy raz
flask db migrate
flask db upgrade
Uruchom serwer:
flask --app blog run
Otwórz w przeglądarce:

http://127.0.0.1:5000/

🗂 Struktura projektu
final_project/
├── blog/
│   ├── __init__.py        # konfiguracja Flask, inicjalizacja DB i migracji
│   ├── routes.py          # logika tras i widoków
│   ├── models.py          # modele bazy danych
│   ├── forms.py           # formularze WTForms
│   ├── utils.py           # dekoratory i funkcje pomocnicze
│   └── templates/         # szablony HTML
│       ├── base.html
│       ├── index.html
│       ├── entry_form.html
│       ├── view_post.html
│       ├── drafts.html
│       └── login_form.html
├── migrations/            # folder migracji bazy danych
├── requirements.txt       # lista pakietów Python
└── config.py              # konfiguracja projektu
⚙️ Konfiguracja

Plik config.py zawiera m.in.:

SECRET_KEY = 'jakis-klucz'
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'change-me'

Uwaga: w środowisku produkcyjnym należy zmienić SECRET_KEY i hasło administratora.

🎮 Użycie
Dodawanie wpisu: Zaloguj się → „Dodaj post”
Edycja wpisu: Kliknij „Edytuj” przy wybranym poście
Czytaj więcej: Kliknij tytuł lub przycisk „Czytaj więcej” (ogólnodostępne)
Usuwanie: Kliknij „Usuń” i potwierdź
Szkice: Wyłącznie dla zalogowanego administratora w zakładce „Szkice”
👤 Autor

Projekt wykonany przez [Twoje Imię / Nick]
📅 Data: 2026

📜 Licencja

Projekt do użytku edukacyjnego.

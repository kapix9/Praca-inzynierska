# Aplikacja Trenerska Online

## Opis projektu

Aplikacja umożliwia trenerom online rozpisywanie i zarządzanie planami treningowymi swoich podopiecznych. Rozwiązuje problemy związane z trudnością w znalezieniu trenera w mniejszych miejscowościach oraz znacząco redukuje koszty prowadzenia treningów poprzez przejście na tryb online. 

## Główni użytkownicy

- **Trenerzy online** – zarządzają bazą ćwiczeń oraz planami treningowymi swoich podopiecznych.
- **Podopieczni** – przeglądają swoje plany treningowe stworzone przez trenerów.

## Technologie

- **Python**: 3.8.2
- **Django**: 4.2.9
- Zależności zawarte w pliku `requirements.txt` (lista poniżej).

## Instalacja

git clone <adres_repozytorium>
cd <nazwa_katalogu>

Stwórz i aktywuj wirtualne środowisko:

python -m venv venv
source venv/bin/activate  # Na Windows: venv\Scripts\activate

Zainstaluj zależności:

pip install -r requirements.txt
Wykonaj migracje bazy danych:

python manage.py makemigrations
python manage.py migrate
Uruchom serwer deweloperski:

python manage.py runserver
Wejdź na http://127.0.0.1:8000 w przeglądarce.

Zależności

Lista zależności z pliku requirements.txt:

makefile
Skopiuj kod
asgiref==3.7.2
attrs==24.2.0
backports.zoneinfo==0.2.1
blinker==1.8.2
click==8.1.7
colorama==0.4.6
contourpy==1.0.7
cycler==0.11.0
Django==4.2.9
et-xmlfile==1.1.0
exceptiongroup==1.2.2
flasgger==0.9.7.1
Flask==3.0.3
Flask-SQLAlchemy==3.1.1
fonttools==4.38.0
greenlet==3.1.1
importlib_metadata==8.5.0
importlib_resources==6.4.5
iniconfig==2.0.0
itsdangerous==2.2.0
Jinja2==3.1.4
jsonschema==4.23.0
jsonschema-specifications==2023.12.1
kiwisolver==1.4.4
MarkupSafe==2.1.5
matplotlib==3.6.3
mistune==3.0.2
numpy==1.24.1
openpyxl==3.1.2
packaging==23.0
pandas==1.5.3
Pillow==9.4.0
pkgutil_resolve_name==1.3.10
pluggy==1.5.0
pyparsing==3.0.9
pytest==8.3.3
python-dateutil==2.8.2
pytz==2022.7.1
PyYAML==6.0.2
referencing==0.35.1
rpds-py==0.20.0
six==1.16.0
SQLAlchemy==2.0.36
sqlparse==0.4.4
tomli==2.0.2
typing_extensions==4.9.0
tzdata==2023.4
Werkzeug==3.0.6
zipp==3.20.2
Funkcjonalności

Panel trenera:

Zarządzanie bazą ćwiczeń.
Tworzenie planów treningowych dla podopiecznych.
Filtrowanie ćwiczeń według dni tygodnia i podopiecznych.
Dodawanie liczby serii, powtórzeń, obciążenia, tempa oraz uwag do ćwiczeń.
Możliwość dodania linku do instrukcji wideo dla ćwiczeń.
Opcjonalne oznaczenie ćwiczeń do nagrania przez podopiecznego.

Panel podopiecznego:

Wyświetlanie spersonalizowanego planu treningowego.
Widok ćwiczeń z podziałem na dni tygodnia.
Instrukcja użytkowania

Trener:

Loguje się do panelu administracyjnego (/admin) przy użyciu konta trenerskiego.
Dodaje ćwiczenia do bazy danych lub edytuje istniejące.
Tworzy plany treningowe dla podopiecznych, wybierając ćwiczenia z bazy.
Może zarządzać dodatkowymi informacjami: liczbą serii, powtórzeń, obciążeniem, tempem, uwagami i linkami do instrukcji.
Podopieczny:

Loguje się na stronie głównej (http://127.0.0.1:8000) przy użyciu swojego konta.
Otrzymuje widok swojego planu treningowego z podziałem na dni tygodnia.

Przykładowe dane

Nowy użytkownik otrzymuje bazę predefiniowanych ćwiczeń, którą może modyfikować i rozszerzać.
Ćwiczenia z bazy mogą być używane do tworzenia planów treningowych dla podopiecznych.

Struktura projektu

Root projektu:
manage.py: Główne narzędzie do zarządzania projektem.
requirements.txt: Lista zależności.

Katalog projektu:
settings.py: Konfiguracja projektu.
urls.py: Główne trasy aplikacji.
wsgi.py, asgi.py: Punkty startowe aplikacji.
Katalog aplikacji (app):
models.py: Definicje modeli (np. Seria, Cwiczenie).
views.py: Logika widoków.
templates/: Szablony HTML.

Autor:
Kacper Pawlak
Numer albumu: 81519


#  Automated Login Testing – Selenium + Pytest + POM

Projekt automatyzacji testów logowania przy użyciu **Selenium**, **Pytest**, wzorca **Page Object Model (POM)** oraz **raportu HTML z załączonymi screenshotami błędów**.

##  Opis

Repozytorium zawiera kompletne testy scenariuszy logowania na stronie:  
 https://the-internet.herokuapp.com/login

Projekt wykorzystuje:

-  Pytest – framework do testowania
-  Selenium – automatyzacja interakcji z przeglądarką
-  Page Object Model – dobre praktyki organizacji kodu
-  Screenshoty na fail i raport HTML (`pytest-html`)
-  Parametryzacja danych z pliku JSON


## Struktura projektu

project_root/
│
├── conftest.py # Globalne konfiguracje i fixture Selenium + HTML Report
├── tests/
│ └── test_login.py # Testy scenariuszy logowania
│
├── POM/
│ └── pages/
│ └── login_page.py # Klasa LoginPage zgodna z POM
│
├── data/
│ └── data.json # Dane testowe (login, hasło, oczekiwany komunikat)
│
├── screenshots/ # Screenshoty z nieudanych testów
└── README.md # Opis projektu (Ten plik)

##  Wymagania

- Python 3.8+
- Google Chrome + chromedriver (musi być zgodny z wersją przeglądarki)


###  Instalacja zależności:

bash
pip install -r requirements.txt

Uruchom wszystkie testy z raportem HTML:

pytest --html=report.html

Znajdziesz raport report.html z załączonymi screenshotami błędów w katalogu głównym.

Screenshoty z błędnych testów znajdziesz w folderze screenshots/.

Przykład danych testowych (data/data.json)
json

[
  {
    "username": "tomsmith",
    "password": "SuperSecretPassword!",
    "expected_text": "You logged into a secure area!"
  },
  {
    "username": "invalid",
    "password": "wrong",
    "expected_text": "Your username is invalid!"
  }
]

Przykładowy przebieg testu
Otwórz stronę logowania

Wprowadź dane z data.json

Sprawdź komunikat na stronie

W przypadku niepowodzenia – wykonaj screenshot i dodaj go do raportu HTML

Dlaczego ten projekt?
- Pokazuje praktyczne użycie POM + Pytest
- Ułatwia debugowanie przez screenshoty i raporty
- Umożliwia łatwą rozbudowę testów o kolejne przypadki
- Może być bazą dla większego frameworka automatyzacji

Autor
Imię i nazwisko: Mateusz Padlo
Rola: Junior Test Automation Engineer
Cel projektu: Nauka automatyzacji testów w realnych warunkach, przygotowanie do pracy komercyjnej

Kontakt
Jeśli masz pytania – chętnie odpowiem!
📧 Email: matpad26@icloud.com
💼 LinkedIn: https://www.linkedin.com/in/mateusz-pad%C5%82o-437504338

📌 Dodatkowo
Możliwość łatwego zintegrowania z CI/CD (GitHub Actions)

Gotowy do rozbudowy o testy rejestracji, dashboardu itp.

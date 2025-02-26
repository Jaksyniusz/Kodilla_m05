from faker import Faker

class Wizytowka:
    def __init__(self, imie, nazwisko, firma, stanowisko, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.firma = firma
        self.stanowisko = stanowisko
        self.email = email

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.email}"

def generuj_wizytowki(liczba_wizytowek=5):
    fake = Faker("pl_PL")  # Ustawiamy język na polski
    wizytowki = []

    for _ in range(liczba_wizytowek):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        firma = fake.company()
        stanowisko = fake.job()
        email = fake.email()

        wizytowka = Wizytowka(imie, nazwisko, firma, stanowisko, email)
        wizytowki.append(wizytowka)

    return wizytowki

def wyswietl_wizytowki(wizytowki):
    for wizytowka in wizytowki:
        print(wizytowka)

# Generowanie i wyświetlanie wizytówek
wizytowki = generuj_wizytowki()
wyswietl_wizytowki(wizytowki)
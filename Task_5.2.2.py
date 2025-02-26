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

    def contact(self):
        print(f"Kontaktuję się z {self.imie} {self.nazwisko} ({self.stanowisko}) - {self.email}")

    @property
    def dlugosc_imienia_nazwiska(self):
        return len(self.imie) + len(self.nazwisko) + 1  # +1 za spację

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

# Generowanie wizytówek
wizytowki = generuj_wizytowki()

# Wyświetlenie wizytówek
print("Lista wizytówek:")
wyswietl_wizytowki(wizytowki)

# Kontakt z każdą osobą
print("\nKontakt z osobami:")
for wizytowka in wizytowki:
    wizytowka.contact()

# Wyświetlenie długości imienia i nazwiska
print("\nDługość imienia i nazwiska:")
for wizytowka in wizytowki:
    print(f"{wizytowka.imie} {wizytowka.nazwisko}: {wizytowka.dlugosc_imienia_nazwiska} znaków")
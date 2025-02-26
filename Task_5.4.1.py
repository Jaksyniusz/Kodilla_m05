from faker import Faker
import time

# Dekorator do mierzenia czasu
def mierz_czas(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Zaczynamy mierzyć czas
        result = func(*args, **kwargs)  # Wywołujemy funkcję
        end_time = time.time()  # Kończymy mierzyć czas
        czas_wykonania = end_time - start_time  # Obliczamy czas wykonania
        print(f"Czas wykonania funkcji {func.__name__}: {czas_wykonania:.4f} sekund")
        return result
    return wrapper

# Klasa wizytówki
class Wizytowka:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.email}"

# Funkcja generująca wizytówki
@mierz_czas
def generuj_wizytowki(ilosc=1000):
    fake = Faker("pl_PL")  # Ustawiamy język na polski
    wizytowki = []

    for _ in range(ilosc):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()

        wizytowka = Wizytowka(imie, nazwisko, telefon, email)
        wizytowki.append(wizytowka)

    return wizytowki

# Przykład użycia
if __name__ == "__main__":
    wizytowki = generuj_wizytowki(1000)
    print(f"Wygenerowano {len(wizytowki)} wizytówek.")
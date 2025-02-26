from faker import Faker

# Klasa bazowa
class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.email}"

    def contact(self):
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko) + 1  # +1 za spację

# Klasa rozszerzona (firmowa)
class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}")

# Funkcja do generowania wizytówek
def create_contacts(rodzaj, ilosc):
    fake = Faker("pl_PL")  # Ustawiamy język na polski
    wizytowki = []

    for _ in range(ilosc):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()

        if rodzaj == "base":
            wizytowka = BaseContact(imie, nazwisko, telefon, email)
        elif rodzaj == "business":
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            wizytowka = BusinessContact(imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy)
        else:
            raise ValueError("Nieznany rodzaj wizytówki. Użyj 'base' lub 'business'.")

        wizytowki.append(wizytowka)

    return wizytowki

# Przykład użycia
if __name__ == "__main__":
    # Tworzymy 3 wizytówki podstawowe
    base_contacts = create_contacts("base", 3)
    print("Wizytówki podstawowe:")
    for contact in base_contacts:
        contact.contact()
        print(f"Długość etykiety: {contact.label_length} znaków\n")

    # Tworzymy 3 wizytówki firmowe
    business_contacts = create_contacts("business", 3)
    print("Wizytówki firmowe:")
    for contact in business_contacts:
        contact.contact()
        print(f"Długość etykiety: {contact.label_length} znaków\n")
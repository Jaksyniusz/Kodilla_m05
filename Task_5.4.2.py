import random
from datetime import datetime

# Klasa Film
class Film:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen=0):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen

    def play(self):
        self.liczba_odtworzen += 1

    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"

# Klasa Serial
class Serial:
    def __init__(self, tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu, liczba_odtworzen=0):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
        self.liczba_odtworzen = liczba_odtworzen

    def play(self):
        self.liczba_odtworzen += 1

    def __str__(self):
        return f"{self.tytul} S{self.numer_sezonu:02d}E{self.numer_odcinka:02d}"

# Funkcje pomocnicze
def get_movies(biblioteka):
    return sorted([item for item in biblioteka if isinstance(item, Film)], key=lambda x: x.tytul)

def get_series(biblioteka):
    return sorted([item for item in biblioteka if isinstance(item, Serial)], key=lambda x: x.tytul)

def search(biblioteka, tytul):
    for item in biblioteka:
        if item.tytul == tytul:
            return item
    return None

def generate_views(biblioteka):
    item = random.choice(biblioteka)
    item.liczba_odtworzen += random.randint(1, 100)
    return item

def run_views(biblioteka):
    for _ in range(10):
        generate_views(biblioteka)

def top_titles(biblioteka, ilosc, content_type=None):
    if content_type == "film":
        items = [item for item in biblioteka if isinstance(item, Film)]
    elif content_type == "serial":
        items = [item for item in biblioteka if isinstance(item, Serial)]
    else:
        items = biblioteka

    items.sort(key=lambda x: x.liczba_odtworzen, reverse=True)
    return items[:ilosc]

# Przykładowa biblioteka
biblioteka = [
    Film("Pulp Fiction", 1994, "Kryminał"),
    Film("Incepcja", 2010, "Sci-Fi"),
    Serial("The Simpsons", 1989, "Animacja", 5, 1),
    Serial("Breaking Bad", 2008, "Dramat", 7, 2),
    Serial("Friends", 1994, "Komedia", 10, 3),
]

# Uruchomienie programu
if __name__ == "__main__":
    print("Biblioteka filmów")

    # Generowanie odtworzeń
    run_views(biblioteka)

    # Wyświetlenie najpopularniejszych tytułów
    data = datetime.now().strftime("%d.%m.%Y")
    print(f"\nNajpopularniejsze filmy i seriale dnia {data}:")
    top3 = top_titles(biblioteka, 3)
    for i, item in enumerate(top3, 1):
        print(f"{i}. {item} - {item.liczba_odtworzen} odtworzeń")

    # Dodatkowe funkcje
    print("\nFilmy:")
    for film in get_movies(biblioteka):
        print(film)

    print("\nSeriale:")
    for serial in get_series(biblioteka):
        print(serial)

    # Wyszukiwanie
    szukany_tytul = "Incepcja"
    wynik = search(biblioteka, szukany_tytul)
    print(f"\nWynik wyszukiwania dla '{szukany_tytul}': {wynik}")
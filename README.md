# Kodilla_m05
5th module tasks

### Zadanie 5.1

Ćwiczenie – książka adresowa<br>
Wyobraź sobie, że właśnie wracasz z obchodów Dni Sapera (niezwykle hucznych), Święta Bigosu, albo Konwencji Wielbicieli Pizzy Hawajskiej. Jedno jest pewne – masz całą kolekcję wizytówek od ludzi, z którymi chcesz utrzymać kontakt i przydałaby się książka adresowa, żeby ich wszystkich nie pogubić.<br>
Stwórz klasę, która będzie przechowywać informacje z jednej wizytówki. Przyjmij, że każda wizytówka zawiera dane takie jak: imię, nazwisko, nazwa firmy, stanowisko, adres e-mail.<br>
Zdefiniuj listę, która będzie zawierała 5 wizytówek ludzi o losowych danych (dane możesz skopiować ze strony takiej jak Fake Name Generator.<br>
Skonstruuj pętlę, która wyświetli całą zawartość listy wizytówek tak, aby w jednej linii widoczne było imię, nazwisko i adres e-mail właściciela wizytówki.
Sensowne losowe dane w Pythonie<br>
Czasami zdarza się, że potrzebujesz większej ilości danych do sprawdzenia działania swojego programu (np. chcesz zweryfikować czy dobrze wszystko zliczasz, jak wyświetlają się dane, jeśli jest ich więcej itd.).<br>
Jest to nie lada problem, ponieważ stworzenie ręcznie zestawu danych, który będzie wyglądał sensownie (inaczej niż losowe ciągi znaków), może być skomplikowane.<br>
Z pomocą przychodzi jedna z wielu bibliotek, dostępnych na PyPi, czyli Faker.<br>
W telegraficznym skrócie: Faker dostarcza klasę, która potrafi tworzyć losowe dane, ale w sposób, który ma sens dla ludzi.<br>
Zachęcamy do zapoznania się z dokumentacją modułu faker, jego instalacji i korzystania w zadaniach, jeśli będziesz potrzebować losowych danych, tworzonych automatycznie.<br>
Jeśli się zdecydujesz, do instalacji wystarczy użyć komendy:<br>
pip install faker==4.0.0<br>
Wersja 4.0.0 będzie dobrym wyborem.<br>
<br>
Ćwiczenie<br>
Napisz funkcję, która tworzy instancje Twojej klasy reprezentującej wizytówkę. Używając biblioteki faker, którą opisaliśmy powyżej. Zapewnij losowość danych w każdej wizytówce, którą zwróci Twoja funkcja.<br>


### Zadanie 5.2.1

Ćwiczenie<br>
<prep>
    Zmodyfikuj kod z poprzedniego ćwiczenia na temat książki adresowej tak, aby obiekt wizytówki przedstawiony jako string zawierał imię, nazwisko i adres e-mail osoby, do której należy wizytówka.
    Stwórz listę wizytówek, a następnie używając funkcji sorted(), ułóż ją na trzy sposoby – według imienia, nazwiska oraz adresu e-mail.
</prep>


### Zadanie 5.2.2

Ćwiczenie<br>
<prep>
    Rozwiń program przechowujący wizytówki. Do klasy opisującej wizytówkę dodaj metodę contact(), która wypisze na konsoli napis “Kontaktuję się z …”, a na końcu wyświetli imię, nazwisko, stanowisko i adres e-mail osoby, z którą chcemy się skontaktować.
    W klasie przechowującej wizytówkę zdefiniuj dynamiczny atrybut (używając @property), który będzie zwracał sumę długości imienia i nazwiska oddzielonych spacją. Tę informację można wykorzystać przykładowo przy adresowaniu kopert lub zaproszeń, gdzie często miejsce na imię i nazwisko jest dosyć ograniczone.
</prep>


### Zadanie 5.3

Zadanie: wizytówki<br>
Dysponujesz już całkiem rozbudowanym programem do obsługi wizytówek. Po dodaniu kilku elementów wyślij go Mentorowi.<br>
<prep>
    Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej klasy (BusinessContact) rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
    Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.
    Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.
    Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje dwa parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.
</prep>


### Zadanie 5.4.1

Ćwiczenie<br>
Napisz funkcję, która tworzy listę zawierającą 1000 wizytówek z losowymi danymi (użyj biblioteki faker, którą opisywaliśmy w tym module).<br>
Następnie stwórz dekorator, który zmierzy czas wykonywania tej operacji. Niech udekorowana funkcja wyświetla czas obliczeń (w sekundach) po ich zakończeniu.<br>
Wskazówka. W Pythonie do operacji na datach i czasie wykorzystuje się moduł datetime.<br>


### Zadanie 5.4.2

Zadanie: biblioteka filmów<br>
A teraz coś z zupełnie innej beczki. Wyobraź sobie, że tworzysz system obsługujący bibliotekę filmów i seriali. Wykorzystaj wiedzę na temat programowania obiektowego i napisz program, który spełnia następujące założenia:<br>
<prep>
    Jest w stanie przechowywać informacje na temat filmów, które znajdują się w systemie. Każdy film powinien mieć następujące atrybuty:
        Tytuł
        Rok wydania
        Gatunek
        Liczba odtworzeń
    Umożliwia przechowywanie informacji na temat seriali. Każdy serial powinien mieć następujące atrybuty:
        Tytuł
        Rok wydania
        Gatunek
        Numer odcinka
        Numer sezonu
        Liczba odtworzeń
    Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.
    Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.: “The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej, natomiast po E - numer odcinka, również w zapisie dwucyfrowym).
    Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.
    Przechowuje filmy i seriale w jednej liście.
</prep>
Dodatkowo:<br>
<prep>
    Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio tylko filmy oraz tylko seriale. Posortuj listę wynikową alfabetycznie.
    Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
    Napisz funkcję generate_views, która losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
    Napisz funkcję, która uruchomi generate_views 10 razy.
    Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki. Dla chętnych: dodaj do funkcji parametr content_type, którym wybierzesz czy mają zostać pokazane filmy, czy seriale.
</prep>
Zadania dla chętnych<br>
<prep>
    Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki. Funkcja powinna przyjmować parametry takie jak: tytuł serialu, rok wydania, gatunek, numer sezonu, liczba odcinków do dodania.
    Do klasy reprezentującej serial, dopisz funkcję zewnętrzną, która wyświetla liczbę odcinków danego serialu dostępnych w bibliotece.
</prep>
Niech program po uruchomieniu działa w następujący sposób:<br>
<prep>
    Wyświetli na konsoli komunikat Biblioteka filmów.
    Wypełni bibliotekę treścią.
    Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
    Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>, gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
    Wyświetli listę top 3 najpopularniejszych tytułów.
</prep>
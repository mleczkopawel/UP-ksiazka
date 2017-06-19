from Ksiazka import Ksiazka
from Polka import Polka

polka_istnieje = False
polka = None


def menu():
    print('''    1. Stwórz półkę
    2. Stwórz książkę i dodaj do półki
    3. Wyświetl półkę
    4. Usuń książkę
    5. Szukaj książki
    6. Sortuj półkę
    7. Zamknij''')


def stworz_polke():
    p_i = True
    nazwa = input('Podaj nazwę półki: ')
    pol = Polka()
    print('Półka ' + nazwa + ' stworzona')
    return pol, p_i


def dodaj_ksiazke():
    if polka_istnieje:
        nazwa = input('Podaj nazwę książki: ')
        autor = input('Podaj autora książki: ')
        ksiazka = Ksiazka(autor, nazwa)
        polka.dodaj(ksiazka)
        print('Książka dodana')
    else:
        print('Półka nie istnieje, na początku stwórz półkę')


def wyswietl_polke():
    if polka_istnieje:
        polka.pokaz()
    else:
        print('Półka nie istnieje, na początku stwórz półkę')


def usun_ksiazke():
    if polka_istnieje:
        indeks_ksiazki = input('Podaj indeks książki do usunięcia: ')
        polka.usun(int(indeks_ksiazki))
    else:
        print('Półka nie istnieje, na początku stwórz półkę')


def szukaj_ksiazki():
    if polka_istnieje:
        szukana_fraza = input('Podaj czego szukasz: ')
        polka.znajdz(szukana_fraza)
    else:
        print('Półka nie istnieje, na początku stwórz półkę')


def sortuj():
    if polka_istnieje:
        fraza_sortowania = input('Podaj po jakiej wartości chcesz sortować (autor/tytul): ')
        polka.sortuj(fraza_sortowania)
        polka.pokaz()
    else:
        print('Półka nie istnieje, na początku stwórz półkę')


zamknij = True
while zamknij:
    menu()
    wybor = int(input('Co chcesz zrobić: '))
    if wybor == 1:
        polka, polka_istnieje = stworz_polke()
    elif wybor == 2:
        dodaj_ksiazke()
    elif wybor == 3:
        wyswietl_polke()
    elif wybor == 4:
        usun_ksiazke()
    elif wybor == 5:
        szukaj_ksiazki()
    elif wybor == 6:
        sortuj()
    elif wybor == 7:
        zamknij = False
    else:
        print('Niewłaściwy wybór')
quit()
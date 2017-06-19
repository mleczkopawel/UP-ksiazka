from Ksiazka import Ksiazka


class Polka:
    def __init__(self, ksiazki):
        self.polka = []
        for item in range(len(ksiazki)):
            self.polka.append(ksiazki[item])

    def dodaj(self, ksiazka):
        for i in range(len(self.polka)):
            ksiega = self.polka[i]
            if ksiazka.tytul == ksiega.tytul and ksiazka.autor == ksiega.autor:
                print('nie można dodać...')
            else:
                self.polka.append(ksiazka)

    def usun(self, index):
        usunieta_ksiazka = False
        for i in range(len(self.polka)):
            if i == index:
                del self.polka[i]
                print('Książka usunięta')
                usunieta_ksiazka = True
        if not usunieta_ksiazka:
            print('Nie istnieje książka o podanym indekie')

    def znajdz(self, tekst):
        for i in range(len(self.polka)):
            ksiega = self.polka[i]
            if ksiega.wyszukaj(tekst):
                print(ksiega)

    def pokaz(self):
        opis_polki = ''
        for i in range(len(self.polka)):
            opis_polki += "----ksiazka " + str(i) + "----\n"
            opis_polki += str(self.polka[i])
            opis_polki += "\n-----------------\n"
        print(opis_polki)

    def sortuj(self, parametr):
        if parametr == 'autor':
            self.polka.sort(key=lambda x: x.autor)
        elif parametr == 'tytul':
            self.polka.sort(key=lambda x: x.tytul)
        else:
            print('zły parametr')

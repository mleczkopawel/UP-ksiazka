class Ksiazka:

    _id = 0

    def __init__(self, autor, tytul):
        self.autor = autor
        self.tytul = tytul
        Ksiazka._id += 1

    def wyszukaj(self, fraza):
        if self.autor == fraza or self.tytul == fraza:
            return True
        else:
            return False

    def __str__(self):
        return self.autor + ': \'' + self.tytul + '\''

    def get_id(self):
        return self._id

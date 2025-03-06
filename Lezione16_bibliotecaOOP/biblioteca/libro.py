class Elemento:
    def __init__(self, titolo, autore, anno):
        self._titolo = titolo 
        self._autore = autore
        self._anno = anno

    def __str__(self):
        return f"{self._titolo} di {self._autore} ({self._anno})"


class Libro(Elemento):
    def __init__(self, titolo, autore, anno, isbn, posizione_scaffale):
        super().__init__(titolo, autore, anno)
        self.__isbn = isbn
        self.posizione_scaffale = posizione_scaffale

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, valore):
        if len(valore) not in (10, 13):
            raise ValueError("L'ISBN deve essere lungo 10 o 13 caratteri!")
        self.__isbn = valore

    def __str__(self):
        return f"Libro: {super().__str__()} - ISBN: {self.__isbn} - Scaffale: {self.posizione_scaffale}"
    
    

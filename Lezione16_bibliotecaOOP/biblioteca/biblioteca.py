import csv
from libro import Libro
from membro import Membro

class Biblioteca:
    def __init__(self):

        self.libri = {}    # key: isbn, value: Libro
        self.membri = {}   # key: id_membro, value: Membro

    def aggiungi_libro(self, libro):
        if libro.isbn in self.libri:
            print("Il libro esiste già!")
        else:
            self.libri[libro.isbn] = libro

    def rimuovi_libro(self, isbn):
        if isbn in self.libri:
            del self.libri[isbn]
        else:
            print("Libro non trovato!")

    def cerca_libri(self, parola_chiave):
        risultati = []
        for libro in self.libri.values():
            if parola_chiave.lower() in libro._titolo.lower() or parola_chiave.lower() in libro._autore.lower():
                risultati.append(libro)
        return risultati

    def carica_libri(self, nome_file):
        try:
            with open(nome_file, newline='', encoding='utf-8') as csvfile:
                lettore = csv.DictReader(csvfile)
                for riga in lettore:
                    titolo = riga.get("titolo")
                    autore = riga.get("autore")
                    anno = int(riga.get("anno"))
                    isbn = riga.get("isbn")
                    sezione_scaffale = riga.get("sezione_scaffale")
                    numero_scaffale = int(riga.get("numero_scaffale"))
                    posizione_scaffale = (sezione_scaffale, numero_scaffale)
                    libro = Libro(titolo, autore, anno, isbn, posizione_scaffale)
                    self.aggiungi_libro(libro)
        except Exception as e:
            print("Errore nel caricamento dei libri:", e)

    def salva_libri(self, nome_file):
        try:
            with open(nome_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ["titolo", "autore", "anno", "isbn", "sezione_scaffale", "numero_scaffale"]
                scrittore = csv.DictWriter(csvfile, fieldnames=fieldnames)
                scrittore.writeheader()
                for libro in self.libri.values():
                    scrittore.writerow({
                        "titolo": libro._titolo,
                        "autore": libro._autore,
                        "anno": libro._anno,
                        "isbn": libro.isbn,
                        "sezione_scaffale": libro.posizione_scaffale[0],
                        "numero_scaffale": libro.posizione_scaffale[1]
                    })
        except Exception as e:
            print("Errore nel salvataggio dei libri:", e)

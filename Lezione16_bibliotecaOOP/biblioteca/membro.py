class Membro:
    def __init__(self, id_membro, nome, email):
        self.id_membro = id_membro
        self.nome = nome
        self.email = email
        self.libri_in_prestito = {}

    def prendi_in_prestito(self, libro):
        if libro.isbn in self.libri_in_prestito:
            print("Il libro è già in prestito!")
        else:
            self.libri_in_prestito[libro.isbn] = libro

    def restituisci_libro(self, libro):
        if libro.isbn in self.libri_in_prestito:
            del self.libri_in_prestito[libro.isbn]

    def __str__(self):
        return f"Membro {self.id_membro}: {self.nome} - Email: {self.email}"


class Studente(Membro):
    def __init__(self, id_membro, nome, email, corso):
        super().__init__(id_membro, nome, email)
        self.corso = corso

    def __str__(self):
        return f"Studente {self.id_membro}: {self.nome} (Corso: {self.corso})"


class Insegnante(Membro):
    def __init__(self, id_membro, nome, email, materia):
        super().__init__(id_membro, nome, email)
        self.materia = materia

    def __str__(self):
        return f"Insegnante {self.id_membro}: {self.nome} (Materia: {self.materia})"
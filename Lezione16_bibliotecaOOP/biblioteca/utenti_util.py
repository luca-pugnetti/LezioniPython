import csv
import hashlib

def genera_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def carica_utenti(filename="utenti.csv"):
    utenti = {}
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            lettore = csv.DictReader(csvfile)
            for riga in lettore:
                email = riga.get("email").strip()
                password_hash = riga.get("password").strip()
                ruolo = riga.get("ruolo").strip()
                utenti[email] = {"password": password_hash, "ruolo": ruolo}
    except FileNotFoundError:
        # Se il file non esiste, lo creiamo con l'intestazione
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            campi = ["email", "password", "ruolo"]
            scrittore = csv.DictWriter(csvfile, fieldnames=campi)
            scrittore.writeheader()
    return utenti

def salva_utente(email, password, ruolo, filename="utenti.csv"):
    password_hash = genera_hash(password)
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        campi = ["email", "password", "ruolo"]
        scrittore = csv.DictWriter(csvfile, fieldnames=campi)
        scrittore.writerow({"email": email, "password": password_hash, "ruolo": ruolo})


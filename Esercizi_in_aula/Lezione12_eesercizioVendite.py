"""

1. Creazione del file CSV con i dati di vendita

dati_vendite = [
    ["Data", "Prodotto", "Quantità", "Prezzo Unitario", "Totale"],
    ["2024-01-01", "Laptop", 2, 800, 1600],
    ["2024-01-01", "Mouse", 5, 20, 100],
    ["2024-01-02", "Laptop", 1, 800, 800],
    ["2024-01-02", "Tastiera", 3, 50, 150],
    ["2024-01-03", "Monitor", 2, 200, 400],
    ["2024-01-03", "Mouse", 4, 20, 80],
    ["2024-01-04", "Laptop", 3, 800, 2400],
    ["2024-01-04", "Tastiera", 2, 50, 100],
    ["2024-01-05", "Monitor", 1, 200, 200],
    ["2024-01-05", "Laptop", 2, 800, 1600]
]


2. Lettura del file CSV e calcolo delle statistiche
Ora dobbiamo leggere il file CSV e calcolare:

Il totale delle vendite per ogni prodotto.
Il totale complessivo delle vendite.
Il prodotto più venduto in termini di quantità.


3. Scrivere i risultati in un nuovo file CSV statistiche_vendite.csv

"""

import csv

dati_vendite = [
    ["Data", "Prodotto", "Quantità", "Prezzo Unitario", "Totale"],
    ["2024-01-01", "Laptop", 2, 800, 1600],
    ["2024-01-01", "Mouse", 5, 20, 100],
    ["2024-01-02", "Laptop", 1, 800, 800],
    ["2024-01-02", "Tastiera", 3, 50, 150],
    ["2024-01-03", "Monitor", 2, 200, 400],
    ["2024-01-03", "Mouse", 4, 20, 80],
    ["2024-01-04", "Laptop", 3, 800, 2400],
    ["2024-01-04", "Tastiera", 2, 50, 100],
    ["2024-01-05", "Monitor", 1, 200, 200],
    ["2024-01-05", "Laptop", 2, 800, 1600]
]

with open("vendite.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(dati_vendite)
    
print("File vendite.csv creato correttamente")

totale_vendite_per_prodotto = {}
quantita_venduta_per_prodotto = {}
totale_complessivo = 0

with open("vendite.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)
    
    for riga in reader:
        prodotto = riga[1]
        quantita = int(riga[2])
        totale = float(riga[4])
        
        if prodotto not in totale_vendite_per_prodotto:
            totale_vendite_per_prodotto[prodotto] = 0
            quantita_venduta_per_prodotto[prodotto] = 0
            
        totale_vendite_per_prodotto[prodotto] += totale
        quantita_venduta_per_prodotto[prodotto] += quantita
        totale_complessivo += totale
        
prodotto_piu_venduto = None
quantita_max = 0

for prodotto in quantita_venduta_per_prodotto:
    if quantita_venduta_per_prodotto[prodotto] > quantita_max:
        prodotto_piu_venduto = prodotto
        quantita_max = quantita_venduta_per_prodotto[prodotto]
        
with open("statistiche_vendite.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(['Prodotto', 'Totale vendite', 'Quantità venduta'])
    
    for prodotto in totale_vendite_per_prodotto:
        writer.writerow([prodotto, totale_vendite_per_prodotto[prodotto], quantita_venduta_per_prodotto[prodotto]])
        
    writer.writerow([])
    
    writer.writerow(["Totale complessivo", totale_complessivo])
    writer.writerow(["Prodotto più venduto", prodotto_piu_venduto, quantita_max])
    
print("\n File statistiche.csv creato con successo")
        
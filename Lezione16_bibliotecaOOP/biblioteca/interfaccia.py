import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from biblioteca import Biblioteca
from libro import Libro
from utenti_util import genera_hash, carica_utenti, salva_utente

class InterfacciaBiblioteca:
    def __init__(self, master, biblioteca):
        self.master = master
        self.biblioteca = biblioteca
        self.utenti = carica_utenti()  # Carica gli utenti dal file utenti.csv
        self.utente_corrente = None    # Utente autenticato
        
        master.title("Sistema di Gestione Biblioteca")
        
        self.centra_finestra(master)
        
        # Frame per il login
        self.frame_accesso = tk.Frame(master)
        self.frame_accesso.pack(expand=True)

        
        tk.Label(self.frame_accesso, text="Email:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(self.frame_accesso)
        self.entry_email.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_accesso, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_password = tk.Entry(self.frame_accesso, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        
        self.bottone_accesso = tk.Button(self.frame_accesso, text="Accedi", command=self.verifica_accesso)
        self.bottone_accesso.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Frame principale per la gestione dei libri (mostrato dopo il login)
        self.frame_principale = tk.Frame(master)
        
    def centra_finestra(self, root, larghezza=800, altezza=600):
        # Ottieni la dimensione dello schermo
        larghezza_schermo = root.winfo_screenwidth()
        altezza_schermo = root.winfo_screenheight()
    
        # Calcola la posizione per centrare la finestra
        x = (larghezza_schermo - larghezza) // 2
        y = (altezza_schermo - altezza) // 2
    
        # Imposta la geometria della finestra
        root.geometry(f"{larghezza}x{altezza}+{x}+{y}")

    
    def verifica_accesso(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get().strip()
        if email in self.utenti:
            expected_hash = self.utenti[email]["password"]
            if genera_hash(password) == expected_hash:
                self.utente_corrente = {"email": email, "ruolo": self.utenti[email]["ruolo"]}
                messagebox.showinfo("Accesso", "Accesso effettuato con successo!")
                self.frame_accesso.destroy()  # Rimuove il frame del login
                self.mostra_interfaccia_principale()
            else:
                messagebox.showerror("Accesso Negato", "Password non valida!")
        else:
            messagebox.showerror("Accesso Negato", "Email non registrata!")
    
    def mostra_interfaccia_principale(self):
        self.frame_principale.pack(pady=10)
        
        # Frame per la ricerca e le azioni sui libri
        self.frame_superiore = tk.Frame(self.frame_principale)
        self.frame_superiore.pack(pady=10)
        
        self.etichetta_ricerca = tk.Label(self.frame_superiore, text="Cerca Libro:")
        self.etichetta_ricerca.pack(side=tk.LEFT, padx=5)
        
        self.entry_ricerca = tk.Entry(self.frame_superiore)
        self.entry_ricerca.pack(side=tk.LEFT, padx=5)
        
        self.bottone_ricerca = tk.Button(self.frame_superiore, text="Cerca", command=self.cerca_libri)
        self.bottone_ricerca.pack(side=tk.LEFT, padx=5)
        
        # Pulsanti per aggiungere e rimuovere libri
        self.bottone_aggiungi = tk.Button(self.frame_superiore, text="Aggiungi Libro", command=self.aggiungi_libro)
        self.bottone_aggiungi.pack(side=tk.LEFT, padx=5)
        
        self.bottone_rimuovi = tk.Button(self.frame_superiore, text="Rimuovi Libro", command=self.rimuovi_libro)
        self.bottone_rimuovi.pack(side=tk.LEFT, padx=5)
        
        self.bottone_logout = tk.Button(self.frame_superiore, text="Log out", command=self.logout)
        self.bottone_logout.pack(side=tk.RIGHT)
        
        # Se l'utente è amministratore, mostra il pulsante per registrare nuovi utenti
        if self.utente_corrente["ruolo"] == "amministratore":
            self.bottone_registra_utente = tk.Button(self.frame_superiore, text="Registra Nuovo Utente", command=self.registra_utente)
            self.bottone_registra_utente.pack(side=tk.LEFT, padx=5)
        
        # Se l'utente è studente, disabilita le funzioni di aggiunta e rimozione libri
        if self.utente_corrente["ruolo"] == "studente":
            self.bottone_aggiungi.config(state="disabled")
            self.bottone_rimuovi.config(state="disabled")
        
        # Frame per la visualizzazione della lista dei libri
        self.frame_lista = tk.Frame(self.frame_principale)
        self.frame_lista.pack(pady=10)
        
        self.tabella = ttk.Treeview(self.frame_lista, columns=("Titolo", "Autore", "Anno", "ISBN", "Scaffale"), show="headings")
        self.tabella.heading("Titolo", text="Titolo")
        self.tabella.heading("Autore", text="Autore")
        self.tabella.heading("Anno", text="Anno")
        self.tabella.heading("ISBN", text="ISBN")
        self.tabella.heading("Scaffale", text="Scaffale")
        self.tabella.pack()
        
        self.riempi_tabella()
        self.avvia_autosalvataggio()
    
    def riempi_tabella(self, libri=None):
        for item in self.tabella.get_children():
            self.tabella.delete(item)
        if libri is None:
            libri = list(self.biblioteca.libri.values())
        for libro in libri:
            self.tabella.insert("", tk.END, values=(
                libro._titolo,
                libro._autore,
                libro._anno,
                libro.isbn,
                libro.posizione_scaffale
            ))
    
    def cerca_libri(self):
        parola = self.entry_ricerca.get()
        risultati = self.biblioteca.cerca_libri(parola)
        self.riempi_tabella(risultati)
    
    def aggiungi_libro(self):
        titolo = simpledialog.askstring("Input", "Inserisci il titolo:")
        if not titolo:
            return
        autore = simpledialog.askstring("Input", "Inserisci l'autore:")
        if not autore:
            return
        try:
            anno = int(simpledialog.askstring("Input", "Inserisci l'anno:"))
        except:
            messagebox.showerror("Errore", "Anno non valido!")
            return
        isbn = simpledialog.askstring("Input", "Inserisci l'ISBN:")
        if not isbn:
            return
        sezione_scaffale = simpledialog.askstring("Input", "Inserisci la sezione dello scaffale:")
        try:
            numero_scaffale = int(simpledialog.askstring("Input", "Inserisci il numero dello scaffale:"))
        except:
            messagebox.showerror("Errore", "Numero dello scaffale non valido!")
            return
        posizione_scaffale = (sezione_scaffale, numero_scaffale)
        nuovo_libro = Libro(titolo, autore, anno, isbn, posizione_scaffale)
        self.biblioteca.aggiungi_libro(nuovo_libro)
        self.riempi_tabella()
        self.salva_dati()
    
    def rimuovi_libro(self):
        elementi_selezionati = self.tabella.selection()
        if not elementi_selezionati:
            messagebox.showerror("Errore", "Seleziona un libro da rimuovere")
            return
        id_selezionato = elementi_selezionati[0]
        valori = self.tabella.item(id_selezionato)["values"]
        isbn_selezionato = str(valori[3]).strip()
        if isbn_selezionato not in self.biblioteca.libri:
            messagebox.showerror("Errore", f"Libro non trovato: ISBN {isbn_selezionato}")
            return
        self.biblioteca.rimuovi_libro(isbn_selezionato)
        self.riempi_tabella()
        self.salva_dati()
    
    def registra_utente(self):
        email = simpledialog.askstring("Nuovo Utente", "Inserisci l'email del nuovo utente:")
        if not email:
            return
        password = simpledialog.askstring("Nuovo Utente", "Inserisci la password del nuovo utente:", show="*")
        if not password:
            return
        ruolo = simpledialog.askstring("Nuovo Utente", "Inserisci il ruolo (studente/professore):")
        if ruolo not in ["studente", "professore"]:
            messagebox.showerror("Errore", "Ruolo non valido! Deve essere 'studente' o 'professore'.")
            return
        salva_utente(email, password, ruolo)
        self.utenti[email] = {"password": genera_hash(password), "ruolo": ruolo}
        messagebox.showinfo("Successo", f"Utente {email} registrato come {ruolo}.")
    
    def salva_dati(self):
        self.biblioteca.salva_libri("libri.csv")
    
    def avvia_autosalvataggio(self):
        self.salva_dati()
        self.master.after(300000, self.avvia_autosalvataggio)
        
    def logout(self):
        self.frame_principale.forget()
        self.__init__(self.master, self.biblioteca)
        
        
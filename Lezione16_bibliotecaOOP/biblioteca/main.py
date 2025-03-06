import tkinter as tk
from biblioteca import Biblioteca
from interfaccia import InterfacciaBiblioteca

def main():
 
    biblioteca = Biblioteca()


    biblioteca.carica_libri("libri.csv")


    root = tk.Tk()
    interfaccia = InterfacciaBiblioteca(root, biblioteca)
    root.mainloop()


    biblioteca.salva_libri("libri.csv")

if __name__ == "__main__":
    main()

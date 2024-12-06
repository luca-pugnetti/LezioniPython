import turtle
import math

def sierpinski(t, lunghezza, ordine):
    """
    Disegna il triangolo di Sierpinski usando turtle.

    :parametro t: Oggetto turtle
    :parametro lunghezza: Lunghezza del lato del triangolo
    :parametro ordine: Ordine del triangolo di Sierpinski
    """
    
    if ordine == 0:
        # Disegna un triangolo pieno alla base della ricorsione
        disegna_triangolo_pieno(t, lunghezza, "aqua")
    else:
        
        print("Lunghezza: ".ljust(10), str(int(lunghezza / 2)).ljust(15), "Ordine: ", ordine - 1)
        # Triangolo in basso a sinistra
        sierpinski(t, lunghezza / 2, ordine - 1)
        
        # Triangolo in basso a destra
        t.forward(lunghezza / 2)
        sierpinski(t, lunghezza / 2, ordine - 1)
        t.backward(lunghezza / 2)
        
        # Triangolo in basso
        t.left(60)
        t.forward(lunghezza / 2)
        t.right(60)
        sierpinski(t, lunghezza / 2, ordine - 1)
        
        # Torna alla posizione iniziale
        t.left(60)
        t.backward(lunghezza / 2)
        t.right(60)

def disegna_triangolo_pieno(t, lunghezza, colore):
    """
    Disegna un triangolo pieno di un dato colore.

    :parametro t: Oggetto turtle
    :parametro lunghezza: Lunghezza del lato del triangolo
    :parametro colore: colore del triangolo
    """
    t.fillcolor(colore)
    t.begin_fill()
    for _ in range(3):
        t.fd(lunghezza)
        t.lt(120)
    t.end_fill()

# Setting iniziale dello schermo
screen = turtle.Screen()
screen.clear()
screen.setup(width=800, height=800)
screen.bgcolor("white")
screen.title("Sierpinski Triangle")

# Creazione e assegnamento dell'oggetto turtle
t = turtle.Turtle()
t.speed(0)


# Posizionamento iniziale
t.penup()
base = 400
altezza = math.sqrt(3)/2 * 400
t.goto(-base/2, -altezza/2)
t.pendown()
t.hideturtle()

sierpinski(t, 400, 4)

turtle.done()

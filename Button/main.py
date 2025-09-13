# Importa as bibliotecas utilizadas
from tkinter import *
from random import *

# Faz as configurações do jogo
GAME_TITLE = "Button"
GAME_WIDHT = 700
GAME_HEIGHT = 700
BACKGROUND_COLOR = "black"

# Cria uma janela
window = Tk()
window.title(GAME_TITLE)
window.geometry(f"{GAME_WIDHT}x{GAME_HEIGHT}")

# Cria uma tela
canvas = Canvas(window, width=GAME_WIDHT, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

# Cria coordenadas aleatórias
def PosicaoAleatoria():
    global x, y
    x = randint(0, GAME_WIDHT - 100)
    y = randint(0, GAME_HEIGHT - 100)
    button.place(x=x, y=y)

# Cria um botão
button = Button(window, text="Clique-me!", font=("sans-safari", 40), command=PosicaoAleatoria)
button.place(x=100, y=100)

# Faz que a janela seja aberta
window.mainloop()

# Importa as bibliotecas essenciais
from tkinter import *
from random import *

# Cria as configurações do jogo
GAME_WIDHT = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# Cria uma classe só para o player
class Snake:
    def __init__(self):
        self.bodySize = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


# Cria uma classe para um coletavel
class Food:
    def __init__(self):
        x = randint(0, (GAME_WIDHT // SPACE_SIZE - 1)) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT // SPACE_SIZE - 1)) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Essa função faz que o player consiga ser rotacionado
def NextTurn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f"Score:{score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if CheckCollisions(snake):
        GameOver()
    else:
        window.after(SPEED, NextTurn, snake, food)

# Essa função faz que o player va para outra direção
def ChangeDirection(newDirection):
    global direction
    if newDirection == "left":
        if direction != "right":
            direction = newDirection
    elif newDirection == "right":
        if direction != "left":
            direction = newDirection
    elif newDirection == "up":
        if direction != "down":
            direction = newDirection
    elif newDirection == "down":
        if direction != "up":
            direction = newDirection

# Essa função dedecta colisões
def CheckCollisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDHT:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for bodyPart in snake.coordinates[1:]:
        if x == bodyPart[0] and y == bodyPart[1]:
            return True
    return False

# Essa funcão verifica se o player morreu
def GameOver():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=("sans-safari", 70), text="Vc perdeu!", fill="red", tag="Fim")

# Cria uma janela para o jogo
window = Tk()
window.title("Snake")
window.resizable(False, False)

# Faz as configurações no inicio do jogo
score = 0
direction = "down"

# Cria um rotulo no jogo
label = Label(window, text=f"Score:{score}", font=("sans-safari", 40))
label.pack()

# Cria uma tela ao jogo
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDHT)
canvas.pack()

# Verifica se o player clicou alguma tecla
window.bind("<Left>", lambda event: ChangeDirection("left"))
window.bind("<Right>", lambda event: ChangeDirection("right"))
window.bind("<Up>", lambda event: ChangeDirection("up"))
window.bind("<Down>", lambda event: ChangeDirection("down"))

# Cria os objetos do jogo
player = Snake()
foodSnake = Food()
NextTurn(player, foodSnake)

# Faz que a janela seja aberta
window.mainloop()

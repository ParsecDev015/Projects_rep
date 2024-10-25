import turtle
import time

# Crear la ventana y ajustar sus propiedades
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Detener actualizaciones automáticas de la pantalla

# Crear la tortuga para los gráficos
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Crear tortugas separadas para las paletas
palette1 = turtle.Turtle()
palette1.speed(0)
palette1.shape("square")
palette1.color("white")
palette1.shapesize(stretch_wid=6, stretch_len=1)
palette1.penup()
palette1.goto(-350, 0)

palette2 = turtle.Turtle()
palette2.speed(0)
palette2.shape("square")
palette2.color("white")
palette2.shapesize(stretch_wid=6, stretch_len=1)
palette2.penup()
palette2.goto(350, 0)

# Crear la pelota
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1  # Velocidad en el eje X
ball.dy = 1  # Velocidad en el eje Y

# Puntajes
score_p1 = 0
score_p2 = 0

# Dibujar el marcador
def draw_scoreboard():
    t.clear()
    t.penup()
    t.color("white")
    t.goto(0, 260)
    t.write(f"Jugador 1: {score_p1}  Jugador 2: {score_p2}", align="center", font=("Courier", 24, "normal"))

# Dibujar la red
def draw_net():
    t.goto(0, 300)
    t.setheading(270)
    t.pensize(3)
    for _ in range(30):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)

# Funciones para mover las paletas
def move_palette1_up():
    y = palette1.ycor()
    if y < 250:
        palette1.sety(y + 20)

def move_palette1_down():
    y = palette1.ycor()
    if y > -250:
        palette1.sety(y - 20)

def move_palette2_up():
    y = palette2.ycor()
    if y < 250:
        palette2.sety(y + 20)

def move_palette2_down():
    y = palette2.ycor()
    if y > -250:
        palette2.sety(y - 20)

# Teclado para mover las paletas
window.listen()
window.onkeypress(move_palette1_up, "w")
window.onkeypress(move_palette1_down, "s")
window.onkeypress(move_palette2_up, "Up")
window.onkeypress(move_palette2_down, "Down")

# Función para mover la pelota y detectar colisiones
def move_ball():
    global score_p1, score_p2

    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Colisión con el borde superior
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Rebotar en el eje Y

    # Colisión con el borde inferior
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Rebotar en el eje Y

    # Colisión con el borde derecho (Jugador 1 anota)
    if ball.xcor() > 390:
        ball.goto(0, 0)  # Reiniciar la posición de la pelota
        ball.dx *= -1  # Cambiar la dirección de la pelota
        score_p1 += 1
        draw_scoreboard()
        draw_net()

    # Colisión con el borde izquierdo (Jugador 2 anota)
    if ball.xcor() < -390:
        ball.goto(0, 0)  # Reiniciar la posición de la pelota
        ball.dx *= -1  # Cambiar la dirección de la pelota
        score_p2 += 1
        draw_scoreboard()
        draw_net()

    # Colisión con la paleta 1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < palette1.ycor() + 50 and ball.ycor() > palette1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1  # Rebotar en el eje X

    # Colisión con la paleta 2
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < palette2.ycor() + 50 and ball.ycor() > palette2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1  # Rebotar en el eje X

# Dibujar marcador inicial y red
draw_scoreboard()
draw_net()

# Bucle principal del juego
while True:
    window.update()
    move_ball()
    time.sleep(0.01)  # Control de la velocidad del juego

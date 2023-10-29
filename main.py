from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Aposta", prompt="¿Quien va a ganar? Ingresa un color")
colores = ["yellow", "blue", "red", "orange", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for i in range(0, 6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.color(colores[i])
    new_turtle.shape("turtle")
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You' ve won! The {winning_color} turtle is the winner!")
            else:
                print(f"You' ve lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(a=0, b=10)
        turtle.forward(rand_distance)


screen.exitonclick()

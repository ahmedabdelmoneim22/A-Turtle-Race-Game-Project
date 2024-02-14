print("A-Turtle-Race-Game.")

from turtle import Turtle,Screen
import random
is_race_on = False
screen = Screen() # Create Instance from Screen();
screen.setup(width=500,height=400) # screen Width & Height;
# A Dialog window for the Input of a string.
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = [] # All turtles object list:
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")#(instance from Class-Turtle).
    new_turtle.penup() # No Drawing Line;
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)#Append-Turtle-instances.
#user_bet if input gives True.
if user_bet:
    is_race_on = True
while is_race_on:
    # [index0,index1,index2,index3,index4,index5,index6]
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)#random-Number
        turtle.forward(rand_distance)#(turtle-list-instances).
screen.exitonclick()#Exit-On-Click().
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#



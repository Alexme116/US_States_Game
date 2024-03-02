from turtle import Screen
from state import State
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

statesFile = pd.read_csv("50_states.csv")
statesGuessed = []

rep = False
gameIsOn = True
while len(statesGuessed) != 50 and gameIsOn:
    screen.update()
    guess = screen.textinput(f"Guessed = {len(statesGuessed)}/50", "Name: ")
    state = statesFile[statesFile.state == guess]

    for i in statesGuessed:
        if i == guess:
            print("You already guess that state")
            rep = True
            break

    if not rep:
        if len(state) != 0:
            stateGuessed = State(state.state.values[0], state.x.values[0], state.y.values[0])
            statesGuessed.append(state.state.values[0])
        elif guess is None:
            gameIsOn = False
    rep = False

screen.exitonclick()
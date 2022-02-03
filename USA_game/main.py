import pandas as pd
import turtle

data = pd.read_csv("50_states.csv")
image = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(image)
screen.clear()
turtle.shape(image)

#answer_state = screen.textinput(title='Guess the State', prompt = 'What\'s another state name? ').title()

all_states = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 guessed states', prompt = 'What\'s another state name? ').title()
    if answer_state == 'Exit':
        missed_states = [state for state in all_states if state not in guessed_states]
        missed_states = pd.DataFrame(missed_states)
        missed_states.to_csv('missed.csv')
        print(missed_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)



screen.exitonclick()

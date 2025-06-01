import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_states = []
missing_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(f"{len(guessed_states)}/50 States correct", "What's another state?").title()

    data = pandas.read_csv('50_states.csv')

    # to check for secret code and exit
    if answer_state == 'Exit':
        for state in data.state.values:
            if state not in guessed_states:
                missing_states.append(state)
        # missing_states = [state for state in data.store.values if state not in guessed_states]
        break

    # to check if the state entered really exists
    if answer_state in data.state.values:

        state_row = data[data.state == answer_state]
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state_row.x[0]), int(state_row.y[0]))
        tim.write(arg=answer_state, align='center', font=('JetBrains Mono', 8, 'normal'))
        guessed_states.append(answer_state)

    else:
        continue

# states_to_learn.csv
data_dict = {
    'states': missing_states
}

missing_states_data = pandas.DataFrame(data_dict)
missing_states_data.to_csv('states_to_learn.csv')

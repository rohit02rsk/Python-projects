import pandas as pd
import turtle as t

screen = t.Screen()
screen.title("States Guesser")
image = "States Guesser/blank_states_img.gif"
screen.addshape(image)
t.shape(image)

#------------------------------------------------------
#how the co-ordinates for the states' names were found:
#def get_coor(x, y):
#    print(x, y)
#t.onscreenclick(get_coor)
#------------------------------------------------------

data = pd.read_csv("States Guesser/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 states guessed", prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States Guesser/missed_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state) 
        turt = t.Turtle()
        turt.hideturtle()
        turt.penup()
        state_data = data[data.state == answer_state]
        turt.goto(int(state_data.x), int(state_data.y))
        turt.write(answer_state)

t.mainloop()

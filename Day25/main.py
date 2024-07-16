import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

t = turtle.Turtle()
t.hideturtle()
t.penup()

states = pandas.read_csv("50_states.csv")

text_input_title = "Guess the State"
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=text_input_title,
                                prompt="What's another state?").title()
    
    if answer_state == "Exit":
        break
    
    if answer_state in states.state.values:
        s = states[states["state"] == answer_state]
        t.goto(s.x.item(), s.y.item())
        t.write(answer_state)
        correct_guesses.append(answer_state)
        text_input_title = f"{len(correct_guesses)}/50 States Correct"

not_guessed_states = states[~states.state.isin(correct_guesses)]
not_guessed_states.state.to_csv("states_to_learn.csv")

# How the coordinates for the State names were created.
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
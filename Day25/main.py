import turtle

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

answer_state = screen.textinput(title="Guess the State",
                                prompt="What's another state?")

print(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
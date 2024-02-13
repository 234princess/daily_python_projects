import turtle
import pandas

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 : Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()

        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

#def get_mouse_click_coor(x,y):
    #print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()
#screen.exitonclick()
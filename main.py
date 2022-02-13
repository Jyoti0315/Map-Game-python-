import turtle
import pandas

screen = turtle.Screen()
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
screen.title("India State Game")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)
answer = pandas.read_csv("29_state.csv")
all_states = answer.state.to_list()
guess_states = []
while len(guess_states) < 29:
    answer_state = screen.textinput(title=f"{len(guess_states)}/29 States Correct",
                                    prompt="What's another states Name").title()
    if answer_state == "Exit":
        missing_list = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_list)
        new_data.to_csv("learn_the_left_states.csv")
        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        state_data = answer[answer.state == answer_state]
        tim.goto(float(state_data.x), float(state_data.y))
        tim.write(answer_state)


# def coordinates(x, y):
#     print(x, y)
#
#
# coordinate = screen.onscreenclick(coordinates)
turtle.mainloop()

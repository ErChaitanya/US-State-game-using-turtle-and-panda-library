import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  # because we have to insert the image into output screen for that we use write like this.
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Whats another states "
                                                                                             "name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        ####$$ You can write either above via condition list comprehension and write below lines of code which are comment out
        # misssing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         misssing_states.append(state)
        # # print(misssing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.items())#This is the alternative line use for putting state name and this item keyword
        # is belong to pandas library which is use to write a single input word
        t.write(answer_state)  ##Write these line or above line either one of them.
    # if answer_state is one of the states in all the states of the 50_states.csv
    # If they got it right
    # Create a turtle to write the name of the state at the state's x and y co-ordinates

# screen.exitonclick()

# turtle.mainloop()  # alternative of screen.exitonclick()

# screen.exitonclick()# as we use turtle.mainloop() so we are notusing this line

import turtle  # Importing the turtle module for graphics
import pandas as pd  # Importing pandas library with alias pd for data manipulation

screen = turtle.Screen()  # Creating a turtle screen object
map = turtle.Turtle()  # Creating a turtle object named map

screen.title("U.S. States Game")  # Setting the title of the turtle screen

image = "blank_states_img.gif"  # Defining the image to be used as map
screen.addshape(image)  # Adding the image to the turtle shapes

map.shape(image)  # Setting the shape of the turtle object to the map image

# The following block of code is commented out but was used to get mouse click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pd.read_csv(
    "50_states.csv"
)  # Reading the CSV file containing state data into a pandas DataFrame

playing = True  # Boolean flag to control the game loop
correct_states = 0  # Counter for the number of correctly guessed states
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:  # Main game loop
    answer_state = ""  # Initializing the answer_state variable to an empty string

    answer_state_info = data[
        data["state"] == answer_state
    ]  # Initializing answer_state_info to an empty DataFrame

    while (
        answer_state_info.empty
    ):  # Loop to keep asking for a state name until a valid one is entered
        # Prompting the user for a state name
        answer_state = screen.textinput(
            title=(f"Guess the State: {correct_states} / 50"),
            prompt="What's another states name?",
        ).title()

        if answer_state == "Exit":
            missing_states = [
                state for state in all_states if state not in guessed_states
            ]
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break

        answer_state_info = data[
            data["state"] == answer_state
        ]  # Updating answer_state_info based on the user's input

    if answer_state not in guessed_states:
        guessed_states.append(answer_state)
        correct_states += 1

    x_cor = answer_state_info[
        "x"
    ].item()  # Extracting the x coordinate of the guessed state
    y_cor = answer_state_info[
        "y"
    ].item()  # Extracting the y coordinate of the guessed state

    print(
        x_cor, y_cor
    )  # Printing the coordinates to the console (for debugging purposes)

    # Creating a new turtle object to draw the state name on the map
    draw = turtle.Turtle()
    draw.penup()  # Lifting the pen up so it doesn't draw while moving
    draw.hideturtle()  # Hiding the turtle cursor
    draw.goto(x_cor, y_cor)  # Moving the turtle to the specified coordinates
    # Writing the state name on the map
    draw.write(
        f"{answer_state}",
        font=("Courier", 7, "normal"),
    )

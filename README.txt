# State Guessing Game

## Overview
The State Guessing Game is an interactive Python application that challenges players to recall and enter the names of U.S. states. Built with Python, the game presents a map of the U.S., and the player must type in the names of states one by one. Each correct guess is displayed on the map in its geographically correct location.

## Features
- Interactive input allows players to enter state names.
- Real-time feedback is given for correct guesses, with the state name appearing on the U.S. map.
- The game continues until all 50 states have been correctly guessed or the player chooses to end the game.

## How to Run
To run the game, you need Python installed on your system. Follow these steps:
```bash
# Clone the repository
git clone https://github.com/yourusername/State-Guessing-Game.git
# Navigate to the directory
cd state-guessing-game
# Run the game
python main.py

## Dependencies
- Python 3
- turtle module - for rendering the U.S. map and displaying state names

## Files in This Repository
- main.py: Contains the game loop and handles user input.
- 50_states.csv: Contains the state names and X and Y coordinates to correctly place name on blank_states.img.
- states_to_learn.txt:  Contains the state names for storing and validating.
- blank_states.img: Blank map of the United States. 

## How to Play
- Run the main.py file to start the game.
- When prompted, enter the name of a U.S. state.
- If the guess is correct, the state name will appear on its corresponding location on the map.
- The game can be exited at any time by typing 'exit'.

## Contributions
- Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

## License
- This project is open source and available under the MIT License.


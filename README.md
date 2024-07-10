## Turtle Crossing Game
This project is a Turtle Crossing game developed using the Turtle graphics module in Python. In this game, the player controls a turtle that moves up and down on the screen to avoid moving cars coming from left to right. The goal is to safely guide the turtle to the top of the screen.

## Table of Contents
Installation
How to Play
Controls
Code Structure
Features
License

## Installation
To run this game, Python must be installed on your system. You can download Python from the official website.

Clone this repository to your local machine:

sh
Copy code
git clone https://github.com/your-username/turtle-crossing-game.git
Navigate to the project directory:

sh
Copy code
cd turtle-crossing-game
Install the required libraries (if not already installed):

sh
Copy code
pip install turtle

## How to Play
Start the game by running the main.py script:

sh
Copy code
python main.py
The player controls the turtle, moving it up and down to avoid the cars moving horizontally across the screen. Each successful crossing to the top increases the level, making the game more challenging.

## Controls
Turtle:
Move Up: Up Arrow Key
Move Down: Down Arrow Key
Move Left: Left Arrow Key
Move Right: Right Arrow Key

## Code Structure
main.py: Contains the main game loop and screen setup.
player.py: Defines the Player class responsible for controlling the turtle's movements.
car_manager.py: Manages the creation and movement of cars across the screen.
scoreboard.py: Handles the game's scoring and level tracking.
main.py
Sets up the screen, initializes the turtle, car manager, and scoreboard objects, and contains the main game loop.

player.py
Defines the Player class with methods to control the turtle's movements up, down, left, and right.

car_manager.py
Creates cars randomly along the y-axis and manages their movement from right to left across the screen. Increases car speed as the player progresses through levels.

scoreboard.py
Tracks and displays the game's level and score.

## Features
Turtle can move up, down, left, and right
Cars are randomly generated and move horizontally across the screen
Level increases and car speed intensifies as the player successfully crosses the screen
Game ends when the turtle collides with a car, displaying a "GAME OVER" message

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

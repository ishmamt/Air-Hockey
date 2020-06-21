# Air Hockey 🏒

This game was made using the awesome pygame module to gain ideas for a object oriented approach to problems.

## How to run it? ❓

- At first you need to have python installed. I've used Python 3.8.1 and you can get the latest version of python from [here](https://www.python.org/downloads/).
- Then use pip to install pygame. Usually pip comes with Python. If not then get it from [here](https://pypi.org/project/pip/).
- **Compile and run the main.py script.** ❗

## What does it contain? 🔎

At first, it has a simple GUI that prompts the players to enter names that would be used ingame
It also contains these scripts:

- *classdef.py*
    > Handles all the class definiton, physics, keeping track of the scores, logging and many more.
- *gui.py*
    > Creates the basic gui that takes in the names of the players.
- *keypress.py*
    > This script detects keyboard inputs and gives the command to move the players around.
- *main.py*
    > This is the script that has the main loop and almost every constant can be maniulated from here.

It also has  *gameBG.jpg* , the background image 🖼 and  *bgMusic.mp3* , the background music 🎵 .

## Future Plans 📝

This project is by no means polished. It still has a few bugs. Some of the fiels that I want to improve upon are:

- The physics in this is not really realistic. Improving the physics would be the number 1 priority.
- The state of the GUI could be improved
- Currently the program doesn't close when it is displaying info about goals or wins (as **time.delay()** is used)
- I couldn't add better sprites and I would certainly like to add them and also sfx.

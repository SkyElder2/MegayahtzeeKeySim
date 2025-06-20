# Megayahtzee Keyboard Play Script

## Description
This project is a convenience tool for a web game made by another university graduate, found at "https://www.starke.gg/programming/games/megayahtzee". It is a separately running add-on that allows the game to be played via the keyboard as the web game only supports mouse inputs by default. In doing so, players are able to perform actions more quickly which alleviates the tedium of some actions in the game.

## Technologies Used
- Python
- Pynput

## Status
This project is completed.

## How to Run and Additional Notes
To resolve dependencies, run: 'pip install -r /path/to/requirements.txt'

To start the program, run autoscript.py.
To pause and unpause the program, use '|' (starts paused)

If you want to have the console window always on top so that you can see which category you are on while playing, you can install Microsoft Powertoys.
In that, there is a keybind you can use, Win+Ctrl+T, on a window to keep it on top while you play.

Note: There is no longer a need to press 'q' after finishing the calibration.
Now, you may begin playing immediately, and there is a console message that prints to notify you of this.

You should be able to use the default config if playing on a 1080p screen.
If your screen size is different or you're not playing in full-screen, you can press 'q' to create a new config.
After starting the config, click on all seven dice from top-left to bottom-right, then click the roll and sort buttons (in that order), and then click all of the score selection locations excluding the bonus. 
Finally, click the browser refresh page and then you can begin playing!
This only needs to be done once per computer assuming you keep the browser in the same location.
Also, the currently selected score tab resets after each choice, so that it is easier to keep track of after each roll.
Refer to the program console for any further instructions.

## Credits
Megayahtzee Web Game - https://www.starke.gg/programming/games/megayahtzee

import time
import functools
from pynput.mouse import Button
from pynput.mouse import Controller as mController
from pynput.mouse import Listener as mListener
from pynput.keyboard import Listener, KeyCode, Key
from pynput.keyboard import Controller as kController

print = functools.partial(print, flush=True)


keyboard = kController()
mouse = mController()

# Globals
cfg = 'config.txt'
pauseResumeKey = KeyCode(char='|')
endKey = KeyCode(char='?')
calibrateKey = KeyCode(char='q')
keybindsKey = KeyCode(char='+')
helpKey = KeyCode(char='j')
rollKey = Key.space
refreshKey = KeyCode(char='a')
reprintKey = KeyCode(char='d')
sortKey = KeyCode(char='s')
tab = Key.tab
pause = True
running = True
calibrating = False
scoreTab = 0
scoreCats = 5
catNums = [7, 5, 5, 7, 10]
catNames = ["Basic Tallies", "Common Combos", "Wildcard Scores", "Complex Clusters", "Super Special Rolls"]
NUMSCORETYPES = sum(catNums)

# Keybinds
diceKeys = [KeyCode(char='t'), KeyCode(char='y'), KeyCode(char='f'), KeyCode(char='g'), KeyCode(char='h'), KeyCode(char='v'), KeyCode(char='b')]
clickLoc = []

def mouseClick(x, y, button, pressed):
        global calibrating
        if calibrating and pressed:
            x, y = mouse.position
            clickLoc.append((x, y))
            if len(clickLoc) == len(diceKeys) + 3 + NUMSCORETYPES:
                mouseListener.stop()
                # Save data to file for loading next time
                file = open(cfg, 'w')
                for i in range(len(clickLoc)):
                    setting = str(clickLoc[i]) + "\n"
                    file.write(setting)

def keybinds():
    return

def keyPress(key):
    global pause, calibrating, clickLoc, scoreTab
    if key == pauseResumeKey:
        pause = not pause
    elif key == helpKey:
        print("'q' - Further info. After pressing q, click dice from top left to bottom right, then the roll button, then the sort button, \nand then the selection boxes from top left to bottom right, and then the browser refresh, \nand then press q again.")
        print("\nTo reiterate, the '|' can be used to pause the program so that typing elsewhere does not cause the mouse to jump around.")
        print("Calibration only needs to be done once, as the inputs will be saved and loaded if present the next time the program is run.")
        print("If you are using the default inputs provided, you just need to unpause to begin using the program.")
        print("A side note, the program does not need focus to work.")
        print("Feel free to DM or message in the programming channel to give feedback and I'll do my best to implement it.")
        print("Also, if you notice any bugs, let me know. Enjoy!")
    elif key == reprintKey:
        printInstructions()
    elif key == endKey:
        mouseListener.stop()
        kListener.stop()
    elif (not pause):
        if key == keybindsKey:
            keybinds()
        elif key == calibrateKey:
            calibrating = not calibrating
            if calibrating:
                clickLoc = []
        elif key == refreshKey:
            mouse.position = clickLoc[-1]
            mouse.click(Button.left, 1)
        elif key == sortKey:
            mouse.position = clickLoc[8]
            mouse.click(Button.left, 1)
        else:
            processed = False
            for i in range(len(diceKeys)):
                if key == diceKeys[i]:
                    processed = True
                    mouse.position = clickLoc[i]
                    mouse.click(Button.left, 1)
            if key == rollKey:
                mouse.position = clickLoc[7]
                mouse.click(Button.left, 1)  
            elif key == tab:
                scoreTab = (scoreTab + 1) % scoreCats
                print(f"\nCurrent Tab: {catNames[scoreTab]}")
            elif not processed:
                for i in range(1, catNums[scoreTab]+1):
                    if key == KeyCode(char=str(i)) or (catNums[scoreTab] == 10 and i == 10 and key == KeyCode(char='0')):
                        if i == 0:
                            val = 10
                        else:
                            val = i
                        if val < catNums[scoreTab] + 1:
                            j = scoreTab - 1
                            scoreChoice = 9
                            while(j > -1):
                                scoreChoice += catNums[j]
                                j -= 1
                            scoreChoice += i - 1
                            mouse.position = clickLoc[scoreChoice]
                            mouse.click(Button.left, 1)
                            scoreTab = 0
                            print(f"\nCurrent Tab: {catNames[scoreTab]}")
            

# Load config if present
try:
    data = open(cfg, 'r')
    if data:
        print("Successfully Opened Config")
        lines = data.readlines()
        for line in lines:
            vals = line.replace("(", "").replace(")", "").split(', ')
            clickLoc.append((int(vals[0]), int(vals[1])))
        print("Successfully Loaded Config")
except IOError:
    print("No config file detected.\n")

def printInstructions():
    print("CONTROLS")
    print(f"{'|'.ljust(19)} - Pause/Unpause Listeners, starting state Paused.")
    print(f"{'d'.ljust(19)} - Print Controls Again.")
    print(f"{'q'.ljust(19)} - Use when unpaused to calibrate locations.")
    print(f"{'t, y, f, g, h, v, b'.ljust(19)} - Dice keys, arranged in the structure of the dice, toggles selection.")
    print(f"{'Tab'.ljust(19)} - Switch currently selected score category.")
    print(f"{'1-9, 0'.ljust(19)} - Select score in current category.")
    print(f"{'Spacebar'.ljust(19)} - Rolls dice.")
    print(f"{'s'.ljust(19)} - Sort Dice.")
    print(f"{'a'.ljust(19)} - Refresh page to restart game.")
    print(f"{'j'.ljust(19)} - Help (Just further instructions)")
    print(f"{'?'.ljust(19)} - Exit Program")

print("To use this program, you can either use the saved calibrations or calibrate yourself.")
print("If playing on a 1080p screen, the saved calibrations should be good, although it might not.")
print("Feel free to dm me or message me if you have any questions or suggestions.")
printInstructions()
print(f"Current Tab: {catNames[scoreTab]}")

with Listener(on_press=keyPress) as kListener, \
    mListener(on_click=mouseClick) as mouseListener:
    kListener.join()
    mouseListener.join()
#Requirements:
#user input
#function w/ params, conditional, and loop
#list or dictionary

import _tkinter
RESET = '\033[0m'

class Color: 
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def colorize(text, color):
    print(f'{color}{text}{RESET}')

colorize("Welcome to Kitty Kombat!", Color.PURPLE)
print(""
          "")

start_choice = input("Press 1 to start: ")
if start_choice == "1":
    print(""
          "")
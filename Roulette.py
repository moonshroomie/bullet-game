import random
import sys
import time
import os

roundList = [0, 0, 0, 0, 0, 1]
  
class Color: 
    RESET = '\033[0m'
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    MAGENTA = '\033[35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'
    GRAY = '\033[90m'
    BR_RED = '\033[91m'
    BR_GREEN = '\033[92m'
    BR_YELLOW = '\033[93m'
    BR_BLUE = '\033[94m'
    BR_MAGENTA = '\033[95m'
    BR_CYAN = '\033[96m'
    BR_WHITE = '\033[97m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def pause(duration):
    time.sleep(duration)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colorize(text, color):
    return f'{color}{text}{Color.RESET}'

def colorize1(text, color):
    return f"{color}{text}{Color.RESET}"

def colorize2(text, text2, text3, color, color2, color3):
    return f'{color}{text}{color2}{text2}{color3}{text3}{Color.RESET}'

def print_with_typewriter_effect(text, color):
    delay = 0.07
    for char in text:
        sys.stdout.write(colorize1(char, color))
        sys.stdout.flush()
        time.sleep(delay)
    print("")


def easy():
    global roundList
    roundList = [0, 0, 0, 0, 0, 0, 0, 1]
    random.shuffle(roundList)
    print("8 Rounds. 1 Live.")


def medium():
    print()
    colorize2("6 Rounds. " , "1 Live. ", "5 Blanks. ", Color.YELLOW, Color.RED, Color.GREEN)
    print_with_typewriter_effect("7 Rounds. ", Color.YELLOW)
    print_with_typewriter_effect("2 Live. ", Color.RED)
    print_with_typewriter_effect("5 Blanks. ", Color.BR_GREEN)
    pause(2)
    clear_screen()
   

def hard():
    global roundList
    roundList = [0, 0, 0, 0, 1, 1]
    random.shuffle(roundList)
    print("6 Rounds. 2 Live.")


print(colorize1("""

 ▄▀▀▀▀▄     ▄▀▀█▀▄    ▄▀▀▀█▄    ▄▀▀█▄▄▄▄      ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄      ▄▀▀▀▀▄     ▄▀▀█▄▄▄▄  ▄▀▀█▄   ▄▀▀█▄▄  
█    █     █   █  █  █  ▄▀  ▀▄ ▐  ▄▀   ▐     █      █ █   █   █     █    █     ▐  ▄▀   ▐ ▐ ▄▀ ▀▄ █ ▄▀   █ 
▐    █     ▐   █  ▐  ▐ █▄▄▄▄     █▄▄▄▄▄      █      █ ▐  █▀▀█▀      ▐    █       █▄▄▄▄▄    █▄▄▄█ ▐ █    █ 
    █          █      █    ▐     █    ▌      ▀▄    ▄▀  ▄▀    █          █        █    ▌   ▄▀   █   █    █ 
  ▄▀▄▄▄▄▄▄▀ ▄▀▀▀▀▀▄   █         ▄▀▄▄▄▄         ▀▀▀▀   █     █         ▄▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄   █   ▄▀   ▄▀▄▄▄▄▀ 
  █        █       █ █          █    ▐                ▐     ▐         █         █    ▐   ▐   ▐   █     ▐  
  ▐        ▐       ▐ ▐          ▐                                     ▐         ▐                ▐        
       
""", Color.BR_RED))
difficulty_choice = input("Select a Difficulty: E/M/H: ")
if difficulty_choice.lower() == "e":
    easy()
elif difficulty_choice.lower() == "m":
    medium()
elif difficulty_choice.lower() == "h":
    hard()
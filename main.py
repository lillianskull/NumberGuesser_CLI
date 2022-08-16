# Another experiment

import numpy as np
import random

from colorama import Fore
from colorama import Style

from emoji import emojize

def play():
    randomNumber = random.randint(0, 25)

    print(f"Welcome to the {Fore.LIGHTCYAN_EX}Ultra-Magical Random Number Guessing Python CLI Game!{Style.RESET_ALL}\n(Better name pending.)\n\n{Fore.LIGHTCYAN_EX}In this CLI, you guess a random number and if you win, you uh.. get cookies?{Style.RESET_ALL}\nWell whatever, let's get started!\n\n")
    print(f"This number is in between {np.clip(randomNumber - random.randint(0, 5), 0, 25)} and {np.clip(randomNumber + random.randint(0, 5), 0, 25)}!")

    userInput = input(f"{Fore.YELLOW}Answer here:{Style.RESET_ALL} ")

    if userInput == str(randomNumber):
        print(emojize(":star:") + f" You {Fore.GREEN}win!{Style.RESET_ALL} " + emojize(":star:"))
    elif userInput != str(randomNumber):
        print(f"{Fore.RED}You lose.{Style.RESET_ALL}\nThe answer was {Fore.LIGHTCYAN_EX}{str(randomNumber)}{Style.RESET_ALL}")

if __name__ == "__main__":
    play()
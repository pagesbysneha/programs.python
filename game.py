import random
import sys
outcomes = ["rock", "paper", "scissor"]

while True:
    outcome = input(
        "rock paper or scissor(enter break to exit) : \n").strip().lower()
    if outcome == "break":
        sys.exit()
    computer = random.choice(outcomes)
    print(computer)
    if computer == outcome:
        print("yes you have won !")
import random
a = range(0, 100)
tries = 0
random_number = random.choice(a)
while True:
    guessed_number = (
        input("guess the number (type exit to exit the game)\n"))
    if guessed_number.lower() == "exit":
        print("Game exited.")
        break
    guessed_number = int(guessed_number)
    tries += 1
    if guessed_number > random_number:
        print("lower")
        continue
    if guessed_number < random_number:
        print("higher")
        continue
    if guessed_number == random_number:
        print("congratulations you have guessed the number !")
        print(f"you took {tries} guesses")
        break
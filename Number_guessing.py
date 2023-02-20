# -------------------------------NUMBER GUESSING --------------------------------#

import random
guesses = 0

comp_guess = random.randrange(1, 100)

your_guess = int(input("Try to guess the number between 1 to 100 "))
while comp_guess != your_guess:
    guesses += 1
    if (your_guess < comp_guess):
        print("Choose a larger number")

        your_guess = int(input("Enter angain :-"))

    elif (your_guess > comp_guess):
        print("Choose a Smaller number")

        your_guess = int(input("Enter angain :-"))

    else:
        break
print("Congratulatations you guessed it right")
print(f"You guessed the number in {guesses} chance ")

#+++++++++ You can also add a .txt file to show the heigh score,++++++++++++++++
#+++++++++++++++++ I will upload after some time ++++++++++++++++++++++++++
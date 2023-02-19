# ROCK PAPER SCISSOR

import random

comp_turn = random.randint(1, 3)

your_turn = int(input("Enter 1 for 'Rock' , Enter 2 for 'Paper' , Enter 3 for 'scissor' :- "))
 
if (comp_turn and your_turn >=4 ):
    print("Wrong input. Choose the correct number ")

if comp_turn == your_turn:
        print(f"Computer chose {comp_turn} You chose {your_turn} its a tie ")

if (comp_turn == 1) and (your_turn == 2):
    print("you win ")

if (comp_turn == 1) and (your_turn == 3):
    print("you lose ")

if (comp_turn == 2) and (your_turn == 1):
    print("you lose ")

if (comp_turn == 2) and (your_turn == 3):
    print("you win ")

if (comp_turn == 3) and (your_turn == 2):
    print("you lose")

if (comp_turn == 3) and (your_turn == 1):
  print("you win ")
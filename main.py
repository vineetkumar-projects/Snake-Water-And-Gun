import random
import time

def game(comp,yours):
    if comp == "snake":
        if yours == "snake":
            print("tie")
        elif yours == "water":
            print("you lose")
        elif yours == "gun":
            print("you win")
    elif comp == "water":
        if yours == "snake":
            print("you win")
        elif yours == "gun":
            print("you lose")
        elif yours == "water":
            print("tie")
    elif comp == "gun":
        if yours == "water":
            print("you win")
        elif yours == "snake":
            print('you lose')
        elif yours == 'gun':
            print("tie")

print("computer turns snake(s),water(w) and gun(g): ")
time.sleep(2)
player = [
    "snake",
    "water",
    "gun"
]

compChoice = random.randint(0,2)
comp = player[compChoice]

print("")

yours = input("your turns choose snake(s),water(w) and gun(g): ")

if yours == "s":
    yours = "snake"
elif yours == "w":
    yours = "water"
elif yours == "g":
    yours = "gun"


game(comp,yours)


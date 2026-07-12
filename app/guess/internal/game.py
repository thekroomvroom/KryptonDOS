import time
import random
import os
import readchar
import sys

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")        

loop = True
while loop == True:
    attempt = 0

    print("""
Select Difficulty:
1 - Baby
2 - Easy
3 - Medium
4 - Hard
5 - Extreme

C - Custom
Q - Exit
    """)

    diff = readchar.readkey()

    lint = 1
    if int(diff) == 1:
        rint = 10
    elif int(diff) == 2:
        rint = 25
    elif int(diff) == 3:
        rint = 50
    elif int(diff) == 4:
        rint = 100
    elif int(diff) == 5:
        rint = 500
    elif int(diff) == 6:
        rint = 1000
    elif diff.lower() == 'c':
        time.sleep(.5)
        clear()
        print("Enter your desired minimum number: ", end="")
        lint = int(input())
        time.sleep(.3)
        print("Enter your desired maximum number: ", end="")
        rint = int(input())
    elif diff.lower() == 'q':
        loop = False
    else:
        sys.exit(1)
    
    gnum = random.randint(int(lint), int(rint))
    
    rloop = True
    print(f"Guess a random number from {lint} to {rint}.")
    while rloop == True:
        guess = input()
        if int(guess) == gnum:
            attempt += 1
            print(f"Correct! It took you {attempt} tries")
            rloop = False
        else:
            attempt += 1
            print("Wrong!")
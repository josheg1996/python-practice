import random

def guess():
    x = random.randint(1,20)
    y = 21
    while y!=x:
        y = int(input("Guess the number (between 1 and 20): "))
        if y == x:
            print("Congratulations!")
            break
        elif y > x:
            print("Too high, try again")
        elif y<x:
            print("Too low, try again")
    
guess()
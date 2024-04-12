import random
from random import randint

#   Rand number from 1 to 100
def rand_number():
    return int(random.randint(1, 100))

#   Users enter a number
def enter_number():
    entered_number = int(input("Guess the number: "))
    return entered_number


rand_number = rand_number()
user_number = False


#   When number is not equal go ahead
while user_number != rand_number:

    try:
        user_number = enter_number()
    except ValueError:
        print("It's not a number!")
        continue

    if user_number < rand_number:
        print("Too small!")

    if user_number > rand_number:
        print("Too big!")

    if user_number == rand_number:
        print("You win!")





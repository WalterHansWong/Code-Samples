import random

print("Pick a number between 1 and 1,000,000!")
try:
    num1 = int(input())
    num2 = random.randint(1, 1000000)

    while num1 != num2:
        if num1 < num2:
            print("Your number is less than the correct answer\nTry again!")
            num1 = int(input())
        elif num1 > num2:
            print("Your number is greater than the correct answer\nTry again!")
            num1 = int(input())

    print("You guessed the number!!! It is {}. Congrats!".format(num2))
except:
    print("Your input is invalid...")

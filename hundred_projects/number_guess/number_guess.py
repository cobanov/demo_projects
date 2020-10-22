import random

number = random.randint(0, 100)

while True:
    guess = int(input("guess a number: "))

    try:
        if guess == number:
            print("won")
            break
        
        elif guess > number:
            print("guess lower")
        else:
            print("guess higher")

    except:
        print("it should be a number")

    
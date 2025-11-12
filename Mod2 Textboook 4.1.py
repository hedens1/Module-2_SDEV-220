secret = 7


while True:
    guess = int(input("Enter a number between 1 and 10: "))
    if guess < secret:
        print("Too low, try again.")
    elif guess > secret:
        print("Too high, try again.")
    else:
        print("Just right")
        break   
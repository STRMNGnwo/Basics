import random
print("This is a guessing game")
number=random.randint(0,100)
attempt=0
i=0
while(i==0):
    guess = int(input("Enter your guess!: "))
    if guess==number:
        print("You guessed the number! It was "+str(number))
        print("\n"+"It took you "+str(attempt)+" guesses")
        attempt+=1
        i=1
        break
    elif guess<number:
        attempt+=1
        print("Your guess is too low. Try again")
    elif guess>number:
        attempt+=1
        print("Your guess is too high. Try again")



import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 100


while not quit:
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while int(number) != random_number:
        number = input("Please guess a number between 1 and {}: ".format(range))
        if not number.isdigit():
                print("Please give a numerical value. ")
        else:
            number = int(number)
            count = count + 1
            print("Try Again")
            if number > random_number:
                print("Lower")
            elif number < random_number:
                print("Higher")
    print("Nicely Done!")
    print("You guessed it in {} tries!" .format(count))
    play_again = input("Would you like to play again? Yes or No? ")
    play_again = play_again.lower()
    if play_again == 'yes' or play_again == 'y':
        quit = False
    else:
        quit = True

print("\n\nThanks for playing Guessing Game! ")

from random import randint
while 1:
    guess=randint(1, 100)
    for i in range(10):
        user=int(input("Enter your guess:\n"))
        if user<guess:
            print("Too low!")
        elif user>guess:
            print("Too high!")
        else:
            print("You guessed it right!")
            break
    print("You lost. Want to play again?")
    want=input()
    if want not in ['Y', 'YES', 'y', 'yes', 'ok']:
        break
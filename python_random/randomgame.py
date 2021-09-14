from random import randint
import sys
answer = randint(1,10)

while True:
    try:
        guess = int(input('guess a number from 1 to 10:  '))
        if 0< guess< 11:
            if guess == answer:
                print("see i can be polite when you are a champion you're welcome bozo this is the true guess you nailed it")
                break
        else:
             print('try it harder give me a number between 1 to 10 uncultured bitch')

    except ValueError:
        print("don't try cheat just give me a number!! how hard it could be indeed")
        continue

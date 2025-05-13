import random

guess = 0
answer = random.randint(1, 100)
while answer != guess:
    guess = int(input('guess='))
    print('Your guess is', guess)
    if guess == answer :
        print('Good guess')
    else:
        if (guess < answer):
            print('Too low')
        else:
            print('Too high')
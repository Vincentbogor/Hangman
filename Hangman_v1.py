from turtle import *

def base():
    color('black')
    pensize(5)
    shape('circle')
    speed(10)
    penup()

    goto(-250,-150)
    pendown()
    forward(500)
    penup()

    goto(-210, -150)
    left(90)
    pendown()
    forward(320)
    penup()
    goto(-210, -150+320-60)
    right(45)
    pendown()
    forward(83)
    penup()
    goto(-210, -150+320)
    right(90-45)
    pendown()
    forward(280)
    penup()

def head():
    pendown()
    right(180)
    circle(35)
    penup()

def torso():
    goto(70, 100)
    left(90)
    pendown()
    forward(80)
    penup()

def left_arm():
    goto(70, 100)
    right(35)
    pendown()
    forward(55)
    penup()

def right_arm():
    goto(70, 100)
    left(35*2)
    pendown()
    forward(55)
    penup()

def left_leg():
    goto(70, 20)
    right(35*2)
    pendown()
    forward(60)
    penup()

def right_leg():
    goto(70, 20)
    left(35*2)
    pendown()
    forward(60)
    penup()

base()
answer = 'Xylophone'
guess = input('Enter a letter to guess: ')
guess = guess.lower()
wrong_guess = 0
right_guess = []
wrong_guess_list = []
game_over = False

while len(right_guess) != 8 and wrong_guess < 6:
    #right guesses
    if guess in right_guess:
        print('That letter already exists, try another letter.')
        print('correct letters:', right_guess)
        print('wrong letters:', wrong_guess_list)
        guess = input('Enter a letter to guess: ')
        guess = guess.lower()
    elif guess == 'x':
        print('You got a letter correct!')
        right_guess.append(guess)
        print('correct letters:', right_guess)
        print('wrong letters:', wrong_guess_list)
        guess = input('Enter a letter to guess: ')
        guess = guess.lower()
    elif guess == 'y':
        print('You got a letter correct!')
        right_guess.append(guess)
        print('correct letters:', right_guess)
        print('wrong letters:', wrong_guess_list)
        guess = input('Enter a letter to guess: ')
        guess = guess.lower()
    elif guess == 'l':
        print('You got a letter correct!')
        right_guess.append(guess)
        print('correct letters:', right_guess)
        print('wrong letters:', wrong_guess_list)
        guess = input('Enter a letter to guess: ')
        guess = guess.lower()
    elif guess == 'o':
        print('You got a letter correct!')
        right_guess.append(guess)
        right_guess.append(guess)
        print('correct letters:', right_guess)
        print('wrong letters:', wrong_guess_list)
        guess = input('Enter a letter to guess: ')
        guess = guess.lower()
    elif guess == 'p':
        print('You got a letter correct!')
        right_guess.append(guess)
        print('correct letters:', right_guess)
        print('wrong letters:', wrong_guess_list)
        guess = input('Enter a letter to guess: ')
        guess = guess.lower()
    elif guess == 'h':
        print('You got a letter correct!')
        right_guess.append(guess)
        print('correct letters:', right_guess)
        print('wrong letters:', wrong_guess_list)
        guess = input('Enter a letter to guess: ')
        guess = guess.lower()
    elif guess == 'n':
        print('You got a letter correct!')
        right_guess.append(guess)
        print('correct letters:', right_guess)
        print('wrong letters:', wrong_guess_list)
        guess = input('Enter a letter to guess: ')
        guess = guess.lower()
    elif guess == 'e':
        print('You got a letter correct!')
        right_guess.append(guess)
        print('correct letters:', right_guess)
        print('wrong letters:', wrong_guess_list)
        guess = input('Enter a letter to guess: ')
        guess = guess.lower()
    else:
        #wrong guess
        if guess in wrong_guess_list:
            print('You already guessed that letter, try another one.')
            print('Wrong letters:', wrong_guess_list)
            guess = input('Enter a letter to guess: ')
            guess = guess.lower()
        else:
            wrong_guess_list.append(guess)
            wrong_guess += 1
            if wrong_guess == 1:
                print('Wrong letter, try again.')
                print('correct letters:', right_guess)
                print('Wrong letters:', wrong_guess_list)
                head()
                guess = input('Enter a letter to guess: ')
                guess = guess.lower()
            elif wrong_guess == 2:
                torso()
                print('Wrong letter, try again.')
                print('correct letters:', right_guess)
                print('Wrong letters:', wrong_guess_list)
                guess = input('Enter a letter to guess: ')
                guess = guess.lower()
            elif wrong_guess == 3:
                print('Wrong letter, try again.')
                print('correct letters:', right_guess)
                print('Wrong letters:', wrong_guess_list)
                left_arm()
                guess = input('Enter a letter to guess: ')
                guess = guess.lower()
            elif wrong_guess == 4:
                print('Wrong letter, try again.')
                print('correct letters:', right_guess)
                print('Wrong letters:', wrong_guess_list)
                right_arm()
                guess = input('Enter a letter to guess: ')
                guess = guess.lower()
            elif wrong_guess == 5:
                print('Wrong letter, try again.')
                print('correct letters:', right_guess)
                print('Wrong letters:', wrong_guess_list)
                left_leg()
                guess = input('Enter a letter to guess: ')
                guess = guess.lower()
            elif wrong_guess == 6:
                right_leg()
                print('Game Over')
                break

if len(right_guess) == 8:
    print('Congratulations')
    print('The word is', answer)
    print('You guessed correcly in', wrong_guess + 1, 'attempts!')

hideturtle()
exitonclick()

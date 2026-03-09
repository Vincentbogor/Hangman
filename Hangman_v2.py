from turtle import *

#themes
themes = {
    'l': ('white', 'black', 'Light mode'),
    'd': ('black', 'white', 'Dark mode'),
    'g': ('#1a1a1a', '#39ff14', 'Binary'),
    'y': ("#d14c2e", '#ffc865', 'CNY'),
    'c': ('#ffe6f0', '#ff69b4', 'Cotton Candy'),
    'b': ('#001f4d', '#00bfff', 'Ocean Blue'),
    'p': ('#ff69b4', '#ffffff', 'Bubblegum'),
    'v': ('#f0b3bd', '#0f090a', 'Blush'),
    'm': ('#1a1a2e', '#e94560', 'Manhwa'),
    'e': ('#1a0000', '#ff4500', 'Devil'),
    's': ('#ffffff', '#ff4500', 'Morningstar')
}

menu = '\n'.join(f' {key.upper()} = {value[2]}' for key, value in themes.items())
mode = input(f'Choose a theme:\n{menu}\n input: ').lower()
while mode not in themes:
    print('Invalid choice.')
    mode = input(f'Choose a theme:\n{menu}\n input: ').lower()
bg, fg = themes[mode][0], themes[mode][1]

#modes
words = {
    'e': ('xylophone', 'Easy'),
    'm': ('zephyr', 'Medium'),
    'h': ('rhythm', 'Hard'),
    'x': ('hippopotomonstrosesquippedaliophobia', 'Hardcore'),
}

diff_menu = '\n'.join(f' {key.upper()} = {val[1]}' for key, val in words.items())
difficulty = input(f'Choose difficulty:\n{diff_menu}\n input: ').lower()

while difficulty not in words:
    print('Invalid choice.')
    difficulty = input(f'Choose difficulty:\n{diff_menu}\n input: ').lower()

answer = words[difficulty][0]

def base():
    bgcolor(bg)
    color(fg)
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
guess = input('Enter a letter to guess: ').lower()
while len(guess) != 1:
        print('One letter only!')
        guess = input('Enter a letter to guess: ').lower()

wrong_guess = 0
right_guess = []
wrong_guess_list = []
total_attempts = 0
draw = [head, torso, left_arm, right_arm, left_leg, right_leg]

while not all(letter in right_guess for letter in answer.lower()) and wrong_guess < 6:
    while len(guess) != 1:
        print('One letter only!')
        guess = input('Enter a letter to guess: ').lower()
    #right guesses
    if guess in right_guess or guess in wrong_guess_list:
        print('That letter already exists, try another one.')
        print('wrong letters:', wrong_guess_list)
    elif guess in answer.lower():
        right_guess.append(guess)
        total_attempts += 1
        display = ' '.join(letter if letter in right_guess else '_' for letter in answer.lower())
        print(display)
        print('Correct letter!')
        if all(letter in right_guess for letter in answer.lower()):
            break
        print('Wrong letters:', wrong_guess_list)
    else:
        #wrong guess
        wrong_guess_list.append(guess)
        wrong_guess += 1
        total_attempts += 1
        if wrong_guess <= 6:
            draw[wrong_guess - 1]()
        display = ' '.join(letter if letter in right_guess else '_' for letter in answer.lower())
        print(display)
        print('Wrong letter!')
        print('Lives left:', 6 - wrong_guess)
        print('Wrong letters:', wrong_guess_list)
        if wrong_guess == 6:
            break
    guess = input('Guess a letter: ').lower()

if wrong_guess == 6: 
    print('Game Over. The word was:', answer)
else:
    print('Congratulations')
    print('The word is', answer)
    print('You guessed correcly in', total_attempts, 'attempts!')

hideturtle()
exitonclick()

from random import randint
import sys
from random import randint
import keyboard
from getpass import getpass
from time import sleep

options = ['r', 'p', 's']


def tie():
    print('tie')


def win(player, p1move, p2move):
    if p1move == '1':
        p1move = 'Rock'
    elif p1move == '2':
        p1move = 'Paper'
    elif p1move == '3':
        p1move = 'Scissors'

    if p2move == '1':
        p2move = 'Rock'
    elif p2move == '2':
        p2move = 'Paper'
    elif p2move == '3':
        p2move = 'Scissors'

    if player == '1':
        print(p1move + ' Beats ' + p2move + '... Player #' + player + ' WINS!')
    elif player == '2':
        print(p2move + ' Beats ' + p1move + '... Player #' + player + ' WINS!')
    elif player == 'Computer':
        print(p2move + ' Beats ' + p1move + '... COMPUTER WINS :(' )


def isInt(string, lowest=1, highest=3):
    try:
        val = int(string)
        if highest >= val >= lowest:
            return True
        else:
            int('h')
    except ValueError:
        return False


def runGame(gameOption):
    print('\n' * 10)
    if gameOption == 3:
        print('Goodbye! Thanks for Playing!')
        sys.exit()
    elif gameOption == 2:
        while True:
            print('\n' * 10)
            print('''
PLAYER! SELECT YOUR MOVE!
    (1) Rock
    (2) Paper
    (3) Scissors
''')

            while True:
                p1 = getpass('Player 1 Move:')
                if isInt(p1):
                    break
                else:
                    print(p1 + ' IS NOT AN OPTION!')

            p2 = str(randint(1,3))
            print('\n' * 10)
            print('''
READY? ON SHOOT!
Press Enter to Start''')
            input()
            print('\n' * 10)
            print("ROCK...")
            sleep(1)
            print('\n' * 10)
            print("PAPER..")
            sleep(1)
            print('\n' * 10)
            print("SCISSORS...")
            sleep(1)
            print('\n' * 10)
            print("SHOOT!\n")
            sleep(1)
            if p1 == p2:
                tie()
            else:
                if p1 == '1':
                    if p2 == '2':
                        win('Computer', p1, p2)
                    elif p2 == '3':
                        win('1', p1, p2)
                elif p1 == '2':
                    if p2 == '1':
                        win('1', p1, p2)
                    elif p2 == '3':
                        win('Computer', p1, p2)
                elif p1 == '3':
                    if p2 == '1':
                        win('Computer', p1, p2)
                    elif p2 == '2':
                        win('1', p1, p2)
            input('Press Enter To Continue')

            while True:
                play_again = input('''
Play Again?
    (1) Yes
    (2) No
-> ''')
                if isInt(play_again):
                    if play_again == '1':
                        break
                    elif play_again == '2':
                        print('\n' * 10)
                        print("Bye Bye!")
                        sys.exit()

    elif gameOption == 1:
        while True:
            print('\n' * 10)
            print('''
PLAYERS! SELECT YOUR MOVE!
    (1) Rock
    (2) Paper
    (3) Scissors
''')
            # p1 = None
            # p2 = None

            while True:
                p1 = getpass('Player 1 Move:')
                if isInt(p1):
                    break
                else:
                    print(p1 + ' IS NOT AN OPTION!')

            while True:
                p2 = getpass('Player 2 Move:')
                if isInt(p2):
                    break
                else:
                    print(p2 + ' IS NOT AN OPTION!')
            print('\n' * 10)
            print('''
READY? ON SHOOT!
Press Enter to Start''')
            input()
            print('\n' * 10)
            print("ROCK...")
            sleep(1)
            print('\n' * 10)
            print("PAPER..")
            sleep(1)
            print('\n' * 10)
            print("SCISSORS...")
            sleep(1)
            print('\n' * 10)
            print("SHOOT!\n")
            sleep(1)
            if p1 == p2:
                tie()
            else:
                if p1 == '1':
                    if p2 == '2':
                        win('2', p1, p2)
                    elif p2 == '3':
                        win('1', p1, p2)
                elif p1 == '2':
                    if p2 == '1':
                        win('1', p1, p2)
                    elif p2 == '3':
                        win('2', p1, p2)
                elif p1 == '3':
                    if p2 == '1':
                        win('2', p1, p2)
                    elif p2 == '2':
                        win('1', p1, p2)
            input('Press Enter To Continue')

            while True:
                play_again = input('''
Play Again?
    (1) Yes
    (2) No
-> ''')
                if isInt(play_again):
                    if play_again == '1':
                        break
                    elif play_again == '2':
                        print('\n' * 10)
                        print("Bye Bye!")
                        sys.exit()


# Guarantees player input of 1 or 2
while True:  # Infinite loop until break
    print('\n' * 10)
    game_type = input('''
Select Game Type:
    (1) Player VS Player
    (2) Player VS Computer
    (3) Exit
-> ''')  # Display Player Options
    if isInt(game_type):
        runGame(int(game_type))
        break
    else:
        print(str(game_type) + ' IS NOT AN OPTION!')  # Says (INPUT) is not an option then returns to loop start

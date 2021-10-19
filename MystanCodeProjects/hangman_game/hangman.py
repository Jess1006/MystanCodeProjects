"""
File: hangman.py
Name: Jess Hung
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Hangman Game!

    First, settle down the word and turns for this round
    Second, remind the player for some tips
    Third, player inputs the character
    Fourth, check the input is legal or not
    Last, hangman!
    """
    word = random_word()
    n_turn = N_TURNS

    reminders(word, n_turn)

    guess = str(input('Your guess: '))

    guess = check(guess)

    hangman(guess, word, n_turn)


def reminders(word, n_turn):
    """
    This function gives the player some hints in the beginning
    """
    print('The word looks like: ' + '-' * len(word))
    print('You have ' + str(n_turn) + ' guesses left.')


def check(guess):
    """
    This function made for case-sensitive,
    and use the loop to confirm the input from player
    """
    guess = guess.upper()

    while not guess.isalpha() or not len(guess) == 1:
        print('illegal format')
        guess = str(input('Your guess: '))
        guess = guess.upper()
    return guess


def hangman(guess, word, n_turn):
    """
    The function for hangman game procedure
    """
    # create the list for documenting the correct guess
    ans = []
    for char in word:
        ans.append('-')

    # the game is still on, until the number of turns turn to 0,
    while n_turn > 0:

        if guess in word:
            print('You are correct!')

            for i in range(len(word)):
                if guess == word[i]:
                    ans[i] = guess

            if "".join(ans) != word:
                print('The word looks like: ' + "".join(ans))
                print('You have ' + str(n_turn) + ' guesses left.')
                guess = str(input('Your guess: '))
                guess = check(guess)
            else:
                win(word)
                break
        else:
            n_turn -= 1
            print('There is no ' + guess + "'s" + ' in the word.')
            if n_turn > 0:
                print('The word looks like: ' + "".join(ans))
                print('You have ' + str(n_turn) + ' guesses left.')
                guess = str(input('Your guess: '))
                guess = check(guess)
            else:
                lose(word)
                break


def win(word):
    """
    Final note for the winner!
    """
    print('You win!!')
    print('The word was: ' + word)


def lose(word):
    """
    Final note for the loser ;(
    """
    print('You are completely hung :(')
    print('The word was: ' + word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

from datetime import date
import re
import requests
import random
import sys

def playGame():
    wordList = getWords()
    hiddenWord = random.choice(wordList)
    invChar = []
    attempts = 6

    while attempts > 0:
        print(f'The current invalid characters are: {invChar }')
        guess = getGuess()
        if guess == hiddenWord:
            winGame(attempts)
            break
        else:
            attempts = attempts - 1
            print(f'you have {attempts} attempt(s) ,, \n ')
            for char, charGuess in zip(hiddenWord, guess):
                if charGuess in hiddenWord and charGuess in char:
                    print(charGuess + ' ✔ ')
                elif charGuess in hiddenWord:
                    print(charGuess + ' ➕ ')
                else:
                    invChar.append(charGuess)
                    print(' ❌ ')
            if attempts == 0:
                print(f' Game over !!!! {hiddenWord} was the word :(')


def getGuess():
    while True:
        guess = str(input('Guess the word: '))
        guess = guess.lower()
        if guess.isalpha() and len(guess) == 5:
            return guess


def winGame(score):
    print(f'You guessed the words correctly! YOU WIN 🕺🕺🕺\n You had {score} attempts left out of 6')
    with open('history.txt', 'a') as f:
        f.write(f'{date.today()}: You only had {score} attempts left\n')
        f.close()


def getHistory():
    with open('history.txt', 'r') as f:
        history = f.readlines()
        f.close()
        return history


def getWords():
    print('Generating word list')
    internetResponse = requests.get('https://meaningpedia.com/5-letter-words?show=all')
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    word_list = pattern.findall(internetResponse.text)
    return word_list


def login():
    username = str(input('Enter your username: '))
    password = str(input('Enter your password: '))

    realUsername = "krish rules"
    realPassword = "raunak rules"

    if username == realUsername and password == realPassword:
        return True
    else:
        return False

if __name__ == '__main__':

    login = login()

    if login:

        status = True
        print(
            '''Wordle is a single player game
A player has to guess a five letter hidden word
You have six attempts 
Your Progress Guide "✔❌➕":
"✔" Indicates that the letter at that position was guessed correctly
"➕" indicates that the letter at that position is in the hidden word, but in a different position
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word   ''')
        print(f'previous game:\n{getHistory()}')
        while status:
            playGame()
            newGame = input('Would you like to play again, enter "n" to exit and anything else to continue: ')
            if newGame == 'n':
                status = False
        print('Thank you for playing!')

    else:
        sys.exit()
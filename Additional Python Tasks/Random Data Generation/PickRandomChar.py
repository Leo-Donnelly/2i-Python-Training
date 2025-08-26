import random

def get_word():
    word = input("Enter an random word: ")
    return word

def rand_char(word):
    randomChar = random.choice(word)
    return randomChar

def display(word, randomChar):
    print("The word you entered is:", word)
    print("The random character that was selected is:", randomChar)

def main():
    word = get_word()
    randomChar = rand_char(word)
    display(word, randomChar)

main()
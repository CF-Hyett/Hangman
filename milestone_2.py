import random

word_list = ['kiwi', 'lemon', 'watermelon', 'feijoa', 'grape']

print(word_list)

word = random.choice(word_list)

print(word)

guess = input('Enter single letter: ')

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! Thats is not a valid input")
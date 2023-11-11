from random_word import RandomWords as r

# Generates random word from the randowm-word package
r = r()
word = r.get_random_word()

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the {word}.")
    else:
        print(f"Sorry, {guess} is not in the {word}. Try again with a new word.")

def ask_for_input():
    while True:
        guess = input('Enter single letter: ')
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
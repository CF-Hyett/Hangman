from random_word import RandomWords as r

# Generates random word from the randowm-word package
r = r()
random_word = r.get_random_word()

def check_guess(randomly_guessed_letter):
    randomly_guessed_letter.lower()
    if randomly_guessed_letter in random_word:
        print(f"Good guess! {randomly_guessed_letter} is in the {random_word}.")
    else:
        print(f"Sorry, {randomly_guessed_letter} is not in the {random_word}. Try again with a new word.")

def ask_for_input():
    while True:
        randomly_guessed_letter = input('Enter single letter: ')
        if len(randomly_guessed_letter) == 1 and randomly_guessed_letter.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(randomly_guessed_letter)

ask_for_input()
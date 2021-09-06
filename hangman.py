import random
from hangman_art import stages, logo
from hangman_words import word_list          # importing a list of words to choose from
print(logo)
chosen_word = random.choice(word_list)
empty_list = list(len(chosen_word) * '_')    # an empty list
lives = 6   # how many wrong attempts

end_of_game = False                            # false for continuous loop
while not end_of_game:
    guess = input('enter a letter ').lower()   # user guess the letter

    for position in range(len(chosen_word)):   # loop to iterate all the letters in the list
        letter = chosen_word[position]
        if letter == guess:
            empty_list[position] = letter      # replacing _ with the guessed letter

    if guess not in chosen_word:               # this condition is to see how many times the user guessed wrong
        lives -= 1                             # so lives decreases by 1
        if lives == 0:                         # to check if any life left
            print("you lose")
            end_of_game = True

    if '_' not in empty_list:                  # to check if their is any empty space left in the empty_list
        end_of_game = True                     # if not then you won
        print("you won")
    print(stages[lives])
print("the chosen word is:  {}".format(chosen_word))
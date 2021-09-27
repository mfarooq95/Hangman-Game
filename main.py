from words import words
import string
import random

# Randomly get a valid word from an imported list of words
def get_valid_word(words):
    
    word = random.choice(words)
    if "-" in word or " " in word: 
        word = get_valid_words(words) # Recursion
    return word 

# Uses random word to start the game, takes player input and determines win and loss
def hangman():

    word = get_valid_word(words).upper() 
    word_letters = set(word) # Deconstructes the winning word into letters as an iterable set to use as refernce
    alphabet = set(string.ascii_uppercase) # Iterable set of English alphabet in uppercase to standardize and use as letter reference against player input
    guessed_letters = set() # Blank set to populate with and reference against player input
    lives = 12 # Number of player lives

    while lives > 0 and len(word_letters) > 0:
        print(f"You have {lives} lives. \nThe following letters have been guessed: ", " ".join(guessed_letters))
        
        word_list = [letter if letter in guessed_letters else "-" for letter in word]
        print("The current word is: ", " ".join(word_list))
        
        player_guess = input("\nPlease enter a letter: ").upper()
        if player_guess in alphabet - guessed_letters:
            guessed_letters.add(player_guess)
            if player_guess in word_letters:
                word_letters.remove(player_guess)
            else:
                lives -= 1
                print(f"\nYour guess, {player_guess} was not in the winning word. You lost a life.\n")
        elif player_guess in guessed_letters:
            print("\nYou already guessed this letter! Try again.\n")
        else:
            print("\nInvalid entry. You can only use English letters. Try again.\n")

    if lives == 0:
        print("\nYou ran out of lives before you finished the word! You lose!")
    else:
        print("\nYou guessed the word, you win!")

def replay_game():
    play_again_bool = False
    user_input = input("Play again? Y or N: ").upper()
    if user_input == 'Y':
        play_again_bool = True
    elif user_input == 'N':
        play_again_bool = False
    else:
        print("Invalid response. Please type Y for yes or N for no.")
        play_again_bool = replay_game() # Recursion
    return play_again_bool

if __name__ == "__main__":
    play_again = True
    while play_again == True:
        hangman()
        play_again = replay_game()
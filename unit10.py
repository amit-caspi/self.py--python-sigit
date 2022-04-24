# Hangman game
# Author: Amit Caspi
# Date: April 2022
# Note: Before running create file ("words.txt") with words for the game (separated by a space)

import os.path
# A constant that represents the string that the function prints as part of the opening of the game.
HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """ 
# A constant that represents the maximum number of failed attempts allowed in the game, which is 6.
MAX_TRIES = 6 
# HANGMAN_PHOTOS- a dictionary that holds the pictures of the hanging man, in each of the situations.
HANGMAN_PHOTOS = {1:"x-------x ", 2:
"""x-------x
 |
 |
 |
 |
 | """, 3:
"""x-------x
 |       |
 |       0
 |
 |
 | """, 4:
"""x-------x
 |       |
 |       0
 |       |
 |
 | """, 5:
"""x-------x
 |       |
 |       0
 |      /|\\
 |
 | """, 6:
"""x-------x
 |       |
 |       0
 |      /|\\
 |      /
 | """, 7:
"""x-------x
 |       |
 |       0
 |      /|\\
 |      / \\
 | """}

 
def opening_screen(MAX_TRIES):
    """
    The function prints the welcome screen- Hangman, and the maximum number of failed attempts.
    :param MAX_TRIES: a constant that represents the maximum number of failed attempts allowed in the game.
    :type MAX_TRIES: int
    :return: None
    """
    print(HANGMAN_ASCII_ART)
    print("\nMaximum tries in the game is: ", MAX_TRIES) 

	
def choose_word(file_path, index): 
    """
    The function finds a word from a text file that will be used as the secret word
    for guessing (depending on the index it receives).
    :param file_path: a string that represents a path to a text file that contains space-separated words.
    :param index: an integer that represents the location of a particular word in the file.
    :type file_path: string
    :type index: int
    :return: the word in the index location, which will be used as the secret word for guessing.
    :rtype: string
    """
    with open(file_path, "r") as my_file:
        the_words = my_file.read() 
    words_splitted = the_words.split(" ")	   
    full_length_words = len(words_splitted) 
    word_index = int(index) % full_length_words - 1
    the_secret_word = words_splitted[word_index].lower()
    return(the_secret_word)


def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function returns string which represents the secret word without the unguessed letters.
    :param secret_word: the secret word for guessing.
    :param old_letters_guessed: a list of letters that the player had previously guessed.
    :type secret_word: string
    :type old_letters_guessed: list (of strings)
    :return: a string which include letters (which the player guessed and in the secret word) 
    and underlines (which the player has not guessed yet).
    :rtype: string
    """
    progress = ""  
    for letter in secret_word:
        if letter in old_letters_guessed:
            progress += letter + " " 
        else:
            progress += "_ "
    return progress


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    The function tries to update old letters guessed by input 
    (it checks if the input is valid and returnes an answer accordingly).
    :param letter_guessed: character that the player has guessed.
    :param old_letters_guessed: a list of letters that the player had previously guessed.
    :type letter_guessed: string 
    :type old_letters_guessed: list (of strings)
    :return: True / False, depending on- if the input received by the player is valid.
    :rtype: bool
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print("X")
        old_letters_guessed.sort()
        letters_guessed = ' -> '.join(old_letters_guessed)
        print("\nThe letters you guessed: ", letters_guessed)
        return False
    else:
        old_letters_guessed.append(letter_guessed.lower())
        return True 


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    The function checks validation of an input (char).
    :param letter_guessed: character that the player has guessed.
    :param old_letters_guessed: a list of letters that the player had previously guessed.
    :type letter_guessed: string 
    :type old_letters_guessed: list (of strings)
    :return: True / False, depending on- if the input (char) is valid.
    :rtype: bool
    """
    return((len(letter_guessed) == 1) and (letter_guessed.isalpha()) 
    and (letter_guessed.lower() not in old_letters_guessed))


def check_win(secret_word, old_letters_guessed):
    """
    The function checks if the player has won.
    :param secret_word: the secret word for guessing.
    :param old_letters_guessed: a list of letters that the player had previously guessed.
    :type secret_word: string
    :type old_letters_guessed: list (of strings)
    :return: True / False, depending on- if all the letters that in the secret word are
    included in the list of letters that guessed (is player won).
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False 
    return True


def check_index_input(index):
    """
    The function checks validation of an index input (an integer & greater than 0).
    :param index: an input that the player has entered.
    :type index: string 
    :return: True / False, depending on- if the input of the index is valid.
    :rtype: bool
    """
    try:
        if int(index) <= 0:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    opening_screen(MAX_TRIES)  
    file_path = input("\nEnter file path: ")
    while not os.path.isfile(file_path): # Return True if path is an existing regular file.
        print("The input of the file path is not valid, Please try again.")
        file_path = input("\nEnter file path: ")
    index = input("Enter index: ")
    while not check_index_input(index):
        print("The input of the index should be an integer greater than 0. Please try again.")
        index = input("Enter index: ")
    print("\nLET'S START!") 
    num_of_tries = 0 # The number of failed attempts by the player so far.
    print("\n", HANGMAN_PHOTOS[num_of_tries+1]) # Opening 
    secret_word = choose_word(file_path, index) # The secret word that the user needs to guess.
    old_letters_guessed = [] # A list that holds the letters the player has guessed so far.
    print(" ", show_hidden_word(secret_word, old_letters_guessed))
    while((not check_win(secret_word, old_letters_guessed)) and (num_of_tries < MAX_TRIES)): 
    # Check- if the game should continue (the user has not won yet \ still can make a mistake).
        letter_guessed = input("\nGuess a letter: ").lower()
        while not try_update_letter_guessed(letter_guessed, old_letters_guessed):
        # Check if the character guessed by the player is valid, 
        # and if not- Input up to a valid character.
            letter_guessed = input("\nGuess a letter: ").lower() 
        if letter_guessed not in secret_word:
            num_of_tries += 1
            print(":(")
            print("\n", HANGMAN_PHOTOS[num_of_tries+1]) 
        print("\n ", show_hidden_word(secret_word, old_letters_guessed))
    if check_win(secret_word, old_letters_guessed):
        print("\nWIN!")
    else:
        print("\nLOSE!") 


if __name__ == '__main__':
    main()

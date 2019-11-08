# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_length = len(secret_word)
    count = 0
    for a in secret_word:
        for b in letters_guessed:
            if a == b:
                count = count + 1
    if count >= secret_word_length:
        return True
    else:
        return False
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ""
    for index, a in enumerate(secret_word, start=1):
        for b in letters_guessed:
            if a == b:
                result = result + b
        if len(result.replace(" ", "")) != index:
            result = result + "_ "
    return result


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alph = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for a in alph:
        if a not in letters_guessed:
            result = result + a
    return result
                
                
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_left = 6
    letters_guessed = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    warning = 3
    unique_letters = 0
    print("The word you must guess has " + str(len(secret_word)) +" letters")
    while(guesses_left > -2):
        print("The remaining letters are: " + get_available_letters(letters_guessed))
        if(guesses_left == 1):
            print("You have " + str(guesses_left) + " guess left")
        else:
            print("You have " + str(guesses_left) + " guesses left")
        user_input = input("Guess a letter:").lower()
        if user_input not in alph:
            print("Please only guess single letters")
            if warning != 0:
                warning = warning - 1
            if(warning == 1):
                print("You have " + str(warning) + " warning left")
            else:
                print("You have " + str(warning) + " warnings left")
            if warning == 0:
                guesses_left = guesses_left - 1
                print("you have no more warnings, one guess lost!")
                if guesses_left == 0:
                    print("Sorry you lose")
            print("--------------------------------------------")
            continue
        if user_input in letters_guessed:
            print(user_input + " has already been guessed, try again")
            if warning != 0:
                warning = warning - 1
                if(warning == 1):
                    print("You have " + str(warning) + " warning left")
                else:
                    print("You have " + str(warning) + " warnings left")
            else:
                guesses_left = guesses_left - 1
                if(guesses_left == 1):
                    print("You have " + str(guesses_left) + " guess left")
                else:
                    print("You have " + str(guesses_left) + " guesses left")
            print("--------------------------------------------")
            continue
        letters_guessed = letters_guessed + user_input
        if user_input in secret_word:
            print("Good job, so far you have: " + get_guessed_word(secret_word, letters_guessed))
            unique_letters = unique_letters + 1
            print("--------------------------------------------")
        if user_input in vowels and user_input not in secret_word:
            print("Try Again, so far you have: " + get_guessed_word(secret_word, letters_guessed))
            print("--------------------------------------------")
            guesses_left = guesses_left - 2
        if user_input not in vowels and user_input not in secret_word:
            print("Try Again, so far you have: " + get_guessed_word(secret_word, letters_guessed))
            print("--------------------------------------------")
            guesses_left = guesses_left - 1
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations you guessed the word!")
            print("Your Score is: " + str(guesses_left * unique_letters))
            break
        if guesses_left < 0:
            print("Sorry you lose")
            print("The word was: " + secret_word)
            return
        
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_length = 0
    other_word_length = 0
    for a in my_word:
        if other_word != "":
            if a != other_word[0] and a != "_" and a != " ":
                return False
            if a == other_word[0] or a == " ":
                other_word = other_word[1:]
                my_word_length = my_word_length + 1
                other_word_length = other_word_length +1
        else:
            return False
    if my_word_length == other_word_length:
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

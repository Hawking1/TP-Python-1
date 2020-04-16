def get_user_name():

 # Fonction is charged of recovering the username 
 # The username must contain minimum 3 caracters, numbers and letters only 
 # If this name is invalid, we call recursively the fonction to obtain a new name

     user_name = input("Type your name")
    # We make the first letter in Uppercase and others in Lowercase #
     user_name = user_name.capitalize()
     if not user_name.isalnum() or len(user_name)<4:
        print("This name is invalid.")
        # We call fonction again to have another name #
        return get_user_name()
     else:
        return user_name    
    
def get_letter():

    # This fonction get the typed letter by user. 
    # If the get chain is not a letter, 
    # then we call recursively the fonction until we get a letter.

    letter = input("Type one letter")
    letter = letter.lower()
    if len(letter)>1 or not letter.isalpha():
        print("The letter you type is invalid")
        return get_letter()
    else:
        return letter

def get_secret_word(complet_word, found_letters):
   # This fonction send back the secret word, partially found or not         
   # 
   # We send back the origine word with * replacing the letters we 
   # still haven't found.

   secret_word = ""
   for letter in complet_word:
       if letter in found_letters:
           secret_word += letter
       else:
           secret_word += "*"
   return secret_word
    
def run():
    # Number of attempts per game
    nb_try = 8

    # Word need to be guessed
    word_to_guess = "alphabet"

    # Variable to stock the found letters
    found_letters = []

    # We get a user name
    user = get_user_name

    print("Welcome {0} Let's play".format(user))

    # Initialization game 
    word_found = get_secret_word(word_to_guess, found_letters)
    nb_chances = nb_try

    # Ongoing game
    while word_to_guess!=word_found and nb_chances>0:

        print(" Word to guess {0} (still {1} chances)".format(word_found,nb_chances))

        # The letter has been already choosen
        if letter in found_letters:
            print("You already use this letter.")

        # The letter is already existing in the word to find
        elif letter in word_to_guess:
            print("Well done.")
        # The letter does exist in the word to find
        else:
            nb_chances -= 1
            print("... no, this letter does not exist in this word...")
        found_letters.append(letter)
        word_found = get_secret_word(word_to_guess,found_letters)


        # Did we find the word or our chances are they exhausted ?
        if word_to_guess ==word_found:
            print("Congratulations ! You found the word {0}.".format(word_to_guess))
        else: 
            print("Game over !!! You lose")
run()
            
        















    
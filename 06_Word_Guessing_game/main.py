import random
def choose_word():
    fruit_list = ['Apple','Banana','Ackee','Apricot','Avocado','Blackberry','Blueberry','Cherry','Grape','Guava','Jackfruit','Jujube','Jostaberry','Kiwifruit','Lanzones','Longan','Mango','Melon','Cantaloupe','Watermelon','Muskmelon','Mulberry','Orange','Clementine','Mandarine','Tangerine','Papaya','Pawpaw','Peach','Pear','Passionfruit','Persimmon','Pineapple','Plum','Pineberry','Pomegranate','Raspberry','Salmonberry','Redcurrant','Strawberry','Tamarind','Soursop','Ximenia','Yuzu']
    # fruit_list = ['Apple','Mango','Pear']
    return random.choice(fruit_list).lower()

# This function Checks if the Input is correct or not
def correct_input(chances):
    char = input("Guess a Character: ")
    char = char.lower().strip() #.strip()->removes spaces 
    if len(char) != 1 or not char.isalpha():
        print(f"Enter a Single Alphabet !")
        chances -= 1
        return correct_input(chances)
    return char,chances

# This function display the current status of the words which is being guessed 
def word_current_status(blanks):
    print(f"\nThe Current Word Status: "+" ".join(blanks))

# Driver's Code
def main():
    # A Random word Is choosen
    word_to_guess = choose_word()

    # Finding the Length of word and STARTING OF THE GAME
    length = len(word_to_guess)
    print(f"\nThe Fruit to be guessed has {length} alphabets in it.")

    # Printing the All Blanks Letter Words
    blanks = ["_"] * length
    word_current_status(blanks)
    chances = length+3
    print(f"\nYou Will be getting {chances} chances to guess the Correct Word.\nAnd for every correct Character guess you no. of attempts will not be reduced.\n")

    # This will keep track of the characte which has already been guessed,Initially EMPTY
    guessed_letter = set()

    # Main game Begin
    while( chances != 0):
        print(f"No of chances Remaining: {chances}")

        # Talking A Valid Input
        taken_value_from_user , chances= correct_input(chances)

        # Checking if the word is already been guessed or not,if not it is added in the set
        if taken_value_from_user in guessed_letter:
            print("\nYou have already Guessed this Letter,\nTRY AGAIN\n")
            continue
        else:
            guessed_letter.add(taken_value_from_user)
        
        # if the user_input is in the random words
        if taken_value_from_user in word_to_guess:
            for index,letter in enumerate(word_to_guess): # Enumerate returns an index
                if letter == taken_value_from_user: # if the iterated value in the for loop == user_input then
                    blanks[index] = taken_value_from_user # at the index return by the enumerated function for that iterated value , the user_input is assigned to the blanks[index] which is same as the letter
            word_current_status(blanks) # Checking Current word status 
            if "_" not in blanks: # Checking If the word is complete
                break
            continue
        else:
            print(f"The Guessed Character : '{taken_value_from_user}' is not in the Actual Word")
        
        chances -= 1

       
    # Deciding the Winner or the lsser
    if chances == 0:
        print(f"You Lost!! Try again Next Time.")
        print(f"The correct Word is '{word_to_guess}'")
    else:
        print(f"Congratualtion!! You Won the Game.")
    

if __name__ == "__main__":
    main()

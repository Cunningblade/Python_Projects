import random
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'
CLEAR ='\033[2J'

# Deciding the maximun no. of guessing Chance
def deciding_chances(lower_bound,upper_bound):
    if upper_bound - lower_bound < 5 :
        return 2
    elif upper_bound - lower_bound < 10:
        return 4
    elif upper_bound - lower_bound < 50:
        return 10
    else:
        return 15
    

def game(no_of_tries,lower_bound,upper_bound):
    
    # Generating a Random Number
    num = random.randint(lower_bound,upper_bound)
    
    # Game starts
    while( no_of_tries != 0):
        guess = int(input("Choose a Number : "))
        # Checking the Guess is in the bound or not
        if guess > upper_bound:
            print(f"{BOLD}Duffer!! you are guessing the value higher than the range you selected.{RESET}")
        elif guess < lower_bound:
            print(f"{BOLD}Idiot!! You guessed the number smaller than the range you selected{RESET}")
        else:
            # if the guess is greater than the random number
            if guess > num:
                if guess - num < 5:
                    print(f"{GREEN}You are too Close!!{RESET}")
                    print(f"Guess a little bit Lower")
                elif guess - num < 20:
                    print(f"{YELLOW}You can Try Better{RESET}")
                    print(f"Guess LOWER")
                else:
                    print(f"{MAGENTA}Your Guess it TOO HIGH !! Try Again{RESET}")

            # if the guess is lesser than the random number
            elif guess < num:
                if guess - num > -5:
                    print(f"{GREEN}You are too Close!!{RESET}")
                    print(f"Guess a little bit Higher")
                elif guess - num > -20:
                    print(f"{YELLOW}You can Try Better{RESET}")
                    print(f"Guess HIGHER")
                else:
                    print(f"{MAGENTA}Your Guess it TOO LOW !! Try Again{RESET}")
            else:
                print(f"{GREEN}{BOLD}You guessed It Correctly!!!")
                print(f"YOU WIN{RESET}")
                break
    
        no_of_tries -= 1
        print(f"\n{ITALIC}No of tries remaining",no_of_tries)
    if no_of_tries == 0:
        print(f"{RED}You LOST!! Try again next time{RESET}")





def main():
    
    
    while True:
        print(f"Enter the Range such that you can Guess the number in between it\n")

        # Talking the Input 
        lower_bound = int(input("Enter the lower Range: "))
        upper_bound = int(input("Enter the Upper Range: "))
        print("")
        print(f"Guess the no. in between : ",lower_bound,"-",upper_bound,"")
        
        # No.of tries
        no_of_tries = deciding_chances(lower_bound,upper_bound)
        print(f"\nYou will be getting",no_of_tries,"chances to guess the Correct Number\n")

        #game Begin
        game(no_of_tries,lower_bound,upper_bound)
        



# Program Execution Start from here
if __name__ == "__main__":
    main()
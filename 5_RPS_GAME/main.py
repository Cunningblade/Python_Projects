import random

BG_BLUE = '\033[44m'
RESET = '\033[0m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'
RETURN_HOME = '\033[H'
CLEAR = '\033[2J'
BLUE = '\033[34m'
BG_MAGENTA = '\033[45m'


# RUlES OF THE GAME
def rules():
    print("\nThe Rules Of the Game are as Follows:\n")
    print("Its a 2 player Game. Here You will PLay with the Computer.")
    print(f"You Have a Option To Choose from Any of the 3 Option: {BOLD}{YELLOW}'Rock' , 'Paper' , 'Scissor'{RESET}. ")
    print("Similarly the Computer will also Select From any of the 3 option.")
    print("How to win if You SELECT")
    print(f"{BOLD}\nFor {YELLOW}Rock:\n{RESET}")
    print(f"{BOLD}Rock X Rock    -> {BLUE}Draw{RESET}")
    print(f"{BOLD}Rock X Scissor -> {GREEN}Rock Wins{RESET}")
    print(f"{BOLD}Rock X Paper   -> {RED}Rock Lose{RESET}")
    print(f"{BOLD}\nFor {YELLOW}Paper:\n{RESET}")
    print(f"{BOLD}Paper X Paper   -> {BLUE}Draw{RESET}")
    print(f"{BOLD}Paper X Rock    -> {GREEN}Paper Wins{RESET}")
    print(f"{BOLD}Paper X Scissor -> {RED}Paper Lose{RESET}")
    print(f"{BOLD}\nFor {YELLOW}Scissor:\n{RESET}")
    print(f"{BOLD}Scissor X Scissor -> {BLUE}Draw{RESET}")
    print(f"{BOLD}Scissor X Paper   -> {GREEN}Scissor Wins{RESET}")
    print(f"{BOLD}Scissor X Rock    -> {RED}Scissor Lose{RESET}\n")
    print(f"{BOLD}\nGame will be in the format of Best of 3 Format{RESET}\n")
    print("."*100,end="\n\n")

# Getting User Choice
def U_choice():
    print("\nChoose from any of the below:\n" 
    + "'R' for ROCK\n"
    + "'P' for PAPER\n"
    + "'S' for SCISSOR\n")
    choice = None

    user_choice = input("YOUR CHOICE IS: ").strip().lower()
    if user_choice == 'r' or user_choice == '1':
        choice = 0
    elif user_choice == 'p' or user_choice == '2':
        choice = 1
    elif user_choice == 's' or user_choice == '3':
        choice = 2
    else:
        print(f"{RED}InValid INPUT!!{RESET}"+"\nChoose Again")
        return U_choice()

    return choice
        
# Game Function
def game():
    points = 0 
    for chances in range(1,4):
        
        #Defining What is in the program to choose from 
        ob = ['ROCK','PAPER','SCISSOR']
        user_choice = U_choice()

        # Computer randomlying selecting
        print(f"\nNow its Computer Turn......")
        Comp_choice = random.randint(0,2)

        # Displaying The Selection by the user and the computer
        print(f"{BG_BLUE}You Chose {ob[user_choice]} & Computer Chose {ob[Comp_choice]}{RESET}")

        Comp_choice += 1 # Balancing the Index of the ob
        user_choice += 1 # Balancing the Index of the ob
        
        #Rules
        # ob = ['ROCK','PAPER','SCISSOR']
        # for Rock
        if user_choice == 1:
            if Comp_choice == 1:
                print(f"{BLUE}{BOLD}DRAW!!{RESET}")
            elif Comp_choice == 2:
                print(f"{RED}You {BOLD}LOST this Round{RESET} ")
            elif Comp_choice == 3:
                print(f"{GREEN}You {BOLD}WON this Round{RESET} ")
                points +=1

        # for Paper
        elif user_choice == 2:
            if Comp_choice == 1:
                print(f"{GREEN}You {BOLD}Won this Round{RESET} ")
                points +=1
            elif Comp_choice == 2:
                print(f"{BLUE}{BOLD}DRAW!!{RESET}")
            elif Comp_choice == 3:
                print(f"{RED}You {BOLD}Lost this Round{RESET} ")

        # # for Scissor
        else:
            if Comp_choice == 1:
                print(f"{RED}You {BOLD}Lost this Round{RESET} ")
            elif Comp_choice == 2:
                print(f"{GREEN}You {BOLD}Won this Round{RESET} ")
                points +=1
            else:
                print(f"{BLUE}{BOLD}DRAW!!{RESET}")
        
        chances += 1
    print(f"You Only Scored {points} point .",end="")
    if points >= 2:
        print(f"{GREEN}{BOLD}YOU WON THE MATCH{RESET}")
    else:
        print(f"{RED}{BOLD}YOU LOST THE MATCH{RESET}")
    print("*"*100,end="\n\n")
        
def main():
    print(f"{CLEAR}\nWelcome to the GAME of {YELLOW}{BOLD}ROCKK-PAPER-SCISSORS{RESET}\n")
    while True:
        print("Select: \n1) 1 for Rules    \n2) 2 for Play    \n3) 3 For EXIT\n")
        print("."*100,end="\n\n")
        flow = input("Your Choice: ")

        if flow == "1":
            rules()
        
        elif flow == "2":
            game()

        elif flow == "3":
            print("See You Again! BYEE")
            exit()
            
        else:
            print(f"{RED}{BOLD}\nINVALID INPUT!!!! {RESET}\nChoose Again\n")

if __name__ == "__main__":
    main() 



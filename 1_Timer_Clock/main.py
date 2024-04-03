from playsound import playsound #(library , Function from that library)
import time

YELLOW = '\033[33m'
RESET = '\033[0m'
BG_GREEN = '\033[42m'
RED = '\033[31m'
CLEAR = '\033[2J'
RETURN_HOME = '\033[H'


## TAKING INPUT 
#Method 1
# hour = int(input("Enter Hour: "))
# min = int(input("Enter min: "))
# sec = int(input("Enter sec : "))

## ************OR******************
#Method 2
# print(f"Input in form of {YELLOW}hh:mm:ss{RESET}")
# hour , min , sec = map(int,input("Enter the time after which you want the ALARM: ").split())

##*****************OR*****************
#Method 3 
# taking input within  range
def taking_input_within_a_range(min_value,max_value,parameter):
    
    while True:
        user_input = int(input(f"Enter {parameter}: "))
        if user_input >= min_value and user_input <= max_value:
            return user_input
        else:
            print(f"{RED}Enter Valid Input!! TRY AGAIN {RESET}")

def main(): # this will show the program will be starting from here

    print(f"Input in form of {YELLOW}hh:mm:ss{RESET}")
    hour = int(input("Enter Hour: "))
    min = taking_input_within_a_range(0,60,"Minutes")
    sec = taking_input_within_a_range(0,60,"Second")

    ##time after which the alarm will ring
    print(f"{RED}Time = {hour}h {min}m {sec}s")

        #total time in seconds 
    total_time_in_sec = ((hour*60*60) + (min*60) + (sec)) 
            
    #print total time in seconds
    print(f"total_time_in_sec={BG_GREEN}{total_time_in_sec}{RESET}")

    #Calling Alarm Function
    Alarm(total_time_in_sec)

    print(f"{CLEAR}{RETURN_HOME}TIME UPs")

def Alarm(total_time_in_sec):
    
    print(CLEAR)
    while(total_time_in_sec != -1 ):
       
        time.sleep(1) # waiting 1sec
        hour_left = total_time_in_sec//3600      #Time left in hour
        min_left = (total_time_in_sec%3600)//60  #Time left in min
        sec_left = (total_time_in_sec%3600)%60   #Time left in sec
       
        print(f"{RETURN_HOME}{hour_left:02d}h {min_left:02d}m {sec_left:02d}s") #printing time left in clock format , 
        #[02d] print decimal no.in 2 digit format and if 2 digit no. not available padd no. with zero 
        total_time_in_sec -= 1 # reducing time by 1 sec
        

    playsound("sound.mp3")
    # playsound("Beep.mp3")

# hour = 00
# min = 00
# sec = 5
    
##*********** so this is used when we define the main function such that when this file is run if the required file he present run that file 
if __name__ == "__main__":
    main()



















    





    




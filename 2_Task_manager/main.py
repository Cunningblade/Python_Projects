import json

BG_BLUE = '\033[44m'
RESET = '\033[0m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'
RETURN_HOME = '\033[H'
CLEAR = '\033[2J'
BLUE = '\033[34m'


def task_can_be_performed():
    print(BOLD)
    print("1. List All the tasks ")
    print("2. Add Task ")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit the Program")
    print(RESET)


def fetch_data_from_file(): ## Using (try except) here because we want to return some thing from this function
    try:
        with open('taskk.txt','r') as file:
            return  json.load(file)     # will go in .txt document and loads the data in the file  
            
    except FileNotFoundError:
        print(f"{RED}NO SUCH FILE EXIST{RESET}")
        return []
    
def data_saver(file_name):  ## Save data in the .txt document
    with open('taskk.txt','w') as file:
        json.dump(file_name , file)
    

        


def list_task(file_name):
    print(f"{BLUE}The List of tasks are :{RESET} \n")
    for index, task in enumerate(file_name , start= 1):
        print(f"{index}.Date - {task['DATE']} || Task - {task['TASK']}")
    print("\n")


def add_tasks(file_name):
    date = input(f"{BLUE}Enter the date :{RESET} ")
    task = input(f"{BLUE}Enter the task :{RESET} ")
    file_name.append({'DATE': date , 'TASK':task})
    data_saver(file_name)

def update_task(file_name):
    list_task(file_name)
    index = int(input(f"Enter the task which you want to Update: "))
    if 1 <= index <= len(file_name):
        date = input(f"{BLUE}Enter the date :{RESET} ")
        task = input(f"{BLUE}Enter the task :{RESET} ")
        file_name[index-1] = {'DATE':date,'TASK':task}
        data_saver(file_name)
    else:
        print(f"{RED}INVALID INPUT!!!{RESET}")
    print(f"{GREEN}The Selected tasks is updated!{RESET}")

def delete_task(file_name):
    list_task(file_name)
    index = int(input(f"Enter the task which you want to delete: "))
    if 1 <= index <= len(file_name):
        file_name.pop(index-1)
        data_saver(file_name)
    else:
        print(f"{RED}INVALID INPUT!!!{RESET}")
    print(f"{GREEN}The Selected tasks is Deleted! {RESET}")


### MAIN FUNCTION STARTS
def main():
    
    file_name =[]
    file_name = fetch_data_from_file() ## Loading the data in the file 
    first_time = True
    print(f"{CLEAR}{RETURN_HOME}")
    while True:
        ## Asing the user what to perform
        if first_time == True:
            print(f"{BG_BLUE}Welcome to Tasks Manager\n{RESET}")
            task_can_be_performed()
            choice = input(f"{YELLOW}Choose An option:{RESET} ")
            print("\n")
            first_time = False
        else:
            task_can_be_performed()
            choice = input(f"{YELLOW}Choose An option:{RESET} ")
            print("\n")

        match choice:
            case '1':
                list_task(file_name)
            case '2':
                add_tasks(file_name)
            case '3':
                update_task(file_name)
            case '4':
                delete_task(file_name)
            case '5':
                data_saver(file_name)
                break
            case _: ## use as default
                print(f"{RED}INVALID CHOICE!!!{RESET}")
        print('=='*100)
        print('=='*100)
        
## Programs Starts from here
if __name__ == '__main__':
    main()
                                                                                                                               
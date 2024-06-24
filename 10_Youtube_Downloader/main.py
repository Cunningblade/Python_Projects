# '''
# Channel_link = "https://www.youtube.com/@Syntax_Sphere"
# '''
from pytube import YouTube
from pytube import Playlist
import os

RESET = '\033[0m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'



# yeh SINGLE VIDEO download karne ke liye hai kki uska resolution kya hona chaheye
def get_resolution(yt):
    res = input("Choose the Resolution in which you want to download the video:\n'L' : Low\n'N' : Normal\n'H' : High\n'O' : Others\n\nYour Choice: ").lower()
    # stream se resolution wale part mein jate hai aur .get_--- to samjh aaraha hai
    if res =='1' or res == 'l':
        return yt.streams.get_lowest_resolution()
    
    elif res == '2' or res == 'n':
        return yt.streams.filter(progressive=True, resolution='720p').first()
    
    elif res == '3' or res == 'h':
        return yt.streams.get_highest_resolution()
    
    # elif  res in ['4','o','0']:
    #     print("The Available Video resolutions are:\n1) 144p\n2) 240p\n3) 360p\n4) 480p\n5) 720p")
    #     quality = input("Choose any Of the Above: ").lower()
    #     if quality == '1' or quality in '144p':
    #         quality == '144p'
    #     elif quality == '2' or quality in '240p':
    #         quality == '240p'
    #     elif quality == '3' or quality in '360p':
    #         quality == '360p'
    #     elif quality == '4' or quality in '480p':
    #         quality == '480p'
    #     elif quality == '5' or quality in '720p':
    #         quality == '720p'
    #     return yt.streams.get_by_resolution(resolution=quality)
    
    else:
        print("INVALID CHOICE EXITING ... ")
        exit()



# yaha se single video download hoga 
def VID():
    link = input("Enter a YouTube video Link: ")
    # *** getting the location of downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")  # Expand user directory path on Linux/macOS
    if os.name == "nt":  # Check if it's Windows
        downloads_folder = os.path.join(os.environ["USERPROFILE"], "Downloads")
    # ***
    try:
        # link = Video_link
        # yt ek youtube object ban raha hai
        yt = YouTube(link)
        print("Video TITLE:",yt.title)
        stream = get_resolution(yt) # uper se resolution stream mein mil raha hai audio ke saath
    
        # video ko locally kaha save karna hai uska loaction maang rahe hai
        location = input("Enter the Path of the Location you want to Save the video:(The defaults is Downloads): ")
        path = location or downloads_folder
        print("The Video is downloading .... ")
        stream.download(output_path=path)
        print("Video Downloaded!")
    
    except Exception as e:
        print(f"An Error Occurred: {RED}{e}{RESET}")




# agar playlist download kkar rahe hai toh uss playlist ka detail
def playlist_details(plist):
    print(f"\nPlaylist Title: {RED}{BOLD}{plist.title}{RESET}")
    print(f"Total No. of Videos in Playlist: {BLUE}{BOLD}{plist.length}{RESET}")
    print(f"Owner of Playlist: {YELLOW}{plist.owner}{RESET}")
    print(f"Total views of the Playlist:{YELLOW} {plist.views}{RESET}\n")
    # harr video jo playlist mein hai uska url ek list mein save kkar rahe hai
    video_link = plist.video_urls
    print(f"The Videos in the Playlist {BOLD}{YELLOW}{plist.title}{RESET} are in Order:\n")

    serial_no = 1 # Indexing ke liye
    # playlist ka video display kar rahe hai
    for videos in video_link :
        yt = YouTube(videos)
        print(f"{serial_no}.{yt.title}")
        serial_no += 1
    print()
    # playlist ke video ke urls return kar rahe hai
    return video_link

# playlist ke video download karne ke liye
def download_videos(video_list,error):
    # *** getting the location of downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")  # Expand user directory path on Linux/macOS
    if os.name == "nt":  # Check if it's Windows
        downloads_folder = os.path.join(os.environ["USERPROFILE"], "Downloads")
    # ***
    # video ko locally kaha save karna hai uska loaction maang rahe hai
    location = input("Enter the Path of the Location you want to Save the video:(The defaults is Downloads):")
    path = location or downloads_folder  # agar loction mein path mila toh thik varna ekk default value downloads ka set ho jayega 

    serial_no = 1 # Indexing ke liye

    for videos in video_list:
        try:
            yt = YouTube(videos) # playlist ke saare video ke url ko haar iteration mein youtube object mein conversion

            print(f"{GREEN}{serial_no}.{yt.title} is downloading...........{RESET}")
            video_name = "".join([str(serial_no),"_",yt.title,".mp4"]) # video ka naam bana rahe hai seriall no. ke saath

            stream = yt.streams.get_highest_resolution() # Sabse highest resolution mein video download hoga 

            # video download kar rahe hai
            stream.download(output_path=path,filename=video_name)
            print(f"{YELLOW}Video Downloaded{RESET}")
            print()
        except Exception as e:
            print(f"An Error Occurred: {RED}{e}{RESET}")
            error = True
        serial_no += 1
    return error


def PL():
    
    link =  input("Enter a YouTube's Playlist video Link: ")
    plist = Playlist(link)
    video_list = playlist_details(plist)

    all_video_download = input("Do You Want to download all the videos In the playlist? (y/n): ").lower()
    error = False # agar download ke samay kop error ya exception raise ho tab

    # agar playlist ka saara video download karna hai
    if all_video_download == "y":
        download_videos(video_list,error)
    
    # agar selected video download karna ho
    elif all_video_download == "n":
        user_input = input("Enter multiple video no. you want to download, separated by space: ").split()
        slashed_video_list = []
        for i in range(0,len(user_input)):
            slashed_video_list.append(video_list[i])

        error = download_videos(slashed_video_list,error) # agar koi exception aaya ho ya error aaya ho tab 
    # galat video no. de diya download karne ke liye
    else:
        print("Invalid Input!! Start Again")
    
    # error occur huaa ki nhi
    if error == True:
        print(f"{BOLD}{RED}Complete Playlist was not downloaded{RESET}")
    else:
        print(f"{RED}{BOLD}Playlist Downloaded{RESET}")
    


def AUD():
    pass

def main():
    print("The Tasks YouTube Butler can Perform.")
    print("1) Download a YouTube Video\n2) Download a Youtube Playlist")
    # print("3) Convert the Youtube Video Into Only Audio")

    task = input("Select any One Task: ").lower()

    if task == '1' or task == 'a':
        VID()
    elif task == '2' or task == 'b':
        PL()
    # elif task == '3' or task == 'c':
    #     AUD()
    else:
        print("Invalid Choice")
        exit()

if __name__ =="__main__":
    main()
import string
RESET = '\033[0m'
BOLD = '\033[1m'

def message_encrypter():
    try:
        key = int(input("Enter a Secret Key(integer): ")) 
    except ValueError :
        key = 4
            
    shift = key % 26
    message = input("Enter a Message to Encrypt: ") or None
    if message == None:
        print("You did not Provided a message to Encrypt")
        exit()

    translation = str.maketrans(string.ascii_lowercase, (string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]))
    encrypted_message = message.lower().translate(translation)
    print(f"Your Encrypted Message is '{BOLD}{encrypted_message}{RESET}'")

def message_decrypter():
    try:
        key = int(input("Enter the Secret Key: ")) 
    except ValueError :
        key = 4
    shift = 26 - (key % 26)
    
    message = input("Enter a Message to Decrypt: ") 
    if not message:
        print('Nothing to Decrypt')
        exit()
        
    
    translation = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift], )
    decrypted_message = message.lower().translate(translation)
    print(f"Your Decrypted Message is '{BOLD}{decrypted_message}{RESET}'")

def main():
    print("\nWelcome to the Message Encrypter-Decrypter Program")
    choice = input(f"What do you Want to do?\n1) Encrypt a Message\n2) Decrypt a Message\n\n{BOLD}Enter Your Choice: {RESET}").lower()

    if (choice == '1') or (choice == 'a') or (choice == 'e'):
        message_encrypter()
    elif (choice == '2') or (choice == 'b') or (choice == 'd'):
        message_decrypter()
    else:
        exit()

if __name__ == '__main__':
    main()

{
# # # Enter a Message to Encrypt: i am om raj singh
# dictonary = {97: 119, 98: 120, 99: 121, 100: 122, 101: 97, 102: 98, 103: 99, 104: 100, 105: 101, 106: 102, 107: 103, 108: 104, 109: 105, 110: 106, 111: 107, 112: 108, 113: 109, 114: 110, 115: 111, 116: 112, 117: 113, 118: 114, 119: 115, 120: 116, 121: 117, 122: 118}

# for key in dictonary:
#     print(chr(key),":",chr(dictonary[key]))
# print("-"*100)
# # # Your Encrypted Message is 'e wi ki nwf oejcd'

# # # Enter a Message to Decrypt: e wi ki nwf oejcd

# dictonary = {97: 101, 98: 102, 99: 103, 100: 104, 101: 105, 102: 106, 103: 107, 104: 108, 105: 109, 106: 110, 107: 111, 108: 112, 109: 113, 110: 114, 111: 115, 112: 116, 113: 117, 114: 118, 115: 119, 116: 120, 117: 121, 118: 122, 119: 97, 120: 98, 121: 99, 122: 100}
# for key in dictonary:
#     print(chr(key),":",chr(dictonary[key]))
# # # Your Decrypted Message is 'i am om raj singh'
}
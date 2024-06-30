def remove_common_char(name1,name2):
    name1 = list(name1)
    name2 = list(name2)

    for char in name1:
        if char in name2:
            name1.remove(char)
            name2.remove(char)
            
    
    return len(name1)+len(name2) 

def flames_game(count):
    flames = ['F','L','A','M','E','S']

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index+1:]
            left = flames[:split_index]
            flames = right + left                                       
                                                   
        else:                                                            
            flames = flames[:len(flames) - 1]

    return flames[0]

def main():
    name1 = input("What is the Name of the FIRST PERSON?\n")
    name2 = input("What is the Name of the SECOND PERSON?\n")

    name1 = name1.replace(" ","")
    name2 = name2.replace(" ","")
    

    character_left = remove_common_char(name1.lower(),name2.lower())
    print(character_left)
    relation = flames_game(character_left)
    relation = relation.upper()
    
    flames_result = {
        'F':'Friends',
        'L':'Love',
        'A':'Affection',
        'M':'Marriage',
        'E':'Enemies',
        'S':'Siblings'
    }
    print(f"The RelationShip between {name1} and {name2} is {flames_result[relation]}")

if __name__ == "__main__":
    main()
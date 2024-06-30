# convert the single character into numerical value by converting into its ASCII value - 96
def char_to_value(char):
    return ord(char.lower()) - 96


def main():
    name1 = input("Enter the 1st Person's Name: ")
    name2 = input("Enter the 2nd Person's Name: ")

    name1 = name1.replace(" ","")
    name2 = name2.replace(" ","")

    sum1 = 0
    sum2 = 0
    for char in name1:
        sum1 = sum1 + char_to_value(char)
    for char in name2:
        sum2 = sum2 + char_to_value(char)

    love_percentage = ((sum1+sum2)%101)
    print(f"The LOVE Percentage between {name1} and {name2} is {love_percentage}%")

if __name__ == "__main__":
    main()
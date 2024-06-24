def letter_to_number(letter):
    """
    Convert a letter to its corresponding numerical value (A=1, B=2, ..., Z=26).
    """
    return ord(letter.lower()) - 96

def sum_digits(number):
    """
    Sum the digits of a number until a single-digit number is obtained.
    """
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number

def numerology_number(name):
    """
    Convert a name to its numerology number.
    """
    name = name.replace(" ", "").lower()
    total = sum(letter_to_number(char) for char in name)
    return sum_digits(total)

def numerology_compatibility(name1, name2):
    """
    Calculate numerology compatibility between two names.
    """
    num1 = numerology_number(name1)
    num2 = numerology_number(name2)
    
    return num1 == num2

# Example usage:
name1 = "ALICE"
name2 = "BOB"
compatible = numerology_compatibility(name1, name2)
print(f"{name1} and {name2} are numerologically {'compatible' if compatible else 'not compatible'}")

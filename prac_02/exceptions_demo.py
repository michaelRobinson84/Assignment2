"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: A ValueError will occur when the user enters a non-decimal character
2. When will a ZeroDivisionError occur?
Answer: A ZeroDivisionError will occur when the user enters 0 for the denominator input
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Yes, see code below
"""
is_Valid = False

try:
    numerator = int(input("Enter the numerator: "))
    while(not is_Valid):
        denominator = int(input("Enter the denominator: "))
        if denominator != 0:
            is_Valid = True
        else:
            print("Cannot have 0 as the denominator")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
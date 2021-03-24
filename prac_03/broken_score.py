"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

import random

def main():
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print(result)

    random_score = random.randint(0,100)
    print("Random score is ", random_score)
    result = calculate_result(random_score)
    print(result)

def calculate_result(score):
    if score < 0:
        return("Invalid score")
    elif score > 100:
        return("Invalid score")
    elif score >= 90:
        return("Excellent score")
    elif score >= 50:
        return("Passable score")
    else:
        return("Bad score")


main()
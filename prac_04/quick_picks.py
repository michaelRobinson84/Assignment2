import random

NUM_OF_RANDOM_NUMS = 6
HIGHEST_NUMBER = 45


num_of_picks = int(input("How many quick picks? "))

for number in range(0, num_of_picks, 1):

    random_numbers = []

    repeated_number = True

    for random_number in range(0, NUM_OF_RANDOM_NUMS, 1):
        random_number = random.randint(1, HIGHEST_NUMBER)
        random_numbers.append(random_number)

    random_numbers.sort()
    print(random_numbers)
    # random_num = random.randint(1, HIGHEST_NUMBER)
    # print(random_num)
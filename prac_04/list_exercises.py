numbers = []

for i in range(1, 6, 1):

    user_input = int(input("Enter a number: "))
    numbers.append(user_input)

print()
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[4]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
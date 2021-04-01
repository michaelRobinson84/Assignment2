numbers = []

for i in range(1, 6, 1):

    user_input = int(input("Enter a number: "))
    numbers.append(user_input)

print()
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[4]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
average = sum(numbers) / 5
print("The average of the numbers is {}".format(average))

print()

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = input("Please enter your username: ")

if user_name in usernames:
    print("Access granted")
else:
    print("Access denied")
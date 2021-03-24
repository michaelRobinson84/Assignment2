# Program 1

name = input("Please enter your name: " )

out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# Program 2

in_file = open("name.txt", "r")
name = in_file.read()
print("Your name is", name)
in_file.close()

# Program 3

in_file = open("numbers.txt", "r")
first_num = int(in_file.readline())
second_num = int(in_file.readline())
result = first_num + second_num
print(result)
in_file.close()

# Program 4

running_total = 0

in_file = open("numbers.txt", "r")

for line in in_file:
    running_total = running_total + int(line)

print(running_total)
in_file.close()
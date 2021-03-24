x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

print("""i. Show the even numbers from x to y
ii. Show the odd numbers from x to y
iii. Show the squares from x to y
iv. Exit the program""")

choice = input(">>> ")

while(choice != "iv"):
    if(choice == "i"):
        for i in range(x, y, 2):
            print(i)
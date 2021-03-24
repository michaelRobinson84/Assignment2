for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

num_of_stars = int(input("Enter the number of stars: "))

for i in range(0, num_of_stars, 1):
    print("*", end='')
print()

for i in range(0, num_of_stars + 1, 1):
    print("*" * i)

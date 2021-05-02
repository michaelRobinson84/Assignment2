from prac_06.guitar import Guitar

print("My guitars!")

guitars = []

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
# guitars.append(Guitar("My cool guitar", 1918, 845.7))

name = input("Name: ")

while name != "":

    year = input("Year: ")
    year = int(year)
    cost = input("Cost: ")
    cost = float(cost)

    new_guitar = Guitar(name, year, cost)

    guitars.append(new_guitar)

    print("{} ({}) : ${} added".format(new_guitar.name, new_guitar.year, new_guitar.cost))

    name = input("Name: ")

vintage_string = ""

print("These are my guitars:")

for i in range(0, len(guitars), 1):

    if guitars[i].is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""

    print("Guitar {} : {} ({}), worth ${} {}".format(i+1, guitars[i].name, guitars[i].year, guitars[i].cost, vintage_string))
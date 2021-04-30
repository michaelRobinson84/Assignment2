from prac_06.guitar import Guitar

def main():
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 800)

    age = first_guitar.get_age()
    print("Gibson L-5 CES get_age() - Expected 99. Got ", age)
    age = another_guitar.get_age()
    print("Another Guitar get_age() - Expected 8. Got ", age)

    vintage = first_guitar.is_vintage()
    print("{} is_vintage() - Expected True. Got {}".format(first_guitar.name, vintage))
    vintage = another_guitar.is_vintage()
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, vintage))

main()
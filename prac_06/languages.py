from prac_06.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    cars = [ruby, python, visual_basic]

    for car in cars:
        print(car)

    print()
    print("The dynamically typed languages are:")

    for car in cars:
        if car.isDynamic():
            print(car.name)

main()
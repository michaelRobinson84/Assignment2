MIN_LENGTH = 8

def main():
    print("Please enter the password")
    password = input(">")
    while len(password) < MIN_LENGTH:
        print("Invalid length, please re-enter")
        password = input(">")
    print(len(password) * "*")

main()
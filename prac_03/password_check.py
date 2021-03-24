MIN_LENGTH = 8

def main():

    password = get_password()
    print_password(password)


def print_password(password):
    print(len(password) * "*")


def get_password():

    print("Please enter the password")
    password = input(">")
    while len(password) < MIN_LENGTH:
        print("Invalid length, please re-enter")
        password = input(">")
    return password


main()
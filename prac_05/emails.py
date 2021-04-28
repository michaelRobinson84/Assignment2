email_dict = {}

email = input("Email: ")

while(email != ""):
    name = email.split("@")
    name = name[0]
    name = name.title()
    name = name.split(".")
    full_name = " ".join(name)

    valid_response = False

    while(not valid_response):
        print("Is your name " + full_name + "?")
        response = input("Y/n ")
        response = response.upper()
        if response == '':
            email_dict[full_name] = email
            valid_response = True
        elif response == 'Y':
            email_dict[full_name] = email
            valid_response = True;
        elif response == 'N':
            correct_name = input("Name:")
            email_dict[correct_name] = email
            valid_response = True
        else:
            print("Invalid response!")

    email = input("Email: ")

for key, value in email_dict.items():
    print("{} ({})".format(key, value))

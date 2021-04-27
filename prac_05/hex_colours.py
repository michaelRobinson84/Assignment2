CODE_TO_NAME = {"ALICEBLUE": "#fof8ff", "BEIGE": "#f5f5dc", "CADETBLUE": "#5f9ea0", "DARKOLIVEGREEN": "#556b2f",
                "FIREBRICK": "#b22222", "FORESTGREEN": "#228b22", "GOLD1": "#ffd700", "GRAY": "#bebebe", "KHAKI": "#f0e68c", "LAVENDER": "#e6e6fa"}
print(CODE_TO_NAME)

colour_name = input("Enter colour name: ")
colour_name = colour_name.upper()
while colour_name != "":
    if colour_name in CODE_TO_NAME:
        print(colour_name, "is", CODE_TO_NAME[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
    colour_name = colour_name.upper()
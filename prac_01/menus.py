name = input("Enter name: ")

print("""(H)ello
(G)oodbye
(Q)uit""")

choice = input(">>> ")
choice = choice.upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print("""(H)ello
(G)oodbye
(Q)uit""")

    choice = input(">>> ")
    choice = choice.upper()

print("Finished.")


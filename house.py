name = input("Enter the name: ")

#if name == "Harry":
#    print("Griffindor")
#elif name == "Hermione":
#    print("Griffindor")
#elif name == "Ron":
#    print("Griffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
# The match statement is a more readable and efficient way to handle multiple conditions.
name = input("What is your name? ")

#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# Read the file

with open("names.txt", "r") as file:
    names = file.readlines()

for name in names:
    print("Hello,", name.rstrip())
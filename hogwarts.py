# This shows how to print a list

students = ["Hermione", "Harry", "Ron", "Draco", "Neville", "Luna"]

for i in range(len(students)):
    print(i + 1, students[i])

print("------------------")

# This code prints the names and houses of students in a Hogwarts that are stored in a dictionary.

students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin",
    "Neville": "Hufflepuff",
    "Luna": "Ravenclaw"
}

for student in students:
    print(student, students[student], sep=", ")

print("------------------")

# This code prints the names, houses, and patronuses of students in a Hogwarts that are have many data in a dictionary.

students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"},
    {"name": "Neville", "house": "Hufflepuff", "patronus": "None"},
    {"name": "Luna", "house": "Ravenclaw", "patronus": "None"}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" -> ")
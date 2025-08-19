import csv

name = input("What is your name? ")
designation = input("What is your designation? ")

with open("employee.csv", "a") as file:
    write = csv.DictWriter(file, fieldnames=["Name", "Designation"])
    write.writerow({"Name": name, "Designation": designation})
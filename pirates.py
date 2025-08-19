import csv

pirates = []

with open("pirates.csv") as file:
    reader = csv.reader(file)
    for pirate, ship in reader:
        pirates.append({"pirate": pirate, "ship": ship})

for pirate in sorted(pirates, key=lambda pirate: pirate["pirate"]):
    print(f"{pirate['pirate']} sails the {pirate['ship']}")
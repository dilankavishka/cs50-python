#Ask user for their name
name =input ("What is your name? ")
age = input("What is your age? ")

#Remove whitespace from str and capitalize users name 
name = name.strip().title()
age = age.strip()

#Say hello to the user
print("Hello," + name + "! You are " + age + " years old.")
#print(f"Hello, {name}! You are {age} years old.")


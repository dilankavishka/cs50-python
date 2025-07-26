score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("You got an A")
elif score >= 75:
    print("You got a B")
elif score >= 65:
    print("You got a C")
elif score >= 45:
    print("You got a D")
else:
    print("You got a F")
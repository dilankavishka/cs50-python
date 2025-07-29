def main():
    number =  get_number()
    print(number)

def get_number():
    while True:
        n = int(input("How many times should I meow? ") )
        if n > 0:
            break
        return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()

# This code prints "Meow" three times using a while loop.

i = 3

while i != 0:
    print("Meow")
    i = i -1
print("------------------")
i = 0
while i < 3:
    print("Meow")
    i += 1
print("------------------")
for i in [0,1,2]:
    print("Meow")
print("------------------")
for i in range(5):
    print("Meow")
print("------------------")
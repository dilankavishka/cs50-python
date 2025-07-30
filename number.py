def main():
    x = get_number()
    print(f"x is {x}")

def get_number():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()
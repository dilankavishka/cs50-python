#x = int(input("Please enter a number: "))

#if x % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

def main():
    x = int(input("Please enter a number: "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
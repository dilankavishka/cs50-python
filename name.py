import sys

try:
    print("Hola, My name is ",sys.argv[1])
except IndexError:
    print("Please enter a name")
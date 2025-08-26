import re

email = input("Enter your email address: ").strip()

# if re.search("@", email):
# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid email address.")
else:
    print("Invalid email address.")

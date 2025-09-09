import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

#username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
import random
import string
import requests
from bs4 import BeautifulSoup

# 16. Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

print("--------------QUESTION -----------------------")
def main():
    #ask user for password length
    l = int(input("Enter password length: "))
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    li = []
    for i in range(l):
        res = random.choice(char)
        li.append(res)

    final = "".join(li)
    print("Your password is: ")
    print(final)


if __name__ == "__main__":
    main()


# 17. Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

print("--------------QUESTION -----------------------")

url = "https://www.nytimes.com/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
titles = soup.find_all("h2")

print("Printing all the titles of New York Times website: ")
for t in titles:
    print(t.get_text())
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




# 18. Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.


print("--------------QUESTION -----------------------")
def randum():
    ran = random.randint(1000, 9999)
    ranstr = str(ran)


    while True:
        asku = input("Enter a 4 digit number: ")
        

        for j in range(len(asku)):
            for k in range(len(ranstr)):
                if (asku[j] == ranstr[k]):
                    return ranstr
                else:
                    return "errrr do it again it was " + ranstr 




hah = randum()
print(hah)


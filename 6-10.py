import random
# 6. Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

print("--------------QUESTION -----------------------")
a = input("Enter a word: ")

for i in range(len(a)):
    if (a[i] != a[len(a)-1-i]):
        
        isPalindrome = False
    else:
        isPalindrome = True

if isPalindrome == True:
    print(f"The word {a} is palindrome")
else:
    print(f"The word {a} is not palindrome")


# 7. Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

print("--------------QUESTION -----------------------")
x = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(f"The values of X are: {x}")
y = [n for n in x if n%2==0 ]
print(f"The values of Y are: {y} ")

# 8. Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

print("--------------QUESTION -----------------------")
while True: 
    p1 = input("Rock, Paper or Scissors: ")
    p2 = input("Rock, Paper or Scissors: ")

    if (p1 == "rock" and p2 == "paper"):
        print(f"p2 won because {p2} beats {p1}")
    elif (p1 == "paper" and p2 == "scissors"):
        print(f"p2 won because {p2} beats {p1}")
    elif (p1 == "scissors" and p2 == "rock"):
        print(f"p2 won because {p2} beats {p1}")
    elif(p1 == p2):
        print("DRAW!!")
    else:
        print(f"p1 won because {p1} beats {p2}")
    
    
    if p1 == "quit":
      break
    else: 
      print("END OF GAME")


# 9. Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
print("--------------QUESTION -----------------------")

randnum = random.randint(1,9)
uinput = int(input("Enter a random number between 1 to 9: "))

if (randnum == uinput):
    print(f"You have guessed the correct number: {uinput}")
elif(randnum > uinput):
    print(f"The number you have guessed it too low, the number was {randnum}")
else:
    print(f"The number you have guessed it too high, the number was {randnum}")


# 10. This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.

print("--------------QUESTION -----------------------")
j = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f"The contents of J are: {j} ")
k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(f"The contents of K are: {k}")

l = list(set([m for m in j if m in k]))
print(f"List comprehension between j and k without duplicate values {l}")


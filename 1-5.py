
# 1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 


print("--------------QUESTION -----------------------")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print_year = 2025 - age + 100

print(f" {name}, You will turn 100 years old in {print_year}")


# 2. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.


print("--------------QUESTION -----------------------")
num = int(input("Enter a number: "))
 
if (num % 2 == 0):
    print(f"Number {num} is Even")
else:
    print(f"Number {num} is Odd")



# 3. Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

print("--------------QUESTION -----------------------")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if (i < 5):
        print(i)


# 4. Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print("--------------QUESTION -----------------------")
uinput = int(input("Enter number to list out its divisors: "))

print(f"The divisors for {uinput} are: ")

for i in range(1, uinput + 1):
    if (uinput % i==0):
        print(i)


# 5. Take two lists, say for example these two:
# c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.


print("--------------QUESTION -----------------------")
c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
e = []
for x in c:
    for y in d:
        if (x == y and x not in e):
            e.append(x)
                
print(e) 
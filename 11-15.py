# 11. Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).

print("--------------QUESTION -----------------------")
def addition():

    print("Enter number to check if it is prime or not: ")
    a = int(input("Enter number: "))
    if(a%2==1):
        return "is prime"
    else:
        return "not prime"


d = addition()
print(d)


# 12. Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.


print("--------------QUESTION -----------------------")
def listwork():
    l = [5, 10, 15, 20, 25]
    print("This is the first list: ")
    print(l)

    m = [l[0], l[-1]]
    print("This is the second list with only first and last element: ")
    return m
            

print(listwork())


# 13. Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.


print("--------------QUESTION -----------------------")
def fib():

    u = int(input("Enter a number for its fibonacci series: "))
    result = []
    i, x = 0, 1

    for j in range(u):
        result.append(i)
        i, x = x, i + x

    return result

print (fib())


# 14. Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

print("--------------QUESTION -----------------------")
    
def comlist():
    l1 = ['apple', 'banana', 'orange', 'grapefruit', 'apple']
    l2 =  []
    
    print("This is the first list: ")
    print(l1)
    
    
    for k in l1:
        if k not in l2:
            l2.append(k)
    
    print("This is the second list minus the duplicates: ")
    return l2
    
print(comlist())


# 15. Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

print("--------------QUESTION -----------------------")

def sent():
    sentence = input("Type a sentence: \n")
    conv = sentence.split()
    conv.reverse() 
    man = " ".join(conv)

    return man

print(sent())
### PracticePython.org - Exercise 12: List Ends ###
# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html #

# The question is: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

def myList(elements):
    list1 = elements.split(" ")    # let me sort our your input first, okay?
    list2 = []
    list2.append(list1[0])    # 
    list2.append(list1[-1])
    print(list2)
    
yourInput= input("Enter a list of numbers divided by space: ")
myList(yourInput)

# For some time now, I was wondering how one can give multiple inputs divided by space, i.e 1 3 12 150 42.
    # I came up with .split() module and it fit to this problem. Maybe there exists a different input() for that. We will see.
# Also I was trying to execute my "example.py" file on my python shell and I've just learned how to do it:
    # Here the command is: exec(open("C:\\Users\\mycomputer\\Desktop\\example.py").read())
    # I studied how to write/read/edit etc. files a month ago but I need to do more exercises on it, obviously.

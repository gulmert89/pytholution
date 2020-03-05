# "A palindrome is a word, number, phrase, or other sequence of characters
# which reads the same backward as forward, such as madam, racecar or 'Was it a car or a cat I saw'." - Wiki
# So, the question is whether your input is a palidrome or not.

palindrome_str = (input("Checking whether your input is a palindrome or not: ").replace(" ","")).lower()

# I wanted to make sure that there would be no space between the letters! So the .replace() module is introduced.
# Also knowing that "A" == "a" is False, all the characters should be lowercase.
# After completing this Exercise-6 of PracticePython.org, I saw similar palindrome codes on the net but most of them
# didn't have this "fail-safe" modules. For example, "Murder for a jar of red rum" failed on those codes.
# Mine prevailed! Muhahaha!

palindrome = list(palindrome_str)

palindrome_rev = palindrome[::-1]    # Please see the comment below.

print(palindrome_str, end="\n")

if palindrome==palindrome_rev:
    print("Your input is a palindrome.")
else:
    print("Your input is not a palindrome.")
    
# Note to myself:
# I was trying to match the words letter by letter but I came up with this simple idea above like 3 hours later.
# I don't know why I was trying the hard way. Maybe I would make it work as well later as a "Solution 2".
# I'll revisit it later but let me put my old code here:
"""
pal= input("Checking whether your input is a palindrome or not: ")

    list1 = []
    list2 = []
for i in range(0,(len(pal)-1)//2):
    list1.append(pal[i])
    list2.append(pal[len(pal)-1-i])
if list1 == list2:
    print("Your input is a palindrom!")
else:
    print("Your input is not a palindrom.")
"""

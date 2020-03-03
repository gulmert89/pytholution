print("""I want you to give me the list and the bag's number.\nIf the number is \"ticking\" in the list, I'll let ya live.
If not, you've got to ask yourself one question: Do I feel lucky?\n""")
list_input = input("Now enter the god damn list to this device, punk: ")
int_input = int(input("Hand me the number! C'mon: "))
print("Okay, bastard. You want the \"solution1\" or \"solution2\"?")
print("\tsolution1 simply take your list and look for the number inside it like a cop checking everone's face on one by one.")
print("\tsolution2 does it with binary search. It checks your number and splits the list into two and keep... Nevermind!")
select_input = input("So, which one do you want? solution1 or solution2? Tell me: ")

def solution1(l_i=list_input, i_i=int_input):
    l_i = sorted(list(map(int,(l_i.split(" ")))), reverse=False)    # from inside to outside: input numbers are filtered, turned to int by map function, converted to list, sorted.
    if i_i in l_i:
        print("Well... The number {0} you have entered IS in the list {1}.".format(i_i,l_i))
        print("It was your lucky day. And please don't take it personal. It's just business.\nNow get out of my sight!")
    else:
        print("Sorry. The number {0} you have entered is not in the list {1}.".format(i_i,l_i))
        print("It's time to say goodbye!")
    
solution1()

def solution2(l_i=list_input, i_i=int_input):
    l_i = sorted(list(map(int,(l_i.split(" ")))), reverse=False)    # same as the above
    
    while len(l_i) > 1:
        if i_i < l_i[len(l_i)//2]:
            l_i = l_i[:(len(l_i)//2)]
        elif i_i == l_i[len(l_i)//2]:
            print("You are a lucky bastard! You have found it! ...and yes, the number is in the list.")
            break
        else:
            l_i = l_i[(len(l_i)//2):]
    

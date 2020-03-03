list_input = input("Enter the god damn list: ")
int_input = int(input("Hand me the number! Now: "))

def solution1(l_i=list_input, i_i=int_input):
    l_i = sorted(list(map(int,(l_i.split(" ")))), reverse=False)    # from inside to outside: input numbers are filtered, turned to int by map function, converted to list, sorted.
    if i_i in l_i:
        print("The number {0} you have entered is in the list {1}.".format(i_i,l_i))
    else:
        print("The number {0} you have entered is not in the list {1}.".format(i_i,l_i))
    
solution1()

def solution2(l_i=list_input, i_i=int_input):
    l_i = sorted(list(map(int,(l_i.split(" ")))), reverse=False)    # same as the above
    if i

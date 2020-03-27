# This particular challenge from codewars.com took me 8 or 9 hours to complete because 
# I failed to understand the problem clearly and came up with 3 solutions
# for 3 scenarios in my mind. I've learned a lot though.
# Let me write the problem definition here and talk about it later:
"""
You are given an array "strarr" of strings and an integer "k".
Your task is to return the first longest string consisting of k consecutive strings taken in the array.
Example:
>>> longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
"abigailtheta"
or
>>> longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)
"ixoyx3452zzzzzzzzzzzz"

"n" being the length of the string array, if n = 0 or k > n or k <= 0, return "".
Note:
consecutive strings : follow one after another without an interruption
"""
# So, the code will give us the longest possible string made of two consecutive element in a given list.

# Here is my correct solution:
def longest_consec(strarr, k):
    if len(strarr)!=0 and k <= len(strarr) and k>0:    # working conditions
        max_list = []
        max_string = []
                
        i = 0
        try:
            while i < len(strarr):
                for j in range(i,k):
                    max_list.append(strarr[j])    # Here I add "k" elements together and form
                max_string.append("".join(max_list))
                i += 1
                k += 1
                max_list.clear()    # 
        except IndexError:
                pass
        finally:
            return max(max_string, key=len)
        
    else:
        return ""
    
# Time: 2374ms Passed: 209 Failed: 0
# Test Results:
#    longest_consec
#       Basic tests (209 of 209 Assertions)
# You have passed all of the tests! :)

    
    
    
# Test Cases:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
# longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
# longest_consec([], 3)
# longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)
# longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2)
# longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)
# longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15)
# longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0)


# first try:
"""
def longest_consec(strarr, k):
    if len(strarr)!=0 and k <= len(strarr) and k>0:
        sort_strarr = sorted(strarr, key=lambda element: len(element), reverse = True)
        c_list = []    # consecutive list
        if len(strarr)!=0 and k <= len(strarr) and k>0:
            for i in range(k):
                c_list.append(sort_strarr[i])
            #c_list.sort(key= lambda indx: strarr.index(indx))
            return ("".join(c_list))
    else:
        return ""
"""

# Time: 2211ms Passed: 11 Failed: 198
# Test Results:
#    longest_consec:
#        > Basic tests (12 of 209 Assertions)

# second try:
"""
if len(strarr)!=0 and k <= len(strarr) and k>0:
        r_max = []
        l_max = []
        max_index = strarr.index(max(strarr, key=len))
        for i in range(k):
            try:
               r_max.append(strarr[max_index+i])
            except IndexError:
               pass
            l_max.append(strarr[max_index-i])
        r_max_string = "".join(r_max)
        l_max_string = "".join(list(reversed(l_max)))
        if len(r_max_string) > len(l_max_string):
            return r_max_string
        else:
            return l_max_string
    else:
        return ""
"""

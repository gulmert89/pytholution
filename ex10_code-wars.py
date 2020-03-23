def longest_consec(strarr, k):
    if len(strarr)!=0 and k <= len(strarr) and k>0:
        max_list = []
        max_string = []
                
        i = 0
        try:
            while i < len(strarr):
                for j in range(i,k):
                    max_list.append(strarr[j])
                max_string.append("".join(max_list))
                i += 1
                k += 1
                max_list.clear()
        except IndexError:
                pass
        finally:
            return max(max_string, key=len)
        
    else:
        return ""

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

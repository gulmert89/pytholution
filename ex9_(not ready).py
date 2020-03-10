import urllib.request as url

ppText = url.urlopen("http://www.practicepython.org/assets/nameslist.txt").read()
ppText = ppText.decode("utf-8")

#solution 1
def sol1():
    print("--- Solution 1 ---")
#    with open("nameslist.txt", "r") as ppFile:
#        ppText = ppFile.read()
    ppList = ppText.split()
    ppDict = {}
    for i in ("Darth","Lea","Luke"):
        ppDict[i] = ppList.count(i)
    print(ppDict)
    print("Total number of names is:",len(ppList))

#solution2
def sol2():
    print("--- Solution 2 ---")
    counter_dict = {}
    with open("nameslist.txt") as ppFile:    # needs a local nameslist.txt file :|
        line = ppFile.readline()
        while line:
            line = line.strip()
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = ppFile.readline()
    print(counter_dict)

#extra solution
def sol3():
    print("--- Extra Solution ---")
    with open("Training_01.txt", "r") as ppFile:
        ppText = ppFile.read()



    # you can use these:
    # str.index(sub, start, end)
    # str.find(sub, start, end)
    # the idea: take the word between the two indices of two /forward slashes/


sol1(); print("\n")
sol2()

# reference webpages: https://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont
# files: http://www.practicepython.org/solution/2014/12/14/22-read-from-file-solutions.html

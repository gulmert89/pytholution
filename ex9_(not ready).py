import urllib.request as url

ppText = url.urlopen("http://www.practicepython.org/assets/nameslist.txt").read()
ppText = ppText.decode("utf-8")

# my solution for Practice Python: Exercise 22
def sol():
    print("--- Solution 1 ---")
    ppList = ppText.split()
    ppDict = {}
    for i in ("Darth","Lea","Luke"):
        ppDict[i] = ppList.count(i)
    print(ppDict)
    print("Total number of names is:",len(ppList))

# my solution for the "Extra" part of the exercise
def sol_ext():
    print("--- Extra Solution ---")
    ppText_ext = url.urlopen("http://www.practicepython.org/assets/Training_01.txt").read()
    ppText_ext = ppText_ext.decode("utf-8")
    ppList_ext = ppText_ext.split()
    ppDict_ext = {}
    ppCategory = set()
    for i in ppList_ext:    # YOU ARE CURRENTLY HERE. RETURN HERE TOMORROW
        ppCategory.add(ppList_ext[3:ppList_ext.index("/",3,(len(ppList_ext)-1))])
    for i in ("Darth","Lea","Luke"):
        ppDict[i] = ppList.count(i)
    print(ppDict)
    print("Total number of names is:",len(ppList))



    # you can use these:
    # str.index(sub, start, end)
    # str.find(sub, start, end)
    # the idea: take the word between the two indices of two /forward slashes/


sol(); print("\n")
sol_ext()

# reference webpages: https://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont
# files: http://www.practicepython.org/solution/2014/12/14/22-read-from-file-solutions.html

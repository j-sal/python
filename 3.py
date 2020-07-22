'''
Lists and tuples are ordered
Tuples are unmutable but can contain mixed typed items
Lists are mutable but don't often contain mixed items
Sets are mutable, unordered and doesn't hold duplicate items,
    sets can also do Unions, Intersections, and Differences
Dictionaries are neat
'''

myList = ["coconut","pear","tomato","apple"]
l2 = ["coconuts","pear","tomato","apple"]
l3 = [56,5,4,3,88,17]
mySet = {2.0, "Joey", ('Pratt')}
mySet2 = {"Jo", 2.0}
myD = {'Spanish level':5,'Eng level':5, 'Chinese level':3,'French level':1.5}

if "apple" in myList:
    print("'apple' is on the list and its index is:",myList.index("apple"))
    print("The fruit apple appears",myList.count("apple"),"time(s)")
else:
    print("'apple' is NOT on the list")
print("potato" in myList)
print(myList)
print(cmp([l2],[myList]))  #cmp only in py2, not in py3
l3.pop()
print("after pop:",l3)
l3.sort()
print("l3 after sort: ", l3)
l3.pop()
l3.remove(l3[0])
l3.reverse()
print("after pop, remove index 0, reverse:",l3)
l3.append(3)
print(l3)
l3.insert(1,16) #insert([index],[value])
print(l3)
l3.sort()
print("l3 after sort: ", l3)
print(mySet)
print(mySet | mySet2)
print(mySet & mySet2)
print(mySet - mySet2)
print(mySet ^ mySet2)
print(sorted(list(myD)))
print('Russian' not in myD)
#myD.fromkeys(2[,3])    #to figure out
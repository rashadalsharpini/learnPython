myList = ["rashad", "alsharpini", "abdElnaser"]
myAnotherList = [1, 2, 3, "ras", False]
# append
myList.append("alaa")
myList.append(True)
myList.append(myAnotherList)
print(myList[5][4])
# extend
myList.extend(myAnotherList)
print(myList)
# remove
myList.remove(myAnotherList)
print(myList)
# sort
# myList.sort()  # it has to be from one kind
# print(myList)
myAnotherList = [4, 2, 6, 8, 2, 1]
myAnotherList.sort(reverse=True)
print(myAnotherList)
myAnotherList = [4, 2, 6, 8, 2, 1]
myAnotherList.reverse()
print(myAnotherList)
# clear and copy
myCopyList = myAnotherList.copy()
myAnotherList.clear()
print(myAnotherList)
print(myCopyList)
# count and index and insert and pop
print(myCopyList.count(2))
print(myCopyList.index(6))
myCopyList.insert(0, 123)
print(myCopyList)
myCopyList.insert(-1, 4321)
print(myCopyList)
print(myCopyList.pop())
print(myCopyList)
print(myCopyList.pop(3))
print(myCopyList)

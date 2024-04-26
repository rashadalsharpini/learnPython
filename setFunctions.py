print("set Functions\n", "="*50)
# set not ordered, not indexed and can't be sliced
mySetOne = {"rashad", "alsharpini", 21}
print(mySetOne)  # every time print a different order
# mySetTwo = {"rashad", 100, 100.5, True, [1, 2, 3]}  # TypeError: unhashable type: 'list'
mySetTwo = {"rashad", 100, 100.5, True, (1, 2, 3)}
print(mySetTwo)
# items is unique
mySetThree = {"rashad", 100, 100.5, True, (1, 2, 3), 100, 2, 3, 2}
print(mySetThree)
# union and add
print(mySetOne | mySetTwo)
print(mySetOne.union(mySetTwo))
mySetThree.add(1234321)
print(mySetThree)
# copy remove clear
# discard if you give it an element that doesn't exist it won't give you and error
# unlike the remove you have to be sure that the element exists
mySetThree.discard(12341324)  # doesn't exist
mySetThree.discard(1234321)  # exist
print(mySetThree)
# pop in the set will pop a random element
print(mySetThree.pop())
# update
Test = {1, 2, 3, 4}
mySetThree.update(Test)
print(mySetThree)
print("="*50)
# difference
A = {1, 2, 3, 4, "rashad", "alsharpini"}
B = {1, 2, 3, 5}
print(A, "first time")
print(A.difference(B), "second time")  # A - B
print(A, "third time")
print("="*50)
# difference update
print(A, "first time")
print(A.difference(B), "second time")  # A - B
A.difference_update(B)
print(A, "third time")
print("="*50)
# intersection
e = {1, 2, 3, 4, 'x'}
f = {1, "rashad", 'x'}
print(e.intersection(f))
print(e & f)
print(e)
print("="*50)
# intersection update
e.intersection_update(f)
print(e)
# symmetric difference
i = {1, 2, 3, 4, 5, "x"}
j = {"osama", "zero", 1, 2, 4}
print(i.symmetric_difference(j))  # i ^j
print(i ^ j)
print(i, "sy")
# symmetric difference update
i.symmetric_difference_update(j)
print(i)
a = {1, 2, 3, 4}
b = {1, 2, 3}
print(a.issuperset(b))  # True
print(a.issubset(b))  # False
print(a.isdisjoint(b))  # False

from functions import *


forward(10)
print("\n")
backward(10)


num = int(input("\nenter the number :"))
for i in range(1, num + 1):
    print(i, end=' ')
    if i % 10 == 0:
        print("\n")

loopForward(num)
loopBackward(num)

s = input("\nenter the name : ")
print(s)
print(s[::-1])
firstName, lastName = splitString(s)
print(firstName, lastName)
print(firstName[::-1], lastName[::-1], end='')

# split
a = input("\nenter the value : ")
s = a.split()
print(s)

# center
e = "rashad"
print(e.center(9))
print(e.center(9, '-'))

# count
f = "I love python and cpp because cpp is fast and python is easy."
print(f.count("cpp"))

# swapCase
g = "I love Python and Cpp because Cpp is fast and Python is easy."
print(g.swapcase())

# startSwitch
h = "I love Python"
print(h.startswith('I'))
print(h.startswith('P', 7, 12))

# endSwitch
print(h.startswith('n'))
print(h.startswith('e', 2, 6))

# index
print(f.index("p"))
print(f.index("p", 0, 10))
# print(f.index("p", 0, 5))

# find
print(f.find('p'))
print(f.find('p', 0, 10))
print(f.find('p', 0, 5))

# rJust
print(e.rjust(10))
print(e.rjust(10, '#'))

# splitLines
es = """first line
second line
third line"""
print(es.splitlines())

# expandTabs
g = "Hello\tWorld\tI\tlove\tpython"
gg = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))

# isTitle
print(g.istitle())
print(gg.istitle())

# isLower isUpper
print(g.islower())
print(g.isupper())

# isIdentifier
seven = 'rashadAlsharpini'
eight = 'rashadAlsharpini100'
nine = 'Rashad--Alsharpini'

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

# isAlpha
print(seven.isalpha())
print(eight.isalpha())

# isalnum
print(seven.isalnum())
print(eight.isalnum())

# replace(oldValue, NewValue, Count)
test = "Hello One Two Three One One"
print(test.replace("One", '1'))
print(test.replace("One", '1', 1))

# join(iterable)
myList = ["rashad", "alsharpini", "abdElnaser"]
print("-".join(myList))


# old way
name = "rashad"
age = 20
# %s string
# %d number
# %f float
print("my name is %s and my age is %d" % (name, age))

myNumber = 6
print("my number is %f" % myNumber)
print("my number is %.2f" % myNumber)

# new way
print("My name is: {}".format(name))
print("My name is: {:s} and my age is: {:.2f}".format(name, age))

myMoney = 134134134124124531
print("my money in the bank is:{:,d}".format(myMoney))
print("my money in the bank is:{:_d}".format(myMoney))
print("my money in the bank is:{:d}".format(myMoney))

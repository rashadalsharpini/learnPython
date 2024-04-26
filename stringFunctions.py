print("string Functions\n", "="*50)
# split
a = input("\nenter the value : ")
s = a.split()
print(s)
print("="*50)

# center
e = "rashad"
print(e.center(9))
print(e.center(9, '-'))
print("="*50)
print("test")
# count
f = "I love python and cpp because cpp is fast and python is easy."
print(f.count("cpp"))
print("="*50)

# swapCase
g = "I love Python and Cpp because Cpp is fast and Python is easy."
print(g.swapcase())
print("="*50)

# startSwitch
h = "I love Python"
print(h.startswith('I'))
print(h.startswith('P', 7, 12))
print("="*50)

# endSwitch
print(h.startswith('n'))
print(h.startswith('e', 2, 6))
print("="*50)

# index
print(f.index("p"))
print(f.index("p", 0, 10))
# print(f.index("p", 0, 5))
print("="*50)

# find
print(f.find('p'))
print(f.find('p', 0, 10))
print(f.find('p', 0, 5))
print("="*50)

# rJust
print(e.rjust(10))
print(e.rjust(10, '#'))
print("="*50)

# splitLines
es = """first line
second line
third line"""
print(es.splitlines())
print("="*50)

# expandTabs
g = "Hello\tWorld\tI\tlove\tpython"
gg = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))
print("="*50)

# isTitle
print(g.istitle())
print(gg.istitle())
print("="*50)

# isLower isUpper
print(g.islower())
print(g.isupper())
print("="*50)

# isIdentifier
seven = 'rashadAlsharpini'
eight = 'rashadAlsharpini100'
nine = 'Rashad--Alsharpini'
print("="*50)

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())
print("="*50)

# isAlpha
print(seven.isalpha())
print(eight.isalpha())

# isalnum
print(seven.isalnum())
print(eight.isalnum())
print("="*50)

# replace(oldValue, NewValue, Count)
test = "Hello One Two Three One One"
print(test.replace("One", '1'))
print(test.replace("One", '1', 1))
print("="*50)

# join(iterable)
myList = ["rashad", "alsharpini", "abdElnaser"]
print("-".join(myList))

print("="*50)

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
print("my money in the bank is:{:d}".format(myMoney))
print(f"my name is {name} and my age is {age:.2f}")
print("="*50)

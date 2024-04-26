def forward(n):
    if n > 0:
        forward(n - 1)
        print(n, end=' ')


def backward(n):
    if n > 0:
        print(n, end=' ')
        backward(n - 1)


def loopBackward(n):
    if n > 0:
        for j in range(n):
            print(j, end=' ')
        print("\n")
        loopBackward(n - 1)


def loopForward(n):
    if n > 0:
        loopForward(n - 1)
        for j in range(n):
            print(j, end=' ')
        print("\n")


def splitString(s):
    index = 0
    for i in range(len(s)):
        if s[i] == ' ':
            index = i
            break
    firstName, lastName = s[:index], s[index + 1:]
    return firstName, lastName


print("recursion Functions\n", "="*50)

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
print("="*50)
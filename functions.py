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

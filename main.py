import functions

functions.forward(10)
print("\n")
functions.backward(10)


num = int(input("\nenter the number :"))
for i in range(1, num + 1):
    print(i, end=' ')
    if i % 10 == 0:
        print("\n")

functions.loopForward(num)
functions.loopBackward(num)

s = input("\nenter the name : ")
print(s)
print(s[::-1])
index = 0
for i in range(len(s)):
    if s[i] == ' ':
        index = i
        break
firstName = s[:index]
lastName = s[index+1:]
print(firstName, lastName)
print(firstName[::-1], lastName[::-1], end='')

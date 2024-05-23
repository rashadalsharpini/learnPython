# tuple
# pairs
def pair():
    pairsList = []
    # Getting pairs from the user
    for _ in range(int(input())):
        pairsList.append(tuple(input().split()))
    # Accessing elements of the list of pairs
    return pairsList


pairs_list = pair()
print(pairs_list)

print("pairs how to enter them and print them")
pairs_list = []

# Getting pairs from the user
for _ in range(int(input("enter the number of pairs: "))):
    pairs_list.append(tuple(input(f"enter the pair {_ + 1} : ").split()))

# Accessing elements of the list of pairs
for pair in pairs_list:
    print(*pair)

# list

pairList = []
for _ in range(int(input())):
    pair = list(input().split())
    pair[0] = int(pair[0])
    pairList.append(pair)
print(pairList)

import queue

myQueue = queue.Queue()
for _ in range(int(input())):
    myQueue.put(input())
while not myQueue.empty():
    print(myQueue.get())
# print("first")
# for i in range(myQueue.qsize()):
#     print(myQueue.get()) 
# error it will return the first element

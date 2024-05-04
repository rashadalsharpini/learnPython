# pairs
print("pairs how to enter them and print them")
pairs_list = []

# Getting pairs from the user
for _ in range(int(input("enter the number of pairs: "))):
    pairs_list.append(tuple(input(f"enter the pair {_ + 1} : ").split()))

# Accessing elements of the list of pairs
for pair in pairs_list:
    print(*pair)

# can't repeat the key
user = {
    "name": "rashad",
    "age": 12,
    "country": "egypt",
    "test": [1, 2, 3],
    (1, 2, 3): [1, 2, 3],
    (1, 2, 3): "test",
}
print(user)
print(user["age"])  # they both do the same job but this will
print(user.get("age"))  # return error if the key doesn't exist
languages = {
    "One": {
        "name": "cpp",
        "progress": "80%"
    },
    "Two": {
        "name": "python",
        "progress": "90%"
    },
    "Three": {
        "name": "java",
        "progress": "85%"
    }
}
print(languages)
print(languages.keys())
print(languages.values())
print(languages["One"])
print(languages["Three"]["name"])
print(len(languages))
print(len(languages["Two"]))
frameWorkOne = {
    "name": "keys",
    "progress": "80%"
}
frameWorkTwo = {
    "name": "Reactjs",
    "progress": "80%"
}
frameWorkThree = {
    "name": "Angular",
    "progress": "80%"
}
allFrameWork = {
    "one": frameWorkOne,
    "two": frameWorkTwo,
    "three": frameWorkThree
}
# clear update copy
member = {
    "name": "rashad"
}
member["age"] = 20
print(member)
member.update({"country": "egypt"})
print(member)

# set default and pop item
print(member.setdefault("name", "yousef"))
print(member.setdefault("test", "yousef"))
print(member)
print(member.popitem())
print(member)
allItems = member.items()
member["shit"] = "fuck"
print(allItems)
a = ("one", 'two', "three")
b = "x"
print(dict.fromkeys(a, b))

mySkills = {
    "html": {
        "main": "80%",
        "sub": "80%",
    },
    'css': {
        "main": "90%",
        "sass": "90%",
    }
}
for main_key, main_value in mySkills.items():
    for sub_key, sub_value in mySkills.items():
        print(main_key, sub_key, main_value, sub_value)


# cnt = dict()
triplet = (1, 2, 3)
test = [tuple()] * 3
test[0] = (0, 2, 3)
test[1] = (1, 0, 3)
test[2] = (1, 2, 0)
ans = 0
cnt = {
    test[0]: 'rashad',
    test[1]: 'yousef',
    test[2]: 'sayd'
}
# print(test)
for trip in test:
    print(cnt.get(trip, 0))  # the second argument is returned if the key doesn't exist
print(cnt)

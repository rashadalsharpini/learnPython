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
print(user["age"])
print(user.get("age"))
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
    "name": "Vuejs",
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

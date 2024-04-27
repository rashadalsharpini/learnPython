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
print(languages["One"])
print(languages["Three"]["name"])

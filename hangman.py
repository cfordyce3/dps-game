from random import choice

words = ["here", "are", "some", "words"]

test = True

while input("> ") != "n":
    print(choice(words))

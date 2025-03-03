from random import choice

words = ["here", "are", "some", "words", "again", "before"]

test = True

while input("> ") != "n":
    print(choice(words))

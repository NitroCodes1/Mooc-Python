word = str(input("Please type in a string:"))

if len(word) < 21:
    length = 20 - len(word)
    print(length * "*" + word)
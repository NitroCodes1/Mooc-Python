word = str(input("Please type in a word"))
letter = str(input("Please type in a character:"))
index = 0
length = len(word)

while letter in word:
    pos = word.find(letter)
    index += pos
    if length > pos+3:
        print(word[pos:pos+3])
    break

story = ""
currentWord = ""

while True:
    word = str(input("Please type in a word:"))
    if word == "end":
        break
    
    if word == currentWord:
        break

    else:
        story += word + " "
        currentWord = word

print(story)



       

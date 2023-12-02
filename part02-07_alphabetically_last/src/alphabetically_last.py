word = str(input("Please type in the 1st word:"))
word2 = str(input("Please type in the 2nd word:"))

if word > word2:
    print(f"{word} comes alpabetically last")

elif word2 > word:
    print(f"{word2} comes alpabetically last")

else:
    print("You gave the same word twice")
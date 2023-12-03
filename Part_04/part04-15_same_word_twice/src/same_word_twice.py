# Write your solution here
my_list = []

word = str(input("Word:"))
while True:
    my_list.append(word)
    word = str(input("Word:"))
    if word in my_list:
        break
print(f"You typed in {len(my_list)} different words")

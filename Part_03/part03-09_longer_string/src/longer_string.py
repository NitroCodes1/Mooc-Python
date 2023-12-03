first = str(input("Please type in string 1:"))
second = str(input("Please type in string 2:"))

if len(first) > len(second):
    print(f"{first} is longer")

elif len(first) < len(second):
    print(f"{second} is longer")

else:
    print("The strings are equally long")
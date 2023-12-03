print("Are you ready?")
number = int(input("Please type in a number:"))
print(number)
newnumber = ""
while number > 1:
    newnumber = number - 1
    number = newnumber
    print(number)

print ("Now!")
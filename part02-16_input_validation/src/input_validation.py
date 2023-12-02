from math import sqrt

while True:
    number = int(input("Please type in a number"))
    if number < 0:
        print("Invalid number")
        number = int(input("Please type in a number"))
    if number == 0:
        break
    print(sqrt(number))

print("Exiting...")
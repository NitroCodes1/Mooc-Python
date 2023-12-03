upper = int(input("Upper limit:"))
base = int(input("Base:"))
number = 1
print(number)
while number < upper:
    number = number * base
    if number <= upper:
        print(number)
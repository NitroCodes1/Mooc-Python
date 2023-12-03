limit = int(input("Limit: "))
number = 1 
total = 1 
consecutive = "The consecutive sum: "
statement = "" 
while total < limit: 
    statement += f"{number} + "
    number += 1 
    total += number 
print(f"{consecutive} {statement}" + f"{number} = {total}")
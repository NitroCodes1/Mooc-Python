
my_list = []
number_items = int(input("How many items:"))
i = 0

while i < number_items:
    value = int(input(f"Item {i+1}:"))
    my_list.append(value)
    i += 1
    
if i == number_items:
    print(my_list)
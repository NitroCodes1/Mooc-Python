my_list = []
while True:
    new_item = int(input("New item:"))
    if new_item == 0:
        print("Bye!")
        break
    
    else:
       my_list.append(new_item)
       in_order = sorted(my_list)
       print(f"The list now: {my_list}")
       print(f"The list in order: {in_order}") 

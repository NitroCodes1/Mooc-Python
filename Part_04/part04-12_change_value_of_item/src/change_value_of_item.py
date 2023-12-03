my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index:"))
    if index == -1:
        break
    if 0 <= len(my_list):
        new_value = int(input("New Value:"))
        my_list[index] = new_value
        print(my_list)
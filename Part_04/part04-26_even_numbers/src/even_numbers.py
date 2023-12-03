def even_numbers(my_list):
    my_list = [i for i in my_list if i % 2  == 0]
    print(my_list)
    return my_list
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)

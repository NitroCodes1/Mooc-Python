def list_of_stars(my_list):
        for item in my_list:
            print(item*"*")
if __name__ == "__main__":
    my_list = [7, 7, 1, 1, 2]
    result = list_of_stars(my_list)
    
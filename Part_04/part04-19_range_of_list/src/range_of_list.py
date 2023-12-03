def range_of_list(my_list):
    minimum = min(my_list)
    maximum = max(my_list)
    return maximum - minimum

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
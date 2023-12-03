def sum_of_positives(my_list):
    my_list = [i for i in my_list if i >= 0]
    addition = sum(my_list)
    return addition

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
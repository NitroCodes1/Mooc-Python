def formatted(list: list):
    new_list = []
    for number in list:
        new_list.append(f"{number:.2f}")
    print(new_list)
    return new_list
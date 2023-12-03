def all_the_longest(my_list: list):
    best = [""]
    for item in my_list:
        if len(item) > len(best[0]):
            best.clear()
            best.append(item)
        elif len(item) == len(best[0]):
            best.append(item)
    print(best)
    return best


if __name__ == "__main__":
    all_the_longest(("adele", "mark", "dorothy", "tim", "hedy", "richard"))
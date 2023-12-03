def distinct_numbers(list):
    distinct = []
    for number in list:
        if distinct.count(number) <= 0:
            distinct.append(number)
    print(sorted(distinct))
    return sorted(distinct)


if __name__ == "__main__":
    distinct_numbers([1, 2, 3, 5, 6, 7, 7, 7,7 ])
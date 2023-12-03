def list_sum(a, b):
    result = []  # Create an empty list to store the sum of corresponding elements
    for i in range(len(a)):
        result.append(a[i] + b[i])  # Add corresponding elements and append to the result list

    print(result)
    return result

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    list_sum(a, b)
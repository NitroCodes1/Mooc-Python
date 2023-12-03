def line(a:int, b:str):
    if b == "":
        b = "*"
    print(a*b[0])

def square_of_hashes(size):
    height = 0
    while height < size:
        line(size, "#")
        height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)

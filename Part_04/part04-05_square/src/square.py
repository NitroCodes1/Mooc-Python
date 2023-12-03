def line(a:int, b:str):
    if b == "":
        b = "*"
    print(a*b[0])

def square(size, character):
        i = 1
        while i <= size:
            line(size, character)
            i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
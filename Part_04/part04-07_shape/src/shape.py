def line(a:int, b:str):
    if b == "":
        b = "*"
    print(a*str(b)[0])

def shape(size1, character1, size2, character2):
    i = 1
    while i <= size1:
        line(i, character1)
        i += 1
    i = 1
    while i <= size2:
        line(size1, character2)
        i += 1

if __name__ == "__main__":
    shape(5, "x", 2, "o")
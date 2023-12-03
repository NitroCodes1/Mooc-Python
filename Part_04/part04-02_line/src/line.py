def line(a:int, b:str):
    if b == "":
        b = "*"
    print(a*b[0])
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")
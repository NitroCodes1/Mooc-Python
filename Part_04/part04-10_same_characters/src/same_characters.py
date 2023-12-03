def same_chars(input_string, index1, index2):
    if 0 <= index1 <len(input_string) and 0 <= index2 < len (input_string):
        if input_string[index1] == input_string[index2]:
            return True
        else:
            return False
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
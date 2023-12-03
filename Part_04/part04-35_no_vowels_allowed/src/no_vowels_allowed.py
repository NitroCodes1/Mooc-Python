def no_vowels(string: str):
    vowels = ["a", "e", "i", "o", "u"]
    my_string = ""
    for character in string:
        if character not in vowels:
            my_string += character
    return my_string


if __name__ == "__main__":
    my_string = "I am learning Python"
    print(no_vowels(my_string))
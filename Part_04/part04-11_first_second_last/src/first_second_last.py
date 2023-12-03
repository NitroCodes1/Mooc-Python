# Write your solution here
def first_word(sentence):
    full = sentence.split()
    first = full[0]
    return first
def second_word(sentence):
    full = sentence.split()
    second = full[1]
    return second
def last_word(sentence):
    full = sentence.split()
    last = full[-1]
    return last
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
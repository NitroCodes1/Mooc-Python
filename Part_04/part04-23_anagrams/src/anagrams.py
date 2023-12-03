def anagrams(string1, string2):
    unpack1 = [*string1]
    unpack2 = [*string2]
    sort1 = unpack1.sort()
    sort2 = unpack2.sort()
    if unpack1 == unpack2:
        return True
    else:
        return False
if __name__ == "__main__":
    string1 = "hgtrhrthr"
    string2 = "qwertrewtweyjfduo"
    result = anagrams(string1, string2)
    print(result)    
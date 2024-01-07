def is_isogram(string):
    string = string.upper().replace(" ", "")
    for char in string:
        if char == "-":
            continue
        occurences = [i for i, letter in enumerate(string) if letter == char]
        if len(occurences) > 1:
            return False
    return True

def rotate(text, key):
    new_text = ""
    for char in text:
        if char in " 123',!.":
            asc = ord(char)
        else:
            asc = ord(char)
            asc += key
            if char.isupper() and asc > 90:
                asc -= 26
            if asc > 122:
                asc -= 26

        new_text += chr(asc)
    return new_text
print(ord("Z"))
print(rotate("The quick brown fox jumps over the lazy dog.", 13))

def is_valid(isbn):
    if len(isbn) < 10:
        return False
    isbn = isbn.replace("-", "")
    check = []
    if len(isbn) > 10:
        return False
    for i, char in enumerate(isbn):
        if i == 9 and char in 'Xx':
            check.append(10)
        elif char not in '1234567890':
            return False
        else:
            check.append(int(char))
    val = (check[0] * 10 + check[1] * 9 + check[2] * 8 + check[3] * 7 + check[4] * 6 + check[5] * 5 + check[6] * 4 + check[7] * 3 + check[8] * 2 + check[9] * 1) % 11
    
    if val == 0:
        return True
    return False

print(is_valid('3-598-2X507-9'))

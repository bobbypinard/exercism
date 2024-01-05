def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    listy = []
    for i, digit in enumerate(digits):
        listy.append(digit ** len(digits))
    if sum(listy) == number:
        return True
    else:
        return False

print(is_armstrong_number(154))

def convert(number):
    fizzbuzz = ""

    if number % 3 == 0:
        fizzbuzz = "Pling"
    if number % 5 == 0:
        fizzbuzz += "Plang"
    if number % 7 == 0:
        fizzbuzz += "Plong"
    if fizzbuzz == "":
        return str(number)
    return fizzbuzz

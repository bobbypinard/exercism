def score(x, y):
    coordinates = sorted([abs(x), abs(y)])
    
    if coordinates[1] > 10:
        return 0
    elif coordinates[1]  > 5:
        return 1
    elif coordinates[1] > 1:
        return 5
    else:
        return 10

print(score(-9, 9))

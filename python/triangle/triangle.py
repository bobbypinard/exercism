def equilateral(sides):
    if not is_triangle(sides):
        return False
    if sides[0] == sides[1] == sides[2]:
        return True
    else:
        return False
    return


def isosceles(sides):
    if not is_triangle(sides):
        return False
    sides = sorted(sides)
    if sides[0] + sides[1] <= sides[2]:
        return False
    else:
        return sides[0] == sides[1] or sides[1] == sides[2]


def scalene(sides):
    if not is_triangle(sides):
        return False
    sides = sorted(sides)
    if sides[0] != sides[1] != sides[2]:
        return True
    else:
        return False

def is_triangle(sides):
    for side in sides:
        if side <= 0 or side >= sum(sides) - side:
            return False
        else:
            return True

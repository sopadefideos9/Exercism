def equilateral(sides):
    a, b, c = sides
    return a > 0 and a == b == c


def isosceles(sides):
    a, b, c = sides
    if a + b >= c and a + c >= b and b + c >= a: 
        if a <= 0 or b <= 0 or c <= 0:
            return False
        if a == b or a == c or b == c:
            return True
    return False


def scalene(sides):
    a, b, c = sides
    if a + b >= c and a + c >= b and b + c >= a: 
        if a <= 0 or b <= 0 or c <= 0:
            return False
        if a == b or a == c or b == c:
            return False
        return True
    return False

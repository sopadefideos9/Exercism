"""Checking types of triangles"""

def equilateral(sides):
    """An equilateral triangle has all three sides the same length."""
    sidea, sideb, sidec = sides
    return sidea > 0 and sidea == sideb == sidec


def isosceles(sides):
    """An isosceles triangle has at least two sides the same length."""
    sidea, sideb, sidec = sides
    if sidea + sideb >= sidec and sidea + sidec >= sideb and sideb + sidec >= sidea: 
        if sidea <= 0 or sideb <= 0 or sidec <= 0:
            return False
        if sidea == sideb or sidea == sidec or sideb == sidec:
            return True
    return False


def scalene(sides):
    """A scalene triangle has all sides of different lengths."""
    sidea, sideb, sidec = sides
    if sidea + sideb >= sidec and sidea + sidec >= sideb and sideb + sidec >= sidea: 
        if sidea <= 0 or sideb <= 0 or sidec <= 0:
            return False
        if sidea == sideb or sidea == sidec or sideb == sidec:
            return False
        return True
    return False

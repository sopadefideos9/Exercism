def equilateral(sides):
    sidea, sideb, sidec = sides
    return sidea > 0 and sidea == sideb == sidec


def isosceles(sides):
    sidea, sideb, sidec = sides
    if sidea + sideb >= sidec and sidea + sidec >= sideb and sideb + sidec >= sidea: 
        if sidea <= 0 or sideb <= 0 or sidec <= 0:
            return False
        if sidea == sideb or sidea == sidec or sideb == sidec:
            return True
    return False


def scalene(sides):
    sidea, sideb, sidec = sides
    if sidea + sideb >= sidec and sidea + sidec >= sideb and sideb + sidec >= sidea: 
        if sidea <= 0 or sideb <= 0 or sidec <= 0:
            return False
        if sidea == sideb or sidea == sidec or sideb == sidec:
            return False
        return True
    return False

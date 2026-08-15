def leap_year(year):
    fourth_of_year = year // 4
    forhunof_year = year // 400
    hundrof_year = year // 100
    if fourth_of_year * 4 == year and hundrof_year * 100 != year:
        return True
    elif  fourth_of_year * 4 == year and hundrof_year * 100 == year:
        if forhunof_year * 400 == year:
            return True
    return False


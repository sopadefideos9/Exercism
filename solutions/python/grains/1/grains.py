def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grain_in_square = 2 ** (number - 1)
        
    return grain_in_square
        


def total():
    return sum(square(number) for number in range(1, 65))

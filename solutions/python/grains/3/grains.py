"""the number of grains on a given square"""
def square(number):
    """the number of grains on a given square"""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grain_in_square = 2 ** (number - 1)
        
    return grain_in_square
        

"""the total number of grains on the chessboard"""
def total():
    """the total number of grains on the chessboard"""
    return sum(square(number) for number in range(1, 65))

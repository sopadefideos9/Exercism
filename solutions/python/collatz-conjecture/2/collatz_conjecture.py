def steps(number):
    """Definition that return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture."""
    numb_steps = 0
    if number == 0 or number <=0:
        raise ValueError("Only positive integers are allowed")
        
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        numb_steps += 1
    return numb_steps

# 1. 
def number_staircase(start, end, increment):
    """
    prints numbers in descending order from start to end by increment
    Use: number_staircase(start, end, increment)

    Parameters:
        start (int) - starting number
        end (int) - ending number
        increment (int) - number to increment by

        start > end
    """
    for i in range(start, end, -increment):
        print(i)

# 2. 
def calculate_factorial(target):
    """
    calculates the factorial of a number (target!)
    Use: factorial = calculate_factorial(target)

    Parameters:
        target (int) - number to calculate factorial of
    
    Returns:
        factorial (int) - target!
    """
    factorial = 1
    for i in range(1, target):
        factorial *= i
    return factorial
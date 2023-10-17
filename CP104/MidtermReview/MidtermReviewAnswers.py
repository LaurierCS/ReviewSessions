#1. 
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
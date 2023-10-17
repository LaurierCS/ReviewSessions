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

# 3.
def format_bio(name, age):
    """
    returns a string in the following format Hi, my name is name and I am age years (rounded to 2 decimal places) old.
    Use: bio = format_bio(name, age)

    Parameters:
        name (string) - name of the person
        age (int) - age of the person in months
    
    Returns:
        bio (string) - formatted bio
    """
    age_years = age / 12
    bio = f"Hi, my name is {name} and I am {age_years:.2f} years old."
    return bio

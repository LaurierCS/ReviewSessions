# 1. Docstrings

def add(num1, num2):
    """
    adds two numbers together and prints the results
    Use: add(num1, num2)
    --------------------------------------------------
    Parameters:
        num1 (int): The first number
        num2 (int): The second number
    
    Returns:
        num3 (int): The sum of num1 and num2
    --------------------------------------------------
    """
    num3 = num1 + num2
    print(num3)


def calc_angles(side_a, side_b, side_c):
    """
    calculates angles of a triangle given the lengths of its sides
    Use: angle_a, angle_b, angle_c = calc_angles(side_a, side_b, side_c)
    --------------------------------------------------
    Parameters:
        side_a (float): The length of side a
        side_b (float)): The length of side b
        side_c (float): The length of side c
        side_c < side_a + side_b
    
    Returns:
        angle_a (float): The angle opposite side a
        angle_b (float): The angle opposite side b
        angle_c (float): The angle opposite side c
    --------------------------------------------------
    """

# 2. Decisions
statement1 = True
statement2 = True
if statement1:
    print("I love LCS")
elif statement2:
    print("Python is cool")
else:
    print("L")

# 3
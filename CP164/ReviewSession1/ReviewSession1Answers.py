from ReviewSession1Content import Stack, Queue
# 1. 
# Create a point class, the class should have two attributes, position and distance from origin
# Include the __str__ method as well as a method to calculate the euclidean distance from one point to another

class Point:
    def __init__(self, x, y):
        self.position = (x, y)
        self.distance = (x**2 + y**2)**0.5
    
    def __str__(self):
        return str(self.position)
    
    def calculate_distance(self, other):
        return ((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)**0.5

# 2.
def evaluate_expression(postfix_expr: str) -> int:
    """
    -------------------------------------------------------
    Evaluates a postfix arithmetic expression using a stack.
    Use: result = evaluate_expression(postfix_expr)
    -------------------------------------------------------
    Parameters:
        postfix_expr - a string containing a postfix arithmetic expression (str)
    Returns:
        result - the result of the expression evaluation (int)
    -------------------------------------------------------
    """
    stack = Stack()
    for i in postfix_expr:
        if i.isdigit():
            stack.push(int(i))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if i == "+":
                result = operand1 + operand2
            elif i == "-":
                result = operand1 - operand2
            elif i == "*":
                result = operand1 * operand2
            elif i == "/":
                result = operand1 / operand2
            stack.push(result)
    return stack.pop()
# 1.
def calcDistance(speed, time):
    """
    -------------------------------------------------------
    calculates the distance an object travels
    Use: distance = calcDistance(speed, time)
    -------------------------------------------------------
    Parameters:
        speed (float): speed the object is going
        time (float): time the object travels
        time > 0
    Returns:
        distance (float): distance the object travels    
    -------------------------------------------------------
    """
    return speed * time

# 2. 
def addFraction(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction sum.
    Use: num, den, sum = addFraction(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of sum (int)
        den - denominator of sum (int)
        sum - num / den (float)
    -------------------------------------------------------
    """
    num = num1 * den2 + num2 * den1
    den = den1 * den2
    sum = num / den
    return num, den, sum

# 3.
def bulkOrder(quantity, price):
    """
    -------------------------------------------------------
    Calculates and returns the total cost of a bulk order.
    If you order less than 5 items you must pay full price
    If you order between 5 and 10 items you get a 10% discount
    If you order more than 10 items you get a 20% discount
    Use: total = bulkOrder(quantity, price)
    -------------------------------------------------------
    Parameters:
        quantity - number of items ordered (int > 0)
        price - price per item (float > 0)
    Returns:
        total - total cost of the order (float)
    --------
    """
    if quantity < 5:
        total = quantity * price
    elif quantity >= 5 and quantity <= 10:
        total = quantity * price * 0.9
    elif quantity > 10:
        total = quantity * price * 0.8
    return total

# 4. 
def checkNumber(num):
    """
    -------------------------------------------------------
    Returns a string based on the value of num
    Use: result = checkNumber(num)
    Parameters:
        num (int): number to check
    Returns:
        result (str): string based on value of num
    -------------------------------------------------------
    """
    if num >= 50 and num%2 == 0:
        result = "thats a really big even number!"
    elif num >= 50 and num%2 != 0:
        result = "thats a really big odd number!"
    elif num < 50 and num%2 == 0:
        result = "thats a small even number!"
    elif num < 50 and num%2 != 0:
        result = "thats a small odd number!"
    return result
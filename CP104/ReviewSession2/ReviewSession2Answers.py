# 1.
def calcDistance(speed, time):
    """
    Calculates the distance travelled given the speed and time travelled
    Use: distance = calcDistance(speed, time)
    Parameters:
        speed (float): speed travelled in km/h
        time (float): time travelled in hours

    Returns:
        float: distance travelled in km
    """
    return speed * time

# 2. 
def add_fraction(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = add_fraction(num1, den1, num2, den2)
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
    --------
    """
    num = num1 * den2 + num2 * den1
    den = den1 * den2
    sum = num / den
    return num, den, sum

# 3. 
def check_number(num):
    """
    -------------------------------------------------------
    Returns a string based on the value of num
    Use: result = check_number(num)
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
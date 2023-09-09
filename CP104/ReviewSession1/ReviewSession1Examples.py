# 1.  print the following using an f string: |    12345| |     123.45| |        Hi There|


# 2.  write a docstring for the following function: 
def calcDistance(speed, time):
    return speed * time

def calcDistance(speed, time):
    """Calculates the distance travelled given the speed and time travelled

    Args:
        speed (float): speed travelled in km/h
        time (float): time travelled in hours

    Returns:
        float: distance travelled in km
    """
    return speed * time
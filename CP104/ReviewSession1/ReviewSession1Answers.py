# 1. 
print(f"|{12345:>10d}| |{123.45:>10.2f}| |{'Hi There':>10s}|")

# 2.
def calcDistance(speed, time):
    """Calculates the distance travelled given the speed and time travelled

    Parameters:
        speed (float): speed travelled in km/h
        time (float): time travelled in hours

    Returns:
        float: distance travelled in km
    """
    return speed * time
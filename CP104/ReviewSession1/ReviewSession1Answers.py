# 1. 
print(f"|{12345:>10d}| |{123.45:>10.2f}| |{'Hi There':>10s}|")



# 3. 
def formatTime(hour, minute):
    """Formats the hour and minute into an analog clock time

    Parameters:
        hour (int): hour of the day
        minute (int): minute of the hour

    Returns:
        string: analog clock time
    """
    return f"{hour:02d}:{minute:02d}"
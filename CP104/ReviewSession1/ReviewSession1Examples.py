# 1.  print the following using an f string: |    12345| |    123.456| |        Hi There|


# 2. align the following words as follows (each line has 10 characters): 
# left******
# **middle**
# *****right

# 3. write a function that takes an hour and minute and returns a formatted analog clock time
#    e.g. 1, 30 -> 01:30
#    e.g. 12, 5 -> 12:05

def formatTime(hour, minute):
    """Formats the hour and minute into an analog clock time

    Parameters:
        hour (int): hour of the day
        minute (int): minute of the hour

    Returns:
        string: analog clock time
    """
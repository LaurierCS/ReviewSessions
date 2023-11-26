# 1.
def parse_log(file_handle):
    """
    Parses a log file and counts the number of error and warning messages.
    Use: error_count, warning_count = parse_log(file_handle)
    Parameters:
        file_handle - log file to process (file - open for reading)
    Returns:
        error_count - number of error messages in the log (int)
        error_list - list of error messages in the log (list)
        warning_count - number of warning messages in the log (int)
        warning_list - list of warning messages in the log (list)

    """    
    error_count = 0
    error_list = []
    warning_count = 0
    warning_list = []
    line = file_handle.readline().strip()
    while line != "":
        fields = line.split(":")
        if fields[0] == "ERROR":
            error_count += 1
            error_list.append(fields[1].strip())
        elif fields[0] == "WARNING":
            warning_count += 1
            warning_list.append(fields[1].strip())
        line = file_handle.readline().strip()

    return error_count, error_list, warning_count, warning_list

# 2. 
def vowel_string():
    """
    Gets a string of vowels from the user.
    Consonants are ignored. Enter a blank line to stop.
    Use: vowel_string = vowel_string()
    Returns:
        vowel_string - string of vowels entered by the user (str)
    """
    vowel_string = ""
    vowel = input("Enter a vowel: ")
    while vowel != "":
        if vowel in "aeiouAEIOU":
            vowel_string += vowel
        vowel = input("Enter a vowel: ")
    return vowel_string

# 3.
def two_sum(target, list):
    """
    Finds the first pair of numbers in a list that add up to a target value.
    Use: index1, index2 = two_sum(target, list)
    Parameters:
        target - target value (int)
        list - list of values (list)
    Returns:
        index1 - index of first number in the pair (int)
        index2 - index of second number in the pair (int)
    """
    index1 = 0
    index2 = 1
    for index1 in range(len(list)):
        for index2 in range(index1+1, len(list)):
            if list[index1] + list[index2] == target:
                return index1, index2

# 4.
def longest_alliteration(list):
    """
    Finds the longest series of consecutive words that start with the same letter.
    Use: longest = longest_alliteration(list)
    Parameters:
        list - list of words (list)
    Returns:
        longest - longest series of consecutive words that start with the same letter (str)
    """
    longest = ""
    current_longest = ""
    last_letter = ""
    for i in range(len(list)):
        if list[i][0] == last_letter:
            current_longest += " " + list[i]
        elif last_letter == "":
            current_longest = list[i]
            last_letter = list[i][0]
        else:
            if len(current_longest) > len(longest):
                longest = current_longest
            current_longest = list[i]
            last_letter = list[i][0]
    
    if len(current_longest) > len(longest):
        longest = current_longest
    return longest

def add_time_stamps(file_read, file_write, time_stamps):
    """
    Adds time stamps to a file.
    Use: add_time_stamps(file_read, file_write, time_stamps)
    Parameters:
        file_read - file to add time stamps to (file - open for reading)
        file_write - file to write to (file - open for writing)
        time_stamps - list of time stamps to add (list)
    """
    line = file_read.readline().strip()
    while line != "":
        date_line = line + " " + f"[{time_stamps.pop(0)}]" + "\n"
        file_write.write(date_line)
        line = file_read.readline().strip()
    
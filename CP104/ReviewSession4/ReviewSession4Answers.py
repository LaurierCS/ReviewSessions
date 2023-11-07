# 1. Implement the following function
def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a string that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 (str) - a string
        source2 (str) - a string
    Returns:
        target (str) - the union of source1 and source2
    -------------------------------------------------------
    """
    target = ""
    for char in source1:
        if char not in target:
            target += char
    
    for char in source2:
        if char not in target:
            target += char
    
    return target

# 2.
def find_range_median(numbers):
    """
    -------------------------------------------------------
    Returns the range and median of a list of numbers.
    Use: range_value, median_value = find_range_median(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list of float)
    Returns:
        range_value - the difference between the largest and smallest numbers (float)
        median_value - the median number in the list (float)
    -------------------------------------------------------
    """
    numbers.sort()
    range_value = numbers[-1] - numbers[0] # max(numbers) - min(numbers)
    
    if len(numbers) % 2 == 0:
        median_value = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        median_value = numbers[len(numbers) // 2]
    
    return range_value, median_value

# 3. 
def convert_to_title_case(sentence):
    """
    -------------------------------------------------------
    Converts a string to title case, where the first letter of each
    word is capitalized and all other letters are lowercase.
    Use: title_case_sentence = convert_to_title_case(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - a string to be converted (str)
    Returns:
        title_case_sentence - the converted string in title case (str)
    -------------------------------------------------------
    """
    title_case_sentence = ""
    sentence_list = sentence.lower().split()
    for word in sentence_list:
        title_case_sentence += word[0].upper() + word[1:].lower() + " "
    
    return title_case_sentence.strip()
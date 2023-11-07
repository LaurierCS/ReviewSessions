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
    
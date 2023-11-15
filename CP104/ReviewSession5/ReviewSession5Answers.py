# 1.

def customer_by_name(fh, name):
    """
    -------------------------------------------------------
    Find the record for a given customer name in a sequential file.
    Use: result = customer_by_name(fh, name)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        name - the name to match (str)
    Returns:
        result - the record with the given name if it exists,
            an empty str otherwise (str)
    -------------------------------------------------------
    """
    result = ""
    line = fh.readline().strip()
    while line != "":
        line = line.strip()
        fields = line.split(",")
        if fields[1] + " " + fields[2] == name:
            result = line
        line = fh.readline().strip()
    return result

# 2.
def filter_by_year(fh, year):
    """
    -------------------------------------------------------
    Find all customer transactions in a given year
    Use: results = filter_by_year(fh, year)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        year - the year to filter records by (int)
    Returns:
        results - list of records that match the year (list of str)
    -------------------------------------------------------
    """
    results = []
    line = fh.readline().strip()
    while line != "":
        fields = line.split(",")
        date = fields[4]
        curr_year = date.split("-")[0]
        if int(curr_year) == year:
            results.append(line)
        line = fh.readline().strip()
    return results

# 3.
def diagonal_sum(matrix):
    """
    -------------------------------------------------------
    Calculates the sum of the diagonal elements of a square matrix.
    Use: sum = diagonal_sum(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D square list (2D list of float/int)
    Returns:
        sum - the sum of the diagonal elements (float/int)
    -------------------------------------------------------
    """
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum

# 4.
def replace_elements(matrix, old, new):
    """
    -------------------------------------------------------
    Replaces all occurrences of 'old' value with 'new' value in a 2D list.
    Use: replace_elements(matrix, old, new)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list)
        old - the value to be replaced (int/float/str)
        new - the new value (int/float/str)
    Returns:
        None.
    -------------------------------------------------------
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == old:
                matrix[i][j] = new

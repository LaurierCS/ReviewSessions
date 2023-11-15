# 1. Implement the following function. The file is ExampleFiles/customers.txt

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

# 2. Implement the following function. The file is ExampleFiles/customers.txt
def filter_by_year(fh, year):
    """
    -------------------------------------------------------
    Find all customer records that signed up in a given year.
    Use: results = filter_by_year(fh, year)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        year - the year to filter records by (int)
    Returns:
        results - list of records that match the year (list of lists)
    -------------------------------------------------------
    """

# 3. Implement the following function.
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

# 4. Implement the following function.
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
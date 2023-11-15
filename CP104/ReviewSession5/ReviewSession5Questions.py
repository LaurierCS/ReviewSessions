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
            an empty list otherwise (list)
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
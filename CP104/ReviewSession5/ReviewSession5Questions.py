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


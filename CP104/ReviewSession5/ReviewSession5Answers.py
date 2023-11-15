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
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = ""
    line = fh.readline()
    while line != "":
        line = line.strip()
        fields = line.split(",")
        if fields[1] + " " + fields[2] == name:
            result = ','.join(fields)
        line = fh.readline()
    return result

fh = open("CP104/ReviewSession5/ExampleFiles/customers.txt", "r")
print(customer_by_name(fh, "Jane White"))
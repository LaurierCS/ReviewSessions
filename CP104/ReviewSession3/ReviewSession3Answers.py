# 1. 
def number_staircase(start, end, increment):
    """
    prints numbers in descending order from start to end by increment
    Use: number_staircase(start, end, increment)

    Parameters:
        start (int) - starting number
        end (int) - ending number
        increment (int) - number to increment by

        start > end
    """
    for i in range(start, end, -increment):
        print(i)
# 2. 
def print_factors(n):
    """
    prints the factors of n
    Use: print_factors(n)

    Parameters:
        n (int) - number to find factors of
    """
    for value in range(1, n):
        if n % value == 0:
            print(value)

# 3. 
def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of -1 indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. 
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    id = int(input("Employee ID: "))
    total = 0
    num_employees = 0
    while id != -1:
        rate = int(input("Hourly wage rate:"))
        hours = int(input("Hours worked:"))
        overtime = hours - 40

        net_payment = rate * hours
        if overtime > 0:
            net_payment +=  overtime * rate * 1.5
        
        total +=  net_payment
        num_employees += 1
        print(f"Net payment for employee {id}: {net_payment}")
        id = int(input("Employee ID: "))
    
    return total, total/num_employees

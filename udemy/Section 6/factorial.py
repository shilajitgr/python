LOW = 0
HIGH = 36

def factorial(num: int) -> int:
    """
    Returns the factorial of given number.

    Args:
        num (int): Number whose factorial is to be provided

    Returns:
        int: factorial of the given number
    """
    fact = 1
    if num < 2:
        return fact
        
    for i in range(1, num+1):
        fact *= i
        
    return fact
    

for num in range(LOW, HIGH):
    print(f"{num} {factorial(num)}")
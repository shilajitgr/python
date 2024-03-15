LOW = 1
HIGH = 101

def fizz_buzz(num: int) -> str:
    """
    This function returns the number itself or fizz if its divisible by 3, 
    or buzz if its divisible by 5 or fizz buzz if its divisible by both 3 and 5.

    Args:
        num (int): value to be processed

    Returns:
        str: stringified number or fizz/ buzz/ fizz buzz based on the function description
    """
    val = []
    if num % 3 == 0:
        val.append("fizz")
    if num % 5 == 0:
        val.append("buzz")
        
    if val:
        return " ".join(val)
    else:
        return str(num)
        

for num in range(LOW, HIGH):
    print(fizz_buzz(num))
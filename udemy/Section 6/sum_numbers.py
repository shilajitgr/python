def sum_numbers(*nums: float) -> float:
    """
    It sums up all the numbers recieved and returns it.

    Args:
        nums (float tuple): A list of float values
    Returns:
        float: sum of all the values received
    """
    return sum(*nums)

for i in [(1,2,3), (8, 20, 2), (12.5, 3.147, 98.1), (1.1, 2.2, 5.5)]:
    print(sum_numbers(i))
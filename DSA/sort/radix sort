
def get_digit(val, digit_num, max_digit):
    """
    converts the val into a list max_digit size(empty spaces are populated with 0)
    returns the digit_num'th value from this list after converting to integer
    """

    return int((['0']*max_digit+list(str(val)))[-max_digit:][digit_num])


def count(arr, base, digit_num, max_digit):

    count_arr = [0] * (base)
    for val in arr:

        digit = get_digit(val, digit_num, max_digit)
        count_arr[digit] += 1

    return count_arr


def cumulate(count_arr):

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]


def populate_sorted_arr(arr, base, digit_num, max_digit):

    count_arr = count(arr, base, digit_num, max_digit)
    cumulate(count_arr)
    sorted = [0] * len(arr)

    for elem in arr[::-1]:
        digit = get_digit(elem, digit_num, max_digit)
        count_arr[digit] -= 1
        sorted[count_arr[digit]] = elem

    return sorted


def radix_sort(arr, base):

    max_digit = len(str(max(arr)))
    sorted = arr.copy()
    for i in range(max_digit-1, -1 , -1):
        sorted = populate_sorted_arr(sorted, base, i, max_digit)

    return sorted

num_list = [330, 554, 22, 4223, 114, 421, 1354, 2, 53235, 311]
print(radix_sort(num_list, base=10))
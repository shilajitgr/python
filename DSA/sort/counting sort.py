
def count(arr, max_val, min_val):

    count_arr = [0] * (max_val - min_val + 1)
    for i in arr:
        count_arr[i - min_val] += 1
    return count_arr


def cumulate(count_arr):
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]


def populate_sorted_arr(arr):

    max_val = max(arr)
    min_val = min(arr)
    count_arr = count(arr, max_val, min_val)
    cumulate(count_arr)
    sorted = [0] * len(arr)

    for elem in arr[::-1]:
        count_arr[elem - min_val] -= 1
        sorted[count_arr[elem - min_val]] = elem

    return sorted

num_list = [33, 55, 22, 42, 11, 42, 54, 2, 5, 31]
print(populate_sorted_arr(num_list))
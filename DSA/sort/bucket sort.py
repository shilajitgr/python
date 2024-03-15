
def insertion_sort(bucket: list) -> None:
    """
    This function sorts a list in-place

    Args:
        bucket (list): A list of integers
    """

    for idx, val in enumerate(bucket):
        if idx != 0:
            temp_idx = idx - 1
            slide = False
            while val < bucket[temp_idx]:
                slide = True
                if temp_idx == 0:
                    break
                temp_idx -= 1

            if slide:
                bucket[temp_idx+1:idx+1] = bucket[temp_idx:idx]
                bucket[temp_idx] = val


def bucket_sort(arr: list) -> None:
    """
    This function sorts the given list of integers and prints it

    Args:
        arr (list): Integer Array to be sorted
    """

    max_val = max(arr)
    arr_len = len(arr)
    bucket_list = [[] for i in range(arr_len)]
    sorted = []
    for val in arr:
        index = int((arr_len*val)/(max_val+1))
        bucket_list[index].append(val)

    for bucket in bucket_list:
        insertion_sort(bucket)
        # bucket.sort()
        sorted += bucket

    print(sorted)

num_list = [33, 55, 22, 42, 11, 42, 54, 2, 5, 31, 52]
bucket_sort(num_list)
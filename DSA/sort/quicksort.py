def quicksort(arr, start, end):
    if start >= end:
        return
    else:
        p = partition(arr, start, end)
        quicksort(arr, start, p-1)
        quicksort(arr, p+1, end)

        print(arr)


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while True:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[right], arr[left] = arr[left], arr[right]
        else:
            break
    
    arr[start], arr[right] = arr[right], arr[start]
    return right


num_list = [113,43231,122,243,663,1122,33,1242423,123134,111]
quicksort(num_list, 0, len(num_list) - 1)
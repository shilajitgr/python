
arr = [6,2,3,5,1,8,7,3]

def merge(arr_left, arr_right):
    len_right = len(arr_right)
    len_left = len(arr_left)
    combined_arr = []
    combined_len = len(arr_left+arr_right)
    i = 0
    j = 0
    while len(combined_arr) != combined_len:
        
        if j == len_right:
            combined_arr.extend(arr_left[i:])
            return combined_arr
        if i == len_left:
            combined_arr.extend(arr_right[j:])
            return combined_arr
        
        if arr_left[i] > arr_right[j]:
            val = arr_right[j]
            j += 1
        else:
            val = arr_left[i]
            i += 1

        combined_arr.append(val)
        
    return combined_arr


def merge_sort(array):

    if len(array) < 2:
        return array
    else:
        mid = len(array)//2
        arr_left = merge_sort(array[:mid])
        arr_right = merge_sort(array[mid:])
        
        result = merge(arr_left, arr_right)
        print(result)
        return result
    
print("-"*80)
print(merge_sort(arr))
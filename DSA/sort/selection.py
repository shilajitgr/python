arr = [6,2,3,5,1,8,7,3]

for i in range(len(arr)):
    
    min_idx = i + arr[i:].index(min(arr[i:]))
    if min_idx == i:
        continue
    temp = arr[min_idx]
    arr[min_idx] = arr[i]
    arr[i] = temp

print(arr)
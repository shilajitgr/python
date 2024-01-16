import json
import math


class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:

        arr_len = len(arr)
        if len(arr) == 3:
            return 1 if sum(arr) == target else 0

        arr.sort()
        count = 0
        final = []
        item_hash = {}
        for x in range(arr_len - 2):
            target_in = target - arr[x]
            i = x + 1
            j = arr_len - 1

            while i < j:
                sum_data = arr[i] + arr[j]
                if sum_data > target_in:
                    j -= 1
                elif sum_data < target_in:
                    i += 1
                else:
                    temp = [arr[x], arr[i], arr[j]]
                    if f"{temp}" in item_hash:
                        i += 1
                        j -= 1
                        continue
                    i_count = 0
                    j_count = 0
                    x_count = 0

                    for obj in arr[x:j+1]:
                        if obj == arr[i]:
                            i_count += 1
                        if obj == arr[j]:
                            j_count += 1
                        if obj == arr[x]:
                            x_count += 1

                    if arr[i] == arr[j] and i + 1 == j:
                        j_count -= 1
                        i_count -= 1
                    elif arr[i] == arr[j]:
                        j_count -= 1
                    item_hash[f"{temp}"] = item_hash.get(f"{temp}", 0) + x_count* i_count * j_count
                    
                    count += x_count * i_count * j_count
                    i += 1
                    j -= 1
            
        print(final)
        print(json.dumps(item_hash, indent=4))
        return count
        
print(Solution().threeSumMulti([1,1,2,2,2,2], 6))
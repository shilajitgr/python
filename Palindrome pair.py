"""
Geeks for geeks
"""


# brute force not efficient

class Solution:
    def palindromepair(self, N, arr):
        # code here
        alen = len(arr)
        for i in range(alen - 1):
            for j in range(i + 1, alen):
                objA = arr[i] + arr[j]
                objB = arr[j] + arr[i]
                if i != j and (objA == objA[::-1] or objB == objB[::-1]):
                    return True

        return False


print(Solution().palindromepair(6, ["geekf", "geeks", "or", "keeg", "abc", "bc"]))
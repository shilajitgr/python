class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > m:
            nums1.pop()
        
        while len(nums2) > n:
            nums2.pop()
        
        j = 0
        i = 0
        while i <= len(nums1):
            while i<len(nums1) and j<len(nums2) and nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1

            if i >= len(nums1):
                nums1 += nums2[j:]
                j = n

            if j >= len(nums2):
                break
            
            i += 1
            
sol_obj = Solution()
nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
sol_obj.merge(nums1,m,nums2,n)
print(nums1, end="\n\n")
print(nums1==[1,2])
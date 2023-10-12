class Solution:
    def maxArea(self, height: list[int]) -> int:
        #x = [1,8,6,2,5,4,8,3,7]
        #y = [[1,7,1*8], [8,7,7*7], [8,3,3*6], [8,8,8*5], [6,8,6*4], [6,4,3*4], [6,5,5*2], [6,2,2*1]]
        i = 0
        j = len(height) - 1
        max_area = 0
        while i != j:
            # min_height_of_pair = min(height[i],height[j])
            area = (min(height[i],height[j]))*(j - i)
            if area > max_area:
                max_area = area
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            
        return max_area
    
print(Solution().maxArea([1,2,4,3]))
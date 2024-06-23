class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        if matrix[0][0] > target or matrix[-1][-1] < target: # if the target does not fall in the range of elements present in the matrix
            return False

        if len(matrix) < 2 and len(matrix[0]) < 2: # if the matrix has only one element
            return True if matrix[0][0] == target else False

        row_num = None
        if len(matrix) > 1:

            low = 0
            high = len(matrix)
            mid = (low+high)//2
            min_diff = None
            min_idx = None

            while low != high and high > low:
                
                if matrix[mid][0] > target:
                    if min_diff == None:
                        min_idx = mid
                        min_diff = matrix[mid][0] - target
                    elif 0 < matrix[mid][0] - target < min_diff:
                        min_diff = matrix[mid][0] - target
                        min_idx = mid
                    high = mid-1

                elif matrix[mid][0] == target:
                    return True

                else:
                    low = mid+1
                
                mid = (low+high)//2

            row_num = len(matrix) - 1
            if min_idx:
                
                if mid != min_idx and 0 < matrix[mid][0] - target < min_diff:
                    min_idx = mid
                    
                row_num = 0
                if 1 < min_idx:
                    row_num = min_idx - 1
            
        else:
            row_num = 0

        if row_num < 0 or matrix[row_num][0] > target or matrix[row_num][-1] < target:
            return False
        
        low = 0
        high = len(matrix[row_num])
        mid = (low+high)//2
        
        while low != high and high > low:
            
            if matrix[row_num][mid] > target:
                high = mid-1

            elif matrix[row_num][mid] == target:
                return True

            else:
                low = mid+1
            
            mid = (low+high)//2
        
        if matrix[row_num][mid] == target:
            return True
        
        return False
    
    
sol_obj = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# matrix = [[1,3], [4,7]]
# matrix = [[-9,-7,-7,-7,-6,-6,-6,-4,-3,-1,0],[3,5,6,8,8,10,12,14,14,16,17],[20,22,23,23,23,23,25,25,27,28,28],[29,31,33,33,35,37,37,39,39,41,42],[43,45,46,48,49,50,50,51,51,53,53],[56,57,58,58,58,58,58,60,61,62,64],[65,67,68,70,72,74,74,76,76,76,77],[78,79,79,80,81,82,83,85,87,89,90],[92,94,96,98,99,100,100,102,102,103,105],[106,106,106,108,109,111,113,115,117,119,120],[123,124,126,128,128,130,131,131,132,132,133],[134,136,138,140,140,142,144,145,146,148,150],[152,153,154,156,158,159,161,163,165,166,167],[170,171,173,173,173,173,174,175,176,178,180],[181,182,184,186,187,189,191,193,195,196,196]]
print(sol_obj.searchMatrix(matrix, 24))

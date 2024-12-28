class Solution:

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_len = len(matrix[0])
        if col_len == 1:
            return

        if col_len == 2:
            transpose(matrix, 1, 0, 0)
            return

        for lev in range(col_len - 2):
            lev_len = col_len - 1 - lev
            
            for i in range(lev,lev_len):
                
                transpose(matrix, lev_len, lev, i)
                
def transpose(matrix: list[list[int]], lev_len: int, lev: int, i: int) -> None:
    matrix[lev][i], matrix[i][lev_len] = matrix[i][lev_len], matrix[lev][i]
    matrix[lev][i], matrix[lev_len][lev_len-i+lev] = matrix[lev_len][lev_len-i+lev], matrix[lev][i]
    matrix[lev][i], matrix[lev_len-i+lev][lev] = matrix[lev_len-i+lev][lev], matrix[lev][i]
    
"""
Sample:
    matrix = [[ 1, 2, 3, 4, 5],
              [ 6, 7, 8, 9,10],
              [11,12,13,14,15],
              [16,17,18,19,20],
              [21,22,23,24,25]]

reqd_output = [[21,16,11,6,1],
               [22,17,12,7,2],
               [23,18,13,8,3],
               [24,19,14,9,4],
               [25,20,15,10,5]]
""" 
matrix = [[ 1, 2, 3, 4, 5],
          [ 6, 7, 8, 9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]

sol_obj = Solution()
# print(*matrix,sep="\n")
sol_obj.rotate(matrix)
print(*matrix,sep="\n", end="\n\n")
print(matrix == [[21,16,11,6,1],
                 [22,17,12,7,2],
                 [23,18,13,8,3],
                 [24,19,14,9,4],
                 [25,20,15,10,5]])

"""
original matrix

[[21,16,11,6,1],
[22,17,12,7,2],
[23,18,13,8,3],
[24,19,14,9,4],
[25,20,15,10,5]]


Transposed matrix

[[21,22,23,24,25],
 [16,17,18,19,20],
 [11,12,13,14,15],
 [ 6, 7, 8, 9,10],
 [ 1, 2, 3, 4, 5]]
 
 
Reversing the transposed matrix

[[25, 24, 23, 22, 21],
 [20, 19, 18, 17, 16],
 [15, 14, 13, 12, 11],
 [10,  9,  8,  7,  6],
 [ 5,  4,  3,  2,  1]]
 
The matrix above is now the 90 degree rotated matrix 
of the original matrix
"""


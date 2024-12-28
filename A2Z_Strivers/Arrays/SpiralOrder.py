class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row = len(matrix)
        col = len(matrix[0])

        level = 0
        final = []
        total = row*col
        if row == 1: 
            return matrix[0]
        if col == 1:
            return [x[0] for x in matrix]

        while total - len(final) > 0:
            # write code to print the top row and right column
            
            bottom = []
            top = []

            i = j = level
            while i+j < row-level-1 + col-level-1 and total > len(final):
                top.append(matrix[i][j])
                if j < col-level-1:
                    j+=1
                elif i < row-level-1:
                    i+=1
            
            final.extend(top+[matrix[row-level-1][col-level-1]])
            i = j = level
            i += 1
            while i + j < row-level-1 + col-level-1 and total > len(final):
                bottom.append(matrix[i][j])
                if i < row-level-1:
                    i+=1
                elif j < col-level-1:
                    j+=1
        
            final.extend(bottom[::-1])
            level += 1

        return final

"""
     0   1   2   
   0 1   2   3

   1 4   5   6

   2 7   8   9


0,0 0,1 0,2 1,2 2,2 2,1 2,0 1,0 1,1

 1   2   3   4   6   9   8   7   5
 
 i = 0
 j = 0
 
 i,j i,j+1 i,j+2 i+1,j+2 i+2,j+2 i+2,j+1 i+2,j i+1,j i+1,j+1
 ###########################################################
 
[[ 1 , 2 , 3 , 4 , 5],
[ 6 , 7 , 8 , 9 , 10],
[ 50, 60, 70, 80, 90],
[ 11, 12, 13, 14, 15]]
 
 
 row = 3
 col = 5
 
 [[3],[5],[7]]
 
"""

matrix = [[ 1 , 2 , 3 , 4 , 5],
          [ 6 , 7 , 8 , 9 , 10],
          [ 50, 60, 70, 80, 90],
          [ 11, 12, 13, 14, 15]]

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matrix = [[1,2],[3,4]]

matrix = [[6,7,8]]

matrix = [[2,3,4],
          [5,6,7],
          [8,9,10],
          [11,12,13],
          [14,15,16]]

print(Solution().spiralOrder(matrix))
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        start = [[1]]
        
        for i in range(1,numRows):
            row_i = [1] * (i+1)
            for m in range(len(start[i-1][:-1])):
                row_i[m+1] = start[i-1][m] + start[i-1][m+1]

            start.append(row_i)
        
        return start
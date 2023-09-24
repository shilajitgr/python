class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s

        zig_matrix = [['']*(len(s)//2) for i in range(numRows)]
        keep_column_same = []

        skip = False
        for y in range(0,len(s),numRows-1):
            if skip:
                skip = False
                continue
            skip = True
            last_element_in_column = y + numRows
            temp = list(range(y, last_element_in_column))
            keep_column_same.append(temp)

        stop = False
        col = 0
        
        for row_nums in keep_column_same:
            # print(row_nums, col, sep=" ")
            row = 0
            for id in row_nums:
                if id >= len(s):
                    stop = True
                    continue
                # print(s[id])
                zig_matrix[row][col] = s[id]
                row += 1
            col += 1
            row -= 1
            if stop:
                break
            id += 1
            for id in range(id, id + numRows - 2):
                row -= 1
                zig_matrix[row][col] = s[id]
                col += 1

        # print(*zig_matrix, sep='\n')
        final = ""
        for i in range(numRows):
            final += "".join(zig_matrix[i][:])
        return final


print(Solution().convert("ABC", 2))
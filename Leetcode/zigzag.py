class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1 or len(s) == numRows:
            return s

        zig_matrix = [['']*(len(s)//2+1) for i in range(numRows+1)]
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
                if id >= len(s):
                    stop = True
                    continue
                row -= 1
                zig_matrix[row][col] = s[id]
                col += 1
            if stop:
                break

        final = ""
        for line in zig_matrix:
            final += "".join(line)
        return final

print(Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
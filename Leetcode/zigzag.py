class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        row_list = list(range(numRows, 0, -1))
        final = []
        gap = (numRows - 2) * 2 + 2
        for row in row_list:
            offset = numRows - row
            col = 1
            final.append(s[offset])
            while True:
                offset = offset + gap
                head_idx = col * gap
                if 1 < row < numRows and (head_idx + head_idx - offset) < len(s):
                    final.append(s[head_idx + head_idx - offset])
                    col += 1

                if offset >= len(s):
                    break

                final.append(s[offset])

        return "".join(final)

s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s, numRows) == "PAHNAPLSIIGYIR")

import re

class Solution:
    def myAtoi(self, s: str) -> int:

        filtered = re.match("^[ ]*[+-]?[\d]+", s)
        if not filtered:
            return 0
        
        int_filtered = int(filtered.group(0))
        limit = - 2**31
        if int_filtered < 0:
            return limit if int_filtered < limit else int_filtered  


        limit = 2**31 - 1
        if int_filtered >= 0:
            return limit if int_filtered > limit else int_filtered

print(Solution().myAtoi("  +0 123"))
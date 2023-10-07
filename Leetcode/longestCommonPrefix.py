class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        common = strs[0]
        for i in strs[1:]:
            something = False
            m = 0
            temp = ""
            while len(common) > 0 and len(i) and i[m] == common[m]:
                something = True
                temp += i[m]
                m += 1
                if m >= len(common) or m >= len(i):
                    break

            common = temp
        
        return common
    

print(Solution().longestCommonPrefix(["dog","","car"]))
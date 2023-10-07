class Solution:
    def longestPalindrome(self, s: str)->str:
        max_len = 0
        max_palindrome = ""
        str_len = len(s)
        if str_len == 1:
            return s
        for i in range(0, str_len-1):
            radius = min(i, str_len - i - 1)
            # mirror = False
            mirror_palindrome = ""
            if s[i] == s[i+1]:
                mirror_palindrome = self.find_palindrome(s, str_len, i+1, i, radius)
            trans_palindrome = self.find_palindrome(s, str_len, i, i, radius)
            palindrome = mirror_palindrome if len(mirror_palindrome) > len(trans_palindrome) else trans_palindrome
            match_len = len(palindrome)
            if max_len < match_len:
                max_len = match_len
                max_palindrome = palindrome
            
        return max_palindrome
    
    def find_palindrome(self, s, str_len, rt_start, lt_start, radius)-> str:

        palindrome = s[lt_start:rt_start+1]
            
        match_idx = 1
        while radius != 0 and match_idx <= radius and (rt_start+match_idx) < str_len:
            lt_idx = lt_start-match_idx
            rt_idx = rt_start+match_idx
            lt_item = s[lt_idx]
            rt_item = s[rt_idx]
            if lt_item == rt_item:
                palindrome = lt_item + palindrome + rt_item
                match_idx += 1
                continue
            break

        return palindrome
            

print(Solution().longestPalindrome("m"))
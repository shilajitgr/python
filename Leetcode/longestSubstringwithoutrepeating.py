class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        temp_sub = ""
        max_sub_len = 0
        hash_map = {}
        max_sub_updated = False
        # once duplicate element is encountered, start considering the new substring by 
        # adding 1 to the previous occurance of the duplicate element
        seq_start_idx = 0
        for i in range(len(s)):   
            if s[i] not in hash_map or hash_map[s[i]] < seq_start_idx:
                hash_map[s[i]] = i
                temp_sub += s[i]
                max_sub_updated = False
            else:
                max_sub_updated = True
                if len(temp_sub) > max_sub_len:
                    max_sub_len = len(temp_sub)
                seq_start_idx = hash_map[s[i]] + 1
                # hash_map = {}
                temp_sub = s[seq_start_idx:i+1]
                hash_map[s[i]] = i

        if not max_sub_updated and len(temp_sub) > max_sub_len:
            max_sub_len = len(temp_sub)
        return max_sub_len
    
print(Solution().lengthOfLongestSubstring("dvdf"))
# https://www.youtube.com/watch?v=2D0D8HE6uak

class Solution:
    def findTwoElement( self,arr): 
        # code here
        arr.sort()
        dups = []
        missing = self.gettingInitialMissingNums(arr[0])
        prev = arr[0]
        seen = set()
        for num in arr[1:]:
            
            if num - prev == 0:
                if dups and dups[-1] == num:
                    continue
                dups.append(prev)
                
            
            if num - prev > 1:
                missing.extend(list(range(prev+1,num)))
                
            prev = num
        
        return dups+missing
        
    def gettingInitialMissingNums(self, startingNum):
        
        if startingNum != 1:
            return list(range(1, startingNum))
        
        return []

    def getMissingNumsFromEnd(self, prev, actualEnd):
        
        if actualEnd - prev != 0:
            return list(range(prev+1, actualEnd+1))
            
        return []
    
inp = [6, 5, 8, 7, 1, 4, 1, 3, 2]

print(Solution().findTwoElement(inp))
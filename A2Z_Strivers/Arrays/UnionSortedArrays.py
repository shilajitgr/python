#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        
        i = j = 0
        union = []
        tracker = {*""}
        while i < len(a) and j < len(b):
            item = None
            if a[i] <= b[j]:
                item = a[i]
                i+=1
            else:
                item = b[j]
                j+=1
            
            self.addItem(item, union, tracker)
            
            if i == len(a):
                for idx in range(j, len(b)):
                    self.addItem(b[idx], union, tracker)
            
            if j == len(b):
                for idx in range(i, len(a)):
                    self.addItem(a[idx], union, tracker)
            
        return union
    
    def addItem(self, item, union, tracker):
        if item not in tracker:
            union.append(item)
            tracker.add(item)
    
print(Solution().findUnion([1, 2, 3, 4, 5], [1, 2, 3]))
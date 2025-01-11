class Solution:
    def getFloorAndCeil(self, x: int, data: list) -> list:
        # code here
        maxFloor = None
        minCeil = None
        for _, num in enumerate(data):
            
            if num == x:
                return [num, num]
            
            temp = num - x
            if temp > 0 and (not minCeil or temp < minCeil):
                minCeil = temp
                
            if temp < 0 and (not maxFloor or temp > maxFloor):
                maxFloor = temp

        maxFloor = -1 if maxFloor == None else maxFloor + x    
        minCeil = -1 if minCeil == None else minCeil + x
        
        return [maxFloor, minCeil]
            
# x, data = 64, [98,9]
x, data = 7,[5, 6, 8, 9, 6, 5, 5, 6]
# x, data = 26, [80, 59, 26, 46]

print(Solution().getFloorAndCeil(x, data))
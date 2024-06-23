class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        """
        copilot's solution
        
        intervals.sort()
        merged_intervals = [intervals[0]]

        for current in intervals:
            last_interval = merged_intervals[-1]
            if current[0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], current[1])
            else:
                merged_intervals.append(current)

        return merged_intervals
        
        """
        
        while True:
            merged_intervals = []
            interval_merged = False
            for interval in intervals:
                if not merged_intervals:
                    merged_intervals.append(interval)
                    continue
                sub_merge = False
                for interval2 in merged_intervals:
                    if interval[0] <= interval2[1] and interval2[0] <= interval[1]:
                        
                        interval2[0] = min(interval[0], interval2[0])
                        interval2[1] = max(interval[1], interval2[1])
                        interval_merged = True
                        sub_merge = True
                
                if not sub_merge: 
                    merged_intervals.append(interval)
            intervals = merged_intervals
            if not interval_merged:
                break
        
        return intervals
        

sol_obj = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol_obj.merge(intervals), end="\n\n")
print(intervals==[[1,6],[8,10],[15,18]])
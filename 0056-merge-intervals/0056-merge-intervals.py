class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for curr in intervals:
            if not merged or merged[-1][1] < curr[0]:  
                merged.append(curr)
            else:  
                merged[-1] = (merged[-1][0], max(merged[-1][1], curr[1]))
        return merged
                
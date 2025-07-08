from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cumulative_sum = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1 
        
        for num in nums:
            cumulative_sum += num
            
            if (cumulative_sum - k) in sum_count:
                count += sum_count[cumulative_sum - k]
            
            sum_count[cumulative_sum] += 1
        
        return count


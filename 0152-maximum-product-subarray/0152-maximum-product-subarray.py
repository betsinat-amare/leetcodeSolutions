class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            if curr < 0:
                max_prod, min_prod = min_prod, max_prod  
            
            max_prod = max(curr, curr * max_prod)
            min_prod = min(curr, curr * min_prod)
            
            result = max(result, max_prod)
        
        return result

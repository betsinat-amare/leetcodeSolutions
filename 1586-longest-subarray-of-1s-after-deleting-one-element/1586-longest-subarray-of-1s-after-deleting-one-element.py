class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        zeros = 0
        l = 0
        for r, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r-l) 
        return res

           

        
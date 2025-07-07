class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        r = 0
        for num in nums:
            r = num ** 2
            res.append(r)
        return sorted(res)
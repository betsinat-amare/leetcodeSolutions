class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        totalcount = 0
        freq = Counter(nums)
        maxvalue = max(freq.values())
        for count in freq.values():
            if count == maxvalue:
                totalcount += count


        return totalcount
        
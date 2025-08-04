class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        mid = (n+1) // 2
        snums = sorted(nums)
        small = snums[:mid][::-1]
        large = snums[mid:][::-1]

        nums[::2] = small
        nums[1::2] = large

        """
        Do not return anything, modify nums in-place instead.
        """
        
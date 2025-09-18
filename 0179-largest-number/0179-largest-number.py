class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        num = ''.join(nums)
        return num if num[0] != '0' else '0'
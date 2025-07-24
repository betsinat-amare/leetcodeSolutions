class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        pos = len(nums) -1
        while pos != 0:
            for i in range(pos):
                if i + nums[i] >= pos:
                    jumps += 1
                    pos = i
                    break

        return jumps

        
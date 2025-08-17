class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        out = [0,0]
        l = -1
        r = -1
        def firstpos(l, r):

            while l <= r:
                mid = (r+l) // 2
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid -1
            return l if l < len(nums) and nums[l] == target else -1

        def lastpos(l, r):

            while l <= r:
                mid = (r+l) // 2
                if nums[mid] > target:
                    r = mid-1
                else:
                    l = mid +1
            return r if r >= 0 and nums[r] == target else -1
        left, right = firstpos(0, len(nums)-1) , lastpos(0, len(nums)-1)

        return [left, right]
        
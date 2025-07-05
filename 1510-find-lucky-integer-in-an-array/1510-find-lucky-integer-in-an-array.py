class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arrr = Counter(arr)
        maxf = -1
        for k, v in arrr.items():
            if k == v:
                maxf = max(maxf, v)
        return maxf

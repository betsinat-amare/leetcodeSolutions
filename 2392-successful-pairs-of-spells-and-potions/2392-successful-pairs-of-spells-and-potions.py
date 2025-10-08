class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []

        for spell in spells:
            req = success / spell
            idx = bisect_left(potions,req)
            count = len(potions) - idx
            ans.append(count) 

        return ans
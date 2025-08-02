from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter()
        for a, b in zip(basket1, basket2):
            cnt[a] += 1
            cnt[b] -= 1
        transfer = []
        for val, diff in cnt.items():
            if diff % 2 != 0:
                return -1  
            times = abs(diff) // 2
            transfer.extend([val] * times)

        if not transfer:
            return 0 

        transfer.sort()
        global_min = min(min(basket1), min(basket2))
        m = len(transfer) // 2  

        cost = 0
        for i in range(m):
            cost += min(transfer[i], 2 * global_min)

        return cost

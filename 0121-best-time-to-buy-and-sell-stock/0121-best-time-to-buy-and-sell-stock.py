class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('inf')
        maxpf = 0

        for price in prices:
            if price < minp:
                minp = price

            else:
                maxpf = max(maxpf, (price-minp))

        return maxpf
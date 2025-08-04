class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            current_max = 0
            for length in range(1, min(k, i + 1) + 1):
                current_max = max(current_max, arr[i - length + 1])
                prev = dp[i - length] if i - length >= 0 else 0
                dp[i] = max(dp[i], prev + current_max * length)

        return dp[-1]

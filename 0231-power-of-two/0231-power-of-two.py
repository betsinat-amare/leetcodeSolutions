class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        log2_n = math.log2(n)
        return log2_n.is_integer()

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log(n, 3)
        return abs(round(x) - x) < 1e-10
            
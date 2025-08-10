from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def isPowerOfTwo(x):
            return x > 0 and (x & (x - 1)) == 0

        digits = list(str(n))
        seen = set()  
        
        for perm in permutations(digits):
            if perm[0] == '0':  
                continue
            num = int(''.join(perm))
            if num not in seen:
                seen.add(num)
                if isPowerOfTwo(num):
                    return True
        return False

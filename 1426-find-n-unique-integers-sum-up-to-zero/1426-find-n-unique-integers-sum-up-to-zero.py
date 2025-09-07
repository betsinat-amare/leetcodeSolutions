class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        res = [0]*n
        res[0] = -(n // 2)
        for i in range(1, len(res)):
            res[i] = res[i-1]+1
            if n% 2 == 0:
                res[n//2] = res[(n//2)-1] +2
            
        return res

        
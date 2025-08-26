import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0
        
        for w, h in dimensions:
            diag = math.sqrt(w**2 + h**2)
            area = w * h
            
            if diag > max_diag:
                max_diag = diag
                max_area = area
            elif abs(diag - max_diag) < 1e-9:  
                max_area = max(max_area, area)
        
        return max_area

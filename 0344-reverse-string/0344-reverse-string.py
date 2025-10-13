class Solution:
    def reverseString(self, s: List[str]) -> None:
        l= 0
        r = len(s) - 1
        temp = 0
        while l<r:
            temp =s[l]
            s[l]=s[r]
            l+=1
            s[r]=temp
            r-=1

            
        """
        Do not return anything, modify s in-place instead.
        """
        
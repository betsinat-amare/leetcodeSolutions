class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        list1 = [int(n) for n in reversed(num1)]
        list2 = [int(n) for n in reversed(num2)]

        for i in range(max(len(list1), len(list2))):
            x = list1[i] if i < len(list1) else 0
            y = list2[i] if i < len(list2) else 0
            
            summ = x + y + carry
            res.append(summ % 10)  
            carry = summ // 10     
        
        if carry:
            res.append(carry)
        
        return ''.join(map(str, reversed(res)))

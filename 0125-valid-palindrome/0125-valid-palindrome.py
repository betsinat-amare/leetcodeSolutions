class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1
        while l < r:
            if 97 <= ord(s[l]) <= 122 or 48 <= ord(s[l]) <= 57:
                if 97 <= ord(s[r]) <= 122 or 48 <= ord(s[r]) <= 57:
                    if s[l] != s[r]:
                        return False
                    l += 1
                r -= 1
            else:
                l+=1
        return True
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(c):
            return c.isalpha() or c.isdecimal()
        chars= "".join(c.upper() for c in s if isAlphanumeric(c))
        s=chars
        if len(s)<2:
            return True        
        odd=len(s)%2
        l=len(s)//2-1 if not odd else len(s)//2
        r = l if odd else l+1   
        while l>=0:
            if isAlphanumeric(s[l]) and isAlphanumeric(s[r]) and s[l].upper()!=s[r].upper():
                return False
            l-=1
            r+=1
        return True
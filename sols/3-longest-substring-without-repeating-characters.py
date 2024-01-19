class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lls=0
        l=0
        known=set()
        if not s: 
            return 0
        for r in range(len(s)):
            while s[r] in known:
                known.remove(s[l])
                l+=1
            known.add(s[r])
            lls=max(lls,r-l+1)
        return lls




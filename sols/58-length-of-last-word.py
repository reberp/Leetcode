class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            l=0
            if needle==haystack:
                return 0
            for r in range(len(needle),len(haystack)+1):
                if haystack[l:r]==needle:
                    return l
                l+=1
        return -1
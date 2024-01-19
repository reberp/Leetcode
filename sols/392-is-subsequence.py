class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tp=0
        sp=0
        if not s:
            return True
        for tp in range(len(t)):
            if t[tp]==s[sp]:
                sp+=1 
                if sp>=len(s):
                    return True
        return False
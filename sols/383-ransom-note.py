class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        notemap = dict()
        magmap = dict()
        for c in ransomNote:
            if c in notemap:
                notemap[c]=notemap[c]+1
            else:
                notemap[c]=1
        for c in magazine:
            if c in magmap:
                magmap[c]=magmap[c]+1
            else:
                magmap[c]=1   
        for c in notemap:
            if c not in magmap:
                return False
            elif magmap[c]<notemap[c]:
                return False
        return True
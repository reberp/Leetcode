class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss=s.split(" ")
        if len(pattern)!=len(ss):
            return False
        m=dict()
        used=set()
        for i in range(len(pattern)):
            print("{} {}".format(pattern[i],m))
            if pattern[i] not in m:
                if ss[i] in used:
                    return False
                m[pattern[i]]=ss[i]
                used.add(ss[i])
            elif m[pattern[i]]!=ss[i]:
                return False
        return True
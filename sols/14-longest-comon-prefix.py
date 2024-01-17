class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        out=""
        min_lens = min([len(x) for x in strs])
        for i in range(min_lens):

            letter = set(x[i] for x in strs)
            if len(letter)>1:
                break
            out+=strs[0][i]
        return out
    
        #for x in range()
        
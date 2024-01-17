class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xstr = str(x)
        same=True
        start=0
        end=len(xstr)-1
        while same and xstr:
            if len(xstr)>1 and xstr[start]!=xstr[end]:
                return False
            else:
                xstr=xstr[1:-1]
                end-=2
        return True


        
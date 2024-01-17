class Solution:
    def reverse(self, x: int) -> int:
        
        #definitely not right since I'm assuming I can take a number bigger
        # than the binary allowed 
        if not x:
          return 0
        neg=False
        if x<0:
          neg=True
          x*=-1
        s=str(x)
        si=s[::-1]
        if neg:
          si="-"+si
        out=int(si)
        if out<(-2**31) or out>(2**31):
          return 0
        return out
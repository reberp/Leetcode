class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ret=""
        swap={
          "upper":"lower",
          "lower":"upper"
        }        
        if numRows==1:
          return s
        for x in range(numRows):
          max=(2*numRows)-2
          lower=max-(x*2)
          upper=max-lower
          n={
            1:upper,
            -1:lower,
          }          
          #print("{},{}".format(upper,lower))
          #have to swap off between upper and lower pulling the values
          if x==0:
            for i in range(0,len(s),lower):
              #print("top: "+s[i])
              ret+=s[i]
          elif x==(numRows-1):
            for i in range((numRows-1),len(s),upper):
              #print("Bot: "+s[i])
              ret+=s[i]
          else:
            # have to take start, then go lower then upper and swap
            i=x
            current=-1
            while i<len(s):
              ret+=s[i]
              #print("x={}: {}".format(x,s[i]))
              i=i+n[current]
              #current=swap[current]
              current*=-1
              #ret+=s[i]
        return ret
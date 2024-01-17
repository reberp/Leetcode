class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        r=len(p)
        out=[]
        pdict = dict()
        for x in p:
            if x not in pdict:
                pdict[x]=1
            else:
                pdict[x]+=1
        #print(pdict)
        sdict=dict()
        for x in s[l:r]:
            if x not in sdict:
                sdict[x]=1
            else:
                sdict[x]+=1  
        if pdict==sdict:
            out.append(l)                             
        while r<len(s):   
            #add new right one
            l+=1
            r+=1
            #print("{} {}".format(l,r))            
            newchar=s[r-1]  
            if newchar in sdict:
                sdict[newchar]=sdict[newchar]+1
            else:
                sdict[newchar]=1
            oldchar=s[l-1]
            if oldchar in sdict:
                if sdict[oldchar]==1:
                    sdict.pop(oldchar)
                else:
                    sdict[oldchar]=sdict[oldchar]-1   
            #print(sdict)                
            if pdict==sdict:
                out.append(l)                

        return out
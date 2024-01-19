class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l=0
        r=0
        arr=[]
        out=[]
        if not nums:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        temp=[nums[0]]
        r=1
        while r < len(nums):
            if r < len(nums) and nums[r]==temp[-1]+1:
                temp.append(nums[r])
                r+=1
            else:
                l=r
                r+=1
                if len(temp)>1:
                    temp = str(temp[0])+"->"+str(temp[-1])
                    out.append(temp)
                    print(temp)
                else:
                    out.append(str(temp[0]))
                temp=[nums[l]]
            if r==len(nums): #have to run again to fix last one before while exits. 
            # definitely a better way to do it that isn't obvious to me. 
                if len(temp)>1:
                    temp = str(temp[0])+"->"+str(temp[-1])
                    out.append(temp)
                    print(temp)
                else:
                    out.append(str(temp[0]))
                temp=[nums[l]]                

        return out


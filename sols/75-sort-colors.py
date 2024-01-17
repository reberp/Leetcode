class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cdict=dict()
        cdict[0]=0
        cdict[1]=0
        cdict[2]=0
        z,y,x=-1,-1,-1 #if they don't exist, have to negate the additions
        for num in nums:
            cdict[num]=cdict[num]+1
        for x in range(cdict[0]):
            nums[x]=0
        for y in range(cdict[1]):
            nums[x+y+1]=1
        for z in range(cdict[2]):
            #print("{},{},{}".format(x,y,z))
            nums[x+y+z+2]=2
        print(nums)   
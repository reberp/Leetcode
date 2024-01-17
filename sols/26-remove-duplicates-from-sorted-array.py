class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        vals = dict()
        for x in range(len(nums)):
            vals[nums[x]]=""
        l=0
        for val in vals:
            nums[l]=val
            l+=1
        for x in range(l,len(nums)):
            nums[x]="_"
        return len(vals)
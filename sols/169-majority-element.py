class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Think a bunch of the solutions are based on the assumption that there's only two different numbers
        That isn't actually stated but seems to the the case? 
        """
        vals=dict()
        if len(nums)==1:
            return nums[0]
        for val in nums:
            if val in vals:
                vals[val]+=1
                if vals[val]>=len(nums)/2:
                    return val
            else:
                vals[val]=1
        return 1
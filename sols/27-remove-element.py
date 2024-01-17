class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=len(nums)-1
        count=0
        if not nums:
            return 0
        while l<len(nums) and nums[l]!="_":
            if nums[l]==val:
                nums[l]=nums[r]
                nums[r]="_"
                r-=1
                count+=1 #count of removed 
            else:
                l+=1
        return len(nums)-count
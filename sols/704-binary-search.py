class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found=False
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            #print("index {}".format(index))
            if nums[m]==target:
                return m
            if nums[m] < target:
                l=m+1
            if nums[m] > target:
                r=m-1
            #print("{},{}".format(l,r))
        return -1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known={} #{visited value : index in list}
        for i,val in enumerate(nums):
          m=target-val
          if m in known:
            return [i,known[m]]
          else:
            known[val]=i
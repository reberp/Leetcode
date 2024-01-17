class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        out=0
        while left != right:
          area=min(height[left],height[right])*(right-left)
          out=max(out,area)
          #print("{},{} area {}".format(left,right,area))
          left_lower= (height[left]<=height[right])
          #print(left_lower)
          if left_lower:
            left+=1
          else:
            right-=1
        return out
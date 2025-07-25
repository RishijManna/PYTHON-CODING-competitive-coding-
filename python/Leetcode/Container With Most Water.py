class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        water=0
        while left<right:
            width=right-left
            ht= min(height[left],height[right])
            w = width*ht
            water=max(water,w)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return water
        

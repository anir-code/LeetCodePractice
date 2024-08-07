"""
#11 container-with-most-water
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        start = 0
        end = len(height)-1
        while (start <= end):
            water = max(water, min(height[start],height[end]) * abs(start - end ))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1    

        return water


        

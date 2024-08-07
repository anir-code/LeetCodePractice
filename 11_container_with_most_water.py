"""
#11 container with most water
You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
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


        

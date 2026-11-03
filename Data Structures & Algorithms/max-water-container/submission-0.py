class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''

        two pointer. start left most, right most (this is going to make sure we take the MAX, as we are maximizing width here.)
        to increment or decrement p1/p2, look what is the lower of the two heights.

        '''

        p1 = 0
        p2 = len(heights) - 1
        maxArea = 0
        while p1 < p2:
            currArea = min(heights[p1], heights[p2]) * (p2 - p1)
            maxArea = max(maxArea, currArea)
            if heights[p1] < heights[p2]:
                p1+=1
            else:
                p2-=1
            
        
        return maxArea

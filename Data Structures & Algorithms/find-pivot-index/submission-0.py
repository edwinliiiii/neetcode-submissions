class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # A pivot index is also an index where the prefix sum for leftToRight and rightToLeft match.
    
        
        rightToLeft = []
        for num in reversed(nums):
            if not rightToLeft:
                rightToLeft.insert(0, num)
            else:
                rightToLeft.insert(0, num+rightToLeft[0])

        print(rightToLeft)

        leftToRight = []
        for index, num in enumerate(nums):
            toAdd = 0
            if leftToRight:
                toAdd += leftToRight[index-1]
            prefixSum = num + toAdd
            if prefixSum == rightToLeft[index]:
                return index
            leftToRight.append(prefixSum)
        
        print(leftToRight)

        return -1
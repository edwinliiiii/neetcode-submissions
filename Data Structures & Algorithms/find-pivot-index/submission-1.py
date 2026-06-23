class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # A pivot index is also an index where the prefix sum for leftToRight and rightToLeft match.
        '''
        We can first find the entire sum and keep track of the running leftSum so we can 
        calculate rightSum on the fly to see if they match.
        '''
        total= sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            rightSum = total - leftSum - num
            if leftSum == rightSum:
                return i
            leftSum+=num

        return -1















# A pivot index is also an index where the prefix sum for leftToRight and rightToLeft match.
        '''
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
        '''

# Time O(n). 2 iterations over nums, where n is the length of nums.
# Spac O(n). 2 lists to track prefix sums from leftToRight and rightToLeft, both worst case having n elements each.

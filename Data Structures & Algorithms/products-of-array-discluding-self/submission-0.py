class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        The idea here is that we can track what's the products to the left of the current number
        by using a leftToRight table.

        We can additionally track what's the products to the right of the current number using a
        rightToLeft table

        And then simply do leftToRight[i-1] * rightToLeft[i+1]
        '''
        size = len(nums)
        leftToRight = [0 for _ in range(size)]
        for i, num in enumerate(nums):
            toMultiplyBy = 1
            if i > 0:
                toMultiplyBy*= leftToRight[i-1]
            leftToRight[i] = toMultiplyBy * num
        
        rightToLeft = [0 for _ in range(size)]
        for i, num in enumerate(reversed(nums)):
            indexToWrite = size - i - 1
            toMultiplyBy = 1
            if i > 0:
                toMultiplyBy*= rightToLeft[indexToWrite+1]
            rightToLeft[indexToWrite] = toMultiplyBy * num

        ans= []
        for i, num in enumerate(nums):
            leftProduct = 1
            rightProduct = 1
            if i > 0:
                leftProduct = leftToRight[i-1]
            if i < size - 1:
                rightProduct = rightToLeft[i+1]
            ans.append(leftProduct*rightProduct)
        return ans
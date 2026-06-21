class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time O(n)
        Space O(n)
        ---
        Use a hashmap to store { Target-number : Index }
        That way in a later iteration we can lookup if the current number exists and if it does,
        we know we've hit the sum.
        """

        lookup = {}
        for index, num in enumerate(nums):
            if num in lookup:
                return [lookup[num], index]
            else:
                lookup[target - num] = index
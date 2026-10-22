class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''

        sorted- binary search-ish

        denote p1 as first index, p2 as last index. 

        if val[p1] + val[p2] == target, we're done.
        if val[p1] + val[p2] > target, we must decrement p2.
        if val[p1] + val[p2] < target, we must increment p1.
        
        O(n) time O(1) space

        '''

        p1 = 0
        p2 = len(numbers) - 1

        while p1 < p2:
            total = numbers[p1] + numbers[p2]
            if total == target:
                return [p1+1, p2+1]
            elif total < target:
                p1+=1
            else:
                p2-=1

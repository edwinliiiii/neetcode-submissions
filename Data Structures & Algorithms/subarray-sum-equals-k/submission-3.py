class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # going for O(n)
        '''
        [2, 1, 2, 3]  |  k = 2

        we know we can arrive at k if either
        
        curr num = k || curr num - (some difference we can store in a hash table) = k

        '''

        pfSumToCount = {}
        total = 0
        ans = 0
        for num in nums:
            total+=num

            if total == k:
                ans+=1
            ans+=pfSumToCount.get(total-k, 0)
            
            
            if total in pfSumToCount:
                pfSumToCount[total]+=1
            else:
                pfSumToCount[total] = 1

            

        return ans
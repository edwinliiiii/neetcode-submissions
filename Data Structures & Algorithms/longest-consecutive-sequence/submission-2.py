class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        find start and then count leftward. each num will only be visited at most twice (checked that not a start, then checked during leftward sweep)
        '''

        longest = 0
        running = 1
        numsAsSet = set(nums)
        startsAlreadyDone = set()

        for num in nums:
            if num not in startsAlreadyDone and num - 1 not in numsAsSet:
                startsAlreadyDone.add(num)
                temp = num
                while temp+1 in numsAsSet:
                    running +=1
                    temp+=1
                
                longest = max(longest, running)
                running = 1
        
        return longest


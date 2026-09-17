class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        '''
        [2,20,4,10,3,4,5]

        <----[2,3,4,5]-----[10]--------------------[20]--->

        we notice that the start of a consecutive sequence has it's num-1 nowhere to be found (constant time lookup via set)

        so for each num in nums:
            check if it's the start- if it is, continuosly check if num+1...+1..+1 is found in the set

        this is O(n) because each number is checked at most twice, once when checking if it's the start of a CS, and once during a CS's consecutive checks

        '''
        maxCount = 0
        runningCount = 0

        setOfNums = set(nums)
        
        for num in nums:
            if num-1 not in setOfNums:
                currentNum = num
                while currentNum in setOfNums:
                    runningCount+=1
                    currentNum = currentNum + 1

                maxCount = max(maxCount, runningCount)
                runningCount = 0
        
        return maxCount
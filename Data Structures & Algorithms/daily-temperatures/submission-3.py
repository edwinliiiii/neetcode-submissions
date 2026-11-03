class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        [30,38,30,36,35,40,28]

        (38, 1) (30, 2) (36, 3) -> triggers popping

        monotonic decreasing stack. we choose decreasing because it allows us to work backwards off the stack once we've hit something increasing.
        '''

        stack = []
        ans = [0 for i in range(len(temperatures))]

        for index, num in enumerate(temperatures):
            while stack and num > stack[-1][0]:
                prevEntry = stack.pop()
                daysTillGreater = index - prevEntry[1]
                ans[prevEntry[1]] = daysTillGreater
            stack.append((num, index))
        
        return ans

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''

        monotonic decreasing stack. 
        whenever we pop a number fill in its result[i] using the diff of curr temp's index - that number's index.

        '''

        result = [0 for _ in range(len(temperatures))]
        stack = [] #pairs (temp, index)

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
                continue

            while stack and temp > stack[-1][0]:
                prevNumIndex = stack.pop()[1]
                result[prevNumIndex] = i - prevNumIndex

            stack.append((temp, i))
            
        return result


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''

        monotonic decreasing stack. 
        whenever we pop a number fill in its result[i] using the diff of curr temp's index - that number's index.

        the reason we use monotonic decreasing is because our base case for each i is a result of 0. if we never find anything greater (violating the
        decreasing nature of our stack, we never write to result and everything stays as 0.) and we only fill in results for the temps that have encountered
        a larger future temp (by working backwards thru the stack. cool problem)

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


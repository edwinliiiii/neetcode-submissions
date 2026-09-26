class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        observation: if we sort the list of speeds and take note of index, then anything with a higher speed + lower index is a 
        candidate. we need to make sure the car has time to catch up b4 target however.


        iterate thru sorted positions in reverse order, we need to keep track of the last car (stack?)

        if the last car gets to target slower than current car, this will become a fleet. treat as one entity (aka don't add this
        car to the stack) and move on.


        '''

        positionSpeed = []

        for i in range(len(position)):
            positionSpeed.append((position[i], speed[i]))

        positionSpeed.sort(reverse=True) # sort by key (position!!)

        stack = []

        for pair in positionSpeed:
            if not stack:
                stack.append(pair)
                continue
            
            timeToArriveCurr = (target - pair[0]) / pair[1]

            last = stack[-1]
            timeToArriveLast = (target - last[0]) / last[1]

            if timeToArriveCurr > timeToArriveLast:
                stack.append(pair)
        
        return len(stack)


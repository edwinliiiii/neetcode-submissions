class MinStack:
    '''

    use the second stack to track the min at the current point in time. whenever we push, compare curr min and whatever just got pushed to recalculate new min

    [-2 0]
    [-2 -

    '''

    def __init__(self):
        self.stack = []
        self.minValues = [] # pairs?
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minValues:
            self.minValues.append(val)
        else:
            self.minValues.append(min(self.minValues[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minValues.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValues[-1]


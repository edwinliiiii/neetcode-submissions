class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(second+first)
                continue
            elif s == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first)
                continue
            elif s == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(second*first)
                continue
            elif s == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(math.trunc(second / first))
                continue
            stack.append(int(s))
        
        return stack.pop()

        '''
            print(s, stack)


                        if (first < 0 and second > 0):
                    first *= -1
                elif (first > 0 and second < 0):
                    second *= -1
                    '''
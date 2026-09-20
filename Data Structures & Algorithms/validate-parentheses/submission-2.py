class Solution:
    def isValid(self, s: str) -> bool:
        '''
        prev solution did not account for order.

        new approach: everytime we encounter a closing, pop from the stack and it must match the approrpirate.
        '''

        stack = []
        d = { "}" : "{", ")": "(", "]": "["}

        for char in s:
            if char in d:
                if len(stack) <= 0:
                    return False
                if d[char] != stack.pop():
                    return False
            else:
                stack.append(char)

        return len(stack) ==0
















        # '''
        # stack. put everything into the stack. as we begin to pop, if we find a opener, make sure the amount matches
        # if we find a closer, add one to the allowed opener
        # '''

        # stack = []
        # for char in s:
        #     stack.append(char)
        
        # d = {"(" : 0, "{" : 0, "[" : 0}
        # while stack:
        #     char = stack.pop()
        #     if char == ")":
        #         d["("] += 1
        #         continue
        #     elif char == "}":
        #         d["{"] += 1
        #         continue
        #     else:
        #         d["["] += 1
        #         continue
            
        #     if d[char] <= 0:
        #         return False
            
        #     d[char] -= 1
            
        # return True
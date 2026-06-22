class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSumTwoD = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                prefix = 0
                if r > 0:
                    prefix+=self.prefixSumTwoD[r-1][c]
                if c > 0:
                    prefix+=self.prefixSumTwoD[r][c-1]
                if r > 0 and c > 0:
                    prefix-=self.prefixSumTwoD[r-1][c-1]
                self.prefixSumTwoD[r][c] = prefix + matrix[r][c]
        print(self.prefixSumTwoD)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        toSubtract = 0
        if row1 > 0:
            toSubtract+=self.prefixSumTwoD[row1-1][col2]
        if col1 > 0:
            toSubtract+=self.prefixSumTwoD[row2][col1-1]
        if row1 > 0 and col1 > 0:
            toSubtract-=self.prefixSumTwoD[row1-1][col1-1]
        return self.prefixSumTwoD[row2][col2] - toSubtract

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

'''
[3,   3,   4,   8,  10]
[8,  14,  18,  25,  33]
[9,  22,  37,  60,  95]
[13, 33,  67, 125, 224]
[14, 44, 111, 233, 459]
'''
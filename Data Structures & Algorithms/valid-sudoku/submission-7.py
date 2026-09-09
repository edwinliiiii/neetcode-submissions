class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        '''

        intuition for 3 * O(81) space:

        we only ever have to track 3 things for every (r, c)
            - Set of numbers in current row, denoted by [r]
            - Set of numbers in current col, denoted by [c]
            - Set of numbers in current 3x3, denoted by the position of (r, c)

            for 3x3, we have (r: 0-8, c: 0-8).

            [ 0.  1.  2.]      [(0, 0), (0, 1), (0, 2)]
            [ 3.  4.  5.]      [(1, 0), (1, 1), (1, 2)]
            [ 6.  7.  8.]      [(2, 0), (2, 1), (2, 2)]

            (r5, c2) should be set i = 3. 5//3 = 1, 2//3 = 0
            (r2, c2) should be set i = 0. 2//3 = 0, 2//3 = 0
            (r8, c8) should be set i = 8. 8//3 = 2, 8//3 = 2


            hard code it for now.

        '''


        row: list[set] = [set() for _ in range(0,9)]
        col: list[set] = [set() for _ in range(0,9)]
        threeByThree: list[set] = [set() for _ in range(0,9)]
        

        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                num = board[r][c]

                if num == ".":
                    continue
                if num in row[r]:
                    print('row')
                    return False
                if num in col[c]:
                    print('col')
                    return False

                indexOfThreeByThree = (r//3) * 3 + c//3
                if num in threeByThree[indexOfThreeByThree]:
                    print('3x3', num, indexOfThreeByThree, threeByThree)
                    print(r, c)
                    return False

                row[r].add(num)
                col[c].add(num)
                threeByThree[indexOfThreeByThree].add(num)

    
        return True
    

    
    
   
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        length = {}


        def helper(r, c):
            if r >= rows or c >= cols:
                return 0

            if (r, c) not in length:
                down = helper(r+1, c)
                right = helper(r, c+1)
                diagonal = helper(r+1, c+1)

                length[(r,c)] = 0

                if matrix[r][c] == "1":
                    length[(r, c)] = 1 + min(down, right, diagonal)
            return length[(r,c)]

        helper(0,0)
        return max(length.values())**2

            
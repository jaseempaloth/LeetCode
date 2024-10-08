# 840. Magic Squares In Grid
# Topics: Array, Hash Table, Math, Matrix
class Solution:
    def num_magic_squares_inside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def magic(r, c):

            values = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])
            #rows
            for i in range(r, r + 3):
                if sum(grid[i][c:c+3]) != 15:
                    return 0
            # colums
            for i in range(c, c + 3):
                if (grid[r][i] + grid[r+1][i] + grid[r+2][i]) != 15:
                    return 0
            # diagonals
            if (
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c + 2] + grid[r+1][c+1] + grid[r+2][c] != 15 
            ):
                return 0
            return 1
        result = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                result += magic(r, c)
        return result
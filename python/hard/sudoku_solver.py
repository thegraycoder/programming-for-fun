# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#   - Each of the digits 1-9 must occur exactly once in each row.
#   - Each of the digits 1-9 must occur exactly once in each column.
#   - Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#
# Empty cells are indicated by the character '.'

# Example:
# ['5', '3', '.', '.', '7', '.', '.', '.', '.']
# ['6', '.', '.', '1', '9', '5', '.', '.', '.']
# ['.', '9', '8', '.', '.', '.', '.', '6', '.']
# ['8', '.', '.', '.', '6', '.', '.', '.', '3']
# ['4', '.', '.', '8', '.', '3', '.', '.', '1']
# ['7', '.', '.', '.', '2', '.', '.', '.', '6']
# ['.', '6', '.', '.', '.', '.', '2', '8', '.']
# ['.', '.', '.', '4', '1', '9', '.', '.', '5']
# ['.', '.', '.', '.', '8', '.', '.', '7', '9']

# Solution to return
# ["5","3","4","6","7","8","9","1","2"]
# ["6","7","2","1","9","5","3","4","8"]
# ["1","9","8","3","4","2","5","6","7"]
# ["8","5","9","7","6","1","4","2","3"]
# ["4","2","6","8","5","3","7","9","1"]
# ["7","1","3","9","2","4","8","5","6"]
# ["9","6","1","5","3","7","2","8","4"]
# ["2","8","7","4","1","9","6","3","5"]
# ["3","4","5","2","8","6","1","7","9"]
import math

EMPTY_ENTRY = "."


def possible(number, x, y, grid):
    """
    Is it possible to put number in position x, y of grid

    :param number: The number we want to place
    :param x: X coordinate
    :param y: Y coordinate
    :param grid: The sudoku board
    :return: Boolean
    """
    if grid[y][x] != EMPTY_ENTRY:
        return False
    region_size = math.sqrt(len(grid))
    row = grid[y]
    column = [grid_row[x] for grid_row in grid]
    sub_grid_rows = grid[int(int(y / region_size) * region_size):int(int(y / region_size) * region_size + region_size)]
    sub_grid = [
        rows[
            int(int(x / region_size) * region_size):int(int(x / region_size) * region_size + region_size)
        ] for rows in sub_grid_rows
    ]
    if number in row or number in column:
        return False
    for sub_row in sub_grid:
        if number in sub_row:
            return False
    return True


def solve(row, column, grid):
    if column == len(grid[row]):
        column = 0
        row += 1

    if row == len(grid):
        print(grid)
        return True

    if grid[row][column] != EMPTY_ENTRY:
        return solve(row, column + 1, grid)

    for i in range(1, len(board) + 1):
        value = str(i)

        if possible(value, column, row, grid):
            grid[row][column] = value
            if solve(row, column + 1, grid):
                return True
            board[row][column] = EMPTY_ENTRY

    return False


board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

solve(0, 0, board)

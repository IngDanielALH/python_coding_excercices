"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3



Constraints:

    m == grid. Length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.


"""
from collections import deque


def num_islands2(grid):
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count


def dfs(grid, i, j):
    if (i < 0 or j < 0
            or i >= len(grid)
            or j >= len(grid[0])
            or grid[i][j] != '1'):
        return
    grid[i][j] = '#'
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


def get_cells_to_analyze(current_cell, rows_number, cols_number):
    cells = []
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for x, y in neighbors:
        if 0 <= current_cell[0] + x < rows_number and 0 <= current_cell[1] + y < cols_number:
            cells.append((current_cell[0] + x, current_cell[1] + y))
    return cells
    pass


def test(message, expected, actual):
    if expected == actual:
        print(f"Test {message}: SUCCESS")
    else:
        print(f"Test {message}: FAIL, expected: {expected} -> got: {actual}")


def print_grid(grid):
    if not grid or not grid[0]:
        print("La matriz está vacía.")
        return

    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


def bfs(grid):
    rows = len(grid)
    cols = len(grid[0])
    islands_counter = 0
    queue = deque()

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == "1":
                islands_counter += 1
                grid[i][j] = "*"
                queue.append((i, j))

                while queue:
                    current_x, current_y = queue.popleft()
                    cells = get_cells_to_analyze((current_x, current_y), rows, cols)
                    for x, y in cells:
                        if grid[x][y] == "1":
                            grid[x][y] = "*"
                            queue.append((x, y))
            print_grid(grid)
            print("________________")
    return islands_counter
    pass


def num_islands(grid):
    return bfs(grid) if grid else 0


if __name__ == '__main__':
    current_cell = (0, 0)
    test("Validació de obtención de vecinos", [(0, 1), (1, 0)],
         get_cells_to_analyze(current_cell, 5, 5))

    current_cell = (5, 5)
    test("Validació de obtención de vecinos", [(5, 4), (4, 5)],
         get_cells_to_analyze(current_cell, 5, 5))
    pass

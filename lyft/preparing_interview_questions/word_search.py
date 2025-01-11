"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.



Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if dfs(board, i, j, word, 0):
                    return True
    return False


def dfs(board, i, j, word, index):
    # Base cases
    if index == len(word):  # All characters matched
        return True
    if (i < 0 or
            i >= len(board) or
            j < 0 or
            j >= len(board[0]) or
            board[i][j] != word[index]):
        return False

    # Mark the current cell as visited
    temp = board[i][j]
    board[i][j] = '*'

    # Explore all possible directions
    found = (dfs(board, i - 1, j, word, index + 1) or
             dfs(board, i + 1, j, word, index + 1) or
             dfs(board, i, j - 1, word, index + 1) or
             dfs(board, i, j + 1, word, index + 1))

    # Backtrack
    board[i][j] = temp
    return found


if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"
    exist(board, word)

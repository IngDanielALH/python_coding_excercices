"""
Markov takout out his Snakes and Ladders game, stares at the board and wonders: "If I can always roll the die to
whatever number I want, what would be the least number of rolls to reach the destination?"

Rules

The game is played with a cubic die of 6 faces numbered 1 to 6.

    Starting from square 1, land on square 100 with the exact roll of the die. If moving the number rolled would place
    the player beyond square 100, no move is made.

    If a player lands at the base of a ladder, the player must climb the ladder. Ladders go up only.

    If a player lands at the mouth of a snake, the player must go down the snake and come out through the tail.
    Snakes go down only.

Function Description

Complete the quickestWayUp function in the editor below. It should return an integer that represents the minimum number
of moves required.

quickestWayUp has the following parameter(s):

    ladders: a 2D integer array where each ladders[i] contains the start and end cell numbers of a ladder

    snakes: a 2D integer array where each snakes[i] contains the start and end cell numbers of a snake

Input Format

The first line contains the number of tests, t.

For each testcase:

    The first line contains n, the number of ladders.

    Each of the next n lines contains two space-separated integers, the start and end of a ladder.

    The next line contains the integer m, the number of snakes.

    Each of the next m lines contains two space-separated integers, the start and end of a snake.

Constraints

1 ≤ t ≤ 10
1 ≤ n, m ≤ 15
The board is always 10 x 10 with squares numbered 1 to 100.
Neither square 1 nor square 100 will be the starting point of a ladder or snake.
A square will have at most one endpoint from either a snake or a ladder.

Output Format

For each of the t test cases, print the least number of rolls to move from start to finish on a separate line.
If there is no solution, print –1.

Sample Input

2
3
32 62
42 68
12 98
7
95 13
97 25
93 37
79 27
75 19
49 47
67 17
4
8 52
6 80
26 42
2 72
9
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21

Sample Output

3
5
"""
from collections import deque


def getTeleports(ladders, snakes):
    teleports = {}
    for inicio, fin in ladders:
        teleports[inicio] = fin
    for inicio, fin in snakes:
        teleports[inicio] = fin
    return teleports


def getRangeOfRoll(currentPosition, teleports):
    posibleRange = []
    currentRoll = currentPosition[1] + 1
    for i in range(1, 7):
        accesibleSquare = currentPosition[0] + i
        posibleRange.append((accesibleSquare, currentRoll))
    return manageTeleports(posibleRange, teleports)


def manageTeleports(posibleSquares, teleports):
    final_destinations = []

    for position, moves in posibleSquares:
        final_pos = teleports.get(position, position)
        final_destinations.append((final_pos, moves))

    return final_destinations


def quickestWayUp(ladders, snakes):
    teleports = getTeleports(ladders, snakes)
    queue = deque([(1, 0)])
    visited = {1}

    while queue:
        currentSquare, currentMoves = queue.popleft()

        if currentSquare == 100:
            return currentMoves

        finalSquares = getRangeOfRoll((currentSquare, currentMoves), teleports)

        for nextSquare, nextMoves in finalSquares:
            if nextSquare not in visited:
                visited.add(nextSquare)
                queue.append((nextSquare, nextMoves))

    return -1
    pass

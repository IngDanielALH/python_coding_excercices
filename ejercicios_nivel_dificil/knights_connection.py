"""
You’re given the position of two knight pieces on an infinite chess board. Write a function that returns the minimum
number of turns required before one of the knights is able to capture the other knight, assuming the knights are working
together to achieve this goal.
The position of each knight is given as a list of 2 values, the x and y coordinates. A knight can make 1 of 8 possible
moves on any given turn. Each of these moves involves moving in an "L" shape. This means they can either move 2 squares
horizontally and 1 square vertically, or they can move 1 square horizontally and 2 squares vertically. For example,
if a knight is currently at position [0, 0], then it can move to any of these 8 locations on its next move:
[
  [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]
]

A knight is able to capture the other knight when it is able to move onto the square currently occupied by the other
knight.
Each turn allows each knight to move up to one time. For example, if both knights moved towards each other once, and
then knightA captures knightB on its next move, two turns would have been used (even though knightB never made
its second move).

Sample Input
knightA = [0, 0]
knightB = [4, 2]

Sample Output
1
"""

import math


def knight_connection(knightA, knightB):
    possibleMoves = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

    queue = [[knightA[0], knightA[1], 0]]
    visited = {positionToString(knightA)}

    while True:
        currentPosition = queue.pop(0)

        if currentPosition[0] == knightB[0] and currentPosition[1] == knightB[1]:
            return math.ceil(currentPosition[2] / 2)

        for possibleMove in possibleMoves:
            position = [currentPosition[0] + possibleMove[0], currentPosition[1] + possibleMove[1]]
            positionString = positionToString(position)
            if positionString not in visited:
                position.append(currentPosition[2] + 1)
                queue.append(position)
                visited.add(positionString)


def positionToString(position):
    return ".".join(map(str, position))
